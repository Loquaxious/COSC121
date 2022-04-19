def bmi_risk(bmi, age):
    """L"""
    if (bmi < 22) and (age < 45):
        return "Low"
    elif (bmi >= 22) and (age >= 45):
        return "High"
    else:
        return "Medium"

print(bmi_risk(21.5, 44))
print(bmi_risk(30, 27))
print(bmi_risk(30, 45))
