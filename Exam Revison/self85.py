"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""
def print_rainfalls(input_csv_filename):
    """Process the given csv file of rainfall data and print the
       monthly rainfall totals. input_csv_filename is the name of
       the input file, which is assumed to have the month number in
       column 1, the number of days in the month in column 2 and the
       floating point rainfalls (in mm) for each month in the remaining
       columns of the row.
    """
    
    data = get_data(input_csv_filename)
    results = process_data(data)
    print_rainfall(results)
    
def get_data(input_csv_filename):
    """L"""
    datafile = open(input_csv_filename)
    data = datafile.readlines()
    datafile.close()
    
    return data

def process_data(data):
    """L"""
    
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns = line.split(',')
        results.append(get_results(columns))
    
    return results
         

def get_results(columns):
    """L"""
    
    total_rainfall = 0
    month = int(columns[0])
    num_days = int(columns[1])
    for col in columns[2:2 + num_days]:
        total_rainfall += float(col)
    tup = (int(month), total_rainfall)
    
    return tup


def print_rainfall(results):
    """L"""
    print('Monthly rainfalls')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))        
        
        

def main():
    """The main function"""
    print_rainfalls("rainfalls2011.csv")



main()