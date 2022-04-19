def sum_numbers_in_file(filename):
    """Returns the sum of the data provided by a given file"""
    file = open(filename)
    lines = file.readlines()
    result = []
    for line in lines:
        for num in line.split():
            result.append(int(num))
    return sum(result) 

ans = sum_numbers_in_file('sum_nums_test_01.txt')
print(ans)