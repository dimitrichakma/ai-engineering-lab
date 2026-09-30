import pytest

from track4_ui.u2_agent_ux.agent_steps import (
    SOURCES, ApprovalGate, render_citations, run_fake_agent, summarize_step,
)


def test_summarize_each_event():
    lines = [summarize_step(e) for e in run_fake_agent("refund policy")]
    assert "search_docs" in lines[0] and "refund policy" in lines[0]
    assert "2" in lines[1]
    assert "send_email" in lines[2]
    assert summarize_step({"type": "mystery"}) == "Working..."


def test_citations_drop_unknown_and_order():
    text, notes = render_citations("A [2]. B [1]. C [2] [5].", SOURCES)
    assert "[5]" not in text
    assert text == "A [2]. B [1]. C [2]."
    assert notes == ["[2] Ticket FAQ (page 1)", "[1] Refund policy (page 2)"]


def test_gate_flow():
    g = ApprovalGate()
    rid = g.request("send_email", {"to": "x@example.com"})
    assert g.status(rid) == "pending"
    g.decide(rid, approved=False)
    assert g.status(rid) == "rejected"
    with pytest.raises(ValueError):
        g.decide(rid, approved=True)
    with pytest.raises(KeyError):
        g.decide(999, approved=True)


def test_risky_actions():
    assert ApprovalGate.needs_approval("make_payment")
    assert not ApprovalGate.needs_approval("search_docs")
