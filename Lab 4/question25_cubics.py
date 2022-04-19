def cubes(data):
    """Returns the cubic of the given numbers"""
    result = []
    for num in data:
        result.append(num ** 3)
    return result

print(cubes([1, 2, 4]))
print(cubes([5]))