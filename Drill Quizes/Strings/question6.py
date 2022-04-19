def left2(s):
    """L"""
    rotated = s[:2]
    rest = s[2:]
    
    return rest + rotated
print(left2('Hello'))
print(left2('java'))
