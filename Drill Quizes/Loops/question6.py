def string_splosion(s):
    """L"""
    string = ""
    for n in range(0, len(s)):
        string += s[0:n]
        fstring = string + s 
    return fstring

print(string_splosion('Code'))
print(string_splosion('abc'))