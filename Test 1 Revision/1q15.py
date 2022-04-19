def num_matches(sentence, word_of_interest):
    """L"""
    count = 0
    sen = sentence.split(" ")
    for letter in sen:
        if letter == word_of_interest:
            count += 1
    return count

s = "the cow jumped over the moon"
print(num_matches(s, 'the'))