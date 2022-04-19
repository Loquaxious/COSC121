def max_number_from_file(filename):
    """L"""
    
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    values = []
    for line in lines:
        values.append(int(line))
    
    return max(values)

answer = max_number_from_file('test_01.txt')
print(answer)