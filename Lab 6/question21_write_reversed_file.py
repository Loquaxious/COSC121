def write_reversed_file(input_filename, output_filename):
    """Writes to a given output the reverse of a input file"""
    infile = open(input_filename)
    lines = infile.readlines()
    infile.close()
    
    outfile = open(output_filename, 'w')
    
    for line in reversed(lines):
        outfile.write("{}\n".format(line.rstrip()))
        
    outfile.close()    
    
import os.path
write_reversed_file('data.txt', 'reversed1.txt')
if not os.path.exists('reversed1.txt'):
    print("You don't seem to have created the required output file!")
else:
    print(open('reversed1.txt').read()) 