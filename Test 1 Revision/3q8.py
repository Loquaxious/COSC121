def string_bits(s):
    """L"""
    string = ""
    string += s[0:len(s):2]
    return string
        
print(string_bits('Hello'))
