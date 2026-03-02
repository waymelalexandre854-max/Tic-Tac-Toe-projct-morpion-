import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QVBoxLayout, QLabel,
    QMainWindow, QComboBox, QRadioButton, QButtonGroup
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

class GameModeSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Mode Selection")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.mode_label = QLabel("Choose Game Mode:")
        layout.addWidget(self.mode_label)

        self.pvp_button = QRadioButton("PVP (Player vs Player)")
        self.ia_button = QRadioButton("IA (Player vs AI)")
        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.pvp_button)
        self.mode_group.addButton(self.ia_button)

        layout.addWidget(self.pvp_button)
        layout.addWidget(self.ia_button)

        self.difficulty_label = QLabel("Choose AI Difficulty:")
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Medium", "Hard"])
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_combo)

        self.difficulty_label.hide()
        self.difficulty_combo.hide()

        self.ia_button.toggled.connect(self.toggle_difficulty)

        self.start_button = QPushButton("Start Game")
        layout.addWidget(self.start_button)

        # Connexion du bouton Start
        self.start_button.clicked.connect(self.start_game)

    def toggle_difficulty(self, checked):
        if checked:
            self.difficulty_label.show()
            self.difficulty_combo.show()
        else:
            self.difficulty_label.hide()
            self.difficulty_combo.hide()

    def start_game(self):
        # Si mode PVP sélectionné
        if self.pvp_button.isChecked():
            self.morpion_window = MorpionUI()
            self.morpion_window.show()
            self.close()  # ferme la fenêtre de sélection

        # Si IA sélectionné → ne rien faire pour l’instant
        elif self.ia_button.isChecked():
            print("Mode IA non implémenté pour le moment.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameModeSelector()
    window.show()
    sys.exit(app.exec_())


