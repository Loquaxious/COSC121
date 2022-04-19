"""L"""
S1 = input("Enter first input: ")
S2 = input("Enter second input: ")
if len(S1) >= len(S2):
    STR = S1
else:
    STR = S2
print("{} is the longer of {} and {}.".format(STR, S1, S2))