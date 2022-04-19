import os
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MAX_BAR_SIZE = 50
BARCHAR = '='
filename = input('Input file name? ')
while not os.path.isfile(filename):
    print('File does not exist.')
    filename = input('Input file name? ')
lines = open(filename).readlines()
s = lines.index('<begin step data>\n')
e = lines.index('<end step data>\n', s + 1)
records = []
for line_num in range(s + 1, e):
    line = lines[line_num]
    date, step_string = line.strip().split(':')
    readings = step_string.split(',')
    total = 0
    for reading in readings:
        steps = int(reading)
        total = total + steps
    line_data = (date, total)
    records.append(line_data)
avers = []
for month in range(1, 13):
    steps_for_month = []
    for date, steps in records:
        rec_month = int(date[5:7])
        if rec_month == month:
            steps_for_month.append(steps)
    if len(steps_for_month) > 0:
        av = sum(steps_for_month) / len(steps_for_month)
        avers.append(av)
    else:
        avers.append(-1)
for m in range(12):
    month_name = MONTHS[m]
    average = avers[m]
    if average >= 0:
        print('{}: {:10.2f}'.format(month_name, average))
    else:
        print('{}: {:>6}'.format(month_name, 'n.a.'))
print()
a = []
for month in range(1, 13):
    steps_for_month = []
    for date, steps in records:
        rec_month = int(date[5:7])
        if rec_month == month:
            steps_for_month.append(steps)
    if len(steps_for_month) > 0:
        av = sum(steps_for_month) / len(steps_for_month)
        a.append(av)
    else:
        a.append(-1)
maxi = max(a)
for m in range(12):
    month_name = MONTHS[m]
    month_average = a[m]
    #month = i+1
    if month_average >= 0:
        proportion = month_average / maxi
        bar_str = int(proportion * MAX_BAR_SIZE) * BARCHAR
        print('{}: {}'.format(month_name, bar_str))
    else:
        print('{}: {}'.format(month_name, 'n.a.'))
