def cigar_party(cigars, is_weekend):
    """F"""
    if is_weekend == False:
        if cigars >= 40 or cigars <= 60:
            return True
        else: 
            return False
    if is_weekend == True:
        if cigars >= 40:
            return True
        else: 
            return False
    else:
        return False
    
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(30, True))
