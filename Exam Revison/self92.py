def inverted_word_counts(word_count_dict):
    """L"""
    
    inverted = {}
    for key, number in sorted(word_count_dict.items()):
        if number not in inverted:
            inverted[number] = [key]
        else:
            inverted[number].append(key)
    
    
    return(inverted)

test_dict = {'a': 20, 'blotto': 1, 'bingo':1, 'x': 5}
inverse = inverted_word_counts(test_dict)
for count in sorted(inverse.keys()):
    print('{}: {}'.format(count, inverse[count]))