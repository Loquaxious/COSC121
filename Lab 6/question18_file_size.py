def file_size(filename):
    """Returns the number of character per line of a file"""
    file = open(filename)
    lines = file.readlines()
    file.close()
    c_list = []
    for line in lines:
        count = len(line)
        c_list.append(count)
        total = sum(c_list)
    return total

print(file_size('data.txt'))