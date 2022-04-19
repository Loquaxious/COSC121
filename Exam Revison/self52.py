def print_odd_squares_to_number(number):
    """L"""
    if number > 0:
        for num in range(1, number+1):
            if num % 2 == 1:
                square = num **2 
                print('{0} * {0} = {1}'.format(num, square)) 
    else:
        print('ERROR: number must be at least 1')
               
        
        
        
print_odd_squares_to_number(5)
print_odd_squares_to_number(3)
print_odd_squares_to_number(0)
