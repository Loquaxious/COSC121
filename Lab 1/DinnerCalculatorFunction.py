def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    meal_cost = meal_cost * 1.15
    drinks_cost = (drinks_cost * .7) * 1.15
    ans = (meal_cost + drinks_cost)
    return ans

print(dinner_calculator(10,0)) 
print(dinner_calculator(12, 4))