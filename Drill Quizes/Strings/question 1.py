def combo_string(str1, str2):
    """L"""
    if len(str1) > len(str2):
        state = (str2 + str1 + str2)
    else:
        state = (str1 + str2 + str1)
    return state 

print(combo_string('Hello', 'hi'))
print(combo_string('Z', 'Apple'))
