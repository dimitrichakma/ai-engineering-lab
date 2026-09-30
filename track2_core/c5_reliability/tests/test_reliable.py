import pytest

from track2_core.c5_reliability.fakes import BadRequestError, FlakyModel, ModelTimeout
from track2_core.c5_reliability.reliable import (CircuitBreaker, CircuitOpenError, ReliableLLM,
                                     backoff_delay, call_with_retry)

no_sleep = lambda s: None  # noqa: E731


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def test_backoff_grows_and_is_capped():
    assert backoff_delay(0, rng=lambda: 1.0) == 0.5
    assert backoff_delay(3, rng=lambda: 1.0) == 4.0
    assert backoff_delay(10, rng=lambda: 1.0) == 8.0
    assert backoff_delay(3, rng=lambda: 0.0) == 0.0


def test_retry_succeeds_on_third_attempt():
    m = FlakyModel("p", [ModelTimeout(), ModelTimeout(), "ok"])
    assert call_with_retry(lambda: m.generate("hi"), sleep=no_sleep) == "ok"
    assert m.calls == 3


def test_bad_request_is_not_retried():
    m = FlakyModel("p", [BadRequestError()])
    with pytest.raises(BadRequestError):
        call_with_retry(lambda: m.generate("hi"), sleep=no_sleep)
    assert m.calls == 1


def test_breaker_opens_and_fails_fast():
    clock = FakeClock()
    br = CircuitBreaker(failure_threshold=3, reset_after=30, clock=clock)
    m = FlakyModel("p", [ModelTimeout()])
    for _ in range(3):
        with pytest.raises(ModelTimeout):
            br.call(lambda: m.generate("x"))
    assert br.state == "open"
    with pytest.raises(CircuitOpenError):
        br.call(lambda: m.generate("x"))
    assert m.calls == 3          # the model was NOT called while open


# TODO: after clock.t += 30 the state is "half_open"; one success closes it
# TODO: primary always down -> ReliableLLM answers from "fallback"
# TODO: primary works -> answer from "primary" and fallback.calls == 0
