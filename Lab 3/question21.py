def same_ends(string_1, string_2):
    """Boolean Function which checks to see whether 2 strings have the same 
    start and end characters but are not same"""
    if string_1 == string_2:
        return False
    elif string_1[0] == string_2[0]:
        if string_1[-1] == string_2[-1]:
            return True
        else:
            return False
    else:
        return False 

print(same_ends("flubber", "fester"))
print(same_ends("flubber", "flubber"))
print(same_ends("flubber", "feast"))
print(same_ends("flubber", "rubber"))