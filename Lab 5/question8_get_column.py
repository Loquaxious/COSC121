def get_column(game, col_num):
    """Returns a given column of the game"""
    col_list = []
    for row in game:
        col_list.append(row[col_num]) 
    return col_list


board = [['O', 'X', 'O'],
         ['X', ' ', ' '],
         ['X', ' ', ' ']]
column1 = get_column(board, 0)
print(column1)

board1 = [['O', 'X', 'O'],
         ['X', ' ', ' '],
         ['X', ' ', ' ']]
column2 = get_column(board1, 2)
print(column2)