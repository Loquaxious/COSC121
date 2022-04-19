def is_odd(number):
    """ Boolean function that states whether a number is odd or not """
    if number % 2 == 0:
        return False
    else:
        return True

print(is_odd(1))
print(is_odd(2))
print(is_odd(-321))