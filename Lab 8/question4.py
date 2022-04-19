"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

def read_bound():
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly - as per the original code."""
    
    upper_bound = None
    while upper_bound is None:
        line = input("Enter the upper bound: ")
        if line.isnumeric():
            return int(line)
        else:
            print("You must enter a positive number.")



def is_perfect_square(num):
    """Returns True if and only if num is a perfect square, 
    otherwise returns False.
    """
    for candidate in range(1, num):
        if candidate * candidate == num:
            return True 

def print_squares(upper_bound, squares):
    """Print the given list of all the squares up to the given upper bound.
    The printout should be in the same format as the original code. """
    
    print("The perfect squares up to {} are: ".format(upper_bound))
    for square in squares:
        print(square, end=' ')
    print()    
    
    

def main():
    """Every home should have one"""
    upper_bound = read_bound()
    squares = []
    for num in range(2, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)
    
    print_squares(upper_bound, squares)


main()