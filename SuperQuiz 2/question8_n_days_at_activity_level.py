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

def n_days_at_activity_level(step_records, activity_level):
    """Returns the number of days with the given activity level"""
    steps = []
    for line in step_records:
        steps.append(line[-1])
    days = 0
    for step in steps:
        if activity_level == activity_level_from_steps(step):
            days += 1
    return days
              

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
days = n_days_at_activity_level(step_records, 'sedentary')
print(days)

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
days = n_days_at_activity_level(step_records, 'active')
print(days)

step_records = []
days = n_days_at_activity_level(step_records, 'sedentary')
print(days)

step_records = [('2010-01-01',12000),
                ('2010-01-02',22000),
                ('2010-01-03',33000)]
days = n_days_at_activity_level(step_records, 'active')
print(days)