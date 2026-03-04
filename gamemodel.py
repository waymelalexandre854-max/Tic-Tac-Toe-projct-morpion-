from random import randint
# Function that verify if the game is win or not by using for loop
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

# Class for reseting the game
class MorpionGame:
    def __init__(self):
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1,2)
        self.game_over = False

    def reset_game(self):
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1,2)
        self.game_over = False
