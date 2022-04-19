def short_words(word_list):
    """F"""
    result = []
    
    for word in word_list:
        if len(word) <= 4:
            result.append(word)
    return result

words = ['A', 'big', 'elephant', 'sat', 'heavily', 'on', 'Alex']
print(short_words(words))