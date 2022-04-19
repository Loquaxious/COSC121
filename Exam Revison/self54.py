def fillerup(strings):
    """L"""
    
    for i in range(0, len(strings)):
        strings[i].upper()
        while len(strings[i]) < 5:
            strings[i] += '?'
        
strings = ['Right', 'SAID', 'jO']
fillerup(strings)
print(strings)