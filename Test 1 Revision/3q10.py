def lower_case(strings):
    """L"""
    result = []
    for string in strings:
        lower = string.lower()
        result.append(lower)
    return result

data = ['HEY', 'Harry']
print(lower_case(data))
