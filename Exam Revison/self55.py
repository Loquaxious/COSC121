def my_enumerate(items):
    """L"""
    enumerated = []
    for i in range(0, len(items)):
        enumerated.append((i, items[i]))
    
    return enumerated

ans = my_enumerate([10, 20, 30])
print(ans)

ans = my_enumerate(['dog', 'pig', 'cow'])
print(ans)

ans = my_enumerate([])
print(ans)