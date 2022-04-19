cities = ['Auckland', 'Wellington', 'Christchurch', 'Dunedin']
for city in cities:
    print(city)
    
print('------------------------')

words = "This is a SENTENCE".split()
for word in words:
    word1 = word.title()
    word2 = word.lower()
    word3 = word.upper()
    print('{}->{}->{}->{}'.format(word, word1, word2, word3))
# the loop body ends at the end of the indented lines
print() # so this is after the loop finishes
print(words)

print('------------------------')

small_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Three-times table:")
for number in small_numbers:
    print("{0} x 3 = {1}".format(number, 3 * number))

print('------------------------')

text = 'Hello there'
for letter in text:
    print(letter)

print('------------------------')

number = 2
numbers = [0, 1, 2, 3, 4]
for number in numbers:
    print(number)
print(number)