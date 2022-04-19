initial_principal = 1000.0 
interest_rate_per_annum = 0.1

interest_rate_per_month = interest_rate_per_annum / 12
principal = initial_principal
num_months = 0

while principal < 3 * initial_principal:
    increase = principal * interest_rate_per_month
    principal = principal + increase
    num_months += 1

print("It took {0} months to double the principal".format(num_months))