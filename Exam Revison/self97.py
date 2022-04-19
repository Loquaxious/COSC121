def inverted_word_counts(word_count_dict):
    """l"""
    
    inverted = {}
    for key, value in sorted(word_count_dict.items()):
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
        
    return inverted

test_dict = {'a': 20, 'blotto': 1, 'bingo':1, 'x': 5}
inverse = inverted_word_counts(test_dict)
for count in sorted(inverse.keys()):
    print('{}: {}'.format(count, inverse[count]))