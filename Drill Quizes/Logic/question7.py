def near_ten(num):
    """L"""
    if num % 10 <= 2 or num % 10 >= 8:
        return True
    else:
        return False
print(near_ten(12))
print(near_ten(17))
print(near_ten(18))
