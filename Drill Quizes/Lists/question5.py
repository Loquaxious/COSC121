def max_end3(nums):
    """L"""
    result = []
    if nums[-1] >= nums[0]:
        for num in nums:
            result.append(nums[-1])
    elif nums[0] > nums[-1]:
        for num in nums:
            result.append(nums[0])
    return result

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([4, 5, 4]))