import csv
from collections import Counter
from pathlib import Path

from common.llm import generate_json
from .models import Triage

DATA = Path(__file__).parent / "data" / "tickets.csv"

PROMPT_VERSION = "v1"  # change this each time you change the prompt, and log the results
SYSTEM = ""  # TODO


def classify(message: str) -> Triage:
    # TODO: generate_json + validate (reuse your retry pattern)
    raise NotImplementedError


def load_gold() -> list[dict]:
    with DATA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate(gold: list[dict], preds: list[Triage]) -> dict:
    """Pure function: no LLM calls here, so it is easy to test.

    Return a dict like:
    {
      "category_accuracy": 0.85,
      "urgency_accuracy": 0.7,
      "confusion": Counter({("refund", "payment"): 1, ...}),   # (gold, predicted) -> count
      "wrong": [ {"id": "10", "gold": "refund", "pred": "payment"}, ... ],
    }
    """
    # TODO
    raise NotImplementedError


def print_report(report: dict) -> None:
    # TODO: print accuracies, the confusion pairs, and the wrong answers in a readable way
    raise NotImplementedError


def main() -> None:
    gold = load_gold()
    # TODO: classify every message, then evaluate and print_report
    print(f"prompt version: {PROMPT_VERSION}")


if __name__ == "__main__":
    main()
