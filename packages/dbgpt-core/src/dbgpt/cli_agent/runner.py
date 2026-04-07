"""Pure CLI agent runner."""

from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Optional, Type

from dbgpt.agent.core.agent import AgentContext, AgentMessage
from dbgpt.agent.core.memory.agent_memory import AgentMemory
from dbgpt.agent.util.llm.llm import LLMConfig
from dbgpt.cli._config import dbgpt_home, read_active_profile, resolve_config_path
from dbgpt.cli._profiles import get_profile

from .agent import CliAssistantAgent, CliUserProxyAgent
from .memory import CliGptsMemory, FileMessageMemory

try:
    import tomllib
except ImportError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[no-redef]


_PROVIDER_CLIENTS = {
    "proxy/openai": "dbgpt.model.proxy.llms.chatgpt:OpenAILLMClient",
    "proxy/moonshot": "dbgpt.model.proxy.llms.moonshot:MoonshotLLMClient",
    "proxy/tongyi": "dbgpt.model.proxy.llms.tongyi:TongyiLLMClient",
    "proxy/zhipu": "dbgpt.model.proxy.llms.zhipu:ZhipuLLMClient",
    "proxy/minimax": "dbgpt.model.proxy.llms.minimax:MiniMaxLLMClient",
}


@dataclass
class RuntimeModelConfig:
    provider: str
    model: str
    api_key: Optional[str]
    api_base: Optional[str]


@dataclass
class CliAgentOptions:
    profile: Optional[str] = None
    config: Optional[str] = None
    model: Optional[str] = None
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    language: str = "en"
    session_id: str = "default"
    history_file: Optional[Path] = None
    prompt: Optional[str] = None
    system_prompt: Optional[str] = None
    temperature: float = 0.2
    max_new_tokens: int = 4096
    new_session: bool = False


def _default_history_file(session_id: str) -> Path:
    return dbgpt_home() / "agent_history" / f"{session_id}.jsonl"


def _load_toml_runtime_config(
    config_path: str, model_override: Optional[str]
) -> RuntimeModelConfig:
    data = tomllib.loads(Path(config_path).read_text(encoding="utf-8"))
    llms = data.get("models", {}).get("llms", [])
    if not llms:
        raise ValueError(f"No llm models found in config: {config_path}")
    llm_entry = llms[0]
    return RuntimeModelConfig(
        provider=llm_entry.get("provider", "proxy/openai"),
        model=model_override or llm_entry.get("name") or "gpt-4o-mini",
        api_key=llm_entry.get("api_key"),
        api_base=llm_entry.get("api_base"),
    )


def _default_api_key_placeholder(profile_name: str) -> Optional[str]:
    spec = get_profile(profile_name)
    if spec.env_key():
        return spec.env_key()
    if spec.env_var:
        return f"${{env:{spec.env_var}}}"
    return None


def resolve_runtime_model_config(options: CliAgentOptions) -> RuntimeModelConfig:
    resolved_config = resolve_config_path(profile=options.profile, config=options.config)
    if resolved_config:
        runtime = _load_toml_runtime_config(resolved_config, options.model)
    else:
        profile_name = options.profile or read_active_profile() or "openai"
        spec = get_profile(profile_name)
        runtime = RuntimeModelConfig(
            provider=spec.llm_provider,
            model=options.model or spec.llm_model,
            api_key=_default_api_key_placeholder(profile_name),
            api_base=spec.llm_api_base,
        )
    runtime.api_key = options.api_key or runtime.api_key
    runtime.api_base = options.api_base or runtime.api_base
    return runtime


def _load_client_class(provider: str) -> Type:
    target = _PROVIDER_CLIENTS.get(
        provider, _PROVIDER_CLIENTS["proxy/openai"]
    )
    module_name, class_name = target.split(":", 1)
    module = import_module(module_name)
    return getattr(module, class_name)


def build_llm_client(options: CliAgentOptions):
    runtime = resolve_runtime_model_config(options)
    client_cls = _load_client_class(runtime.provider)
    return client_cls(
        api_key=runtime.api_key,
        api_base=runtime.api_base,
        model=runtime.model,
        model_alias=runtime.model,
    )


async def _build_session(options: CliAgentOptions):
    conv_id = options.session_id
    history_file = options.history_file or _default_history_file(conv_id)
    if options.new_session and history_file.exists():
        history_file.unlink()

    message_memory = FileMessageMemory(history_file)
    gpts_memory = CliGptsMemory(message_memory=message_memory)
    gpts_memory.init(conv_id, enable_vis_message=False)

    shared_memory = AgentMemory(gpts_memory=gpts_memory)
    context = AgentContext(
        conv_id=conv_id,
        language=options.language,
        temperature=options.temperature,
        max_new_tokens=options.max_new_tokens,
        enable_vis_message=False,
    )
    llm_client = build_llm_client(options)
    llm_config = LLMConfig(llm_client=llm_client)

    user = CliUserProxyAgent().bind(context).bind(shared_memory)
    assistant = (
        CliAssistantAgent(system_prompt=options.system_prompt)
        .bind(context)
        .bind(shared_memory)
        .bind(llm_config)
    )

    await user.build()
    await assistant.build()
    return user, assistant, message_memory.transcript_path


async def run_agent_chat(options: CliAgentOptions) -> int:
    user, assistant, transcript_path = await _build_session(options)
    if options.prompt:
        await user.send(AgentMessage(content=options.prompt), assistant)
        return 0

    import click

    click.echo(f"Session: {options.session_id}")
    click.echo(f"Transcript: {transcript_path}")
    click.echo("Type /exit to quit.")
    while True:
        prompt = click.prompt(">>>", prompt_suffix=" ", default="", show_default=False)
        if not prompt.strip():
            continue
        if prompt.strip().lower() in {"/exit", "/quit"}:
            break
        await user.send(AgentMessage(content=prompt), assistant)
    return 0
