def double_char(s):
    """L"""
    string = ""
    for char in s:
        char = char * 2
        string += char
    return string

print(double_char('The'))
print(double_char('Hi-There'))
