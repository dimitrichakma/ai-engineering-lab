import pytest

from track6_models.m1_model_selection.compare import Result, pick, score


def r(pred, gold="payment", valid=True, ms=100, tok=10, sec=0.5):
    return Result(model="m", example_id=1, gold=gold, pred=pred, valid_json=valid,
                  latency_ms=ms, output_tokens=tok, gen_seconds=sec)


def test_score_counts_invalid_as_wrong():
    s = score([r("payment"), r(None, valid=False), r("refund"), r("payment")])
    assert s["accuracy"] == 0.5
    assert s["valid_json_rate"] == 0.75
    assert s["tokens_per_s"] == pytest.approx(20.0)


def test_score_latency():
    s = score([r("payment", ms=m) for m in [100, 200, 300, 400, 1000]])
    assert s["p50_ms"] == 300
    assert s["p95_ms"] == 1000


def test_pick_respects_latency_and_ties():
    scores = {
        "big": {"accuracy": 0.9, "p95_ms": 5000},
        "mid": {"accuracy": 0.8, "p95_ms": 1500},
        "fast": {"accuracy": 0.8, "p95_ms": 900},
    }
    assert pick(scores, max_p95_ms=2000) == "fast"
    assert pick(scores, max_p95_ms=10000) == "big"
    assert pick(scores, max_p95_ms=100) is None
