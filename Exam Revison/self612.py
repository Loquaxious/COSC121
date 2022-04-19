def generate_stats(filename):
    """L"""
    
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    values = []
    for line in lines:
        for value in line.split(','):
            values.append(float(value))
    
    tupe = (max(values), min(values), sum(values)/len(values))
    
    return tupe    

f = open('day_temps.txt', 'w')
f.write("10.3,10.1,9.9,9.9,9.8,9.6,9.0,10.1,10.2,11.1")
f.close()
(maximum, minimum, average) = generate_stats('day_temps.txt')
print("({0:.5}, {1:.5}, {2:.5})".format(maximum, minimum, average))