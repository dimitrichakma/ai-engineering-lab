import pytest
from fastapi.testclient import TestClient

from track3_backend.b1_api_design import store
from track3_backend.b1_api_design.app import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean():
    store.reset()


def create(**kw):
    body = {"company": "Nodi Labs", "role": "Junior AI Engineer", **kw}
    return client.post("/v1/applications", json=body)


def test_create_returns_201_and_location():
    r = create()
    assert r.status_code == 201
    assert r.headers["location"].endswith(f"/v1/applications/{r.json()['id']}")


def test_missing_is_404_in_common_format():
    r = client.get("/v1/applications/999")
    assert r.status_code == 404
    assert r.json()["error"]["code"] == "not_found"


def test_validation_error_uses_common_format():
    r = client.post("/v1/applications", json={"role": "x"})       # no company
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validation_error"


def test_invalid_status_transition_is_409():
    app_id = create().json()["id"]                               # starts as "saved"
    r = client.patch(f"/v1/applications/{app_id}", json={"status": "offer"})
    assert r.status_code == 409
    assert r.json()["error"]["code"] == "invalid_transition"


def test_cursor_pagination():
    for i in range(25):
        create(company=f"Company {i}")
    seen, cursor, sizes = [], None, []
    while True:
        params = {"limit": 10, **({"cursor": cursor} if cursor else {})}
        page = client.get("/v1/applications", params=params).json()
        sizes.append(len(page["items"]))
        seen += [a["id"] for a in page["items"]]
        cursor = page["next_cursor"]
        if cursor is None:
            break
    assert sizes == [10, 10, 5]
    assert len(set(seen)) == 25

# TODO: filter by status; PATCH a valid transition; DELETE gives 204 then 404; notes endpoints
