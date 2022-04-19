def print_square(inner_size, border_width):
    for i in range(0, border_width):
        print('o' * (inner_size + 2*border_width))
    for i in range(0, inner_size):
        print_str = (border_width*'o' + inner_size * '+' + border_width * 'o')
        print(print_str)
    for i in range(0, border_width):
        print('o' * (inner_size + 2*border_width))        