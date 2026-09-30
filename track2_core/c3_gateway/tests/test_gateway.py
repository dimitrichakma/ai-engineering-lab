import asyncio
from datetime import date

import pytest

from track2_core.c3_gateway.gateway import (DailyBudget, GatewayError, GatewayTimeout, TokenBucket,
                                check_request, luhn_ok, mask_pii, with_timeout)


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def test_bucket_allows_burst_then_blocks_then_refills():
    clock = FakeClock()
    b = TokenBucket(capacity=3, refill_per_sec=1.0, clock=clock)
    assert [b.allow() for _ in range(4)] == [True, True, True, False]
    clock.t += 1.0
    assert b.allow() is True


def test_luhn():
    assert luhn_ok("4539578763621486")        # a valid test number
    assert not luhn_ok("1234567812345678")


def test_mask_pii():
    out = mask_pii("mail me at rina@example.com or call 01711000001, card 4539 5787 6362 1486")
    assert "<EMAIL>" in out and "<PHONE>" in out and "<CARD>" in out
    assert "01711000001" not in out


def test_invalid_luhn_number_is_not_masked():
    assert "1234567812345678" in mask_pii("order ref 1234567812345678")


def test_timeout():
    async def slow():
        await asyncio.sleep(1)
    with pytest.raises(GatewayTimeout):
        asyncio.run(with_timeout(slow(), 0.05))


def test_size_cap_gives_413():
    b = TokenBucket(10, 1)
    with pytest.raises(GatewayError) as e:
        check_request(1, "x" * 5000, b, DailyBudget(1000), date.today())
    assert e.value.status_code == 413


# TODO: budget exceeded -> 429
# TODO: rate limit hit -> 429 BEFORE the size check runs (order matters: why?)
# TODO: +8801711000001 is masked too
