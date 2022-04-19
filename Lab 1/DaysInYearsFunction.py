def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    ans = number_of_years * 365
    return ans

print(days_in_years(1))
print(days_in_years(15))