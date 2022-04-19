def word_counter(input_str):
    """Takes a string and returns occurances of words within the string"""
    str_dict = {}
    
    s_list = input_str.split()
    
    for word in s_list:
        word = word.lower()
        str_dict[word] = str_dict.get(word, 0) + 1
    
    return str_dict
    
word_count_dict = word_counter("This is a sentence this is")
print(word_count_dict)

word_count_dict = word_counter("A WORD is a word it is")
print(word_count_dict)