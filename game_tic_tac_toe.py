
import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QVBoxLayout, QLabel,
    QMainWindow, QComboBox, QRadioButton, QButtonGroup
)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

def create_new_Grid(Grid):
    retur_grid = [[0,0,0],[0,0,0],[0,0,0]]
    x = 0
    for j in Grid[0]:
        if j == 1:
            retur_grid[0][x] = 1
        elif j == 2:
            retur_grid[0][x] = 2
        x += 1
    x = 0
    for j in Grid[1]:
        if j == 1:
            retur_grid[1][x] = 1
        elif j == 2:
            retur_grid[1][x] = 2
        x += 1
    x = 0
    for j in Grid[2]:
        if j == 1:
            retur_grid[2][x] = 1
        elif j == 2:
            retur_grid[2][x] = 2
        x += 1
    x = 0
    return retur_grid

def create_tree(Grid,player):
    Tree = [Grid, []]
    for i in range (9):
        Grid_modif = create_new_Grid(Grid)
        if i == 0 or i == 1 or i == 2:
            if Grid_modif[0][i] == 0:
                Grid_modif[0][i] = player
        if i == 3 or i == 4 or i == 5:
            if Grid_modif[1][i-3] == 0:
                Grid_modif[1][i-3] = player
        if i == 6 or i == 7 or i == 8:
            if Grid_modif[2][i-6] == 0:
                Grid_modif[2][i-6] = player
        Tree[1].append(Grid_modif)
        Grid_modif = [[0,0,0],[0,0,0],[0,0,0]]

    return Tree

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

def easy_AI(Grid):
    from random import choice
    from random import randint
    
    # List empty positions from 1 to 9
    empty = []
    for i in range(3):
        for j in range(3):
            if Grid[i][j] == 0:
                empty.append(i*3 + j + 1)

    if empty:
        return choice(empty)
    return None

def normal_AI(Grid):
    from random import choice

    play_list = []
    best_value = 0
    result_dico = {}
    Tree = create_tree(Grid, 2)  # AI is player 2

    # Expand tree for possible human responses
    for i in range(9):
        Node = create_tree(Tree[1][i], 1)  # Human is player 1
        Tree[1][i] = Node

    x = 1
    for i in Tree[1]:
        result_dico[x] = 0
        for y in i[1]:
            win = verifgame(y)
            if win == 1:
                result_dico[x] -= 1000
            elif win == 2:
                result_dico[x] += 1000
        win = verifgame(i[0])
        if win == 1:
            result_dico[x] -= 1000
        elif win == 2:
            result_dico[x] += 1000
        if i == Grid:
            del result_dico[x]
        x += 1

    # Select the best moves
    for key, value in result_dico.items():
        if best_value < value:
            best_value = value
    for key, value in result_dico.items():
        if value == best_value:
            play_list.append(key)

    return choice(play_list)

def difficult_AI(Grid):
    from random import choice

    def available_moves(g):
        return [(r, c) for r in range(3) for c in range(3) if g[r][c] == 0]

    def minmax(grid, player, depth=0):
        winner = verifgame(grid)
        if winner != 0:
            return (1000 - depth) if winner == 2 else (-1000 + depth)

        moves = available_moves(grid)
        if moves == []:
            return 0

        if player == 2:
            best = -1000000000000000000000000000000
            for r, c in moves:
                new_grid = create_new_Grid(grid)
                new_grid[r][c] = player
                score = minmax(new_grid, 1, depth + 1)
                if score > best:
                    best = score
            return best
        else:
            best = 1000000000000000000000000000000
            for r, c in moves:
                new_grid = create_new_Grid(grid)
                new_grid[r][c] = player
                score = minmax(new_grid, 2, depth + 1)
                if score < best:
                    best = score
            return best

    best_value = -1000000000000000000000000000000
    play_list = []

    for i in range(9):
        if i in [0, 1, 2]:
            r = 0; c = i
        elif i in [3, 4, 5]:
            r = 1; c = i - 3
        elif i in [6, 7, 8]:
            r = 2; c = i - 6
        if Grid[r][c] != 0:
            continue
        trial = create_new_Grid(Grid)
        trial[r][c] = 2
        score = minmax(trial, 1, 1)
        if score > best_value:
            best_value = score
            play_list = [i + 1]
        elif score == best_value:
            play_list.append(i + 1)

    return choice(play_list)

