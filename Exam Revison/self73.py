def double_first(data, nuclear=False):
    """L"""
    new = []
    if nuclear:
        for thing in data:
            new.extend([thing, thing])
    else:
        for index, thing in enumerate(data):
            if index == 0:
                new.append(thing)            
            new.append(thing)            
    
    return new 

ans = double_first([1,2,3,4,5,6])
print(ans)

ans = double_first([1 , 2, 3], True)
print(ans)

ans = double_first(['hi','there','what','fun'], False)
print(ans)