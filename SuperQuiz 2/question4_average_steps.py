def total_steps(step_records):
    """Returns the total number of steps made"""
    total = []
    for line in step_records:
        total.append(line[-1])
    sums = sum(total)
    return sums

def average_steps(step_records):
    """Returns the average number steps from given data"""
    if (step_records == []):
        return
    else:
        total = []
        for line in step_records:
            total.append(line[-1])        
        
        denom = len(total)
        av_steps = total_steps(step_records) / denom 
        
        return av_steps        


step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
avg = average_steps(step_records)
print(avg)

step_records = []
avg = average_steps(step_records)
print(avg)

step_records = [('2010-01-01',3),
                ('2010-01-02',3),
                ('2010-01-03',3),
                ('2010-01-04',3),
                ('2010-01-05',3)]
avg = average_steps(step_records)
print(avg)