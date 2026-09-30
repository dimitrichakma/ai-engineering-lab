import asyncio
import time

from pydantic import BaseModel

from .fake_llm import FakeAsyncLLM


class Result(BaseModel):
    index: int
    ok: bool
    label: str | None = None
    error: str | None = None


async def run_sequential(items: list[str], llm) -> list[Result]:
    # TODO: await llm.classify(item) one by one; catch errors into Result(ok=False)
    raise NotImplementedError


async def run_concurrent(items: list[str], llm, limit: int) -> list[Result]:
    # TODO 1: sem = asyncio.Semaphore(limit)
    # TODO 2: async def one(i, text): async with sem: try classify -> Result(ok=True) except -> ok=False
    # TODO 3: return await asyncio.gather(*(one(i, t) for i, t in enumerate(items)))
    #         (Does gather keep the order? Check the docs, then test it.)
    raise NotImplementedError


async def benchmark(n: int = 40, delay: float = 0.1) -> None:
    items = [f"text {i} is good" if i % 2 else f"text {i}" for i in range(n)]
    # TODO: time run_sequential and run_concurrent with limits 2, 4, 8, 16
    #       (a NEW FakeAsyncLLM for each run) and print: setup | seconds | max_running
    _ = (items, time, FakeAsyncLLM)


if __name__ == "__main__":
    asyncio.run(benchmark())
