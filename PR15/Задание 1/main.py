import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, \
    QLabel
from fractions import Fraction, multiply_fractions


class FractionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите дроби через пробел (например: 1/2 3/4)")
        layout.addWidget(self.input_field)

        self.calculate_button = QPushButton("Вычислить произведение")
        self.calculate_button.clicked.connect(self.calculate_product)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат: ")
        layout.addWidget(self.result_label)

    def calculate_product(self):
        try:
            fractions_str = self.input_field.text().strip().split()
            fractions = []
            for frac in fractions_str:
                num, den = map(int, frac.split('/'))
                fractions.append(Fraction(num, den))

            result = multiply_fractions(fractions)
            self.result_label.setText(f"Результат: {result}")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FractionWindow()
    window.show()
    sys.exit(app.exec())
