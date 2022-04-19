def word_separator(string_list):
    """L"""
    list1 = []
    list2 = []
    
    for word in string_list:
        if word.isalpha() == True:
            list1.append(word)
        else:
            list2.append(word)
    return tuple([list1, list2])
strings = ['COSC121', 'is', 'always', 'fun!']
print(word_separator(strings))