"""Turn the CSVs into chat JSONL for training.
uv run python -m track6_models.m3_lora_finetune.prepare_data"""
import csv  # noqa: F401
import json  # noqa: F401
from pathlib import Path

DATA = Path(__file__).parent / "data"
LABELS = ["delivery", "payment", "refund", "account", "product_issue", "other"]
SYSTEM = "Classify the customer ticket. Reply with exactly one label: " + ", ".join(LABELS) + "."


def to_chat_example(text: str, label: str) -> dict:
    # TODO: {"messages": [{"role": "system", "content": SYSTEM},
    #                     {"role": "user", "content": text},
    #                     {"role": "assistant", "content": label}]}
    #       ValueError if label not in LABELS
    raise NotImplementedError


def write_jsonl(rows: list[dict], path: Path) -> None:
    # TODO: one json.dumps(row, ensure_ascii=False) per line
    raise NotImplementedError


def label_from_output(text: str) -> str:
    # TODO: lowercase and strip; accept "product issue" / "Product_Issue." etc.
    #       return the first label found in the text, else "other"
    raise NotImplementedError


def main():
    # TODO: read train.csv and test.csv, write train.jsonl and test.jsonl next to them
    pass


if __name__ == "__main__":
    main()
