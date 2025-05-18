import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from long_numbers import LongNumber, power


class LongNumberWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.base_input = QLineEdit()
        self.base_input.setPlaceholderText("Введите основание")
        layout.addWidget(self.base_input)

        self.exponent_input = QLineEdit()
        self.exponent_input.setPlaceholderText("Введите показатель степени")
        layout.addWidget(self.exponent_input)

        self.calculate_button = QPushButton("Возвести в степень")
        self.calculate_button.clicked.connect(self.calculate_power)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат: ")
        layout.addWidget(self.result_label)

    def calculate_power(self):
        try:
            base = LongNumber(self.base_input.text())
            exponent = LongNumber(self.exponent_input.text())
            result = power(base, exponent)
            self.result_label.setText(f"Результат: {result}")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LongNumberWindow()
    window.show()
    sys.exit(app.exec())
