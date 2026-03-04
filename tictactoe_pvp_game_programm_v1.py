"""first try for game"""
"""this programm is only for the game on python and doesn't have the interface or any form of player versus AI"""
"""it was the first programm created to give us a look at how we can make the game work"""

def tictactoe():
    from random import randint        #randint is only used to make choose the first player to start
    from Recurring_function import verifgame        #verifgame is a function that verify if there a win, it's in Recurring_function file
    Grid = [[0,0,0],[0,0,0],[0,0,0]]        #this is the starting grid of the game 
    enter = [1,2,3,4,5,6,7,8,9]        #All the possible move that the player can do, the one that will be played will be removed from the list until there is a win or a draw
    x = 0        #the variable of the player move
    player = randint(1,2)        #randomize the first player with randint
    if player == 1:
        print("player 1 start")
    else:
        print("player 2 start")
    good_play = False        #variable that verify that the player don't make a wrong play
    for i in range(9):
        while good_play == False:
            x = int(input("which place do you want to use ?"))        #ask the player move, if the answer is in the list, the game will goes on. Otherwise, it will show an error message then ask again
            if x in enter:        #The player move is in the list, so the game will put the number corresponding to the player in the grid. 1 is player one and 2 is player 2
                if x == 1 or x == 2 or x == 3:
                    Grid[0][x-1] = player
                elif x == 4 or x == 5 or x == 6:
                    Grid[1][x-4] = player
                else:
                    Grid[2][x-7] = player
                enter.remove(x)        #We remove the played point
                good_play = True
                print(Grid[0])        #Show the grid to the player
                print(Grid[1])
                print(Grid[2])
            else:
                print("this place have been used by the other player, please choose another place")
        good_play = False
        if player == 1:        #change between player 1 and 2
            player = 2
        else:
            player = 1
        y = verifgame(Grid)        #verify if there is a win, if true, stop the game and give the winner and a show of the whole game
        if y == 1:
            return "player 1 win", Grid
        if y == 2:
            return "player 2 win", Grid
    return "no player have win this match"

