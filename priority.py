def get_priority(dif, days):

    if days <= 3:
        pri = "High"

    elif dif == "hard" and days <= 7:
        pri = "High"

    elif dif == "medium" and days <= 7:
        pri = "High"

    elif dif == "hard":
        pri = "Medium"

    else:
        pri = "Low"

    return pri
