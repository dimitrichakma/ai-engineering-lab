"""Compare local models on the S3 ticket set.
uv run python -m track6_models.m1_model_selection.compare"""
import statistics  # noqa: F401
from pathlib import Path

from pydantic import BaseModel

TICKETS = Path(__file__).parents[2] / "track1_structured_output" / "s3_ticket_triage" / "data" / "tickets.csv"
MODELS = ["qwen2.5:3b", "llama3.2:3b", "gemma3:4b"]


class Result(BaseModel):
    model: str
    example_id: int
    gold: str
    pred: str | None
    valid_json: bool
    latency_ms: int
    output_tokens: int
    gen_seconds: float  # Ollama eval_duration / 1e9


def run_model(model: str, rows: list[dict]) -> list[Result]:
    # TODO: ollama.chat(model=model, messages=..., format=<schema>, options={"temperature": 0})
    #       time it; parse JSON safely (valid_json False and pred None on failure)
    raise NotImplementedError


def percentile(values: list[float], p: float) -> float:
    """Given. Nearest rank percentile, p in 0..100."""
    s = sorted(values)
    k = max(0, min(len(s) - 1, round(p / 100 * len(s) + 0.5) - 1))
    return s[k]


def score(results: list[Result]) -> dict:
    # TODO: accuracy (pred == gold over ALL rows, invalid counts as wrong), valid_json_rate,
    #       p50_ms, p95_ms (use percentile), tokens_per_s = sum(output_tokens) / sum(gen_seconds)
    raise NotImplementedError


def pick(scores: dict[str, dict], max_p95_ms: float) -> str | None:
    # TODO: among models with p95_ms <= max_p95_ms: highest accuracy, then lowest p95_ms
    raise NotImplementedError


def main():
    # TODO: load TICKETS, run each model, print a table, save results/m1.csv (U3 format)
    pass


if __name__ == "__main__":
    main()
