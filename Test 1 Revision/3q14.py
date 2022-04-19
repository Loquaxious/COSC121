def my_enumerate(items):
    """L"""
    n = 0
    result = []
    for num in items:
        nums = tuple([n, num])
        result.append(nums)
        n += 1
    return result
ans = my_enumerate([10, 20, 30])
print(ans)