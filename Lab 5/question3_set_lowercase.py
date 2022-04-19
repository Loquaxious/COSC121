def set_lowercase(strings):
    """Returns the lowercase of a list of strings"""
    for s in range(0, len(strings)):
        strings[s] = strings[s].lower()
        
    
    return strings
    
print(set_lowercase(['Right', 'SAID', 'Fred']))