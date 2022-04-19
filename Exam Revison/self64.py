def sum_numbers_in_file(filename):
    """L"""
    
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    values = []
    for line in lines:
        try:
            int(line)
        except ValueError:
            pass
        else:
            values.append(int(line))
            
    return sum(values)

answer = sum_numbers_in_file('sum_nums_test_01.txt')
print(answer)