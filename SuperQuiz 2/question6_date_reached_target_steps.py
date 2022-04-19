def date_reached_target_steps(step_records, target_steps):
    """Returns the date where the total number of steps reaches 
    or exceeds target_steps"""
    
    results = 0
    days = 0
    n = 0
    
    while results < target_steps and len(step_records) > days:
        date, steps = step_records[n]
        results += steps
        days += 1
        n += 1
    if results >= target_steps:
        return date
    
step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
date = date_reached_target_steps(step_records, 3)
print(date)

step_records = [('2010-01-01',3),
                ('2010-01-02',2),
                ('2010-01-03',1)]
date = date_reached_target_steps(step_records, 3)
print(date)

step_records = [('2010-01-01',3),
                ('2010-01-02',2),
                ('2010-01-03',1)]
date = date_reached_target_steps(step_records, 50)
print(date)

step_records = [('2010-01-01',12000),
                ('2010-01-02',4000),
                ('2010-01-03',6500),
                ('2010-01-04',5400),
                ('2010-01-05',15200),
                ('2010-01-06',18100),
                ('2010-01-07',18100)]
date = date_reached_target_steps(step_records, 50000)
print(date)