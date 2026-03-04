from PyQt5.QtWidgets import QApplication
from model import MorpionGame, verifgame
from view import MorpionUI, GameModeSelector
from random import randint
# Controller is doing the interactions and the connections
class MorpionController:
    def __init__(self, game: MorpionGame, view: MorpionUI):
        self.game = game
        self.view = view
        self.connect_signals()
        self.update_status()
# connect each case of the grid to a button
     def connect_signals(self):
        for row in range(3):
           for col in range(3):
                self.view.buttons[row][col].clicked.connect(
                   lambda _, r=row, c=col: self.play(r, c)
                )
        self.view.reset_button.clicked.connect(self.reset_game)
# function play check if the case is empty and if the game is over and place a cross or a rond depend on the player number
      def play(self, row, col):
        if self.game.Grid[row][col] == 0 and not self.game.game_over:
            if self.game.player == 1:
                self.view.buttons[row][col].setText("X")
                self.view.buttons[row][col].setStyleSheet("color: red; font-size: 80px;")
            else:
                self.view.buttons[row][col].setText("O")
                self.view.buttons[row][col].setStyleSheet("color: #3498db; font-size: 80px;")
            self.game.Grid[row][col] = self.game.player
# We see if there is a win condition on this round with the function verifgame
            winner = verifgame(self.game.Grid)
            if winner != 0:
                self.view.status_label.setText(f"Player {winner} win!")
                self.game.game_over = True
                return
  # If there is no more empty case on the grid at the end of the turn, it is a draw !
            if all(self.game.Grid[i][j] != 0 for i in range(3) for j in range(3)):
                self.view.status_label.setText("Draw...")
                self.game.game_over = True
                return
    # Change to the other player turn and update_status make sure that the text change too
            self.game.player = 2 if self.game.player == 1 else 1
            self.update_status()
  # reset_game reset all the case to empty and allow to restart 
            def reset_game(self):
                self.game.reset_game()
                for row in self.view.buttons:
                      for button in row:
                         button.setText("")
                self.update_status()
            def update_status(self):
                self.view.status_label.setText(f"Player {self.game.player}")

class GameModeController:
# Connect the view to button 
    def __init__(self):
        self.app = QApplication([])
        self.view = GameModeSelector()
        self.view.start_button.clicked.connect(self.start_game)
        self.view.show()
        self.app.exec_()
  # the function will open the game mode depending on the GameModeSelector
     def start_game(self):
        if self.view.pvp_button.isChecked():
            game = MorpionGame()
            game_view = MorpionUI()
            MorpionController(game, game_view)
            game_view.show()
            self.view.close()
        elif self.view.ia_button.isChecked():
 
             



