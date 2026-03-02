"first try for game"

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

def tictactoe():
    from random import randint
    Grid = [[0,0,0],[0,0,0],[0,0,0]]
    enter = [1,2,3,4,5,6,7,8,9]
    x = 0
    player = randint(1,2)
    if player == 1:
        print("player 1 start")
    else:
        print("player 2 start")
    good_play = False
    for i in range(9):
        while good_play == False:
            x = int(input("which place do you want to use ?"))
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
    return "no player have win this match"
print(tictactoe())
