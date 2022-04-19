"""Function
   Date: 9/10/19
   Author: Logan Lee
"""

def make_person(id_num, name, weight, height, age):
    """Creates and returns a dictionary with the inputs names as keys"""
    person = {"id_num": id_num, "name": name, "weight": weight, \
              "height": height, "age": age, "num_steps": 0, \
              "first_date_recorded": None, "last_date_recorded": None}
    
    return person

def bmi(person):
    """Returns float of body mass index"""
    
    weight = person['weight']
    height = person['height']
    bmi_val = weight / (height ** 2)
    return bmi_val

def add_steps(person, date, steps):
    """Updates the given persons steps by incrementing the num_steps value 
    by the given number of steps"""
    
    person['num_steps'] += steps
    
    if person['first_date_recorded'] == None and person['last_date_recorded']\
       == None:
        person['first_date_recorded'] = date
        person['last_date_recorded'] = date
    
    if person['first_date_recorded'] > date:
        person['first_date_recorded'] = date
    
    elif person['last_date_recorded'] < date:
        person['last_date_recorded'] = date
        
    

def print_person(person):
    """Prints a formatted string of a given persons details"""
    print('----------------------------------------')
    print('{0} - {1}'.format(person['id_num'], person['name']))
    print('{0:.2f} kgs, {1:.2f} m, {2} years'.format(person['weight'], \
                                                     person['height'], \
                                                     person['age']))
    print('BMI = {0:.2f}'.format(bmi(person)))
    print('Total steps = {0}'.format(person['num_steps']))
    print('First date recorded = {0}'.format(person['first_date_recorded']))
    print('Last date recorded = {0}'.format(person['last_date_recorded']))
    print('----------------------------------------')


# Check the (key, value) pairs in the dictionary
#bod = make_person(123456, 'Dude', 90.0, 2.0, 20)
#print(bod['id_num'])
#print(bod['name'])
#print(bod['weight'])
#print(bod['height'])
#print(bod['age'])
#print(bod['num_steps'])
#print(bod['first_date_recorded'])
#print(bod['last_date_recorded'])

# Check the bmi function
#person = make_person(123457, 'Art', 78.0, 0.8724, 39)
#person_bmi = bmi(person)
#print('{:.1f}'.format(person_bmi))

# Check the print_person function
#person = make_person(123456, 'Jane', 78.0, 0.8724, 39)
#print_person(person)

# A simple check of add_steps
person = make_person(123456, 'Lee', 78.0, 0.8724, 39)
add_steps(person, '2017-01-02', 1234)
print_person(person)

# Check date handling by add_steps
person = make_person(123457, 'Art', 78.0, 0.8724, 39)
add_steps(person, '2018-01-02', 200)
add_steps(person, '2017-02-03', 100)
print_person(person)