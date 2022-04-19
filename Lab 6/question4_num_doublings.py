def num_doublings(initial_population, final_population):
    """Returns the number of iterations to double a given value to
    reach another given value""" 
    num = 0
    while initial_population < final_population:
        initial_population *= 2
        num += 1
    return num



ans = num_doublings(1, 8)
print(ans)