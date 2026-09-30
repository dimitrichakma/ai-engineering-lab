# A4: Code running agent (with limits)

**Time:** 2 evenings · **Skill:** letting a model write Python to answer questions about data, and
running that code with limits so a bad script can't hang or harm your machine.

## The job
"Which city had the highest total sales in March?" over `data/sales.csv`. The model writes pandas
code, you run it, and if it errors, the model sees the error and tries again (max 3 attempts).

## Safety: be honest about what this is
A subprocess with limits is **not** a real security sandbox. It stops accidents (infinite loops,
huge memory, reading your `.env`), not a determined attacker. For untrusted users, run code in a
throwaway container with no network. Write this in your log; interviewers ask about it.

## What you write in `sandbox.py`
`run_code(code, workdir, timeout_s=5, memory_mb=1024) -> RunResult`:
- write the code to a file inside a fresh temporary `workdir` and run `python -I` (isolated mode)
  with `cwd=workdir`
- **empty environment** except `PATH` (so no API keys leak), and `timeout_s` (kill on timeout)
- memory limit with `resource.setrlimit(RLIMIT_AS, ...)` in `preexec_fn` on Linux. This limits
  VIRTUAL memory, and importing pandas alone reserves a few hundred MB, so 1024 MB is a safe default. On macOS this
  limit is not enforced well: note it, and rely on the timeout there.
- cut stdout/stderr to `MAX_OUTPUT` characters (a model printing a 1 GB table must not crash you)

## What you write in `agent.py`
`answer(question, csv_path, llm, max_attempts=3)`: copy the CSV into the workdir, ask the model
for code (show it the column names and 3 rows, not the whole file), run it, feed errors back.
Return the answer, the final code, and the number of attempts.

## Done when
- [ ] `uv run pytest track5_agentic/a4_code_agent` passes.
- [ ] 5 questions about `sales.csv` answered correctly (check them by hand once).
