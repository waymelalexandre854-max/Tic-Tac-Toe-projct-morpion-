"""AI easy tictactoe"""
"""This programm is the easy form of the AI for the tic tac toe game. It mostly play hasardly, only looking at all the possibility of his move."""
"""it don't use minmax because we were trying to see other way to do programm other than minmax"""

def easy_AI(Grid):
    from random import choice        #choice from random give us a possibility from all possible one, resulting to a hazardous play
    from Recurring_function import verifgame, create_tree
    play_list = []        #This is the list of possibilities that the AI have at the end, one is selected at the end
    best_value = 0        #The way to know what is the best way to win, put at 0 because the AI can't know player possibilities
    result_dico = {}        #Where we input all the result to know what is the move that have the best value
    Tree = []        #The tree of possibilities
    win = 0        #a variable to say if the move is a win or a lose
    x = 1        #a variable to change from one node to another
    Tree = create_tree(Grid,2)        #create the tree of possibilities that the programm will study
    for i in Tree[1]:
        win = verifgame(i)        #the value of win give point to the resepctive play
        if win == 0:
            result_dico[x] = 0
        elif win == 1:
            result_dico[x] = -1000
        else:
            result_dico[x] = 1000
        if i == Grid:        #if the play look like the previouse one, it's removed from the dico
            del result_dico[x]
        x += 1
    for key,value in result_dico.items():        #look for the best value in the dico
        if best_value < value:
            best_value = value
    for key,value in result_dico.items():        #create the list of possibilitties
        if value == best_value:
            play_list.append(key)

    return choice(play_list)        #send back a number which is where the AI is playing


"""Python form of the game with Easy AI implemented"""

def tictactoe():        #the start is mostly like tictactoe_pvp_game_programm_v1, only little modification to make using AI possible
    from random import randint
    from Easy_AI_tictactoe import easy_AI
    from Recurring_function import verifgame
    Ai = 0
    PV = int(input("Enter 1 for play against another player and 2 for play against a AI "))
    Type_AI = int(input("What level of AI ? (1 = easy) "))
    Grid = [[0,0,0],[0,0,0],[0,0,0]]
    enter = [1,2,3,4,5,6,7,8,9]
    x = 0
    player = randint(1,2)
    if player == 1:
        print("player 1 start")
    else:
        print("player 2 start")
    good_play = False
    if PV == 1:
        for i in range(9):
            while good_play == False:
                x = int(input("which place do you want to use ? "))
                if x in enter:
                    if x == 1 or x == 2 or x == 3:
                        Grid[0][x-1] = player
                    elif x == 4 or x == 5 or x == 6:
                        Grid[1][x-4] = player
                    else:
                        Grid[2][x-7] = player
                    enter.remove(x)
                    good_play = True
                    print(Grid[0])
                    print(Grid[1])
                    print(Grid[2])
                else:
                    print("this place have been used by the other player, please choose another place")
            good_play = False
            if player == 1:
                player = 2
            else:
                player = 1
            y = verifgame(Grid)
            if y == 1:
                return "player 1 win", Grid
            if y == 2:
                return "player 2 win", Grid
    elif PV == 2:        #this is where the player versus AI programm start, the player move is like the on in PVP, but AI use the easy_AI function
        for i in range(9):
            if player == 1:
                while good_play == False:
                    x = int(input("which place do you want to use ? "))
                    if x in enter:
                        if x == 1 or x == 2 or x == 3:
                            Grid[0][x-1] = player
                        elif x == 4 or x == 5 or x == 6:
                            Grid[1][x-4] = player
                        else:
                            Grid[2][x-7] = player
                        enter.remove(x)
                        good_play = True
                    else:
                        print("this place have been used by the other player, please choose another place")
                good_play = False
                player = 2
            else:
                if Type_AI == 1:        #with more AI, the Type_AI can be the way to know the difference between each AI
                    Ai = easy_AI(Grid)
                    if Ai == 1 or Ai == 2 or Ai == 3:
                        Grid[0][Ai-1] = player
                    elif Ai == 4 or Ai == 5 or Ai == 6:
                        Grid[1][Ai-4] = player
                    else:
                        Grid[2][Ai-7] = player
                    enter.remove(Ai)
                    player = 1
            print(Grid[0])
            print(Grid[1])
            print(Grid[2])
            y = verifgame(Grid)
            if y == 1:
                return "player 1 win", Grid
            if y == 2:
                return "player 2 win", Grid
    return "no player have win this match"
print(tictactoe())

