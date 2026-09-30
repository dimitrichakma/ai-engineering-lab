# S2: Job post extractor

**Time:** 1 to 2 evenings · **Concepts:** nested models, lists, enums, field descriptions,
"do not invent" rules, batch processing, CSV export.

## The idea
Job posts are long and messy. Turn each one into a clean `JobPost` so you can compare jobs in a
spreadsheet. Useful for your own job search too.

Samples in `data/` are made up. Later you can paste real public job posts you are interested in.

## The models you design (in `models.py`)
```
Salary          min_bdt: int | None, max_bdt: int | None, period: "month" | "year" | None
Requirement     skill: str, required: bool   (True = must have, False = nice to have)
JobPost
  title: str
  company: str
  location: str | None
  work_mode: "onsite" | "hybrid" | "remote" | "unknown"
  min_experience_years: float | None
  requirements: list[Requirement]
  salary: Salary | None
  deadline_text: str | None
```

## Steps
1. Write `Salary`, `Requirement` and `JobPost`. Nested models are just classes used as field types.
2. Look at the JSON schema. Find where `Requirement` appears (hint: `$defs`).
3. Write the prompt. Key rule: **if the post doesn't say it, return null. Do not guess the salary.**
4. Parse `job_1.txt` first. Check each field by hand against the text.
5. Run all posts and write `jobs.csv` with one row per job. Put requirements in one cell,
   joined by `; `.
6. Run the tests.

## Done when
- [ ] All 3 sample posts parse.
- [ ] `job_2.txt` (no salary in the text) gives `salary = None`, not a made up number.
- [ ] `jobs.csv` opens correctly in a spreadsheet.
- [ ] A validator makes sure `salary.min_bdt <= salary.max_bdt` when both exist (tested).

## Stretch goals
- Add `match_score(job, my_skills)` that returns the share of required skills you have.
- Compare a 3B local model with Gemini on the same posts. Which fields differ?
