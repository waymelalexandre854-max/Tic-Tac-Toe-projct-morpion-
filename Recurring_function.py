"""Recurring function"""

"""This function verify if the game is a win or not, it's really importante for the game and the AI"""
def verifgame(List):
    player = 0
    for i in range(3):
        if List[i][0] == List[i][1] == List[i][2] != 0:
            player = List[i][0]
    for i in range(3):
        if List[0][i] == List[1][i] == List[2][i] != 0:
            player = List[0][i]
    if List[0][0] == List[1][1] == List[2][2] != 0:
        player = List[1][1]
    if List[0][2] == List[1][1] == List[2][0] != 0:
        player = List[1][1]
    return player

"""This function is only used for AI and create a Grid."""
def create_new_Grid(Grid):
    retur_grid = [[0,0,0],[0,0,0],[0,0,0]]
    x = 0
    for j in Grid[0]:
        if j == 1:
            retur_grid[0][x] = 1
        elif j == 2:
            retur_grid[0][x] = 2
        x += 1
    x = 0
    for j in Grid[1]:
        if j == 1:
            retur_grid[1][x] = 1
        elif j == 2:
            retur_grid[1][x] = 2
        x += 1
    x = 0
    for j in Grid[2]:
        if j == 1:
            retur_grid[2][x] = 1
        elif j == 2:
            retur_grid[2][x] = 2
        x += 1
    x = 0
    return retur_grid

"""This function is only used by the AI to have a list of possibilities in a tree branch."""
"""The function don't make the whole tree, just some node, and is specialised for tic tac toe game"""
def create_tree(Grid,player):
    Tree = [Grid, []]
    for i in range (9):
        Grid_modif = create_new_Grid(Grid)
        if i == 0 or i == 1 or i == 2:
            if Grid_modif[0][i] == 0:
                Grid_modif[0][i] = player
        if i == 3 or i == 4 or i == 5:
            if Grid_modif[1][i-3] == 0:
                Grid_modif[1][i-3] = player
        if i == 6 or i == 7 or i == 8:
            if Grid_modif[2][i-6] == 0:
                Grid_modif[2][i-6] = player
        Tree[1].append(Grid_modif)
        Grid_modif = [[0,0,0],[0,0,0],[0,0,0]]

    return Tree
