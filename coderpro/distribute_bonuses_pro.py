def getBonuses(performances):
    count = len(performances)
    bonuses = [1] * count

    for i in range(1, count):
        if performances[i - 1] < performances[i]:
            bonuses[i] = bonuses[i - 1] + 1

    for i in range(count - 2, -1, -1):
        if performances[i + 1] < performances[i]:
            bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

    return bonuses

print(getBonuses([1, 2, 3, 4, 3, 1]))
# [1, 2, 3, 4, 2, 1]