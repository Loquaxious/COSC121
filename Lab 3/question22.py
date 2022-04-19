def bmi_risk(bmi, age):
    """Boolean Function to show bmi risk"""
    if bmi < 22 and age < 45:
        return "Low"
    elif bmi < 22 and age >= 45:
        return "Medium"
    if bmi >= 22 and age < 45:
        return "Medium"
    elif bmi >= 22 and age >= 45:
        return "High"
    

print(bmi_risk(21.5, 44)) 
print(bmi_risk(30, 27))
print(bmi_risk(30, 45))
print(bmi_risk(22.0, 44.9))