import json

from fastapi.testclient import TestClient

from track1_structured_output.s5_extract_api.app import app, get_generator

client = TestClient(app)

GOOD_JOB = {
    "title": "Junior AI Engineer",
    "company": "Nodi Labs Ltd.",
    "location": "Dhaka",
    "work_mode": "hybrid",
    "min_experience_years": 0,
    "requirements": [{"skill": "Python", "required": True}],
    "salary": {"min_bdt": 45000, "max_bdt": 60000, "period": "month"},
    "deadline_text": "20 October 2026",
}
JOB_TEXT = "Junior AI Engineer at Nodi Labs, Dhaka, hybrid. Python required. BDT 45k to 60k."


def fake_good(prompt, schema, system=None):
    return json.dumps(GOOD_JOB)


def fake_broken(prompt, schema, system=None):
    return '{"title": "missing everything else"'


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_extract_job_with_good_fake():
    app.dependency_overrides[get_generator] = lambda: fake_good
    try:
        r = client.post("/extract/job", json={"text": JOB_TEXT})
        assert r.status_code == 200
        assert r.json()["company"] == "Nodi Labs Ltd."
    finally:
        app.dependency_overrides.clear()


# TODO: test that fake_broken gives status 502 and writes a line to failures.log.
# TODO: test that text shorter than 20 characters gives 422 (no override needed; why?).
