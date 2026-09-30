"""Attack tests. Write the `client`, `rina_key` and `arif_key` fixtures in conftest.py
(start from B2's conftest and add two seeded users)."""


def test_arif_cannot_read_rinas_application(client, rina_key, arif_key):
    app_id = client.post("/v1/applications", json={"company": "A", "role": "B"},
                         headers={"X-API-Key": rina_key}).json()["id"]
    r = client.get(f"/v1/applications/{app_id}", headers={"X-API-Key": arif_key})
    assert r.status_code == 404


def test_arifs_list_never_shows_rinas_items(client, rina_key, arif_key):
    client.post("/v1/applications", json={"company": "Secret", "role": "B"},
                headers={"X-API-Key": rina_key})
    items = client.get("/v1/applications", headers={"X-API-Key": arif_key}).json()["items"]
    assert all(a["company"] != "Secret" for a in items)


def test_missing_key_is_401(client):
    assert client.get("/v1/applications").status_code == 401

# TODO: Arif can't PATCH, DELETE, or POST a note to Rina's application
# TODO: a body with {"owner_id": <rina's id>} from Arif is ignored or rejected
