def count_lines_with_word(filename, word):
    """L"""
    infile = open(filename)
    lines = infile.readlines()
    infile.close
    count = 0
    for line in lines:
        words = line.split()
        if word in words:
            count += 1
    return count

print(count_lines_with_word('hippo.txt', 'hippo'))
