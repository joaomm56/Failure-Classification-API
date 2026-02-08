def apply_scoring_rules(incident, scores):
    error_type = incident["error_type"]
    load = incident["load"]
    frequency = incident["frequency_last_24h"]
    deployment_recent = incident["deployment_recent"]

    # Error type rules
    if error_type == "timeout":
        scores["database"] += 3
        scores["network"] += 1

    if error_type == "connection_refused":
        scores["network"] += 3
        scores["infrastructure"] += 1

    if error_type == "out_of_memory":
        scores["infrastructure"] += 4
        scores["application"] += 2

    # Load-based rules
    if load >= 0.85:
        scores["infrastructure"] += 3
        scores["database"] += 2

    # Frequency rules
    if frequency >= 5:
        scores["infrastructure"] += 2
        scores["application"] += 1

    # Deployment correlation
    if deployment_recent:
        scores["deploy"] += 4

    return scores
