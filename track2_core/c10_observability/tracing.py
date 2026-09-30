import contextvars
import json
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

TRACE_FILE = Path("traces.jsonl")

_trace_id: contextvars.ContextVar[str | None] = contextvars.ContextVar("trace_id", default=None)
_current: contextvars.ContextVar["Span | None"] = contextvars.ContextVar("span", default=None)


def new_trace() -> str:
    # TODO: make a uuid4 hex, store it in _trace_id, return it
    raise NotImplementedError


class Span:
    def __init__(self, name: str, parent_id: str | None, attrs: dict):
        self.id = uuid.uuid4().hex[:12]
        self.name = name
        self.parent_id = parent_id
        self.attrs = dict(attrs)

    def set(self, **attrs) -> None:
        self.attrs.update(attrs)


def current_span() -> Span | None:
    return _current.get()


def write_record(record: dict, path: Path = TRACE_FILE) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


@contextmanager
def span(name: str, sink=write_record, **attrs):
    """Usage:
        with span("retrieve", k=5):
            ...
            current_span().set(tokens_in=120)
    """
    # TODO 1: parent = current_span(); s = Span(name, parent.id if parent else None, attrs)
    # TODO 2: token = _current.set(s); start = time.perf_counter()
    # TODO 3: yield s inside try/except/finally:
    #           on exception: status "error", error message; RE-RAISE it
    #           finally: duration_ms, _current.reset(token), sink({...record...})
    #   record keys: trace_id, span_id, parent_id, name, start_ts, duration_ms, status, error, **attrs
    raise NotImplementedError
    yield  # noqa (keeps this a generator until you write it)
