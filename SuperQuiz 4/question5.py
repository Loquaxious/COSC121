"""Function that reads files and extracts person data then creates a step log for
   them
   Date: 13/10/19
   Author: Logan Lee
"""
class Person:
    """Defines a Person class, suitable for a steps log context 
    Data Attributes: id_num of class int
                     name of type str
                     weight of type float
                     height of type float
                     age of type int
                     num_steps of type int
                     first_date_recorded of type str
                     last_date_recorded of type str
    
    Methods: bmi()
             __str__()
             __repr__()
    """

    def __init__(self, id_num, name, weight, height, age):
        """Creates and returns a dictionary with the inputs names as keys"""
        
        self.id_num = id_num
        self.name = name
        self.weight = weight
        self.height = height 
        self.age = age
        self.num_steps = 0
        self.first_date_recorded = None
        self.last_date_recorded = None
        
    
    
    def bmi(self):
        """Returns float of body mass index based off persons details"""
        
        weight = self.weight
        height = self.height
        bmi_val = weight / (height ** 2)
        return bmi_val
    
    
    def add_steps(self, date, steps):
        """Updates the given persons steps by incrementing the num_steps value 
        by the given number of steps"""
        
        self.num_steps += steps
        
        if self.first_date_recorded == None and self.last_date_recorded == None:
            self.first_date_recorded = date
            self.last_date_recorded = date
        
        elif self.first_date_recorded > date:
            self.first_date_recorded = date
        
        elif self.last_date_recorded < date:
            self.last_date_recorded = date
            
        
    def __str__(self):
        """Prints the formatted details of a given person"""
        
        final_str = ''
        final_str += '----------------------------------------\n'
        final_str += '{0} - {1}\n'.format(self.id_num, self.name)
        final_str += '{0:.2f} kgs, {1:.2f} m, {2} years\n'.format(self.weight, \
                                                         self.height, \
                                                         self.age)
        final_str += 'BMI = {0:.2f}\n'.format(self.bmi())
        final_str += 'Total steps = {0}\n'.format(self.num_steps)
        final_str += 'First date recorded = {0}\n'.format(self.first_date_recorded)
        final_str += 'Last date recorded = {0}\n'.format(self.last_date_recorded)
        final_str += '----------------------------------------'
        return final_str
    
    def __repr__(self):
        """Return a formatted string of a given person"""
        
        template = "Person({0}, '{1}', {2:.2f}, {3:.2f}, {4})"
        id_num = self.id_num
        name = self.name
        weight = self.weight
        height = self.height
        age = self.age
        
        return template.format(id_num, name, weight, height, age)
    
    
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

    return Person(id_num, name, weight, height, age)


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
        Person.add_steps(person, date, total_steps)
        
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
    
# Exercise the Person class a bit
bod = Person(1665845, 'Rurick', 101.00,1.98, 75)
print(bod)
print(repr(bod))
print("{:.2f}".format(bod.bmi()))
bod.add_steps("2018-07-23", 2000)
print(bod)
bod.add_steps("2018-06-31", 2000)
print(bod)
bod.add_steps("2019-01-01", 2000)
print(bod)

people = read_people_from_file('data1.txt')
for person in people:
    print(person)
    
people = read_people_from_file('data1.txt')
print(people)