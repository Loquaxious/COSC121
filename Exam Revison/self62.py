def flawed_glue(list1, list2):
    """L"""
    
    return list2[:-1] + list1[2:]

ans = flawed_glue([10, 20, 30, 40, 50, 60], [11, 12, 13, 14, 15, 16])
print(ans)