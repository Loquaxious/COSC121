def check_age(age):
    """A docstring that gives nothing away"""
    if age < 18:
        underage = True
    elif age > 18:
        underage = False
    return underage

print(check_age(17))