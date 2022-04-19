def formatted_title(given_name, family_name, weight):
    """function that returns a title of a person"""
    family = family_name.upper()
    given = given_name.title()
    
    title = (('{0}, {1} ({2:.1f} kg)').format(family, given, weight))
    
    return title 

print(formatted_title('jay', 'smith', 80))
print(formatted_title('Lee', 'Smith', 120.4321))
print(formatted_title('BranDeen', 'McGurkingshaw', 54.9876)) 