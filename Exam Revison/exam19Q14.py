def program():
    
    prompt = 'Enter a line: '
    string = input(prompt)
    
    while string.startswith('GO') == False:
        string = input(prompt)
    
    count = -1
    while string.startswith('STOP') == False:
        prompt = 'Next: '
        string = input(prompt)
        count += 1
    print('Counted {} lines'.format(count))

program()