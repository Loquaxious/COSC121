def thing(i, j):
    """Does something silly"""
    return (i > 10 and not (j < 5 or i > 20))



#Below is testing to see if function above is correct
def thing2(i, j):
    """Does something silly"""
    if i > 10:
        if j < 5 or i > 20:
            return False
        else:
            return True
    else:
        return False

print(thing(10,6), thing2(10,6))
print(thing(11,5), thing2(11,5))
print(thing(12,5), thing2(12,5))
print(thing(13,5), thing2(13,5))
print(thing(18,5), thing2(18,5))
print(thing(19,5), thing2(19,5))
print(thing(12,0), thing2(12, 0))
print(thing(19,0), thing2(19, 0))
print(thing(20,0), thing2(20, 0))