def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    return "{} {}, {}".format(day_num, month_name, year_num)

print(date_string(1, "December", 1984))
