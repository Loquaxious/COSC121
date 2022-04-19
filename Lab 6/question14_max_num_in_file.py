def max_num_in_file(filename):
    """Returns the largest integer found in a given file"""
    file = open(filename)
    lines = file.readlines()
    result = []
    for line in lines:
        for num in line.split():
            result.append(int(num))
    return max(result)
 

answer = max_num_in_file('max_num_in_file_test_01.txt')
print(answer)            