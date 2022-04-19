def rotate_left3(nums):
    """L"""
    copy = nums[:]
    
    nums.remove(nums[0])
    nums.append(copy[0])
    return nums
    
print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))