"""AI easy tictactoe"""
"""AI show nothing, it just take a choice depending on it's difficulty. Easy is mostly random"""

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


"""Python form of the game with Easy AI implemented"""

def tictactoe():
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
    elif PV == 2:
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
                if Type_AI == 1:
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
