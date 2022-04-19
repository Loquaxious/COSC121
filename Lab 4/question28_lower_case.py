def lower_case(strings):
    """Returns the lower case of the given list"""
    lower = []
    
    for s in strings:
        lower.append(s.lower())
    return lower

print(lower_case(['HEY', 'Harry']))
