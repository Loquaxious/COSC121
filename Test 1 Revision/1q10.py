def abs_nums(numbers):
    """L"""
    result = []
    for num in numbers:
        num = abs(num)
        result.append(num)
    
    return result

print(abs_nums([2, -3, -7]))
