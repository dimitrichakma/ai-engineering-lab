import json
from pathlib import Path

from .chunkers import by_heading, fixed_size
from .search import BM25Index, VectorIndex, hybrid_search

DATA = Path(__file__).parent / "data"


def hit_at_k(results: list[str], answer_contains: str) -> bool:
    return any(answer_contains.lower() in r.lower() for r in results)


def run(name: str, search_fn, questions: list[dict]) -> dict:
    """search_fn(query, k) -> list of chunk texts. Return {"setup": name, "hit@1": .., "hit@3": .., "hit@5": ..}"""
    # TODO: for each question, search with k=5 once and check hits in the first 1, 3 and 5 results
    raise NotImplementedError


def main() -> None:
    text = (DATA / "handbook.md").read_text(encoding="utf-8")
    questions = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    # TODO: build the 5 setups from TASK.md, run each, print a table
    #       (Hint: build each index ONCE, embeddings are the slow part.)


if __name__ == "__main__":
    main()
