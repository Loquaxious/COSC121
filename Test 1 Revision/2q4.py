def x_at_either_end(string):
    """L"""
    if string.startswith("x") or string.endswith("x"):
        return True
    else:
        return False
print(x_at_either_end('Ping Pong'))
print(x_at_either_end('pax'))
