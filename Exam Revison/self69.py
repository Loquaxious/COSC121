def case_fixer(input_name, output_name):
    """L"""
    
    infile = open(input_name)
    lines = infile.readlines()
    infile.close()
    
    outfile = open(output_name, 'w')
    
    for line in lines:
        for word in line:
            word = word.upper()
            outfile.write(word)
    
    infile.close()
    outfile.close()    

# setup a file to convert
text = """Hey??
  This is A funny looking text 
    That nEeds converting 
      tO upper cAse"""
f = open('test.txt', 'w')
f.write(text)
f.close()
# test your function
case_fixer('test.txt', 'output.txt') 
print(open('output.txt').read())