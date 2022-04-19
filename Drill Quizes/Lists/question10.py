def sum2(nums):
    """L"""
    if len(nums) > 2:
        state = sum(nums[0:2])
    else:
        state = sum(nums)
    return state 

print(sum2([1, 2, 3]))
print(sum2([1, 1, 1, 1]))
print(sum2([]))