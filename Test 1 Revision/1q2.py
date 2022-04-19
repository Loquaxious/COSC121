def full_name(first_name, last_name):
    """Return a string consisting of the first name, a space
       and the last name. 
    """
    name = ("{} {}".format(first_name, last_name))
    return name

name = full_name('Alex', 'Ng')
print(name)