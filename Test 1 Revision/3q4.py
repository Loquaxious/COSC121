def my_abs(value):
    """L"""
    if value < 0:
        state = ((value ** 2) ** 0.5)
    else:
        state = value
    return state

print(my_abs(3.5))
print(my_abs(-7.0))
