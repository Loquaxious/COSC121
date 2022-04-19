"""L"""

def get_file():
    """L"""
    
    filename = input()
    infile = open(filename)
    lines = infile.read().splitlines()
    infile.close()
    
    return lines


def get_indexes(lines):
    """L"""
    
    s = lines.index('<begin step data>')
    e = lines.index('<end step data>', s + 1)
    
    return s, e

def process_data(lines, start, end):
    """L"""
    
    total_steps = 0
    for line in lines[start + 1 : end]:
        steps = line.strip().split(',')
        total_steps += get_sum(steps)
    
    return total_steps

def get_sum(steps):
    """L"""
    
    sums = 0
    for step_string in steps:
        sums += int(step_string)
    
    return sums

def print_total_steps(total_steps):
    """L"""
    
    print("Total steps:", total_steps)


def main():
    """L"""
    
    data = get_file()
    start, end = get_indexes(data)
    total_steps = process_data(data, start, end)
    print_total_steps(total_steps)

main()
    