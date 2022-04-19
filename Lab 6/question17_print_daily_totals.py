def print_daily_totals(filename):
    """Returns the date and the totals of the vlues recorded in a
    given data set"""
    file = open(filename)
    lines = file.readlines()
    floats = []
    for line in lines:
        data = line.split(",")
        date = data[0]
        floats = list(map(float, data[1:]))
        total = sum(floats)
        print("{0} = {1:.2f}".format(date, total))
            
        
        
                  
        


print_daily_totals('data61.txt')