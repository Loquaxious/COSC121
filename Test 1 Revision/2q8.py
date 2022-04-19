def double_char(s):
    """L"""
    string =""
    for letter in s:
        letter = letter * 2
        string += letter
    return string


print(double_char('The'))
print(double_char('Hi-There'))

