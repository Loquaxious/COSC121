def print_nth_item_divided(data, n, divisor):
    """L"""
    
    try:
        print(data[n] / divisor)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except IndexError:
        print("Invalid position provided.")
    except TypeError:
        print("Parameters must be numbers.")
    


print_nth_item_divided([2, 4, 5], '1', 2)
print_nth_item_divided([2, 4, 5], 2, 2)
print_nth_item_divided([2, 4, 5], 9, 2)
print_nth_item_divided([2, 4, 5], 1, 0)