class MorpionUI(QWidget):
    def __init__(self, ai_mode=False, difficulty=None):
        super().__init__()
        self.ai_mode = ai_mode
        self.difficulty = difficulty

        self.setWindowTitle("Morpion")
        self.setFixedSize(400, 600)
        self.setObjectName("mainWindow")
        self.setStyleSheet("""
        #mainWindow {
            background-color: #1ABC9C;
        }
        """)

        self.buttons = []
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1, 2)
        self.game_over = False
        

        # If AI mode and AI starts first, play immediately
        if self.ai_mode and self.player == 2:
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(200, self.ai_play)
            
        self.score_player1 = 0
        self.score_player2 = 0
        
        self.init_ui()
        
    def init_ui(self):


        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Status label
        self.status_label = QLabel(f"Player {self.player} starts")
        self.status_label.setFont(QFont("Montserrat", 15, QFont.Bold))
        self.status_label.setStyleSheet("color: white;")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)
        
        self.score_label = QLabel(f"Score - Player 1: {self.score_player1} | Player 2: {self.score_player2}")
        self.score_label.setFont(QFont("Montserrat", 14, QFont.Bold))
        self.score_label.setStyleSheet("color: white;")
        self.score_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.score_label)
        
        self.reset_button = QPushButton("Restart")
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border-radius: 15px;
                padding: 10px;
            }
        """)
        self.reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(self.reset_button)
        
        self.menu_button = QPushButton("Menu")
        self.menu_button.setStyleSheet("""
            QPushButton {
               background-color: #34495e;
               color: white;
               border-radius: 15px;
               padding: 10px;
            }
         """)
        self.menu_button.clicked.connect(self.return_to_menu)
        main_layout.addWidget(self.menu_button)
        
        # Grid 3x3
        grid_layout = QGridLayout()
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(120, 120)
                button.setStyleSheet("font-size: 36px;")
                button.clicked.connect(lambda _, r=row, c=col: self.play(r, c))
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        main_layout.addLayout(grid_layout)
        


    def play(self, row, col):
        if self.Grid[row][col] != 0 or self.game_over:
            return

        if self.player == 1:
            self.buttons[row][col].setText("X")
            self.buttons[row][col].setStyleSheet("color: #2c3e50; font-size: 80px;")
        else:
            self.buttons[row][col].setText("O")
            self.buttons[row][col].setStyleSheet("color: #1ABC9C; font-size: 80px;")
        
        self.Grid[row][col] = self.player

        winner = verifgame(self.Grid)
        if winner != 0:
            self.status_label.setText(f"Player {winner} wins !!")
            self.game_over = True
    # Mise à jour du score
            if winner == 1:
              self.score_player1 += 1
            else:
              self.score_player2 += 1
            self.score_label.setText(f"Score - Player 1: {self.score_player1} | Player 2: {self.score_player2}")
            return

        if all(self.Grid[i][j] != 0 for i in range(3) for j in range(3)):
            self.status_label.setText("Draw...")
            self.game_over = True
            return

        # Switch player
        self.player = 2 if self.player == 1 else 1
        self.status_label.setText(f"Player {self.player}")

        if self.ai_mode and self.player == 2 and not self.game_over:
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(200, self.ai_play)

    def ai_play(self):
        if self.game_over:
            return

        Ai = None
        if self.difficulty == "Facile":
            Ai = easy_AI(self.Grid)
        elif self.difficulty == "Moyen":
            Ai = normal_AI(self.Grid)
        elif self.difficulty == "Difficile":
            Ai = difficult_AI(self.Grid)
        else:  # Moyenne difficulty fallback
            Ai = easy_AI(self.Grid)

        if Ai is not None:
            if Ai in [1, 2, 3]:
                row, col = 0, Ai - 1
            elif Ai in [4, 5, 6]:
                row, col = 1, Ai - 4
            else:
                row, col = 2, Ai - 7

            self.play(row, col)  # Let play() handle switching

    # reset all buttons to 0 and game_over to False
    def reset_game(self):
        self.Grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = randint(1,2)
        self.game_over = False
        self.status_label.setText(f"Player {self.player} start")

        for row in self.buttons:
            for button in row:
                button.setText("")
                
    def return_to_menu(self):
       self.close()  # Ferme la fenêtre actuelle
       self.menu_window = GameModeSelector()  # Crée une nouvelle fenêtre menu
       self.menu_window.show()

class GameModeSelector(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.setWindowTitle("Chose Game Mode")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #2c3e50;")  # fond sombre

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Label titre
        self.mode_label = QLabel("Choose game mode :")
        self.mode_label.setFont(QFont("Montserrat", 16, QFont.Bold))
        self.mode_label.setStyleSheet("color: white;")
        self.mode_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mode_label)

        # Boutons radio pour PVP et IA
        radio_layout = QVBoxLayout()
        radio_layout.setAlignment(Qt.AlignCenter)
        self.pvp_button = QRadioButton("PVP (Player vs Player)")
        self.ia_button = QRadioButton("AI (Player vs AI)")
        self.pvp_button.setFont(QFont("Montserrat", 14))
        self.pvp_button.setStyleSheet("color: white;")
        self.ia_button.setFont(QFont("Montserrat", 14))
        self.ia_button.setStyleSheet("color: white;")

        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.pvp_button)
        self.mode_group.addButton(self.ia_button)
        layout.addWidget(self.pvp_button)
        layout.addWidget(self.ia_button)

        # Sélection de la difficulté pour l'IA
        self.difficulty_label = QLabel("Choose AI difficulty :")
        self.difficulty_label.setFont(QFont("Montserrat", 14))
        self.difficulty_label.setStyleSheet("color: white;")
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.setFont(QFont("Montserrat", 16))
        self.difficulty_combo.addItems(["Facile", "Moyen", "Difficile"])
        self.difficulty_combo.setStyleSheet("color: white")
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_combo)

        # Au départ, la difficulté est cachée
        self.difficulty_label.hide()
        self.difficulty_combo.hide()
        self.ia_button.toggled.connect(self.toggle_difficulty)

        # Bouton Start
        self.start_button = QPushButton("Start Game")
        self.start_button.setFont(QFont("Montserrat", 10, QFont.Bold))
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2c3e50;
                border-radius: 15px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_game)

    # Affiche ou cache la difficulté selon le mode choisi
    def toggle_difficulty(self, checked):
        if checked:
            self.difficulty_label.show()
            self.difficulty_combo.show()
        else:
            self.difficulty_label.hide()
            self.difficulty_combo.hide()

    # Lancement du jeu
    def start_game(self):
        if self.pvp_button.isChecked():
            self.morpion_window = MorpionUI()
            self.morpion_window.show()
            self.close()
        elif self.ia_button.isChecked():
            difficulty = self.difficulty_combo.currentText()
            self.morpion_window = MorpionUI(ai_mode=True, difficulty=difficulty)
            self.morpion_window.show()
            self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameModeSelector()
    window.show()
    sys.exit(app.exec_())
