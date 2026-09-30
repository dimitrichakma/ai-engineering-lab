"""Data question -> code -> run -> fix loop."""
from collections.abc import Callable
from pathlib import Path

from track5_agentic.a4_code_agent.sandbox import run_code  # noqa: F401

SYSTEM = (
    "You write short Python using pandas to answer a question about data.csv in the current folder. "
    "Print ONLY the final answer. Reply with code only, no markdown fences."
)


def strip_fences(text: str) -> str:
    """Given. Models often wrap code in ```python fences anyway."""
    lines = [ln for ln in text.strip().splitlines() if not ln.strip().startswith("```")]
    return "\n".join(lines)


def answer(question: str, csv_path: Path, llm: Callable[[str, str], str], max_attempts: int = 3) -> dict:
    # TODO: tempfile.TemporaryDirectory() as workdir; copy csv to workdir/"data.csv"
    #       preview = columns + first 3 rows; prompt = question + preview
    #       loop: code = strip_fences(llm(prompt, SYSTEM)); result = run_code(code, workdir)
    #             ok -> return {"answer": stdout.strip(), "code": code, "attempts": n}
    #             else add the error (stderr, last 20 lines) to the prompt and try again
    #       after max_attempts: {"answer": None, "code": code, "attempts": max_attempts}
    raise NotImplementedError
