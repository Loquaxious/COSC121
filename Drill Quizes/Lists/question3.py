def has23(nums):
    """L"""
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False
    


print(has23([2, 5]))
print(has23([42, 53]))
print(has23([4, 3]))