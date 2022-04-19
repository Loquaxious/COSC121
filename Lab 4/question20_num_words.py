def num_words(string):
    """Function that returns the amount or words in a string"""
    words = string.split()
    count = len(words)
    return count

print(num_words("Welcome to lists!"))
print(num_words("thi01234&*9 &^%x 1"))