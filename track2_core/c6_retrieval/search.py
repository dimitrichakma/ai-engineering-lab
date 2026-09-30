import math
from typing import Callable

EMBED_MODEL = "nomic-embed-text"


def ollama_embed(texts: list[str]) -> list[list[float]]:
    import ollama
    return ollama.embed(model=EMBED_MODEL, input=texts).embeddings


def cosine(a: list[float], b: list[float]) -> float:
    # TODO: dot(a, b) / (|a| * |b|)
    raise NotImplementedError


class VectorIndex:
    def __init__(self, chunks: list[str], embed: Callable = ollama_embed):
        # TODO: keep chunks and their embeddings (embed ALL chunks in one call)
        raise NotImplementedError

    def search(self, query: str, k: int) -> list[str]:
        # TODO: embed the query, score every chunk, return the top k chunk texts
        raise NotImplementedError


class BM25Index:
    def __init__(self, chunks: list[str]):
        # TODO: from rank_bm25 import BM25Okapi; tokenize simply (lowercase, split on spaces)
        raise NotImplementedError

    def search(self, query: str, k: int) -> list[str]:
        # TODO
        raise NotImplementedError


def rrf(rankings: list[list[str]], k: int, c: int = 60) -> list[str]:
    """Reciprocal Rank Fusion. `rankings` = several ranked lists of chunk texts.
    score(chunk) = sum of 1 / (c + rank), rank starting at 1. Return the top k by score."""
    # TODO
    raise NotImplementedError


def hybrid_search(query: str, k: int, vec: VectorIndex, bm25: BM25Index,
                  depth: int = 10) -> list[str]:
    # TODO: take the top `depth` from each index, fuse with rrf, return top k
    raise NotImplementedError
