def months_to_reach_target(principal, interest_rate_per_annum, target):
    """returns the number of months it takes to reach a target savings"""
    irpa = interest_rate_per_annum / 100
    irpm = irpa / 12
    num_months = 0
    
    while principal < target:
        increase = principal * irpm
        principal += increase
        num_months += 1
    return num_months 
print(months_to_reach_target(100, 10, 200))
print(months_to_reach_target(100, 24, 105))
print(months_to_reach_target(100, 10, 100))
print(months_to_reach_target(100, 30, 130))
