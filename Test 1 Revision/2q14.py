def set_lowercase(strings):
    """F"""
    n = 0
    result = []
    for word in strings:
        word = word.lower()
        strings[n] = word
        n += 1
    return strings

strings = ['Right', 'SAID', 'Fred']
set_lowercase(strings)
print(strings)