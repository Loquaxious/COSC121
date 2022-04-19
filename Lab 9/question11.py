def get_name(name_dict, id_num):
    """takes as its first parameter a dictionary mapping an ID number to a name 
    and as its second parameter a particular ID number (which might be invalid) 
    and returns the name associated with the given ID number if that ID number 
    exists in the dictionary or None otherwise."""
    
    return name_dict.get(id_num, None)

test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 2001)
print(ans)

test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 10)
print(ans)