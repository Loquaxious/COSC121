"""Demo of importing and using a module.
   To be modified for this question as explained in the instructions.
"""
import statistics

FILENAME = "data.txt"   # Name of file containing numbers, one per line

def main():
    """Read some numbers from a file and print their median"""
    in_file = open(FILENAME)
    lines = in_file.read().splitlines()
    in_file.close()

    # Now convert all the lines of text (strings) to numeric values
    numbers = []
    for line in lines:  # Process each line, which must be a number
        numbers.append(float(line))  # Convert string to a number

    # Print the count and the median
    #median_value = statistics.median(numbers)  # Call the median function
    #print("{} numbers read".format(len(numbers)))
    #print("Median is {:.3f}".format(median_value))
    
    #Print and count the standard deviation
    standard_deviation = statistics.stdev(numbers)
    print("Standard deviation is {:.2f}".format(standard_deviation))

main()