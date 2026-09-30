from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from track5_agentic.a3_human_in_loop import graph as g


def fake_llm(prompt: str) -> str:
    return "KIND reply" if "kinder" in prompt else "reply"


def cfg(tid):
    return {"configurable": {"thread_id": tid}}


def test_pauses_before_sending():
    g.SENT.clear()
    app = g.build_graph(InMemorySaver(), fake_llm)
    out = app.invoke({"message": "Please refund 1200 taka"}, cfg("t1"))
    assert "__interrupt__" in out
    assert g.SENT == []
    payload = out["__interrupt__"][0].value
    assert payload["refund_amount"] == 1200


def test_approve_sends():
    g.SENT.clear()
    app = g.build_graph(InMemorySaver(), fake_llm)
    app.invoke({"message": "refund 500 taka"}, cfg("t2"))
    out = app.invoke(Command(resume={"approved": True}), cfg("t2"))
    assert out["sent"] is True
    assert g.SENT == [{"text": "reply", "amount": 500}]


def test_reject_revises_then_approve():
    g.SENT.clear()
    app = g.build_graph(InMemorySaver(), fake_llm)
    app.invoke({"message": "refund 300 taka"}, cfg("t3"))
    out = app.invoke(Command(resume={"approved": False, "note": "be kinder"}), cfg("t3"))
    assert "__interrupt__" in out
    assert out["__interrupt__"][0].value["draft"] == "KIND reply"
    app.invoke(Command(resume={"approved": True}), cfg("t3"))
    assert g.SENT[0]["text"] == "KIND reply"


def test_survives_restart_with_same_checkpointer():
    g.SENT.clear()
    saver = InMemorySaver()
    g.build_graph(saver, fake_llm).invoke({"message": "refund 700 taka"}, cfg("t4"))
    new_app = g.build_graph(saver, fake_llm)  # "restart": a new graph object, same saved state
    new_app.invoke(Command(resume={"approved": True}), cfg("t4"))
    assert g.SENT[0]["amount"] == 700
