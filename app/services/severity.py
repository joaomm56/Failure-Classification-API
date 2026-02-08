def calculate_severity(incident):
    duration = incident["duration_seconds"]
    frequency = incident["frequency_last_24h"]
    affected_users = incident["affected_users"]

    if duration >= 30 or affected_users >= 500:
        return "critical"

    if duration >= 15 or frequency >= 5:
        return "high"

    if duration >= 5 or frequency >= 2:
        return "medium"

    return "low"
