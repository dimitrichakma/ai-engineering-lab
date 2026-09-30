"""Agent UX logic (no Streamlit here)."""
import itertools
import re
from collections.abc import Iterator

RISKY = {"send_email", "delete_record", "make_payment"}

SOURCES = [
    {"id": 1, "title": "Refund policy", "page": 2},
    {"id": 2, "title": "Ticket FAQ", "page": 1},
]


def run_fake_agent(question: str) -> Iterator[dict]:
    """Given. A fake agent so the UI works with no model."""
    yield {"type": "tool_call", "tool": "search_docs", "args": {"query": question}}
    yield {"type": "tool_result", "tool": "search_docs", "result": SOURCES}
    yield {"type": "needs_approval", "action": "send_email",
           "args": {"to": "customer@example.com", "subject": "Your refund"}}
    yield {"type": "answer",
           "text": "Refunds take 7 days [1]. Cancel within 24 hours for a full refund [2] [5].",
           "sources": SOURCES}


def summarize_step(event: dict) -> str:
    # TODO: tool_call -> "🔎 Using <tool>: <first arg value>"
    #       tool_result -> "✅ <tool> returned <n> results" (n = len(result) if it's a list, else 1)
    #       needs_approval -> "✋ Needs your approval: <action>"
    #       answer -> "💬 Answer ready"
    #       anything else -> "Working..."
    raise NotImplementedError


CITE = re.compile(r"\s?\[(\d+)\]")


def render_citations(text: str, sources: list[dict]) -> tuple[str, list[str]]:
    # TODO: for each [n] in text: if n is a known source id keep it, else remove it (with its space).
    #       footnotes: "[n] <title> (page <page>)" in order of FIRST use, no duplicates
    raise NotImplementedError


class ApprovalGate:
    def __init__(self):
        self._ids = itertools.count(1)
        self.requests: dict[int, dict] = {}

    def request(self, action: str, args: dict) -> int:
        # TODO: store {"action", "args", "status": "pending"} under a new id; return the id
        raise NotImplementedError

    def decide(self, request_id: int, approved: bool) -> None:
        # TODO: KeyError if unknown id; ValueError if already decided; else set approved/rejected
        raise NotImplementedError

    def status(self, request_id: int) -> str:
        # TODO
        raise NotImplementedError

    @staticmethod
    def needs_approval(action: str) -> bool:
        return action in RISKY
