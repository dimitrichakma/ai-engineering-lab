import pandas as pd

from track4_ui.u3_eval_dashboard.metrics import confusion, summary, worst_examples


def small_df():
    return pd.DataFrame([
        {"run_id": "r1", "model": "a", "example_id": 1, "gold": "x", "pred": "x", "latency_ms": 100, "tokens": 10},
        {"run_id": "r1", "model": "a", "example_id": 2, "gold": "y", "pred": "x", "latency_ms": 300, "tokens": 20},
        {"run_id": "r2", "model": "b", "example_id": 1, "gold": "x", "pred": "x", "latency_ms": 200, "tokens": 30},
        {"run_id": "r2", "model": "b", "example_id": 2, "gold": "y", "pred": "y", "latency_ms": 200, "tokens": 30},
    ])


def test_summary_sorted_by_accuracy():
    s = summary(small_df())
    assert list(s.index) == ["r2", "r1"]
    assert s.loc["r1", "accuracy"] == 0.5
    assert s.loc["r2", "avg_tokens"] == 30
    assert s.loc["r1", "model"] == "a"


def test_confusion_has_all_labels():
    c = confusion(small_df(), "r1")
    assert c.loc["y", "x"] == 1
    assert c.loc["y", "y"] == 0


def test_worst_examples():
    w = worst_examples(small_df(), "r1", n=5)
    assert list(w["example_id"]) == [2]
