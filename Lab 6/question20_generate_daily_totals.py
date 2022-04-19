def generate_daily_totals(input_filename, output_filename):
    """Reads an input file and for each line of that file
    writes out a summary line"""
    infile = open(input_filename)
    lines = infile.readlines()
    infile.close()
    
    outfile = open(output_filename, 'w')
    
    floats = []
    for line in lines:
        data = line.split(",")
        date = data[0]
        floats = list(map(float, data[1:]))
        total = sum(floats)
        outfile.write("{0} = {1:.2f}\n".format(date, total))
    
    outfile.close()

generate_daily_totals('data61.txt', 'totals.txt')
checker = open('totals.txt')
print(checker.read())
checker.close()