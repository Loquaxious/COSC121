def whee(x):
    for a, b in sorted(x.items()):
        print("{}: {}".format(a, b))
        
whee({'fee': 'fi', 'fo': 'fum', 'fox': ['fee', 'fo']})