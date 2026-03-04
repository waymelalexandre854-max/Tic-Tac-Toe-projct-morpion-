from PyQt5.QtWidgets import (
    QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel,
    QMainWindow, QComboBox, QRadioButton, QButtonGroup
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
# Define the main window interface
class MorpionUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.setFixedSize(400, 600)
        self.setObjectName("mainWindow")
        self.setStyleSheet("""
        #mainWindow {
            background-color: #2c3e50;
        }
        """)
       self.buttons = []
       self.init_ui()
# Function for the text and the grid
       def init_ui(self):
        main_layout = QVBoxLayout()

        self.status_label = QLabel("Player X start")
        self.status_label.setFont(QFont("Montserrat", 15, QFont.Bold))
        self.status_label.setStyleSheet("color: white;")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)
        grid_layout = QGridLayout()
# Grid 3x3 for loop to have 9 case
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(120, 120)
                button.setStyleSheet("font-size: 36px;")
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        main_layout.addLayout(grid_layout)
        self.reset_button = QPushButton("Recommencer")
        main_layout.addWidget(self.reset_button)

        self.setLayout(main_layout)
# Class for the game selector
class GameModeSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Mode Selector")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #2c3e50;")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
# Text on the window
        self.mode_label = QLabel("Chose the game mode :")
        self.mode_label.setFont(QFont("Montserrat", 16, QFont.Bold))
        self.mode_label.setStyleSheet("color: white;")
        self.mode_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mode_label)
# The buttons for the Game modes
        self.pvp_button = QRadioButton("PVP (Joueur vs Joueur)")
        self.ia_button = QRadioButton("IA (Joueur vs IA)")
        self.pvp_button.setFont(QFont("Montserrat", 14))
        self.pvp_button.setStyleSheet("color: white;")
        self.ia_button.setFont(QFont("Montserrat", 14))
        self.ia_button.setStyleSheet("color: white;")
# Group and display the button on the window
        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.pvp_button)
        self.mode_group.addButton(self.ia_button)
        layout.addWidget(self.pvp_button)
        layout.addWidget(self.ia_button)
# The difficulty of the AI 
        self.difficulty_label = QLabel("Choisissez la difficulté de l'IA :")
        self.difficulty_label.setFont(QFont("Montserrat", 14))
        self.difficulty_label.setStyleSheet("color: white;")
# Combo Box to select difficulty
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.setFont(QFont("Montserrat", 16))
        self.difficulty_combo.addItems(["Facile", "Moyen", "Difficile"])
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_combo)
# I hide the difficulty label while the AI button hasn't been checked
        self.difficulty_label.hide()
        self.difficulty_combo.hide()
        self.ia_button.toggled.connect(self.toggle_difficulty)
# Button to start the game once one game mode is selected
        self.start_button = QPushButton("Démarrer le jeu")
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
# Function to display difficulty combo button if AI is checked
    def toggle_difficulty(self, checked):
        if checked:
            self.difficulty_label.show()
            self.difficulty_combo.show()
        else:
            self.difficulty_label.hide()
            self.difficulty_combo.hide()


