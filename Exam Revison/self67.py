def num_words(string, length):
    """L"""
    
    words = string.strip().split()
    
    count = 0
    for word in words:
        if len(word) == length:
            count += 1
    
    return count

word_count = num_words("Oh no it's a list filter!", 2)
print(word_count)

word_count = num_words("Oh no its a list filter!", 4)
print(word_count)