def fillerup(items, capacity):
    """L"""
    i = 0
    w_update = 0
    weight = 0
    total_weight = 0
    result = []
    while i < len(items):
        thing = items[i]
        w_update +=thing[-1]
        if w_update < capacity:
            result.append(thing)
            weight += thing[-1]   
        i += 1
    return result, weight

items, weight = fillerup([('a',10),('b',20)], 15)
print(items, weight)
print(type(items))

items = [('a',10),
         ('b',20),
         ('f',50),
         ('g',70)]
items, weight = fillerup(items, 90)
print(items, weight)