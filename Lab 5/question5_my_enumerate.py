def my_enumerate(items):
    """enumerte function without using pythons built in function"""
    for i in range(0, len(items)):
        items[i] = (i, items[i])
    return items

ans = my_enumerate([10, 20, 30])
print(ans)
ans1 = my_enumerate(['dog', 'pig', 'cow'])
print(ans1)
ans2 = my_enumerate([])
print(ans2)