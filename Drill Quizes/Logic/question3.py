def cigar_party(cigars, is_weekend):
    """L"""
    if is_weekend == True:
        if cigars > 39:
            return True
        else:
            return False
    else:
        if cigars > 39 and cigars < 61:
            return True
        else:
            return False
        
print(cigar_party(50, False))
print(cigar_party(70, True))

    