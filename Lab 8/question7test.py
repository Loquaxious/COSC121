"""Read and process a file of student names and marks.
   Written for COSC121S2.
   Author: Logan Lee
   Date: 23 September 2019.
"""

def get_filename():
    """Return the name of the student data file to be processed.
       This is a so-called 'stub' implementation which always returns
       the same filename. A fuller implementation would prompt the user
       for the filename.
    """
    return "test.txt"


def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    line_list = []
    for line in lines:
        line = line.split(",")
        line_list.append(tuple(line))
    return line_list


def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple containing
       statistics extracted from the list. The components of the returned tuple 
       are minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    stats = []
    for item in student_data:
        stats.append(float(item[1]))
    max_mark = max(stats)
    min_mark = min(stats)
    average_mark = (sum(stats) / len(stats))
    
    top_students = []
    for item in student_data:
        if float(item[1]) == float(max_mark):
            top_students.append(item[0])
    return(min_mark, max_mark, average_mark, sorted(top_students))

def print_results(stats):
    """Print the statistics given. The parameters 'stats' is a
       tuple of the form returned by the 'statistics' function
       above. The required output is shown in the example output table.
    """
    (minimum, maximum, average, top_students) = stats
    print("Minimum mark: {:.2f}".format(minimum))
    print("Maximum mark: {:.2f}".format(maximum))
    print("Average mark: {:.2f}".format(average))

    if len(top_students) == 1:
        print("The top student is: {}".format(top_students[0]))
    else:
        print("The top-equal students are:\n  {}".format(", ".join(top_students)))


def main():
    """The main function (see module docstring)"""
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)

main()