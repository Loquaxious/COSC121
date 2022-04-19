def isbn_dictionary(filename):
    """Reads a file and returns a dictionary that msps ISBNs to (author, title)
    tuples"""
    
    try:
        infile = open(filename)
    except FileNotFoundError:
        print("The file {} was not found.".format(filename))
        return None
    else:
        lines = infile.readlines()
        infile.close()         
    
    books = {}
    for line in lines:
        line = line.strip().split(",")
        book_id = (line[0], line[1])
        books[line[2]] = book_id
    return books

isbn_dictionary("data16.txt")

your_dict = isbn_dictionary('books.csv')
if your_dict != None:
    for isbn in sorted(your_dict.keys()):
        print(isbn + ':', your_dict[isbn])