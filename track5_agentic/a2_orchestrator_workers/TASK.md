# A2: Orchestrator, parallel workers, and a critic

**Time:** 1 to 2 evenings · **Skill:** the multi agent pattern most real products use: one model
splits the job, several workers do parts at the same time, a critic checks the result.

## Example job
"Write a one page brief comparing 3 free LLM hosting options." The orchestrator splits it into
subtasks (one per option + one for the summary), workers write their parts in parallel, the
writer joins them, and the critic returns `{"ok": bool, "feedback": str}`. If not ok, the writer
fixes it using the feedback, at most `max_rounds` times.

## What you write in `orchestrator.py`
1. `split_task(job, llm) -> list[Subtask]`: structured output; at most `MAX_SUBTASKS`.
2. `run_workers(subtasks, worker, limit)`: async, at most `limit` at the same time (C8 semaphore);
   a failing worker gives `WorkerResult(ok=False, error=...)` and does NOT crash the others.
3. `review_loop(draft_fn, critic, max_rounds)`: draft, critique, redraft with feedback. Return the
   final text, the number of rounds, and whether the critic approved it.
4. `run_job(job, llm, worker, critic)`: glue. Report total model calls (you'll use this in A6).

## Done when
- [ ] `uv run pytest track5_agentic/a2_orchestrator_workers` passes.
- [ ] Your log compares: one big prompt vs orchestrator + workers. Quality? Time? Number of calls?
      (Multi agent is not always better. Write down when it's worth the extra calls.)
