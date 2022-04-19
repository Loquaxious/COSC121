def diagonals(game):
    """returns the twoo diagonals of a game"""
    diagonal1 = []
    diagonal2 = []
    i = 2
    j = 0 
    for row in game:
        diagonal1.append(row[j])
        diagonal2.append(row[i])
        i -= 1
        j += 1
    tuple1 = (diagonal1, diagonal2)
    return(tuple1)

board = [['X', 'O', 'O'],
         ['O', 'X', 'O'],
         [' ', 'X', ' ']]
diags = diagonals(board)
print(diags)