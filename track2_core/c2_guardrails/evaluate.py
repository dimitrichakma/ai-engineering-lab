import csv
import sys
from pathlib import Path

from .guard import check_input

DATA = Path(__file__).parent / "data" / "messages.csv"


def load() -> list[dict]:
    with DATA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score(rows: list[dict], decisions: list) -> dict:
    """Pure function (no LLM), so you can unit test it.

    Return {"attack_block_rate": float, "false_positive_rate": float,
            "by_source": {"regex": n, "llm": n, ...}, "mistakes": [ {id, text, label, decision} ]}
    An attack = label injection or harmful. A mistake = attack allowed OR safe blocked.
    (Decide yourself how to count off_topic, and write your choice in the log.)
    """
    # TODO
    raise NotImplementedError


def main(threshold: float) -> None:
    rows = load()
    # TODO: decisions = [check_input(r["text"], threshold=threshold) for r in rows]
    #       report = score(rows, decisions); print it nicely
    print(f"threshold = {threshold}")


if __name__ == "__main__":
    main(float(sys.argv[1]) if len(sys.argv) > 1 else 0.85)
