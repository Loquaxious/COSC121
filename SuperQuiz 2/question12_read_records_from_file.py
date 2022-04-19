def read_records_from_file(filename):
    """Takes a filename and returns the list of records within the file"""
    in_file = open(filename)
    lines = in_file.readlines()
    in_file.close()
    found = False
    initial_data = []
    data = []
    tup_data = []
    for line in lines:
        line = line.rstrip()
        initial_data.append(line)
    for string in initial_data:
        if string == ('<end step data>'):
            found = False
        if found == True:
            data.append(string)
        if string == ('<begin step data>'):
            found = True
    for line in data:
        line.splitlines()
        date = line[0:10]
        steps = int(line[11:])
        tupled = (date, steps)
        tup_data.append(tupled)
    
    return tup_data
        
        
    
        
            
records = read_records_from_file('data1.txt')
print(records)        