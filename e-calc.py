import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLineEdit, QLabel, QGridLayout)
from PyQt5.QtCore import Qt
import random

class EvilCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evil Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Transparent UI
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.display)

        # Buttons (using QGridLayout for Windows-like layout)
        button_grid = QGridLayout()
        buttons = [
            '%', 'CE', 'C', '⌫',
            '1/x', 'x²', '√x', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        positions = [(i, j) for i in range(6) for j in range(4)]
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            button.setStyleSheet("QPushButton { font-size: 18px; padding: 15px; background-color: rgba(255, 255, 255, 0.5); border: none; }")  # Bigger and transparent
            button_grid.addWidget(button, *position)

        self.layout.addLayout(button_grid)

        self.input_expression = ""

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == '=':
            self.calculate_result()
        elif button_text == 'C':
            self.clear_display()
        else:
            self.input_expression += button_text
            self.display.setText(self.input_expression)

    def calculate_result(self):
        try:
            # Introduce evil randomness here!
            if random.random() < 0.3:  # 30% chance of error
                result = self.evil_calculate(self.input_expression)
            else:
                result = str(eval(self.input_expression))

            self.input_expression = result
            self.display.setText(result)
        except Exception as e:
            self.display.setText("Error")

    def evil_calculate(self, expression):
        # Implement your evil logic here!
        # Here are a few examples:

        # 1. Off by one:
        if "+" in expression:
            return str(eval(expression) + 1)
        
        # 2. Swap operators:
        if "-" in expression:
            expression = expression.replace("-", "+")
            return str(eval(expression))

        # 3. Random decimal shift:
        if "." in expression:
            result = eval(expression)
            result *= 10 ** random.choice([-1, 1])  # Shift decimal left or right
            return str(result)

        # Add more evil calculations as you like!
        return str(eval(expression))  # Default to correct if no evil applied


    def clear_display(self):
        self.input_expression = ""
        self.display.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = EvilCalculator()
    calculator.show()
    sys.exit(app.exec_())