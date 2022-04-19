def num_matches(sentence, word_of_interest):
    """L"""
    strings = sentence.split()
    count = 0
    for string in strings:
        if string == word_of_interest:
            count += 1
    return count

s = "the cow jumped over the moon"
print(num_matches(s, 'the'))
