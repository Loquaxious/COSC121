def censor(s):
    """L"""
    if len(s) == 4:
        return "****"
    else:
        return s
print(censor('wxyz'))
print(censor('xyz'))
