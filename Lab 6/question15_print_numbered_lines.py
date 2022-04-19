def print_numbered_lines(filename):
    """Prints out all the lines of a given file with a line number"""
    file = open(filename)
    lines = file.readlines()
    result = []
    for (num, line) in enumerate(lines):
        print("{0}: {1}".format((num + 1), line), end="")
    
        
print_numbered_lines('marks1.txt')
print_numbered_lines('marks2.txt')