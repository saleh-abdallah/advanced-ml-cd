def test_prediction(client):
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200

