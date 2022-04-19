def long_enough(strings, min_length):
    """Returns the strings that are greater than the minimum length"""
    result = []
    
    for s in strings:
        if ((len(s)) >= min_length):
            result.append(s)
    return result

data = ['a','bc', 'def', 'ghij', 'klmno']
print(long_enough(data, 3)) 