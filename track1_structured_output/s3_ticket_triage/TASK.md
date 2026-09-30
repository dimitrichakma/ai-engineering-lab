# S3: Support ticket triage

**Time:** 1 to 2 evenings · **Concepts:** classification with enums, a labeled test set,
accuracy, a confusion matrix, comparing prompts.

## The idea
An online shop in Bangladesh gets customer messages in English, Bangla and Banglish.
Sort each message into a category and urgency, so the right team sees it first.

This is the first project where you **measure** the model instead of just looking at it.

## The model you design
```
Triage
  category: "delivery" | "payment" | "refund" | "product_issue" | "account" | "other"
  urgency: "low" | "medium" | "high"
  language: "english" | "bangla" | "banglish"
  summary: str          (one short English sentence)
```

## Steps
1. Write `Triage` in `models.py`.
2. Look at `data/tickets.csv`. It has 20 messages with the **correct** labels (the "gold" labels).
   Read them all. Do you agree with every label? Change any you disagree with; that's normal.
3. Write `classify(message) -> Triage` in `triage.py`.
4. Write `evaluate()`: run all 20, compare with the gold labels, print:
   - category accuracy and urgency accuracy
   - a small confusion matrix for category (gold vs predicted counts)
   - the list of wrong answers
5. Improve the prompt ONE change at a time (for example, add short definitions of each category).
   Re-run the eval after each change and write the numbers in your log.

## Done when
- [ ] `uv run python -m track1_structured_output.s3_ticket_triage.triage` prints accuracy and the confusion matrix.
- [ ] You tried at least 2 prompt versions and logged the numbers for each.
- [ ] `evaluate()` has a unit test that uses fake predictions (no LLM call).

## Stretch goals
- Add 10 more tickets yourself, especially hard ones.
- Add `confidence: float` (0 to 1) and check: is the model more often right when confidence is high?
