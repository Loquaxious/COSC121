engr101 = {
    'Joanna Rodriguez', 'John Smith',
    'Maria Martinez', 'Sam Cassidy',
    'David Smith'
}
cosc121 = {
    'Sam Cassidy', 'Maria Martinez',
    'David Smith', 'David Chu',
    'Jennifer Johnston'
}

programming_engineers = cosc121 & engr101

for person in sorted(programming_engineers):
    print(person)