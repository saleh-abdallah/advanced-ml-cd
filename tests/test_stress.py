def test_repeated_calls(client):
    for _ in range(100):
        r = client.post("/predict", json={"text": "Good"})
        assert r.status_code == 200


