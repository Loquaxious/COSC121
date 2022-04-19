def BMI ():
    """ Prompt the user for their weight in kg and height in m 
    then calculate and print an their BMI """
    
    weight = input(" what is your weight in kg? ")
    height = input(" what is your height in m? ")
    
    weight = float(weight)
    height = float(height)
    
    BMI_value = weight / height ** 2 
    
    print(" Your BMI is ", BMI_value)
    
BMI()




