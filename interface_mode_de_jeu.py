import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QComboBox, QRadioButton, QButtonGroup
)

class GameModeSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Mode Selection")
        self.setGeometry(100, 100, 300, 200)

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # modes de jeu
        self.mode_label = QLabel("Choose Game Mode:")
        layout.addWidget(self.mode_label)

        self.pvp_button = QRadioButton("PVP (Player vs Player)")
        self.ia_button = QRadioButton("IA (Player vs AI)")
        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.pvp_button)
        self.mode_group.addButton(self.ia_button)
        layout.addWidget(self.pvp_button)
        layout.addWidget(self.ia_button)

        # AI difficulty selection (only visible if AI is selected)
        self.difficulty_label = QLabel("Choose AI Difficulty:")
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Medium", "Hard"])
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_combo)
        self.difficulty_label.hide()
        self.difficulty_combo.hide()

        self.ia_button.toggled.connect(self.toggle_difficulty)

        # Start button
        self.start_button = QPushButton("Start Game")
        layout.addWidget(self.start_button)

    def toggle_difficulty(self, checked):
        if checked:
            self.difficulty_label.show()
            self.difficulty_combo.show()
        else:
            self.difficulty_label.hide()
            self.difficulty_combo.hide()


app = QApplication(sys.argv)
window = GameModeSelector()
window.show()
sys.exit(app.exec_())