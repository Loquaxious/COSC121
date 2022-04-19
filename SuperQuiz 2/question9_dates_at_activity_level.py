def activity_level_from_steps(steps):
    """Function determining activity level based on number of steps done"""
    if (steps == 0):
        state = 'alive?'
    elif (steps < 5000):
        state = 'sedentary'
    elif (steps < 7500):
        state = 'very low'
    elif (steps < 10000):
        state = 'low'
    elif (steps < 12500):
        state = 'active'
    else:
        state = 'very active'
    return state

def dates_at_activity_level(step_records, activity_level):
    """Returns the dates that had the given activity level"""
    dates = []
    n = 0
    
    for line in step_records:
        date, steps = step_records[n]
        n += 1
        
        if activity_level == activity_level_from_steps(steps):
            dates.append(date)    
    return dates

        

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
days = dates_at_activity_level(step_records, 'sedentary')
print(days)

step_records = [('2010-01-01',10000),
                ('2010-01-02',20123),
                ('2010-01-03',30342)]
days = dates_at_activity_level(step_records, 'sedentary')
print(days)

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3),
                ('2010-01-04',3),
                ('2010-01-05',12000),
                ('2010-01-06',18000)]
dates = dates_at_activity_level(step_records, 'active')
print(dates)