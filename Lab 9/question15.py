def print_word_counts(filename):
    """Takes a filename and prints a alpabetically ordered list of all words and
    the occurance of them"""
    import re
    
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    input_file.close()
    
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    alpha_word_count = sorted(word_count.items())
    
    for item in alpha_word_count:
        print("{}: {}".format(item[0], item[1]))


"""Test using a file containing the following 2 lines:
This is the way, this is.
That was the way, that was.
"""
print_word_counts('dictionaryinputtestfile.txt')