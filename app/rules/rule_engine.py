from app.models.enums import FailureType, SeverityLevel


class RuleEngine:

    @staticmethod
    def classify(description: str) -> dict:
        text = description.lower()

        # HARDWARE
        if any(word in text for word in ["disk", "cpu", "overheat", "memory", "ram"]):
            return {
                "failure_type": FailureType.HARDWARE,
                "severity": SeverityLevel.HIGH,
                "confidence": 0.85,
                "reason": "Hardware-related keywords detected"
            }

        # NETWORK
        if any(word in text for word in ["timeout", "latency", "packet", "dns", "network"]):
            return {
                "failure_type": FailureType.NETWORK,
                "severity": SeverityLevel.MEDIUM,
                "confidence": 0.80,
                "reason": "Network-related issue detected"
            }

        # SOFTWARE
        if any(word in text for word in ["exception", "crash", "bug", "null", "stacktrace"]):
            return {
                "failure_type": FailureType.SOFTWARE,
                "severity": SeverityLevel.MEDIUM,
                "confidence": 0.75,
                "reason": "Software failure pattern found"
            }

        # HUMAN
        if any(word in text for word in ["misconfiguration", "wrong", "deleted", "manual"]):
            return {
                "failure_type": FailureType.HUMAN,
                "severity": SeverityLevel.LOW,
                "confidence": 0.65,
                "reason": "Human error indicators detected"
            }

        # DEFAULT
        return {    
            "failure_type": FailureType.UNKNOWN,
            "severity": SeverityLevel.LOW,
            "confidence": 0.40,
            "reason": "No matching rules found"
        }
