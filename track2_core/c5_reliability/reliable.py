import random
import time
from typing import Callable, TypeVar

from .fakes import FlakyModel, RetryableError

T = TypeVar("T")


def backoff_delay(attempt: int, base: float = 0.5, cap: float = 8.0,
                  rng: Callable[[], float] = random.random) -> float:
    """attempt 0, 1, 2 ... -> random delay in [0, min(cap, base * 2**attempt)]."""
    # TODO
    raise NotImplementedError


def call_with_retry(fn: Callable[[], T], max_attempts: int = 3,
                    sleep: Callable[[float], None] = time.sleep) -> T:
    # TODO: try fn(); on RetryableError sleep(backoff_delay(attempt)) and try again.
    #       Any other exception -> raise at once. After max_attempts -> raise the last error.
    raise NotImplementedError


class CircuitOpenError(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3, reset_after: float = 30.0,
                 clock: Callable[[], float] = time.monotonic):
        # TODO: state = "closed", failure count, time it opened
        raise NotImplementedError

    @property
    def state(self) -> str:
        # TODO: "open" becomes "half_open" once reset_after seconds have passed
        raise NotImplementedError

    def call(self, fn: Callable[[], T]) -> T:
        # TODO:
        #  open       -> raise CircuitOpenError without calling fn
        #  half_open  -> allow ONE call: success -> closed; failure -> open again (reset timer)
        #  closed     -> call fn; success resets the count; failure counts up; at threshold -> open
        raise NotImplementedError


class ReliableLLM:
    def __init__(self, primary: FlakyModel, fallback: FlakyModel,
                 breaker: CircuitBreaker | None = None, max_attempts: int = 3,
                 sleep: Callable[[float], None] = time.sleep):
        # TODO
        raise NotImplementedError

    def generate(self, prompt: str) -> tuple[str, str]:
        """Return (text, "primary" | "fallback")."""
        # TODO: breaker.call(lambda: call_with_retry(lambda: primary.generate(prompt), ...))
        #       on any failure (incl. CircuitOpenError) -> fallback.generate(prompt)
        raise NotImplementedError
