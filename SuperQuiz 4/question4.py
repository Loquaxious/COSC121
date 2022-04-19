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


def process_steps(person, lines, index):
    """Takes a persons dictionary, a list of lines and and a index and processes 
    each line of the required data computing the total steps in each line and 
    upadating the dictionary"""
    
    begin = index
    end = lines.index('<end step data>', begin + 1)
    
    steps_data = []
    for line_num in range(begin + 1, end):
        date, steps = lines[line_num].strip().split(':')
        for num in steps.split(','):
            num = int(num)
            steps_data.append(num) 
        total_steps = sum(steps_data)
        steps_data = []
        add_steps(person, date, total_steps)
        
def read_people_from_file(filename):
    """Takes a filename a returns a list of person dictionaries"""
    
    infile = open(filename)
    lines = infile.read().strip().splitlines()
    infile.close()
    
    
    person_indexes = []
    step_indexes = []
    for index, line in enumerate(lines):
        if line == '<begin person data>':
            person_indexes.append(index)
        elif line == '<begin step data>':
            step_indexes.append(index)
    
    people = []
    for num in range(0, len(person_indexes)):
        person = extract_person(lines, person_indexes[num])
        process_steps(person, lines, step_indexes[num])
        people.append(person)
    
    return people
    

    

people = read_people_from_file('data1.txt')
for person in people:
    print_person(person)

