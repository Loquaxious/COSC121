"""
Function that returns some stuff about how many steps done in each month
Author: Logan Lee
Date: 28/09/19
"""
import os

def daily_totals_from_lines(lines):
    """Takes the full list of lines from the file and returns 
    a list of records"""
    begin_step = lines.index('<begin step data>\n')
    end_step = lines.index('<end step data>\n', begin_step + 1)
    records = []
    for line_num in range(begin_step + 1, end_step):
        line = lines[line_num]
        date, step_string = line.strip().split(':')
        readings = step_string.split(',')
        total = 0
        for reading in readings:
            steps = int(reading)
            total = total + steps
        line_data = (date, total)
        records.append(line_data)    
    return records
    
def monthly_averages(records):
    """ Takes a list of records and returns a list containing 
    12 monthly averages
    """
    average_steps = []
    for month in range(1, 13):
        steps_for_month = []
        for date, steps in records:
            rec_month = int(date[5:7])
            if rec_month == month:
                steps_for_month.append(steps)
        if len(steps_for_month) > 0:
            average = sum(steps_for_month) / len(steps_for_month)
            average_steps.append(average)
        else:
            average_steps.append(-1)
    return average_steps

def print_table(averages):
    """Takes a list of averages and prints the average table"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']    
    for month in range(12):
        month_name = months[month]
        average = averages[month]
        if average >= 0:
            print('{}: {:10.2f}'.format(month_name, average))
        else:
            print('{}: {:>6}'.format(month_name, 'n.a.')) 
            
def print_graph(averages):
    """That takes a list of averages and prints the average graph"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']    
    max_bar_size = 50
    bar_char = '='    
    maxi = max(averages)
    for month in range(12):
        month_name = months[month]
        month_average = averages[month]
        #month = i+1
        if month_average >= 0:
            proportion = month_average / maxi
            bar_str = int(proportion * max_bar_size) * bar_char
            print('{}: {}'.format(month_name, bar_str))
        else:
            print('{}: {}'.format(month_name, 'n.a.'))    

def main():
    """Main Function"""
    filename = input('Input file name? ')
    while not os.path.isfile(filename):
        print('File does not exist.')
        filename = input('Input file name? ')
    lines = open(filename).readlines()
    
    records = daily_totals_from_lines(lines)
    
    average_steps = monthly_averages(records)
    
    print_table(average_steps)   
    print()
    print_graph(average_steps)

main()    