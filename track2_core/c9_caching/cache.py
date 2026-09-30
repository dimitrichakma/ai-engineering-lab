import hashlib
import json
import sqlite3
import time
from typing import Callable


def cache_key(model: str, prompt: str, settings: dict) -> str:
    # TODO: sha256 of json.dumps({"model":..., "prompt":..., "settings":...}, sort_keys=True)
    raise NotImplementedError


class ExactCache:
    def __init__(self, path: str = ":memory:", ttl_seconds: float = 86400,
                 clock: Callable[[], float] = time.time):
        # TODO: connect, create the table if it doesn't exist
        raise NotImplementedError

    def get(self, key: str) -> str | None:
        # TODO: None if missing OR older than ttl_seconds
        raise NotImplementedError

    def set(self, key: str, answer: str) -> None:
        # TODO: insert or replace, with created_at = clock()
        raise NotImplementedError


class SemanticCache:
    def __init__(self, embed_fn: Callable[[list[str]], list[list[float]]], threshold: float = 0.9):
        self.embed_fn = embed_fn
        self.threshold = threshold
        self.items: list[tuple[list[float], str, str]] = []   # (vector, question, answer)

    def get(self, question: str) -> tuple[str, float] | None:
        # TODO: embed the question, find the best cosine match, return (answer, score) if >= threshold
        raise NotImplementedError

    def set(self, question: str, answer: str) -> None:
        # TODO
        raise NotImplementedError


def cached_generate(prompt: str, llm: Callable[[str], str], exact: ExactCache,
                    semantic: SemanticCache | None, model: str = "qwen2.5:3b") -> tuple[str, str]:
    """Return (answer, source) with source in {"exact", "semantic", "model"}."""
    # TODO
    raise NotImplementedError
