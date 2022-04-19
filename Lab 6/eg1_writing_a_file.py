def write_matching_lines(infile_name, outfile_name, test_string):
    infile = open(infile_name)
    lines = infile.readlines()
    outfile = open(outfile_name, 'w')
    for line in lines:
        if test_string in line:
            outfile.write(line)
    infile.close()
    outfile.close()