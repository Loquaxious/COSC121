def num_words(strings):
    """F"""
    count = 0
    string = strings.split()
    for char in string:
        count += 1
    return count

word_count = num_words("Welcome to lists!")
print(word_count)
word_count = num_words("thi01234&*9 &^%x 1")
print(word_count)