"""A tiny job queue on SQLite. Plain sqlite3 so every SQL statement is visible to you."""
import json
import sqlite3
import time
import uuid
from typing import Callable

MAX_ATTEMPTS = 3

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    input TEXT NOT NULL,
    status TEXT NOT NULL,
    result TEXT,
    error TEXT,
    idempotency_key TEXT UNIQUE,
    attempts INTEGER NOT NULL DEFAULT 0,
    created_at REAL NOT NULL,
    updated_at REAL NOT NULL
)
"""


class JobStore:
    def __init__(self, path: str = "jobs.db", clock: Callable[[], float] = time.time):
        self.conn = sqlite3.connect(path, isolation_level=None, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(SCHEMA)
        self.clock = clock

    def enqueue(self, kind: str, input: dict, idempotency_key: str | None = None) -> dict:
        # TODO: if idempotency_key exists already, return that job
        #       else insert a new job with status "queued"
        raise NotImplementedError

    def get(self, job_id: str) -> dict | None:
        # TODO
        raise NotImplementedError

    def claim_next(self) -> dict | None:
        """Atomically move the oldest queued job to running, add 1 to `attempts`, and return it.
        Hint: BEGIN IMMEDIATE ... SELECT ... UPDATE ... COMMIT, or a single
        UPDATE ... WHERE id = (SELECT ...) RETURNING * (SQLite 3.35+)."""
        # TODO
        raise NotImplementedError

    def finish(self, job_id: str, result: dict) -> None:
        # TODO
        raise NotImplementedError

    def fail(self, job_id: str, error: str) -> None:
        """attempts is already counted in claim_next. Below MAX_ATTEMPTS -> back to queued; else -> failed."""
        # TODO
        raise NotImplementedError


_ = (json, uuid)
