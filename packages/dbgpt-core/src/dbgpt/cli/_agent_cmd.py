"""CLI commands for the pure CLI agent runtime."""

from __future__ import annotations

import asyncio
from pathlib import Path

import click

from dbgpt.cli_agent.runner import CliAgentOptions, run_agent_chat


@click.group("agent")
def agent_cli_group():
    """Run the pure CLI agent."""


@agent_cli_group.command("chat")
@click.option("--profile", type=str, default=None, help="Configured DB-GPT profile name.")
@click.option("--config", type=str, default=None, help="Path to a DB-GPT TOML config.")
@click.option("--model", type=str, default=None, help="Override the model name.")
@click.option("--api-key", type=str, default=None, envvar="DBGPT_API_KEY")
@click.option("--api-base", type=str, default=None, help="Override the API base URL.")
@click.option(
    "--language",
    type=click.Choice(["en", "zh"], case_sensitive=False),
    default="en",
    show_default=True,
    help="Prompt language for the assistant profile.",
)
@click.option("--session-id", type=str, default="default", show_default=True)
@click.option(
    "--history-file",
    type=click.Path(path_type=Path, dir_okay=False, resolve_path=True),
    default=None,
    help="Transcript JSONL file. Defaults to ~/.dbgpt/agent_history/<session>.jsonl.",
)
@click.option("--prompt", type=str, default=None, help="Run a single prompt and exit.")
@click.option(
    "--system-prompt",
    type=str,
    default=None,
    help="Extra system prompt appended to the assistant profile.",
)
@click.option("--temperature", type=float, default=0.2, show_default=True)
@click.option("--max-new-tokens", type=int, default=4096, show_default=True)
@click.option(
    "--new-session",
    is_flag=True,
    default=False,
    help="Delete the existing transcript for this session before starting.",
)
def chat_command(
    profile: str | None,
    config: str | None,
    model: str | None,
    api_key: str | None,
    api_base: str | None,
    language: str,
    session_id: str,
    history_file: Path | None,
    prompt: str | None,
    system_prompt: str | None,
    temperature: float,
    max_new_tokens: int,
    new_session: bool,
):
    """Start a single-agent terminal chat session."""
    options = CliAgentOptions(
        profile=profile,
        config=config,
        model=model,
        api_key=api_key,
        api_base=api_base,
        language=language,
        session_id=session_id,
        history_file=history_file,
        prompt=prompt,
        system_prompt=system_prompt,
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        new_session=new_session,
    )
    return asyncio.run(run_agent_chat(options))
