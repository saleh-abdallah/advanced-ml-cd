def test_empty_string(client):
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
