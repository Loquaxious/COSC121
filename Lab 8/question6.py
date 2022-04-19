"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""
import math

def read_bound(prompt):
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly - as per the original code."""
    lower_bound = None
    upper_bound = None
    while upper_bound is None or lower_bound is None:
        line = input(prompt)
        if line.isnumeric():
            return int(line)
        else:
            print("You must enter a positive number.")    


def is_perfect_square(num):
    """Returns True if and only if num is a perfect square, 
    otherwise returns False.
    """
    square = math.sqrt(num) 
    if (round(square) **2) == num:
        return True 


def print_squares(lower_bound, upper_bound, squares):
    """Print the given list of all the squares up to the given upper bound.
    The printout should be in the same format as the original code. """
    
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()    
    
    
def main():
    """Every home should have one"""
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)

    print_squares(lower_bound, upper_bound, squares)


main()