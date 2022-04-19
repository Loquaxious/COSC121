def cubes(data):
    """L"""
    result = []
    for num in data:
        cube = num ** 3
        result.append(cube)
    return result

cubes_list = cubes([1, 2, 4])
print(cubes_list)
