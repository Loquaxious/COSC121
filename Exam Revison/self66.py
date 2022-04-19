def process_file(input_name, output_name):
    """L"""
    
    in_file = open(input_name)
    lines = in_file.readlines()
    
    out_file = open(output_name, 'w')
    
    for line in lines:
        line = line.strip(" ")
        for word in line:
            word = word.lower()
            out_file.write(word)
    
    in_file.close()
    out_file.close()
    
# setup a file to convert
text = """Hey??
  This is A funny looking text 
    That nEeds converting 
      tO lower cAse"""
f = open('test.txt', 'w')
f.write(text)
f.close()
# test your function
process_file('test.txt', 'output.txt') 
print(open('output.txt').read())
    