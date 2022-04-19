def are_anagrams(word1, word2):
    """Function that determines whether two words are anagrams"""
    list1 = list(word1)
    list2 = list(word2)

    formatted1 = sorted(list1)
    formatted2 = sorted(list2)

    if (list1 == list2):
        state = False    
    elif (formatted1 == formatted2):
        state = True
    else:
        state = False
    
    return state
    
print(are_anagrams("looped", "poodle"))
print(are_anagrams("lopped", "poodle"))
print(are_anagrams("poodle", "poodle"))
