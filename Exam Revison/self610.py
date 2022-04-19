def flawed_combine(list1, list2):
    """L"""
    
    return list2[:-2] + list1[:-2]

ans = flawed_combine([10, 20, 30, 40, 50, 60], [11, 12, 13, 14, 15, 16])
print(ans)