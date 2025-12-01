<<<<<<< HEAD
def test_repeated_calls(client):
    for _ in range(100):
        r = client.post("/predict", json={"text": "Good"})
        assert r.status_code == 200
=======
def test_repeated_calls(client):
    for _ in range(100):
        r = client.post("/predict", json={"text": "Good"})
        assert r.status_code == 200
>>>>>>> 1a1f71ae28618944827e6543f0f861c593d8a044
