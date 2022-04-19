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
    datafile = open(input_csv_filename)
    data = datafile.readlines()
    datafile.close()
    
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns = line.split(',')
        month = int(columns[0])
        total_rainfall = 0
        for col in columns[2:]:
            total_rainfall += float(col)
        results.append((month, total_rainfall))

    print('Rainfall totals for each month')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))


def main():
    """The main function"""
    print_month_totals("rainfalls2011.csv")


main()