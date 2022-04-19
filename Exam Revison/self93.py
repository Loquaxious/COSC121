def lookup(phonebook, phone_number):
    """L"""
    
    contacts = phonebook.items()
    for contact in contacts:
        if contact[1] == phone_number:
            return contact[0]
        

phonebook = {'Fred':311567, 'Barb':311569, 'logan':556774, 'Bob':556773}
print(lookup(phonebook, 556774))

phonebook = {'Fred':311567, 'Barb':311569, 'logan':556774, 'Bob':556773}
print(lookup(phonebook, 556777))