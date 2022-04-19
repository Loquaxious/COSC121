def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    ans = eggs // 12
    return ans

print(calculate_cartons(1))
print(calculate_cartons(65))