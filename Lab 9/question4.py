def character_set_counts(string_1, string_2, string_3):
    """Returns a count of the number of distinct charatcers that are 
    common to both strings string_1 and string_2 but are absent from the string 
    string_3.
    """
    set1 = set(string_1)
    set2 = set(string_2)
    set3 = set(string_3)
    set1 = set2 & set1 
    result = set1 - set3
    return len(result)

answer = character_set_counts('abcdef', 'bcd', 'ace')
print(answer)