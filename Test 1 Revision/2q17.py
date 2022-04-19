def pivot(nums, threshold):
    """F"""
    list1 = []
    list2 = []
    
    for num in nums:
        if num < threshold:
            list1.append(num)
        else:
            list2.append(num)
    return tuple([list1, list2])

nums = [6, 100, -5, 20, 4, 9, 10]
print(pivot(nums, 10))