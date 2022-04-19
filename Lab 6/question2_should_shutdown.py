def should_shutdown(battery_level, time_on):
    """Returns whether a device should shutdown based on battery
    level and time on"""
    if ((time_on < 60) and (battery_level < 4.7)):
        state = True
        
    elif ((battery_level < 4.8) and (time_on >= 60)):
        state = True
        
    else:
        state = False
        
    return state 

ans1 = should_shutdown(5, 10)
print(ans1)
        
ans2 = should_shutdown(4.74, 90)
print(ans2)  

ans = should_shutdown(4.74, 50)
print(ans)