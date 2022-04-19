def love6(num1, num2):
    """L"""
    if num1 == 6 or num2 == 6:
        return True
    elif (num1 + num2) == 6:
        return True
    elif (num1 - num2) == 6 or (num2 - num1) == 6:
        return True
    else:
        return False
#print(love6(1, 5))
#print(love6(6, 4))
print(love6(4, 5))
