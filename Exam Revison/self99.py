def commoners(course1, course2, course3):
    """L"""
    
    one = set(course1)
    two = set(course2)
    three = set(course3)
    
    all3 = one & two & three
    
    return all3