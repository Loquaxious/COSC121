def find_first(value, array, start_index=0):
    """Not a valid solution, does it find the first instance?"""
    found_index = -1
    for i in range(start_index, len(array)):
        if value == array[i]:
            found_index = i
    return found_index

print(find_first(1, [0, 1, 0]))
print(find_first(2, [0, 0, 1, 1, 2]))
print(find_first(3, [0, 0, 0, 1]))
print(find_first(1, [0, 1, 0], 2))
print(find_first(2, [0, 2, 1, 1, 2], 1))