def total_steps(step_records):
    """Returns the total number of steps made"""
    total = []
    for line in step_records:
        total.append(line[-1])
    sums = sum(total)
    return sums

step_records = []
total = total_steps(step_records)
print(total)