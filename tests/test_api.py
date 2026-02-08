from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint():
    payload = {
        "system": "api",
        "component": "database",
        "error_type": "timeout",
        "duration_seconds": 18,
        "frequency_last_24h": 6,
        "load": 0.92,
        "deployment_recent": True,
        "affected_users": 200
    }

    response = client.post("/incidents/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "probable_cause" in data
    assert "severity" in data
