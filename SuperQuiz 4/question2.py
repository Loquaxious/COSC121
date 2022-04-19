"""Function that reads files and extracts person data then creates a step log for
   them
   Date: 13/10/19
   Author: Logan Lee
"""

def make_person(id_num, name, weight, height, age):
    """Creates and returns a dictionary with the inputs names as keys"""
    
    person = {"id_num": id_num, "name": name, "weight": weight, \
              "height": height, "age": age, "num_steps": 0, \
              "first_date_recorded": None, "last_date_recorded": None}
    
    return person


def bmi(person):
    """Returns float of body mass index based off persons details"""
    
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
    """Prints the formatted details of a given person"""
    
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


def extract_person(lines, start_index=0):
    """Takes a list of lines, extracts person details a returns it in a 
    dictionary"""
    
    data = []
    for line in lines[start_index + 1 : start_index + 6]:
        line = line.split(":") 
        item = line[1]
        data.append(item)
    
    id_num = int(data[0])
    name = data[1]
    weight = float(data[2])
    height = float(data[3])
    age = int(data[4])

    return make_person(id_num, name, weight, height, age)

lines = ['<begin person data>',
         'Id:1613184',
         'Name:Mireielle',
         'Weight:88',
         'Height:1.0378',
         'Age:77',
         '<end person data>']
person = extract_person(lines)
print_person(person)

lines = ['extra junk',
         'and other stuff',
         '<begin person data>',
         'Id:1613184',
         'Name:Mireielle',
         'Weight:88',
         'Height:1.0378',
         'Age:77',
         '<end person data>',
         'blahdyblah']
person = extract_person(lines, 2)
print_person(person)