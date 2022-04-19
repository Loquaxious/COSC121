def first_last6(nums):
    """L"""
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
print(first_last6([1, 2, 6]))
print(first_last6([3, 2, 1]))