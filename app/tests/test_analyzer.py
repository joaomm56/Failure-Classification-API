from app.services.analyzer import analyze_incident

def test_timeout_after_deploy():
    incident = {
        "error_type": "timeout",
        "load": 0.92,
        "frequency_last_24h": 6,
        "deployment_recent": True,
        "duration_seconds": 18,
        "affected_users": 200
    }

    result = analyze_incident(incident)

    assert result["probable_cause"] == "deploy"
    assert result["severity"] == "high"
    assert result["confidence"] > 0.5
