def metres_from_steps(num_steps, step_length):
    """Function that calculates distance travelled based on number of steps"""
    
    distance = (num_steps * step_length)
    
    return float(distance)

print(metres_from_steps(100, 1))
print(metres_from_steps(100, 0.8))
print(metres_from_steps(1, 0.1))