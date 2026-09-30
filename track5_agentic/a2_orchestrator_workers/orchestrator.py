"""Orchestrator + parallel workers + critic."""
import asyncio  # noqa: F401
from collections.abc import Awaitable, Callable

from pydantic import BaseModel

MAX_SUBTASKS = 5


class Subtask(BaseModel):
    id: int
    instruction: str


class WorkerResult(BaseModel):
    subtask_id: int
    ok: bool
    text: str = ""
    error: str = ""


class Review(BaseModel):
    ok: bool
    feedback: str = ""


class ReviewOutcome(BaseModel):
    text: str
    rounds: int
    approved: bool


Worker = Callable[[Subtask], Awaitable[str]]


def split_task(job: str, llm: Callable[[str, dict], str]) -> list[Subtask]:
    # TODO: ask llm for {"subtasks": [...]} with structured output; keep at most MAX_SUBTASKS
    raise NotImplementedError


async def run_workers(subtasks: list[Subtask], worker: Worker, limit: int = 3) -> list[WorkerResult]:
    # TODO: asyncio.Semaphore(limit); gather; catch exceptions per worker; keep input order
    raise NotImplementedError


def review_loop(
    draft_fn: Callable[[str], str],      # draft_fn(feedback) -> text ("" feedback on first round)
    critic: Callable[[str], Review],
    max_rounds: int = 3,
) -> ReviewOutcome:
    # TODO
    raise NotImplementedError


async def run_job(job, llm, worker, critic) -> dict:
    # TODO: split -> run_workers -> join ok parts -> review_loop -> return text + stats
    raise NotImplementedError
