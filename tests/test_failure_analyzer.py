from app.services.failure_analyzer import FailureAnalyzerService

def test_hardware_failure_from_text():
    result = FailureAnalyzerService.analyze(
        "CPU overheating and disk failure detected"
    )

    assert result.failure_type.value == "hardware"
    assert result.severity.value == "high"
    assert result.confidence > 0.7
