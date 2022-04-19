"""
Function that returns some stuff about how many steps done in each month
Author: Logan Lee
Date: 28/09/19
"""
import os


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


def main():
    """Main Function"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']    
    max_bar_size = 50
    bar_char = '='
    
    filename = input('Input file name? ')
    while not os.path.isfile(filename):
        print('File does not exist.')
        filename = input('Input file name? ')
    lines = open(filename).readlines()
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
    
    average_steps = monthly_averages(records)
    
    for month in range(12):
        month_name = months[month]
        average1 = average_steps[month]
        if average1 >= 0:
            print('{}: {:10.2f}'.format(month_name, average1))
        else:
            print('{}: {:>6}'.format(month_name, 'n.a.'))    
    print()
    maxi = max(average_steps)
    for month in range(12):
        month_name = months[month]
        month_average = average_steps[month]
        #month = i+1
        if month_average >= 0:
            proportion = month_average / maxi
            bar_str = int(proportion * max_bar_size) * bar_char
            print('{}: {}'.format(month_name, bar_str))
        else:
            print('{}: {}'.format(month_name, 'n.a.'))

main()    