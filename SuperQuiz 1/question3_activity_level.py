def activity_level_from_steps(steps):
    """ Function determining activity level based on number of steps done"""
    if (steps == 0):
        state = 'alive?'
    elif (steps < 5000):
        state = 'sedentary'
    elif (steps < 7500):
        state = 'very low'
    elif (steps < 10000):
        state = 'low'
    elif (steps < 12500):
        state = 'active'
    else:
        state = 'very active'
    return state

print(activity_level_from_steps(0))
print(activity_level_from_steps(2454))
print(activity_level_from_steps(21000))
print(activity_level_from_steps(12500))