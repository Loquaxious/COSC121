def my_max(data):
    """Function that returns the max value of a list"""
    max_value = float('-inf') 
    for num in data:
        if (num > max_value):
            max_value = num
    return max_value
        
print(my_max([11, 99, 3, -6]))
print(my_max([-3, -5, -9, -10]))
    