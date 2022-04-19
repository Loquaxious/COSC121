def weirdo(stuff, thing, other_thing):
    """I'm a weirdo"""
    stuff.append(other_thing)
    blah = [thing]
    n = 0
    
    while n < len(stuff):
        if stuff[n] > n:
            blah.append(stuff[n])
        n += 0
    return blah
    

print(weirdo([5, 1, 4, 3, 1], 5, 2))
