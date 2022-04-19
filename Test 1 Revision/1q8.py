def count_evens(nums):
    """L"""
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return len(result)

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
