def first_half(s):
    """L"""
    length = len(s)
    
    if length % 2 != 0:
        oddl = len(s[:-1])
        n = oddl / 2
        return s[:int(n)]
    else:
        n = length / 2
        return s[:int(n)]
    

print(first_half('WooHoo'))

print(first_half('HelloCOSC'))
