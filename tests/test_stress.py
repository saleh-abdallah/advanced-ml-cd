def test_repeated_calls(client):
    for _ in range(100):
        response = client.post("/predict", json={"text": "Good"})
        assert response.status_code == 200
        assert response.json() == {"sentiment": 1}
