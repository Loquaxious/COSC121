def alarm_clock(day, on_vacation):
    """L"""
    if on_vacation == False:
        if day == 0 or day == 6:
            return "10:00"
        else:
            return "7:00"
    else:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
        
print(alarm_clock(1, False))
print(alarm_clock(0, True))
