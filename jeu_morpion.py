
"""
Created on Sat Feb 28 15:50:56 2026

@author: ESME
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QVBoxLayout, QLabel
)
from PyQt5.QtCore import Qt


class MorpionUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Morpion")
        self.setFixedSize(300, 350)

        self.buttons = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Label statut
        self.status_label = QLabel("Prêt")
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
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        main_layout.addLayout(grid_layout)

        # Bouton reset
        self.reset_button = QPushButton("Recommencer")
        main_layout.addWidget(self.reset_button)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MorpionUI()
    window.show()

    sys.exit(app.exec_())
