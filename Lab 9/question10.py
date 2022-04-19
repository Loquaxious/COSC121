inventory = {'apples': 10, 'bananas': 20}
item = 'apples'

quantity = inventory.get(item, 0)

print("We have {0} crates of {1} in stock.".format(quantity, item))

inventory = {'apples': 10, 'bananas': 20}
item = 'carrots'

quantity = inventory.get(item, 0)

print("We have {0} crates of {1} in stock.".format(quantity, item))