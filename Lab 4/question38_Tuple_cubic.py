def cubed_tuple(number):
    """Returns the cubic of the given numbers"""
    cubic = number ** 3
    result = (number, cubic)
    return result    

print(cubed_tuple(1))
print(cubed_tuple(3))