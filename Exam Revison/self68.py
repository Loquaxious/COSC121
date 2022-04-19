def min_number_from_file(filename):
    """l"""
    
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    values = []
    for line in lines:
        values.append(int(line))
    
    return min(values)

answer = min_number_from_file('test_01.txt')
print(answer)