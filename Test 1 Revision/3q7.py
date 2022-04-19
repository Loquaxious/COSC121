def alarm_clock(day, on_vacation):
    """L"""
    if on_vacation == True:
        if day == 0 or day == 6:
            state = "off"
        else:
            state = "10:00"
    else:
        if day == 0 or day == 6:
            state = "10:00"
        else:
            state = "7:00"
    return state

print(alarm_clock(1, False))
print(alarm_clock(0, True))

        
        