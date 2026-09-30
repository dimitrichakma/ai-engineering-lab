import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "pairs.csv"
THRESHOLDS = [0.80, 0.85, 0.90, 0.95]


def main() -> None:
    rows = list(csv.DictReader(DATA.open(encoding="utf-8")))
    # TODO: for each threshold:
    #   - a fresh SemanticCache with the real embed function (reuse search.ollama_embed from C6)
    #   - for each row: cache.set(cached_question, "ANSWER"), then cache.get(new_question)
    #     hit + label same -> correct hit; hit + label different -> WRONG hit; no hit -> miss
    #     (use a fresh cache per row so rows don't affect each other)
    #   - print: threshold | correct hits | wrong hits | misses
    _ = rows


if __name__ == "__main__":
    main()
