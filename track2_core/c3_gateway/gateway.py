import asyncio
import re
import time
from collections import defaultdict
from datetime import date
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")

MAX_MESSAGE_CHARS = 1000


class GatewayError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class GatewayTimeout(Exception):
    pass


# ---------- 1. Token bucket ----------
class TokenBucket:
    """`capacity` tokens max; refills `refill_per_sec` tokens per second; each allow() costs 1."""

    def __init__(self, capacity: int, refill_per_sec: float,
                 clock: Callable[[], float] = time.monotonic):
        # TODO: store settings; start full; remember the last refill time
        raise NotImplementedError

    def allow(self) -> bool:
        # TODO: refill based on time passed (never above capacity), then spend 1 token if possible
        raise NotImplementedError


# ---------- 2. PII masking ----------
EMAIL_RE = re.compile(r"")      # TODO
BD_PHONE_RE = re.compile(r"")   # TODO: 01XXXXXXXXX and +8801XXXXXXXXX
CARD_CANDIDATE_RE = re.compile(r"")  # TODO: 13-19 digits, optional spaces or dashes


def luhn_ok(digits: str) -> bool:
    # TODO: the Luhn check (look it up, then write it yourself)
    raise NotImplementedError


def mask_pii(text: str) -> str:
    # TODO: cards first (only if luhn_ok), then emails, then phones
    raise NotImplementedError


# ---------- 3. Daily token budget ----------
class DailyBudget:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self._used: dict[tuple[int, date], int] = defaultdict(int)

    def record(self, user_id: int, tokens: int, day: date) -> None:
        # TODO
        raise NotImplementedError

    def exceeded(self, user_id: int, day: date) -> bool:
        # TODO
        raise NotImplementedError


# ---------- 4. Timeout ----------
async def with_timeout(coro: Awaitable[T], seconds: float) -> T:
    # TODO: asyncio.wait_for; convert the timeout into GatewayTimeout
    raise NotImplementedError


# ---------- 5. All checks in order ----------
def check_request(user_id: int, text: str, bucket: TokenBucket, budget: DailyBudget,
                  today: date) -> str:
    """Rate limit -> size cap -> PII masking -> budget. Return masked text or raise GatewayError."""
    # TODO
    raise NotImplementedError
