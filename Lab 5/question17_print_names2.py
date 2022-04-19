def print_names2(people):
    """Print a list of people's names, which each person's name
       is itself a list of names (first name, second name etc)
    """
    i = 0
    while i < len(people):
        string = ""
        name = people[i]
        j = 0
        while j < len(name):
            string += name[j] + " "
            j += 1
        print(string[:-1])
        i += 1

print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])
print_names2([['Bilbo', 'Baggins'], ['Gollum'], ['Tom', 'Bombadil'], ['Aragorn']])
