def print_names2(people):
    """Print a list of people's names, which each person's name
       is itself a list of names (first name, second name etc)
    """
    
    i = 0
    while i < len(people):
        to_print = ""
        name = people[i]
        n = 0
        while n < len(name):
            to_print += name[n] + " "
            n += 1
        print(to_print[:-1])
        i += 1

print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])

print_names2([['Bilbo', 'Baggins'], ['Gollum'], ['Tom', 'Bombadil'], ['Aragorn']])

        