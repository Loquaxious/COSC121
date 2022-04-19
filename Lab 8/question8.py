"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""

def print_month_totals(input_csv_filename):
    """Process the given csv file of rainfall data and print the
       monthly rainfall totals. input_csv_filename is the name of
       the input file, which is assumed to have the month number in
       column 1, the number of days in the month in column 2 and the
       floating point rainfalls (in mm) for each month in the remaining
       columns of the row.
    """
    data = read_file(input_csv_filename)
    results = process_data(data)
    print_data(results)
    
def read_file(input_csv_filename):
    """Reads ands stores the file in memory"""
    datafile = open(input_csv_filename)
    data = datafile.readlines()
    datafile.close()
    return data
    
def process_data(data):
    """Processes data"""
    results = []
    for line in data:
        columns = line.split(',')
        results.append(rain_total(columns))
    return results

def rain_total(columns):
    """Totals and formats data"""
    total_rainfall = 0
    for col in columns[2:2 + int(columns[1])]:
        total_rainfall += float(col)
    tup = (int(columns[0]), total_rainfall)
    return tup
    
def print_data(results):
    """Prints stuff"""
    print('Rainfall totals for each month')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))


def main():
    """The main function"""
    print_month_totals("rainfalls2011.csv")


main()