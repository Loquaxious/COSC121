def Four_letters():
    filename = input("Enter filename: ")
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    string = ""
    for line in lines:
        words = line.split()
        for word in words:
            if len(word) == 4:
                string.join("****")
            else:
                string.join(word)
    return print(string)

Four_letters()
    