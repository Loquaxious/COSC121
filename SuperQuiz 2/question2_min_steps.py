def min_steps(step_records):
    """Returns the minimum steps in a day from given data"""
    if (step_records == []):
        return
    else:
        total = []
        for line in step_records:
            total.append(line[-1])
            
        min_step = min(total)
        
        return min_step        
    

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
mini = min_steps(step_records)
print(mini)

step_records = []
mini = min_steps(step_records)
print(mini)