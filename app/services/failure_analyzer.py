from app.rules.rule_engine import RuleEngine
from app.models.analysis_result import AnalysisResult


class FailureAnalyzerService:

    @staticmethod
    def analyze(description: str) -> AnalysisResult:
        result = RuleEngine.classify(description)

        return AnalysisResult(
            failure_type=result["failure_type"],
            severity=result["severity"],
            confidence=result["confidence"],
            explanation=result["reason"]
        )
