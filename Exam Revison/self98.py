def oink(z):
    a = list(z.keys())
    v = sorted(list(z.values()))
    print(sum(a))
    print(', '.join(v))
    
oink({1:'1', 2:'2', 3:'3'})