def swap_halves(s):
    """L"""
    length = len(s) / 2
    
    return s[int(length):]+ s[:int(length)]

print(swap_halves('ab'))
print(swap_halves('Batman!'))
print(swap_halves(''))
