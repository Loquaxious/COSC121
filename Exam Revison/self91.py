def spit(x, y):
    z = x - y
    print(len(x), len(y))
    if (x|y).issuperset(x|z):
        print(sorted(list(z)))
    else:
        print(sorted(list(y)))

spit({'fee','fi','fo','fum','hey'}, {'me','dude','sup','hey'})