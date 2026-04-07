from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from dbgpt.cli.cli_scripts import cli
from dbgpt.core import LLMClient, ModelMetadata, ModelOutput


class FakeLLMClient(LLMClient):
    async def generate(self, request, message_converter=None):
        del message_converter
        prompt = request.get_messages()[-1].content
        return ModelOutput(error_code=0, text=f"echo:{prompt}")

    async def generate_stream(self, request, message_converter=None):
        del message_converter
        prompt = request.get_messages()[-1].content
        yield ModelOutput(error_code=0, text=f"echo:{prompt}")

    async def models(self):
        return [ModelMetadata(model="fake-model")]

    async def count_token(self, model: str, prompt: str) -> int:
        del model
        return len(prompt)


def test_agent_chat_one_shot_outputs_answer(isolated_dbgpt_home):
    runner = CliRunner(mix_stderr=False)
    history_path = Path(isolated_dbgpt_home) / "cli-agent.jsonl"
    with patch(
        "dbgpt.cli_agent.runner.build_llm_client", return_value=FakeLLMClient()
    ):
        result = runner.invoke(
            cli,
            [
                "agent",
                "chat",
                "--prompt",
                "hello",
                "--history-file",
                str(history_path),
                "--new-session",
            ],
        )
    assert result.exit_code == 0, result.output
    assert "echo:" in result.output
    assert history_path.exists()
    lines = history_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) >= 2
