def guess_a_number(target_number, lower_bound, upper_bound): 
    """Checks whether you have guessed the wrong or correct number
    and displays whether it is or not"""
    print("I'm thinking of a number between {0} and {1}.".format(lower_bound, upper_bound))
    
    while True:
        num = int(input("What do you think it is? "))
        if num != target_number:
            print("That's not my number. Try again.")
        else:
            print("Congratulations! You guessed my number!")
            break 
guess_a_number(7, 6, 8)