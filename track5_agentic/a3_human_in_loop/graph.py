"""Refund agent with a human approval step. Packages: langgraph, langgraph-checkpoint-sqlite."""
from collections.abc import Callable
from typing import TypedDict

from langgraph.graph import END, START, StateGraph  # noqa: F401
from langgraph.types import Command, interrupt  # noqa: F401

AUTO_LIMIT = 0  # every refund needs review in this lab; try raising it later and think about risk

SENT: list[dict] = []  # the fake "email outbox"; tests read it


class State(TypedDict, total=False):
    message: str
    refund_amount: int
    draft: str
    review_note: str
    approved: bool
    sent: bool
    revisions: int


def classify(state: State) -> dict:
    # TODO: find an amount like "1200 taka" / "Tk 1200" in the message (regex is fine for now)
    raise NotImplementedError


def make_draft_reply(llm: Callable[[str], str]):
    def draft_reply(state: State) -> dict:
        # TODO: build a prompt from message, amount and review_note (if any); count revisions
        raise NotImplementedError
    return draft_reply


def human_review(state: State) -> dict:
    # TODO: decision = interrupt({"draft": ..., "refund_amount": ...})
    #       return {"approved": decision["approved"], "review_note": decision.get("note", "")}
    raise NotImplementedError


def send_reply(state: State) -> dict:
    # TODO: SENT.append({"text": state["draft"], "amount": state["refund_amount"]}); return {"sent": True}
    raise NotImplementedError


def build_graph(checkpointer, llm: Callable[[str], str]):
    # TODO: StateGraph(State); add the 4 nodes; START -> classify -> draft_reply -> human_review
    #       conditional edge: approved -> send_reply -> END, else -> draft_reply
    #       return graph.compile(checkpointer=checkpointer)
    raise NotImplementedError
