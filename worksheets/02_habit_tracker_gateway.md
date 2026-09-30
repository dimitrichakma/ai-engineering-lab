# Worksheet 2: Gateway · habit tracker `src/main.py`

Look at: `_apply_gateway_checks`, `mask_pii`, `_mask_cards`, `_luhn_ok`, `_telegram_rate_ok`,
`_budget_exceeded`, `_invoke_agent`, `_sum_usage`, the slowapi limiter setup.

## Questions
1. List the gateway checks in order for `POST /chat`. Why is there one shared function for `/chat` and `/chat/stream`?
2. Which HTTP status code does each check return (size, budget, rate limit)?
3. Why are card numbers masked before phone numbers?
4. A 16 digit order reference number is in a message. Is it masked? What decides?
5. PII masking crashes. Does the request go through? Why that choice?
6. The token budget lookup crashes. Does the request go through? Why is this different from question 5?
7. Why can't slowapi rate limit the Telegram webhook by chat id? What was built instead, and how does it work?
8. The rate limiter is in memory. What breaks if you run two backend instances?
9. Why does the token count come from a callback and not from `result["messages"]`? Which model calls would be missed otherwise?
10. What happens when the agent takes longer than `AGENT_TIMEOUT_SECONDS`? Why is the streaming timeout longer?
11. Where does the user id come from for Telegram messages?

## Draw it
A Telegram message and a web chat message, side by side, through every check.

## Interview answer
"How do you control cost and abuse in an LLM app?"

## Compare with C3 of the lab
Token bucket (yours) vs sliding window (habit tracker): which allows short bursts? Which would you use for Somajji?
