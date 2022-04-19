def zapper(x):
    print(len(x))
    s = set(x)
    y = {'fo', 'fum'}
    if len(s.intersection(y)) == 1:
        s = s.union(y)
        print(', '.join(sorted(list(s))))
        
zapper(['fi','fum','logan', 'fi', 'logan'])