def caught_speeding(speed, is_birthday):
    """L"""
    if is_birthday == False:
        if speed > 60 and speed < 81:
            return 1
        elif speed > 80:
            return 2
        else:
            return 0
    else:
        if speed > 65 and speed < 86:
            return 1
        elif speed > 85:
            return 2
        else:
            return 0

print(caught_speeding(85, True))
print(caught_speeding(60, False))

    