def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    
    date = (str(day_num) + " " + month_name + "," + " " + str(year_num))
    return date

print(date_string(1, "December", 1984))
print(date_string(29, "February", 2020))