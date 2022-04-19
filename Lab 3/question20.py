def x_at_either_end(string):
    """Boolean function that shows whether a str. starts or ends with 'x'"""
    return string.startswith("x") or string.endswith("x")

print(x_at_either_end("Ping Pong"))
print(x_at_either_end("pax"))
print(x_at_either_end("xposure"))