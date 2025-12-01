def test_sql_injection_input(client):
    response = client.post("/predict", json={"text": "'; DROP TABLE users; --"})
    assert response.status_code == 200
    assert response.json() == {"sentiment": 1}
