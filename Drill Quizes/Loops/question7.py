def sum13(nums):
    """L"""
    result = []
    for n in range(len(nums)):
        if nums[n] != 13:
            if n == 0 or nums[n-1] != 13:
                result.append(nums[n])
    return sum(result)
            
    


print(sum13([1, 2, 2, 1, 13]))
print(sum13([13, 2, 2, 1]))            
print(sum13([]))