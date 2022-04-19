def has22(nums):
    """L"""
    n = 0
    for num in nums:
        if nums[n] == 2 and nums[n - 1] == 2:      
            state = True
        else:
            state = False
        n += 1 
    return state

print(has22([1, 2, 2]))
print(has22([1, 2, 21, 2]))
