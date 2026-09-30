# C4: Evals from scratch + judge calibration

**Time:** 1 to 2 evenings · **Rebuilds:** habit tracker `evaluation/metrics/custom_empathy.py`,
chatbot `evaluate.py`

## The idea
Your projects use an LLM as a judge (DeepEval, Ragas, a custom empathy metric). But who checks the
judge? Here you build a small judge yourself and then **measure how often it agrees with you**.
This is called judge calibration, and it's what makes an eval believable.

## The setup
`data/answers.jsonl` has 16 answers from a **bus ticket support bot**. Each has the customer
question, the policy text the bot should use, and the bot's answer. Some are good, some are wrong
or rude. The `human_label` field is **empty**: you fill it in.

## Steps
1. **Label first, before writing code.** Read each item and set `human_label` to `"pass"` or
   `"fail"`. Rule: pass only if the answer is correct per the policy AND polite. Write a one line
   reason in `human_reason`. Do this without AI help. That's the point.
2. `judge.py`: `JudgeResult` (verdict pass/fail, faithful: bool, polite: bool, reason) and
   `judge(item, llm=generate_json)`. Put a clear rubric in the prompt.
3. `calibrate.py`: run the judge on all items and print:
   - **agreement**: the share of items where judge verdict == your label
   - **Cohen's kappa** (agreement corrected for chance; write the formula yourself)
   - the list of disagreements, with both reasons side by side
4. Change ONE thing in the judge (for example, ask for the reasoning before the verdict, or add
   2 examples to the prompt). Re-run. Log both results.

## Done when
- [ ] All 16 items have your label and reason.
- [ ] `calibrate.py` prints agreement, kappa and the disagreements.
- [ ] Two judge versions compared in the log.
- [ ] `agreement()` and `cohens_kappa()` are unit tested with hand made numbers.

## Questions for your log
- On the disagreements: who was right, you or the judge? Did the judge find something you missed?
- Your habit tracker uses a stronger model (Opus) as judge than as worker (Sonnet). Why?
- What kappa would make you trust this judge to run in CI?
