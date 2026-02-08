def calculate_confidence(scores, winning_category):
    total = sum(scores.values())
    if total == 0:
        return 0.0

    return round(scores[winning_category] / total, 2)
