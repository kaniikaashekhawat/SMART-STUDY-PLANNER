def get_priority(difficulty, days):

    if days <= 3:
        priority = "High"

    elif difficulty == "hard" and days <= 7:
        priority = "High"

    elif difficulty == "medium" and days <= 7:
        priority = "High"

    elif difficulty == "hard":
        priority = "Medium"

    else:
        priority = "Low"

    return priority
