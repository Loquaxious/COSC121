items = [0.0, 3.2, 7.6, 5.9, 1.4]
for (i, num) in enumerate(items):
    items[i] = round(num)
print(items)

print("-------------------------")

items = ['man', 'woman', 'girl', 'boy']
for (i, person) in enumerate(items):
    items[i] = "super" + person
print(items)

print("-------------------------")

names = ['John', 'Pete', 'Mary', 'Jane']
for name in names:
    names.remove(name)
print(names)