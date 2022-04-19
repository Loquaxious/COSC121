def full_name(first_name, last_name):
    """Return a string consisting of the first name, a space
       and the last name. 
    """
    state = "{} {}".format(first_name, last_name)
    return state 

name = full_name('Alex', 'Ng')
print(name)