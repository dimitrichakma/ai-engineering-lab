from track3_backend.b3_background_jobs.jobs import JobStore
from track3_backend.b3_background_jobs.worker import run_once


def store(tmp_path):
    return JobStore(str(tmp_path / "jobs.db"))


def test_idempotency_returns_same_job(tmp_path):
    s = store(tmp_path)
    a = s.enqueue("x", {"n": 1}, idempotency_key="abc")
    b = s.enqueue("x", {"n": 1}, idempotency_key="abc")
    assert a["id"] == b["id"]


def test_two_claims_never_get_the_same_job(tmp_path):
    s = store(tmp_path)
    s.enqueue("x", {})
    first, second = s.claim_next(), s.claim_next()
    assert first is not None and second is None


def test_retry_then_success(tmp_path):
    s = store(tmp_path)
    job = s.enqueue("flaky", {})
    calls = {"n": 0}

    def flaky(_input):
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("temporary")
        return {"ok": True}

    for _ in range(3):
        run_once(s, handlers={"flaky": flaky})
    final = s.get(job["id"])
    assert final["status"] == "done"
    assert final["attempts"] == 3

# TODO: a job that always fails ends as "failed" after MAX_ATTEMPTS
# TODO: API test: POST twice with the same Idempotency-Key header -> same job_id, status 202
