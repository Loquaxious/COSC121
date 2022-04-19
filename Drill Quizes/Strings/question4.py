def first_two(s):
    """L"""
    if len(s) < 2:
        return s
    else:
        return s[:2]
print(first_two('Hello'))
print(first_two('X'))
print(first_two(''))
