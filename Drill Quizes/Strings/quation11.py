def swap_ends(s):
    """L"""
    swap1 = s[0]
    swap2 = s[-1]
    rest = s[1:-1]
    
    return swap2 + rest + swap1

print(swap_ends('WooHoo'))
print(swap_ends('ab'))

