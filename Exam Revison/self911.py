def find_key(input_dict, value):
    """L"""
    
    for key, val in input_dict.items():
        if val == value:
            return key
test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))
test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))