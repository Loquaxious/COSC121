def short_words(word_list):
    """L"""
    result = []
    for letter in word_list:
        if len(letter) < 5:
            result.append(letter)
    return result

words = ['A', 'big', 'elephant', 'sat', 'heavily', 'on', 'Alex']
print(short_words(words))