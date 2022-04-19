""" Program to show key details from data set  
    Author: Logan Lee
    Date: 04/09/19
"""

import os

# def function 1, Calculates the total number of steps in the data given 
def total_steps(step_records):
    """Returns the total number of steps made"""
    total = []
    for line in step_records:
        total.append(line[-1])
    state = sum(total)
    return state

# def function 2, Returns the mininimum steps done in a day
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

# Def feunction 3, Returns the maximum steps done in a day
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

# def function 4, Calculates and returns the average number of steps in the given data
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

# def function 5, 
def days_to_reach_target(step_records, target_steps):
    """Returns the number of days it took to reach or exceed
    a target number"""
    results = 0
    days = 0
    n = 0
    
    while results < target_steps and len(step_records) > days:
        date, steps = step_records[n]
        results += steps
        days += 1
        n += 1
    if results >= target_steps:
        return days

# def function 6,
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

# def function 7,
def activity_level_from_steps(steps):
    """ Function determining activity level based on number of steps done"""
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

# def function 8, 
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

# def function 9, 
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

# def function 10, 
def longest_run_at_level(step_records, activity_level):
    """Returns the length of then longest run of days in a row with 
    the given activity level"""
    run = []
    runs = []
    len_runs = []
    n = 0
    max_len_runs = []
    
    for line in step_records:
        date, steps = step_records[n]
        n += 1
        
        if activity_level == activity_level_from_steps(steps):
            run.append(steps)
            runs.append(run[:])            
        else:
            run = []
    for run in runs:
        len_runs.append(len(run))
        max_len_runs.append(max(len_runs))
    return max(max_len_runs, default=0)

# def function 11, 
def get_valid_filename():
    """Asks the user for a filename and keeps asking until a filename is 
    found"""
    prompt = 'Input file name? '
    filename = input(prompt)
    
    while os.path.isfile(filename) == False:
        print('File does not exist.')
        filename = input(prompt)
    
    return filename

# def function 12, 
def read_records_from_file(filename):
    """Takes a filename and returns the list of records within the file"""
    in_file = open(filename)
    lines = in_file.readlines()
    in_file.close()
    found = False
    initial_data = []
    data = []
    tup_data = []
    for line in lines:
        line = line.rstrip()
        initial_data.append(line)
    for string in initial_data:
        if string == ('<end step data>'):
            found = False
        if found == True:
            data.append(string)
        if string == ('<begin step data>'):
            found = True
    for line in data:
        line.splitlines()
        date = line[0:10]
        steps = int(line[11:])
        tupled = (date, steps)
        tup_data.append(tupled)
    
    return tup_data



# Main def function,
def main():
    """Main function"""
    filename = get_valid_filename()
    step_records = read_records_from_file(filename)
    
    v_a = 'very active'
    
    print("Number of records = {}".format(len(step_records)))
    print("Total steps = {}".format(total_steps(step_records)))
    print("Average steps = {:.2f}".format(average_steps(step_records)))
    print("Maximum steps = {}".format(max_steps(step_records)))
    print("Days to reach 100000 steps = {}".format(days_to_reach_target(step_records, 100000)))
    print("Date reached 100000 steps = {}".format(date_reached_target_steps(step_records, 100000)))
    print("Number of active days = {}".format(n_days_at_activity_level(step_records, 'active')))
    print("Number of very active days = {}".format(n_days_at_activity_level(step_records, v_a)))
    print("Longest run of active days = {}".format(longest_run_at_level(step_records, 'active')))
    
         
main() # A call to the main function