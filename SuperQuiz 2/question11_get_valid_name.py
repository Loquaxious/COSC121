import os
def get_valid_filename():
    """Asks the user for a filename and keeps asking until a filename is 
    found"""
    prompt = 'Input file name? '
    filename = input(prompt)
    
    while os.path.isfile(filename) == False:
        print('File does not exist.')
        filename = input(prompt)
    
    return filename

filename = get_valid_filename()
print(filename, 'exists. Yay!')