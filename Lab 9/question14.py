def produce_dictionary(filename):
    """Reads a file and returns the occurnace of words in the file"""
    word_count = {}
    
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            word_count[line] = word_count.get(line, 0) + 1
    
    return word_count 

# Testing with the example data in the question
dictionary = produce_dictionary('data.txt')
for key in dictionary:
    print(key + ': ' + str(dictionary[key]))
    
            
# Testing with an input file that contains only a blank line
dictionary = produce_dictionary('empty.txt')
for key in sorted(dictionary.keys()):
    print(key + ': ' + str(dictionary[key]))