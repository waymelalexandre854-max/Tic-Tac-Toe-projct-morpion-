"""AI easy tictactoe"""

def easy_AI(Grid):
    from random import choice
    from Recurring_function import verifgame, create_tree
    play_list = []
    best_value = 0
    result_dico = {}
    Tree = []
    win = 0
    x = 1
    Tree = create_tree(Grid,2)
    for i in Tree[1]:
        win = verifgame(i)
        if win == 0:
            result_dico[x] = 0
        elif win == 1:
            result_dico[x] = -1000
        else:
            result_dico[x] = 1000
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