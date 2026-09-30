# S5: Extraction API

**Time:** 1 to 2 evenings · **Concepts:** structured output inside a web service, FastAPI
`response_model`, dependency injection, testing with a **fake LLM**, logging failures.

## The idea
Put your S2 job extractor behind an API: `POST /extract/job` with the job text,
get back a validated `JobPost` as JSON. This is how structured output is used in real products.

Extra packages: `uv add fastapi uvicorn httpx`

## Endpoints
| Method | Path | Body | Returns |
| --- | --- | --- | --- |
| GET | `/health` | none | `{"status": "ok"}` |
| POST | `/extract/job` | `{"text": "..."}` | `JobPost` (200) or an error (422 / 502) |

## Errors to design
- Empty or very long text (over 8,000 characters) → **422** with a clear message (validate the request body).
- The model keeps returning invalid JSON after all retries → **502** `{"detail": "model output invalid"}`.
  Log the raw model output to `failures.log` so you can study it later.

## The key idea: a fake LLM for tests
Your tests must NOT call a real model (slow, not free, not repeatable). So the endpoint gets its
"JSON generator" through a FastAPI dependency. In tests, you override it with a fake function that
returns a fixed JSON string.

## Steps
1. Create `ExtractRequest` with a `text` field (min length 20, max length 8000).
2. Write `get_generator()` that returns `common.llm.generate_json`.
3. Write the endpoint. It uses the generator from the dependency, validates with `JobPost`,
   retries, and raises `HTTPException(502)` on final failure.
4. Run it: `uv run uvicorn track1_structured_output.s5_extract_api.app:app --reload`. Try it at `http://127.0.0.1:8000/docs`.
5. Write the tests with `app.dependency_overrides`.

## Done when
- [ ] `/docs` shows both endpoints with the `JobPost` response schema.
- [ ] Tests pass for: a good fake response (200), invalid fake JSON every time (502 + a line in
      `failures.log`), and too short text (422).
- [ ] No test calls a real model.

## Stretch goals
- Add `POST /extract/sms` using your S1 model.
- Return the number of attempts used in a response header, e.g. `X-Attempts: 2`.
