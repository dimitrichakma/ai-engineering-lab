# A1: Plan and execute, with replanning ⭐

**Time:** 1 to 2 evenings · **Skill:** an agent that writes a plan FIRST, checks it, runs it step by
step, and makes a new plan when a step fails.

## Why not just a tool loop (C1)?
A tool loop decides one step at a time and easily wanders. A plan can be checked before anything
runs (unknown tools? steps in a loop?), shown to a user, and repaired when reality differs.

## The plan (Pydantic, given in `planner.py`)
`Step(id, tool, args, depends_on: list[int])` and `Plan(goal, steps)`.
The model produces it with structured output (Track 1 skills).

## What you write in `planner.py`
1. `validate_plan(plan, tools) -> list[str]`: problems as text. Check: unknown tool, duplicate step
   ids, `depends_on` pointing to a missing step, and cycles. Empty list = valid.
2. `order_steps(plan) -> list[Step]`: a topological order (a step comes after its dependencies).
3. `execute(plan, tools, replan, max_replans=2) -> RunResult`:
   - run steps in order; a step's args may use `"$<id>"` to mean "the result of step id"
     (use the given `resolve_args`)
   - on an exception, call `replan(plan, failed_step, error, results_so_far)` which returns a
     new Plan; validate it and continue with the new plan, keeping the results you already have
   - stop with `status="failed"` after `max_replans`
4. `make_plan(goal, tools, llm)`: ask the model for a Plan JSON (try it with Ollama after the tests pass).

## Done when
- [ ] `uv run pytest track5_agentic/a1_plan_execute` passes.
- [ ] With the real model: a goal like "find the cheapest flight in flights.csv and convert the
      price to BDT" gives a valid plan. Try 5 goals and count how many plans pass validation.
