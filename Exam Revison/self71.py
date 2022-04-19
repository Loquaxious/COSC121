def hacker(stuff):
    for s in stuff:
        if s.startswith('t'):
            print(s + 't')
        else:
            print('t' + s[1:] + s[0])

hacker(['tero', 'yero', 'yactl', 'y'])