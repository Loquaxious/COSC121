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
    
    
lines = [
    'Earlier lines all omitted here',
    'Junk line',
    '<begin step data>',
    '2001-01-10:218,37,356,621,466,319,147,774,231,167,399,150,417,34,3',
    '2001-01-04:639,118,328,413,222,491,738,389,11,372,183,650,281,643,26,398,685,171',
    '<end step data>',
    'more junk',
    'and still more',
]
person = make_person(1294919, 'Russell', 97.00, 1.90, 24)
process_steps(person, lines, 2)
print_person(person)

infile = open('data0.txt')
lines = infile.read().splitlines()
infile.close()
person = extract_person(lines, 4)
print_person(person)
process_steps(person, lines, 18)
print_person(person)