def squirrel_play(temp, is_summer):
    """L"""
    
    if is_summer == True:
        if temp < 60 or temp > 100:
            return False
        else: 
            return True
    elif is_summer == False:
        if temp < 60 or temp > 90:
            return False
        else:
            return True        
        
 

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
