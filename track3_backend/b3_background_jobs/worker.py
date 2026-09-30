"""Run: uv run python -m track3_backend.b3_background_jobs.worker"""
import time
from typing import Callable

from .jobs import JobStore


def analyse_job_post(input: dict) -> dict:
    # TODO: reuse your S2 extractor on input["text"]; return the JobPost as a dict
    raise NotImplementedError


HANDLERS: dict[str, Callable[[dict], dict]] = {"analyse_job_post": analyse_job_post}


def run_once(store: JobStore, handlers: dict = HANDLERS) -> bool:
    """Claim one job and run it. Return False if there was nothing to do."""
    # TODO: claim_next; call the handler; finish or fail
    raise NotImplementedError


def main(poll_seconds: float = 1.0) -> None:
    store = JobStore()
    while True:
        if not run_once(store):
            time.sleep(poll_seconds)


if __name__ == "__main__":
    main()
