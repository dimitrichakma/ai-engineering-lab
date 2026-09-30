"""Given. A tiny in memory store. B2 replaces this with a real database."""
import itertools
from datetime import datetime, timezone

_ids = itertools.count(1)
APPLICATIONS: dict[int, dict] = {}
NOTES: dict[int, list[dict]] = {}


def now() -> datetime:
    return datetime.now(timezone.utc)


def next_id() -> int:
    return next(_ids)


def reset() -> None:
    global _ids
    _ids = itertools.count(1)
    APPLICATIONS.clear()
    NOTES.clear()
