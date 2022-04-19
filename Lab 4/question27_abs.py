def abs_values(numbers):
    """Returns the abs values of the given numbers"""
    result = []
    
    for num in numbers:
        result.append(int((num ** 2)**.5))
        
    return result

print(abs_values([2, -3, -7]))
    