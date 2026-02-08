from app.rules.scoring_rules import apply_scoring_rules
from app.services.severity import calculate_severity
from app.services.confidence import calculate_confidence
from app.data.playbooks import PLAYBOOKS

FAILURE_CATEGORIES = [
    "database",
    "infrastructure",
    "deploy",
    "network",
    "application",
    "external"
]


def analyze_incident(incident, similar_incidents_count=0):
    # Initialize scores
    scores = {category: 0 for category in FAILURE_CATEGORIES}

    # Apply rules
    scores = apply_scoring_rules(incident, scores)

    # Determine probable cause
    probable_cause = max(scores, key=scores.get)

    # Calculate confidence
    confidence = calculate_confidence(scores, probable_cause)

    # Determine severity
    severity = calculate_severity(incident)

    return {
        "probable_cause": probable_cause,
        "confidence": confidence,
        "severity": severity,
        "recommended_actions": PLAYBOOKS.get(probable_cause, []),
        "score_breakdown": scores,
        "similar_incidents": similar_incidents_count
    }
