def print_squares_to_number(number):
    """prints all the squares of the values upto a given number"""
    if (number < 1):
        state = print("ERROR: number must be at least 1")
    else:
        for i in range(number, (number + 1)):
            state = print("{0} * {0} = {1}".format(i, (i**2))) 
    return state 

print(print_squares_to_number(5))
print(print_squares_to_number(3))
print(print_squares_to_number(0))