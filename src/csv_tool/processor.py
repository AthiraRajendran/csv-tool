def summarize(rows):
    total = 0
    highest = 0
    name = ""
    for row in rows:
        amount = int(row["amount"])
        total += amount
        if amount > highest:
            highest = amount
            name = row["name"]
    return total, name, highest