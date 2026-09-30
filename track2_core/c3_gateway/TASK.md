# C3: Gateway by hand

**Time:** 1 to 2 evenings · **Rebuilds:** habit tracker `src/main.py` (`_apply_gateway_checks`,
`mask_pii`, `_telegram_rate_ok`, `_budget_exceeded`, `_invoke_agent`)

## The idea
Before any message reaches the model, your habit tracker runs checks **in a fixed order**:
size cap → PII masking → daily token budget, with a rate limit before and a hard timeout around
the agent. No LLM is needed for any of this, which is exactly why it's a good place for rules.

You rebuild each piece as plain Python, with a **token bucket** rate limiter (your habit tracker
uses slowapi plus a sliding window, so this is a new design to compare).

## What you write in `gateway.py`
1. `TokenBucket(capacity, refill_per_sec, clock)`: `allow() -> bool`.
   Pass `clock` in (a function returning seconds) so tests can control time.
2. `mask_pii(text)`: emails → `<EMAIL>`, Bangladeshi mobile numbers (`01XXXXXXXXX`,
   `+8801XXXXXXXXX`) → `<PHONE>`, Luhn valid card numbers (13 to 19 digits) → `<CARD>`.
   Mask cards FIRST. Why? Your habit tracker's docstring explains it.
3. `DailyBudget(max_tokens)`: `record(user_id, tokens, day)`, `exceeded(user_id, day) -> bool`.
4. `async with_timeout(coro, seconds)`: returns the result, or raises `GatewayTimeout`.
5. `check_request(user_id, text, ...) -> str`: runs the checks in order and returns the masked text,
   or raises `GatewayError(status_code, message)` with 429 (rate), 413 (size), 429 (budget).

## Fail open or fail closed? (write your answers in the log)
Your habit tracker makes a deliberate choice for each check:
- PII masking error → **fail closed** (block).
- Rate limiter bug → **fail open** (allow).
- Budget read error → **fail open** (allow).
Why is each one chosen that way? Would you choose the same for Somajji?

## Done when
- [ ] Token bucket tests pass with a fake clock (burst, then refill over time).
- [ ] PII tests pass, including a 16 digit number that is NOT Luhn valid staying unmasked.
- [ ] `check_request` raises the right status code for each failure, in the right order.
- [ ] All tests pass.

## Stretch
- Add a sliding window limiter too and compare: which allows bursts? Which is fairer?
