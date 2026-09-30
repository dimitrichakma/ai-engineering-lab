"""Agent evaluation: success, trajectory, cost, latency."""
import json
from pathlib import Path

from pydantic import BaseModel

DATA = Path(__file__).parent / "data"

# USD per 1M tokens. Example numbers for a small paid model; check real prices before using them.
PRICES = {"input": 0.10, "output": 0.40}


class CaseScore(BaseModel):
    case_id: str
    success: bool
    tool_precision: float   # needed calls / all calls (1.0 if no calls)
    tool_recall: float      # required tools called / required tools (1.0 if none required)
    in_order: bool
    forbidden_calls: int
    steps: int
    latency_ms: int
    cost_usd: float


def load_jsonl(path: Path) -> list[dict]:
    """Given."""
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def in_order(required: list[str], called: list[str]) -> bool:
    # TODO: subsequence check
    raise NotImplementedError


def cost_usd(trace: dict, prices: dict = PRICES) -> float:
    # TODO: trace["tokens_in"] and trace["tokens_out"] -> USD, rounded to 6 decimals
    raise NotImplementedError


def score_case(case: dict, trace: dict) -> CaseScore:
    # TODO: trace has: case_id, final_answer, tool_calls (list of names), steps, latency_ms,
    #       tokens_in, tokens_out.
    #       success: every string in case["expected_answer_contains"] is in the answer (case insensitive)
    #       precision: calls whose name is in required_tools / all calls
    #       recall: distinct required tools that were called / len(required_tools)
    raise NotImplementedError


def summarize(scores: list[CaseScore]) -> dict:
    # TODO: success_rate, mean_precision, mean_recall, forbidden_calls (total), mean_steps,
    #       p95_latency_ms, total_cost_usd
    raise NotImplementedError


def main():
    cases = {c["case_id"]: c for c in load_jsonl(DATA / "cases.jsonl")}
    traces = load_jsonl(DATA / "sample_traces.jsonl")
    # TODO: score each trace against its case; print a table and the summary
    _ = (cases, traces)


if __name__ == "__main__":
    main()
