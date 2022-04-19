def date_fashion(you, date):
    """L"""
    if you <= 2 or date <= 2:
        return 0
    elif you > 7 or date > 7:
        return 2
    else:
        return 1
        
print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(10, 2))
