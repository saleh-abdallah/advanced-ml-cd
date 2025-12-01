<<<<<<< HEAD
def test_sql_injection_input(client):
    response = client.post("/predict", json={"text": "'; DROP TABLE users; --"})
    assert response.status_code == 200
=======
def test_sql_injection_input(client):
    response = client.post("/predict", json={"text": "'; DROP TABLE users; --"})
    assert response.status_code == 200
>>>>>>> 1a1f71ae28618944827e6543f0f861c593d8a044
