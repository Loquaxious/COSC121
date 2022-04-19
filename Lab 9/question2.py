fake101 = {
    'Joanna Rodriguez', 'John Smith',
    'Sam Cassidy'
}
joke112 = {
    'Sam Cassidy', 'Maria Martinez',
    'David Smith'
}
haha102 = {
    'Joanna Rodriguez', 'David Chu', 
    'Sam Cassidy'
}
eligible_students = fake101 | joke112 | haha102

for person in sorted(eligible_students):
    print(person)