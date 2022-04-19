def twiddle(s):
    """Do mysterious things with s and return an int"""
    i = 0
    num = -17
    while i < len(s):
        if ord(s[i]) > 73:
            num = num * 2 + (ord(s[i]) - 70) * 11
        else:
            num = num // 2 + ord(s[i]) * 7
        i += 1
    return num

print(twiddle('This is a test!'))
