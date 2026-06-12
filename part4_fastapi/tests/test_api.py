from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict():
    payload = {
        "recency_days": 50,
        "frequency_180d": 5,
        "monetary_180d": 200,
        "ticket_count_90d": 1,
        "sessions_30d": 10
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200


def test_batch_predict():
    payload = [
        {
            "recency_days": 50,
            "frequency_180d": 5,
            "monetary_180d": 200,
            "ticket_count_90d": 1,
            "sessions_30d": 10
        }
    ]

    response = client.post("/batch_predict", json=payload)

    assert response.status_code == 200