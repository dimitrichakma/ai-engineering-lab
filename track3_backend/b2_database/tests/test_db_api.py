def test_create_and_read_back(client):
    r = client.post("/v1/applications", json={"company": "Nodi Labs", "role": "AI Engineer"})
    assert r.status_code == 201
    app_id = r.json()["id"]
    assert client.get(f"/v1/applications/{app_id}").json()["company"] == "Nodi Labs"


def test_deleting_application_deletes_its_notes(client):
    app_id = client.post("/v1/applications", json={"company": "A", "role": "B"}).json()["id"]
    client.post(f"/v1/applications/{app_id}/notes", json={"text": "call HR on Sunday"})
    assert client.delete(f"/v1/applications/{app_id}").status_code == 204
    assert client.get(f"/v1/applications/{app_id}/notes").status_code == 404

# TODO: copy the B1 tests here, using the `client` fixture instead of a module level client
# TODO: a failing request (e.g. invalid transition) leaves the row unchanged (rollback works)
