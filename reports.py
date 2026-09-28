def count_by_blood_type(donors):
    counts = {}
    for d in donors:
        blood = d[2]
        if blood in counts:
            counts[blood] = counts[blood] + 1
        else:
            counts[blood] = 1
    return counts
def age_summary(donors):
    # Returns [youngest, oldest, average] or an empty list if no donors
    if len(donors) == 0:
        return []
    ages = []
    for d in donors:
        ages.append(d[3])
    average = round(sum(ages) / len(ages), 1)
    return [min(ages), max(ages), average]