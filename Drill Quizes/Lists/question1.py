def common_end(list_a, list_b):
    """L"""
    if list_a[0] == list_b[0]:
        return True
    elif list_a[-1] == list_b[-1]:
        return True
    else:
        return False
    
    
print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([2], [1, 2]))    