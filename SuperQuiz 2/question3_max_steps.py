def max_steps(step_records):
    """Returns the maximum steps in a day from given data"""
    if (step_records == []):
        return
    else:
        total = []
        for line in step_records:
            total.append(line[-1])
            
        max_step = max(total)
        
        return max_step    

step_records = [('2010-01-01',1),
                ('2010-01-02',2),
                ('2010-01-03',3)]
maxi = max_steps(step_records)
print(maxi)