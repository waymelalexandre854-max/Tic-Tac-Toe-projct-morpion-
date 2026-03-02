import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QVBoxLayout, QLabel
)
from PyQt5.QtCore import Qt


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


class MorpionUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Morpion")
        self.setFixedSize(300, 350)

        self.buttons = []
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1,2)
        self.game_over = False

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

    
        self.status_label = QLabel(f"Joueur {self.player} commence")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Grille 3x3
        grid_layout = QGridLayout()

        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda _, r=row, c=col: self.play(r, c))
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        main_layout.addLayout(grid_layout)

        # Bouton reset
        self.reset_button = QPushButton("Recommencer")
        self.reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(self.reset_button)

        self.setLayout(main_layout)

    def play(self, row, col):
        if self.Grid[row][col] == 0 and not self.game_over:

            # Mettre symbole
            if self.player == 1:
                self.buttons[row][col].setText("X")
            else:
                self.buttons[row][col].setText("O")

            self.Grid[row][col] = self.player

            # Vérifier victoire
            winner = verifgame(self.Grid)
            if winner != 0:
                self.status_label.setText(f"Joueur {winner} a gagné !")
                self.game_over = True
                return

            # Vérifier match nul
            if all(self.Grid[i][j] != 0 for i in range(3) for j in range(3)):
                self.status_label.setText("Match nul !")
                self.game_over = True
                return

            # Changer joueur
            self.player = 2 if self.player == 1 else 1
            self.status_label.setText(f"Tour du joueur {self.player}")

    def reset_game(self):
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1,2)
        self.game_over = False
        self.status_label.setText(f"Joueur {self.player} commence")

        for row in self.buttons:
            for button in row:
                button.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MorpionUI()
    window.show()
    sys.exit(app.exec_())
