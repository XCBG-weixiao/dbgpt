"""Pure CLI agent implementations built on top of the existing agent core."""

from __future__ import annotations

import click

from dbgpt.agent.core.action.blank_action import BlankAction
from dbgpt.agent.core.base_agent import ConversableAgent
from dbgpt.agent.core.profile.base import ProfileConfig
from dbgpt.agent.core.user_proxy_agent import UserProxyAgent


class CliAssistantAgent(ConversableAgent):
    """Single assistant used by the pure CLI runtime."""

    profile: ProfileConfig = ProfileConfig(
        name="CLI Agent",
        role="Assistant",
        goal="Answer the user's request clearly and directly in the terminal.",
        constraints=[
            "Prefer concise, terminal-friendly answers.",
            "Use Markdown only when it improves readability.",
        ],
        desc="A pure CLI assistant built from DB-GPT's agent core.",
    )

    stream_out: bool = False

    def __init__(self, system_prompt: str | None = None, **kwargs):
        super().__init__(**kwargs)
        self._init_actions([BlankAction])
        if system_prompt:
            self.profile = self.profile.model_copy(
                update={"expand_prompt": system_prompt}
            )

    def _print_received_message(self, message, sender):
        del message, sender


class CliUserProxyAgent(UserProxyAgent):
    """Terminal-facing human proxy."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_reply: str | None = None

    def _print_received_message(self, message, sender):
        del sender
        content = None
        if message.action_report:
            content = message.action_report.content
        if not content:
            content = message.content or ""
        self.last_reply = content
        click.echo(content)
