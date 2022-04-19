def max_num_in_file(filename):
    """L"""
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    result = []
    for line in lines:
        line = int(line)
        result.append(line)
    maxnum = max(result)
    return maxnum

answer = max_num_in_file('max_num_in_file_test_01.txt')
print(answer)