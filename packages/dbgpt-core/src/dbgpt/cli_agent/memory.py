"""Lightweight memory implementation for the pure CLI agent."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from dbgpt.agent.core.action.base import ActionOutput
from dbgpt.agent.core.memory.gpts.base import (
    GptsMessage,
    GptsMessageMemory,
    GptsPlan,
    GptsPlansMemory,
)


def _serialize_message(message: GptsMessage) -> Dict:
    payload = message.to_dict()
    payload["created_at"] = message.created_at.isoformat()
    payload["updated_at"] = message.updated_at.isoformat()
    return payload


def _deserialize_message(payload: Dict) -> GptsMessage:
    restored = dict(payload)
    restored["created_at"] = datetime.fromisoformat(payload["created_at"])
    restored["updated_at"] = datetime.fromisoformat(payload["updated_at"])
    return GptsMessage.from_dict(restored)


class CliPlansMemory(GptsPlansMemory):
    """Minimal in-memory plans store for the single-agent CLI runtime."""

    def __init__(self) -> None:
        self._plans: Dict[str, List[GptsPlan]] = defaultdict(list)

    def batch_save(self, plans: List[GptsPlan]) -> None:
        for plan in plans:
            self._plans[plan.conv_id].append(plan)

    def get_by_conv_id(self, conv_id: str) -> List[GptsPlan]:
        return list(self._plans.get(conv_id, []))

    def get_by_conv_id_and_num(
        self, conv_id: str, task_nums: List[int]
    ) -> List[GptsPlan]:
        wanted = set(task_nums)
        return [
            plan
            for plan in self._plans.get(conv_id, [])
            if plan.sub_task_num in wanted
        ]

    def get_todo_plans(self, conv_id: str) -> List[GptsPlan]:
        return list(self._plans.get(conv_id, []))

    def complete_task(self, conv_id: str, task_num: int, result: str) -> None:
        for plan in self._plans.get(conv_id, []):
            if plan.sub_task_num == task_num:
                plan.result = result

    def update_task(
        self,
        conv_id: str,
        task_num: int,
        state: str,
        retry_times: int,
        agent: Optional[str] = None,
        model: Optional[str] = None,
        result: Optional[str] = None,
    ) -> None:
        for plan in self._plans.get(conv_id, []):
            if plan.sub_task_num == task_num:
                plan.state = state
                plan.retry_times = retry_times
                plan.sub_task_agent = agent or plan.sub_task_agent
                plan.agent_model = model or plan.agent_model
                plan.result = result

    def remove_by_conv_id(self, conv_id: str) -> None:
        self._plans.pop(conv_id, None)


class FileMessageMemory(GptsMessageMemory):
    """Message store backed by a JSONL transcript file."""

    def __init__(self, transcript_path: Path) -> None:
        self._transcript_path = transcript_path
        self._transcript_path.parent.mkdir(parents=True, exist_ok=True)
        self._messages: List[GptsMessage] = []
        if self._transcript_path.exists():
            for line in self._transcript_path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                self._messages.append(_deserialize_message(json.loads(line)))

    @property
    def transcript_path(self) -> Path:
        return self._transcript_path

    def append(self, message: GptsMessage) -> None:
        self._messages.append(message)
        with self._transcript_path.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(_serialize_message(message), ensure_ascii=False) + "\n")

    def get_by_agent(self, conv_id: str, agent: str) -> Optional[List[GptsMessage]]:
        return [
            message
            for message in self._messages
            if message.conv_id == conv_id
            and (message.sender == agent or message.receiver == agent)
        ]

    def get_between_agents(
        self,
        conv_id: str,
        agent1: str,
        agent2: str,
        current_goal: Optional[str] = None,
    ) -> List[GptsMessage]:
        return [
            message
            for message in self._messages
            if message.conv_id == conv_id
            and {message.sender, message.receiver} == {agent1, agent2}
            and (current_goal is None or message.current_goal == current_goal)
        ]

    def get_by_conv_id(self, conv_id: str) -> List[GptsMessage]:
        return [message for message in self._messages if message.conv_id == conv_id]

    def get_last_message(self, conv_id: str) -> Optional[GptsMessage]:
        messages = self.get_by_conv_id(conv_id)
        return messages[-1] if messages else None

    def delete_by_conv_id(self, conv_id: str) -> None:
        self._messages = [
            message for message in self._messages if message.conv_id != conv_id
        ]
        with self._transcript_path.open("w", encoding="utf-8") as fp:
            for message in self._messages:
                fp.write(
                    json.dumps(_serialize_message(message), ensure_ascii=False) + "\n"
                )


class CliGptsMemory:
    """Minimal GPTs memory used by the pure CLI runtime."""

    def __init__(
        self,
        message_memory: FileMessageMemory,
        plans_memory: Optional[CliPlansMemory] = None,
    ) -> None:
        self._message_memory = message_memory
        self._plans_memory = plans_memory or CliPlansMemory()
        self.messages_cache: Dict[str, List[GptsMessage]] = defaultdict(list)

    @property
    def plans_memory(self) -> CliPlansMemory:
        return self._plans_memory

    @property
    def message_memory(self) -> FileMessageMemory:
        return self._message_memory

    def init(
        self,
        conv_id: str,
        enable_vis_message: bool = False,
        history_messages: Optional[List[GptsMessage]] = None,
        start_round: int = 0,
    ) -> None:
        del enable_vis_message, start_round
        self.messages_cache[conv_id] = history_messages or self.message_memory.get_by_conv_id(
            conv_id
        )

    def clear(self, conv_id: str) -> None:
        self.messages_cache.pop(conv_id, None)
        self.message_memory.delete_by_conv_id(conv_id)
        self.plans_memory.remove_by_conv_id(conv_id)

    async def append_message(self, conv_id: str, message: GptsMessage) -> None:
        self.messages_cache[conv_id].append(message)
        self.message_memory.append(message)

    async def push_message(self, conv_id: str, temp_msg: Optional[str] = None) -> None:
        del conv_id, temp_msg

    async def complete(self, conv_id: str) -> None:
        del conv_id

    async def get_messages(self, conv_id: str) -> List[GptsMessage]:
        cached = self.messages_cache.get(conv_id)
        if cached:
            return list(cached)
        messages = self.message_memory.get_by_conv_id(conv_id)
        self.messages_cache[conv_id] = list(messages)
        return messages

    async def get_agent_history_memory(
        self, conv_id: str, agent_role: str
    ) -> List[ActionOutput]:
        agent_messages = self.message_memory.get_by_agent(conv_id, agent_role) or []
        outputs: List[ActionOutput] = []
        for message in agent_messages:
            if not message.action_report:
                continue
            outputs.append(ActionOutput.from_dict(json.loads(message.action_report)))
        return outputs
