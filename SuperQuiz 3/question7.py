"""
Function that returns some stuff about how many steps done in each month
Author: Logan Lee
Date: 28/09/19
"""
import os


def get_data():
    """Returns the data in a given file"""
    filename = input('Input file name? ')
    while not os.path.isfile(filename):
        print('File does not exist.')
        filename = input('Input file name? ')
    lines = open(filename).readlines() 
    return lines


def get_person_data(lines):
    """Collects the person data from the file"""
    data = []
    begin = lines.index('<begin person data>\n')
    end = lines.index('<end person data>\n', begin + 1)
    for line_num in range(begin+1, end):
        key, value = lines[line_num].strip().split(":")
        data.append(value)
    return data


def print_person_data(person_data):
    """Takes a list of the person data and prints it"""
    name = person_data[0]
    weight = float(person_data[1])
    age = int(person_data[2])
    print('----------------------------------------')
    print('{}, {:.2f} kgs, {} years'.format(name, weight, age))
    print('----------------------------------------')    


def daily_totals_from_lines(lines):
    """Takes the relevant data from the file and returns 
    a list of records"""    
    records = []
    for line_num in range((lines.index('<begin step data>\n')) + 1, 
                          lines.index('<end step data>\n', 
                                      (lines.index('<begin step data>\n')) + 1)):
        date, step_string = lines[line_num].strip().split(':')
        readings = step_string.split(',')    
        total = 0
        for reading in readings:
            total = total + check_invalid_data(reading)
        line_data = (date, total)
        records.append(line_data)    
    return records


def check_invalid_data(reading):
    """Checks for whether data is corrpted or invalid"""
    try:
        int(reading)
    except ValueError:
        return 0
    else:
        if int(reading) < 0:
            return 0
        else:
            return int(reading)


def monthly_averages(records):
    """ Takes a list of records and returns a list containing 
    12 monthly averages
    """
    average_steps = []
    for month in range(1, 13):
        steps_for_month = []
        for date, steps in records:
            if int(date[5:7]) == month:
                steps_for_month.append(steps)
        if len(steps_for_month) > 0:
            average_steps.append(sum(steps_for_month)/len(steps_for_month))                 
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
    maxi = max(averages)
    for month in range(12):
        month_name = months[month]
        month_average = averages[month]
        #month = i+1
        if month_average >= 0:
            proportion = month_average / maxi
            bar_str = int(proportion * 50) * '='
            print('{}: {}'.format(month_name, bar_str))
        else:
            print('{}: {}'.format(month_name, 'n.a.'))    


def main():
    """Main Function"""
    lines = get_data()
    person_data = get_person_data(lines)
    print_person_data(person_data)
    records = daily_totals_from_lines(lines)
    average_steps = monthly_averages(records)
    print_table(average_steps)   
    print()
    print_graph(average_steps)

main()    