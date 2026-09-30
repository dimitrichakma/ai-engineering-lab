import pytest

from track5_agentic.a6_agent_eval.agent_eval import (
    DATA, cost_usd, in_order, load_jsonl, score_case, summarize,
)

CASES = {c["case_id"]: c for c in load_jsonl(DATA / "cases.jsonl")}
TRACES = {t["case_id"]: t for t in load_jsonl(DATA / "sample_traces.jsonl")}


def test_in_order():
    assert in_order(["a", "b"], ["x", "a", "y", "b"])
    assert not in_order(["a", "b"], ["b", "a"])
    assert in_order([], ["x"])


def test_cost():
    assert cost_usd({"tokens_in": 1_000_000, "tokens_out": 1_000_000}) == pytest.approx(0.50)


def test_clean_case():
    s = score_case(CASES["c1"], TRACES["c1"])
    assert s.success and s.tool_precision == 1.0 and s.tool_recall == 1.0 and s.forbidden_calls == 0


def test_extra_tool_lowers_precision():
    s = score_case(CASES["c3"], TRACES["c3"])
    assert s.success and s.tool_precision == 0.5


def test_wrong_answer_good_path():
    s = score_case(CASES["c4"], TRACES["c4"])
    assert not s.success and s.tool_recall == 1.0


def test_forbidden_tool_counted():
    s = score_case(CASES["c6"], TRACES["c6"])
    assert s.forbidden_calls == 1


def test_summary():
    scores = [score_case(CASES[k], TRACES[k]) for k in CASES]
    out = summarize(scores)
    assert out["success_rate"] == pytest.approx(5 / 6)
    assert out["forbidden_calls"] == 1
    assert out["total_cost_usd"] > 0
