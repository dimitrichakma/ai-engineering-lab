# C5: Reliability (retries, fallback, circuit breaker)

**Time:** 1 to 2 evenings · **Fills a gap:** your projects have timeouts and fail safe behaviour,
but no retry with backoff, no fallback model and no circuit breaker.

## The idea
Real model APIs fail: timeouts, rate limits (429), server errors (5xx). A reliable app:
1. **Retries** errors that may pass (timeout, 429, 5xx) with **exponential backoff + jitter**.
2. **Does not retry** errors that won't pass (400 bad request, 401 auth).
3. **Falls back** to a second model when the main one keeps failing.
4. Uses a **circuit breaker**: after many failures in a row, stop calling the broken model for a
   while (fail fast), then let one test call through ("half open").

## What is given
`fakes.py`: `FlakyModel`, a fake model that fails in a pattern you choose, and error classes.
No real API calls, so you can test everything in milliseconds.

## What you write in `reliable.py`
1. `backoff_delay(attempt, base=0.5, cap=8.0, rng=random.random) -> float`
   Exponential with "full jitter": a random value between 0 and `min(cap, base * 2**attempt)`.
2. `call_with_retry(fn, max_attempts=3, sleep=time.sleep)`: retry only `RetryableError`.
3. `CircuitBreaker(failure_threshold=3, reset_after=30, clock=time.monotonic)`:
   states `closed → open → half_open → closed`. `call(fn)` raises `CircuitOpenError` when open.
4. `ReliableLLM(primary, fallback, ...)`.`generate(prompt)`: breaker + retry on the primary,
   then the fallback. Return which model answered.

## Done when
- [ ] A model that fails twice with `TimeoutError` then works → succeeds on attempt 3.
- [ ] `BadRequestError` is raised at once, never retried.
- [ ] After 3 failures the breaker opens; calls fail fast without touching the model;
      after `reset_after` seconds one call is allowed through.
- [ ] Primary always down → the fallback answers, and the result says `"fallback"`.
- [ ] All tests use `sleep=lambda s: None` and a fake clock, so they run instantly.

## Questions for your log
- Why jitter? What happens when 1,000 clients retry at exactly the same moment?
- Should Somajji's risk classifier use a fallback model, or fail safe (treat as high risk)? Why?
