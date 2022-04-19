def silly(stuff, more_stuff=None):
    data = []
    for i, thing in enumerate(stuff):
        if thing >= 0 or i < 2:
            data.append(thing + i)
    print(len(stuff))
    if more_stuff is not None:
        data += more_stuff
    print(data)
    
silly([5, 2, -1, -1], [1, 5,-3])