# B5: Docker + CI with an eval gate

**Time:** 1 to 2 evenings · **Skill:** packaging an app so it runs the same everywhere, and making
GitHub check every push automatically. Companies ask about this in almost every interview.

## Part 1: Docker
Package your B2 (or B4) app.
1. Write a `Dockerfile` (a starter is given with TODOs):
   - a small Python base image, `uv` for installs, a **non root user**
   - copy dependency files first, install, THEN copy code (why this order? cache layers)
   - config only from environment variables; `PORT` from the environment (cloud platforms set it)
   - a `HEALTHCHECK` hitting `/health`
2. Write `.dockerignore` so `.env`, `.venv`, `*.db` and `__pycache__` never enter the image.
3. `docker compose up` with `compose.yaml`: the API + a Postgres container, `DATABASE_URL` pointing to it.
4. Check: `docker run` the image with a wrong `DATABASE_URL`. Does it fail with a clear message?

Docker on a Mac: Docker Desktop or Colima (you already have `.colima`). Both are free for personal use.

## Part 2: CI with GitHub Actions (free for public repos)
`ci.yml` (given skeleton) runs on every push and pull request:
1. install with uv, run `ruff` (lint) and `pytest` (unit tests with fake LLMs: no model, no key)
2. build the Docker image
3. **eval gate:** run a small eval (for example S3 triage accuracy using saved model outputs in a
   JSON file, so CI needs no model) and FAIL the job if accuracy drops below a threshold in
   `eval_threshold.txt`

## Done when
- [ ] `docker compose up` gives a working API on http://localhost:8000/docs
- [ ] The image has no `.env` inside (check with `docker run --rm IMAGE ls -la`)
- [ ] A pull request that lowers the saved eval results turns CI red
- [ ] The image is under 300 MB (`docker images`)

## Budget note
GitHub Actions is free for public repos. For private repos there's a monthly free minute quota;
keep CI fast and never run paid model calls in CI.
