def count_evens(nums):
    """L"""
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count    

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
