def splatter(stuff):
    for s in stuff:
        if s.startswith('v'):
            print(s + 'v')
        else:
            print('v' + s[1:] + s[0])

splatter(['vero', 'yero', 'yactl', 'y'])