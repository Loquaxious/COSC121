"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""
    
def get_data(filename): 
    """ahaahahah"""
    datafile = open(filename)
    data = datafile.readlines()
    datafile.close()
    return data

def results_processing(data):
    """processes results"""
    results = []
    for line in data:
        columns = line.split(',')
        results.append(column_thingy(columns))
    return results

def column_thingy(columns):
    """cat"""
    total_rainfall = 0
    for col in columns[2:2 + int(columns[1])]:
        total_rainfall += float(col)
    tuple0 = (int(columns[0]), total_rainfall)
    return tuple0

def print_rainfalls(results):
    """rainuk"""
    print('Rainfall totals for each month')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))
    
def print_monthly_rainfalls(input_csv_filename):
    """Process the given csv file of rainfall data and print the
       monthly rainfall totals. input_csv_filename is the name of
       the input file, which is assumed to have the month number in
       column 1, the number of days in the month in column 2 and the
       floating point rainfalls (in mm) for each month in the remaining
       columns of the row.
    """
    data = get_data(input_csv_filename)
    results = results_processing(data)
    print_rainfalls(results)

def main():
    """The main function"""
    print_monthly_rainfalls("rainfalls2011.csv")

main()