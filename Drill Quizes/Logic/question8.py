def sorta_sum(int_a, int_b):
    """L"""
    sums = int_a + int_b
    if sums >= 10 and sums <= 19:
        return 20
    else:
        return sums
    
print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
    