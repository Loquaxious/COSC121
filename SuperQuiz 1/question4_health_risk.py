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

print(health_risk('low', True)) 
print(health_risk('active', False)) 
print(health_risk('sedentary', True)) 