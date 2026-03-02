"""AI normal tictactoe"""
"""This AI should know how to defend itself from player gameplay but don't know more than that"""


def normal_AI(Grid):
    from random import choice
    from Recurring_function import verifgame, create_tree
    play_list = []
    best_value = 0
    result_dico = {}
    Tree = []
    Branch = []
    win = 0
    x = 1
    Tree = create_tree(Grid,2)
    for i in range(9):
        Branch = create_tree(Tree[1][i],1)
        Tree[1][i]= Branch
    for i in Tree[1]:
        result_dico[x] = 0
        for y in i[1]:
            win = verifgame(y)
            if win == 0:
                result_dico[x] += 0
            elif win == 1:
                result_dico[x] -= 1000
            else:
                result_dico[x] += 1000
        win = verifgame(i[0])
        if win == 0:
            result_dico[x] += 0
        elif win == 1:
            result_dico[x] -= 1000
        else:
            result_dico[x] += 1000
        if i == Grid:
            del result_dico[x]
        x += 1
    for key,value in result_dico.items():
        if best_value < value:
            best_value = value
    for key,value in result_dico.items():
        if value == best_value:
            play_list.append(key)
    return choice(play_list)
