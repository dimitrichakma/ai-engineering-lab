import asyncio
import time

from track2_core.c8_async.batch import run_concurrent
from track2_core.c8_async.fake_llm import FakeAsyncLLM


def test_concurrency_limit_is_respected():
    llm = FakeAsyncLLM(delay=0.02)
    asyncio.run(run_concurrent([f"t{i}" for i in range(20)], llm, limit=4))
    assert llm.max_running <= 4


def test_concurrent_is_faster():
    llm = FakeAsyncLLM(delay=0.05)
    start = time.perf_counter()
    asyncio.run(run_concurrent([f"t{i}" for i in range(20)], llm, limit=10))
    assert time.perf_counter() - start < 0.5     # sequential would take about 1.0 s


def test_one_failure_does_not_break_the_batch():
    llm = FakeAsyncLLM(delay=0.0, fail_every=3)
    results = asyncio.run(run_concurrent([f"t{i}" for i in range(9)], llm, limit=3))
    assert sum(not r.ok for r in results) == 3
    assert sum(r.ok for r in results) == 6


# TODO: results come back in input order (check r.index == position)
# TODO: run_sequential never has max_running above 1
