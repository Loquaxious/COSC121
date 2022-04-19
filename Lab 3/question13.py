hours = 12
is_cold = True
if hours < 12:
    if not is_cold:
        print("It's not cold")
    else:
        print("It's cold")
    print("It's before noon")
else:
    if is_cold:
        print("It's cold")
    else:
        print("It's not cold")
    print("It's after noon")    