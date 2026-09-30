"""A fake request pipeline to produce traces. No model needed."""
import random
import time

from .tracing import current_span, new_trace, span

PRICE_PER_1K_TOKENS = 0.002  # pretend price, just for the dashboard


def guard(text: str) -> None:
    time.sleep(random.uniform(0.01, 0.05))


def retrieve(text: str) -> list[str]:
    time.sleep(random.uniform(0.05, 0.2))
    if random.random() < 0.05:
        raise TimeoutError("vector store timeout")
    return ["chunk a", "chunk b"]


def generate(text: str, chunks: list[str]) -> str:
    time.sleep(random.uniform(0.2, 0.8))
    if random.random() < 0.05:
        raise RuntimeError("model error")
    return "answer"


def handle_request(text: str) -> str | None:
    new_trace()
    # TODO: wrap the whole request in span("request"), and each step in its own span.
    #       In the generate span, set tokens_in, tokens_out (make up realistic numbers)
    #       and cost_usd. Catch the error at the request level so the loop continues,
    #       but make sure the error is still recorded in the spans.
    _ = (guard, retrieve, generate, current_span, span, PRICE_PER_1K_TOKENS)
    return None


if __name__ == "__main__":
    for i in range(50):
        handle_request(f"question {i}")
    print("wrote traces.jsonl")
