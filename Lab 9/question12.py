def find_key(input_dict, value):
    """takes as a parameter a dictionary and a value and returns the key in the 
    dictionary that maps to the given value or None if no such key exists"""
    
    items = input_dict.items()
    for item in items:
        if item[1] == value:
            return item[0]
        

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))