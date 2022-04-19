""" Program to display a persons, formatted title, distance travelled, 
    activity level and health risk 
    Author: Logan Lee
    Date: 11/08/19
""" 


def metres_from_steps(num_steps, step_length):
    """Function that calculates distance travelled based on number of steps"""
    
    distance = (num_steps * step_length)
    
    return float(distance)


def formatted_title(given_name, family_name, weight):
    """function that returns a title of a person"""
    family = family_name.upper()
    given = given_name.title()
    
    title = (('{0}, {1} ({2:.1f} kg)').format(family, given, weight))
    
    return title 


def activity_level_from_steps(num_steps):
    """ Function determining activity level based on number of steps done"""
    if (num_steps == 0):
        state = 'alive?'
    elif (num_steps < 5000):
        state = 'sedentary'
    elif (num_steps < 7500):
        state = 'very low'
    elif (num_steps < 10000):
        state = 'low'
    elif (num_steps < 12500):
        state = 'active'
    else:
        state = 'very active'
    return state


def health_risk(activity_level, is_smoker):
    """Function that checks health risk based of activity level
    and whether person is a smoker"""
    if ((activity_level == 'alive?') or (activity_level == 'sedentary')):
        if (is_smoker == True):
            state = 'extreme'
        else:
            state = 'high'
    elif ((activity_level == 'very low') or (activity_level == 'low')):
        if (is_smoker == True):
            state = 'high'
        else:
            state = 'medium'
    else:
        if (is_smoker == True):
            state = 'medium'
        else:
            state = 'low'
    
    return state




def main():
    """The main function"""
    given_name = input('Given name? ')
    family_name = input('Family name? ')
    weight_str = input('Weight? ')
    weight = float(weight_str)
    step_length_str = input('Step length (in m)? ')
    step_length = float(step_length_str)
    num_steps_str = input('Number of steps? ')
    num_steps = int(num_steps_str)
    is_smoker = input('Do you smoke (y or n)? ')
    
    if (is_smoker == 'y' or is_smoker == 'Y'):
        is_smoker = True
    else:
        is_smoker = False
    
    distance_walked = metres_from_steps(num_steps, step_length)
    activity = activity_level_from_steps(num_steps)
    health = health_risk(activity_level_from_steps(num_steps), is_smoker)
    
    print()
    print('-------------------------')
    print(formatted_title(given_name, family_name, weight))
    print('-------------------------')
    print(('Steps walked: {0} ').format(num_steps))
    print(('Distance walked: {0}').format(distance_walked))
    print(('Activity level: {0}').format(activity))
    print(('Health risk: {0}').format(health))
    print('-------------------------')
    
main() # call to main function to get things going