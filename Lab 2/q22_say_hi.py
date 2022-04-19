def say_hi():
    """ Function that will display a persons name with appropiate 
    capitalisiation """
    
    name = input("What is your name? ")
    name = name.title()
    
    print("Hi " + name)
    
say_hi()