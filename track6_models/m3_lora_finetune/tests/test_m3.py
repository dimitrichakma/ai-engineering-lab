import csv
import json

import pytest

from track6_models.m3_lora_finetune.evaluate import accuracy, macro_f1, per_class_f1
from track6_models.m3_lora_finetune.prepare_data import (
    DATA, LABELS, label_from_output, to_chat_example, write_jsonl,
)


def test_data_labels_are_valid():
    for name in ("train.csv", "test.csv"):
        with open(DATA / name) as f:
            rows = list(csv.DictReader(f))
        assert rows and all(r["label"] in LABELS for r in rows)


def test_chat_example():
    ex = to_chat_example("where is my parcel", "delivery")
    roles = [m["role"] for m in ex["messages"]]
    assert roles == ["system", "user", "assistant"]
    assert ex["messages"][2]["content"] == "delivery"
    with pytest.raises(ValueError):
        to_chat_example("x", "shipping")


def test_write_jsonl_keeps_bangla(tmp_path):
    p = tmp_path / "a.jsonl"
    write_jsonl([{"t": "টাকা"}, {"t": "b"}], p)
    lines = p.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2 and "টাকা" in lines[0]
    assert json.loads(lines[1]) == {"t": "b"}


def test_label_from_output():
    assert label_from_output(" Refund.") == "refund"
    assert label_from_output("Product issue") == "product_issue"
    assert label_from_output("I think it's about Payment") == "payment"
    assert label_from_output("no idea") == "other"


def test_metrics():
    gold = ["a", "a", "b", "b"]
    pred = ["a", "b", "b", "b"]
    assert accuracy(gold, pred) == 0.75
    f1 = per_class_f1(gold, pred)
    assert f1["a"] == pytest.approx(2 / 3)
    assert f1["b"] == pytest.approx(0.8)
    assert macro_f1(gold, pred) == pytest.approx((2 / 3 + 0.8) / 2)
