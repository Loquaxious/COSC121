def are_anagrams(word1, word2):
    """L"""
    
    if word1 == word2:
        return False
    
    list1 = list(word1)
    list2 = list(word2)
    
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    else:
        return False
    
print(are_anagrams("looped", "poodle"))
print(are_anagrams("lopped", "poodle"))
print(are_anagrams("poodle", "poodle"))
