def flawed_fuse(list_1, list_2):
    """Returns all elements except for last for list_1 and all elements except for first for list_2"""
    list_3 = list_1[0 : -1] + list_2[1:]
    return list_3

ans = flawed_fuse([10, 20, 30], [100, 200, 300])
print(ans)