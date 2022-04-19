def print_reversed(filename):
    """Returns the reversed lines of a given txt document"""
    file = open(filename)
    lines = file.readlines()
    for line in reversed(lines):
        print(line.rstrip())
    
    

print_reversed('data.txt')        