"""AI normal tictactoe"""
"""This AI know how to defend itself from player gameplay but don't know more than that, being able only to see the his move and the player move."""
"""it don't use minmax because we were trying to see other way to do programm other than minmax and testing limit of less efficienty programm"""


def normal_AI(Grid):
    from random import choice        #choice from random give us a possibility from all possible one, resulting to a hazardous play
    from Recurring_function import verifgame, create_tree
    play_list = []        #This is the list of possibilities that the AI have at the end, one is selected at the end
    best_value = 0        #The way to know what is the best way to win, put at 0 because the AI can't know player possibilities
    result_dico = {}        #Where we input all the result to know what is the move that have the best value
    Tree = []        #The tree of possibilities
    Node = []        #Node of the tree after the main part are done
    win = 0        #a variable to say if the move is a win or a lose
    x = 1        #a variable to change from one node to another
    Tree = create_tree(Grid,2)        #create the tree of possibilities that the programm will study
    for i in range(9):
        Node = create_tree(Tree[1][i],1)        #create the node of possibilities of the potential player move
        Tree[1][i]= Node
    for i in Tree[1]:        #the value of win give point to the resepctive play
        result_dico[x] = 0
        for y in i[1]:        #verify first for the player move then the AI actual move
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
        if i == Grid:        #if the play look like the previouse one, it's removed from the dico
            del result_dico[x]
        x += 1
    for key,value in result_dico.items():       #look for the best value in the dico
        if best_value < value:
            best_value = value
    for key,value in result_dico.items():        #create the list of possibilitties
        if value == best_value:
            play_list.append(key)

    return choice(play_list)        #send back a number which is where the AI is playing

