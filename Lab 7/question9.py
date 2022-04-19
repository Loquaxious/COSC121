def is_old_enough(age):
    """Blah"""
    LEGAL_AGE = 18
    
    if age >= LEGAL_AGE:
        return True
    else:
        return False
 
print(is_old_enough(19))
print(is_old_enough(18))
print(is_old_enough(17))
