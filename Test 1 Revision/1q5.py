def first_and_last(s):
    """L"""
    if s == "":
        return ""
    else:
        return (s[0] + s[-1])
    

print(first_and_last('a-string'))
print(first_and_last(''))
print(first_and_last('X'))
