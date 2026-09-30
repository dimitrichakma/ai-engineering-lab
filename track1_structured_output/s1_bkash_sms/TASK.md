# S1: Mobile money SMS parser

**Time:** 1 to 2 evenings · **Concepts:** Pydantic basics, `Optional`, `Literal`, `Field`,
validation errors, a simple retry.

## The idea
bKash and Nagad send an SMS for every transaction, in slightly different formats. Turn each SMS
into a clean `Transaction` object you could put in a spreadsheet.

All sample messages in `data/sms_samples.txt` are **made up**. Never use your real SMS or account numbers.

## The model you design (in `models.py`)
| Field | Type | Notes |
| --- | --- | --- |
| provider | `Literal["bkash", "nagad", "unknown"]` | |
| kind | `Literal["send_money", "cash_in", "cash_out", "payment", "received", "other"]` | |
| amount_bdt | `float` | must be > 0 |
| fee_bdt | `float \| None` | None if the SMS has no fee |
| counterparty | `str \| None` | number or merchant name, as written |
| balance_bdt | `float \| None` | balance after the transaction |
| trx_id | `str \| None` | |
| date_text | `str \| None` | keep the date as written for now |

## Steps
1. Write the model in `models.py`. Use `Field(description=...)` on every field; the model reads these.
2. Print `Transaction.model_json_schema()` and look at it.
3. In `parser.py`, write the prompt (TODO) and `parse_sms()`.
4. Make the FIRST sample work. Print the object.
5. Run all samples with `uv run python -m track1_structured_output.s1_bkash_sms.parser`. Count how many parse on the first try.
6. Add a retry: if `ValidationError`, try once more. Count again.
7. Run `uv run pytest track1_structured_output/s1_bkash_sms`.

## Done when
- [ ] At least 8 of 10 samples parse into valid `Transaction` objects.
- [ ] `amount_bdt` rejects 0 and negative numbers (tested).
- [ ] The script prints a summary: `parsed 9/10, retries used 2`.

## Stretch goals
- Convert `date_text` to a real `datetime` with a validator.
- Write the results to `transactions.csv`.
- Add 3 samples written in Bangla. What changes?
