import json
from pathlib import Path

from .judge import JUDGE_VERSION, judge

DATA = Path(__file__).parent / "data" / "answers.jsonl"


def load() -> list[dict]:
    return [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]


def agreement(human: list[str], judge_labels: list[str]) -> float:
    # TODO: share of positions where they are equal
    raise NotImplementedError


def cohens_kappa(human: list[str], judge_labels: list[str]) -> float:
    """kappa = (p_observed - p_expected) / (1 - p_expected)
    p_expected = P(both pass by chance) + P(both fail by chance)
               = (h_pass * j_pass) + (h_fail * j_fail), using each rater's own pass/fail shares.
    If p_expected == 1, return 1.0 (both always say the same single label)."""
    # TODO
    raise NotImplementedError


def main() -> None:
    items = load()
    if any(not it["human_label"] for it in items):
        raise SystemExit("Label every item in data/answers.jsonl first (human_label = pass/fail).")
    # TODO: judge every item, then print agreement, kappa and the disagreements
    #       (id, your label + reason, judge verdict + reason)
    print(f"judge version: {JUDGE_VERSION}")


if __name__ == "__main__":
    main()
