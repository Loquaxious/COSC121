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