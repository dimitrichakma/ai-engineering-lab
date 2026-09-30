# B3: Long running jobs

**Time:** 1 to 2 evenings · **Skill:** handling AI work that takes longer than an HTTP request should.

## The problem
"Analyse this job post against my CV" can take 30 to 120 seconds with a local model. If the API
waits, the request times out, the user clicks again, and now it runs twice.

## The pattern
```
POST /v1/jobs            -> 202 Accepted + {"job_id": "...", "status": "queued"}
GET  /v1/jobs/{job_id}   -> {"status": "queued" | "running" | "done" | "failed", "result": ..., "error": ...}
```
A **worker** picks queued jobs from a `jobs` table and runs them. The client **polls** the status.

## Idempotency (the double click problem)
The client sends an `Idempotency-Key` header (any unique string). If the same key comes again,
return the SAME job instead of creating a new one. This is how payment APIs avoid double charges.

## What you write
1. `jobs.py`: a `jobs` table (SQLite is fine): id, kind, input, status, result, error,
   idempotency_key (UNIQUE), attempts, created_at, updated_at.
   - `enqueue(kind, input, idempotency_key)`
   - `claim_next()`: atomically move ONE queued job to running (why atomically? two workers!)
   - `finish(job_id, result)` / `fail(job_id, error)`; retry up to 3 attempts, then `failed` for good
2. `worker.py`: a loop that claims and runs jobs. The job itself uses your S2 job post extractor
   (or `LLM_PROVIDER=fake` for tests).
3. `app.py`: the two endpoints, with the `Idempotency-Key` header.
4. Run the API and the worker in two terminals. Post a job, poll it until done.

## Done when
- [ ] Posting twice with the same `Idempotency-Key` returns the same `job_id` (tested).
- [ ] Two workers never claim the same job (test: call `claim_next()` twice, get two different jobs or None).
- [ ] A job that fails twice then works ends as `done` with `attempts == 3` (tested with a fake).
- [ ] A crashed worker (killed mid job) leaves the job `running` forever. Write in the log how you
      would detect and recover that (hint: a timeout on `updated_at`).

## Questions for your log
- Polling vs server sent events vs webhooks: when would you use each?
- Somajji's high risk alert must never be lost. Would you send it through a job queue? Why?
