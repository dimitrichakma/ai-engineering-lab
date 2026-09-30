"""Compare embedding models on the C6 handbook.
uv run python -m track6_models.m2_embeddings.compare_embeddings"""
import json  # noqa: F401
from pathlib import Path

C6 = Path(__file__).parents[2] / "track2_core" / "c6_retrieval" / "data"
MODELS = ["nomic-embed-text", "mxbai-embed-large", "all-minilm"]


def embed_all(model: str, texts: list[str], batch: int = 16) -> tuple[list[list[float]], float]:
    # TODO: return (vectors, seconds)
    raise NotImplementedError


def cosine(a: list[float], b: list[float]) -> float:
    # TODO (or import yours from C6)
    raise NotImplementedError


def rank(query_vec: list[float], chunk_vecs: list[list[float]]) -> list[int]:
    # TODO: indexes sorted by cosine, highest first
    raise NotImplementedError


def hit_at_k(ranked_hits: list[bool], k: int) -> bool:
    # TODO: any correct chunk in the first k
    raise NotImplementedError


def mrr(all_ranked_hits: list[list[bool]]) -> float:
    # TODO: mean over questions of 1/rank of the FIRST correct chunk (0 if none)
    raise NotImplementedError


def main():
    # TODO: chunks = by_heading(handbook text) (import from track2_core.c6_retrieval.chunkers)
    #       for each model: embed chunks and questions, rank, compute hit@1, hit@3, MRR, dims, time
    pass


if __name__ == "__main__":
    main()
