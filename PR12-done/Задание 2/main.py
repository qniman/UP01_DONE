import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget


def calculate_b_array(a):
    b = []
    for i in range(0, len(a) - 1, 2):
        average = (a[i] + a[i + 1]) / 2
        b.append(average)
    return b


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задача с массивами A и B")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Введите массив A (через пробел):")
        layout.addWidget(self.label)

        self.input_a = QLineEdit(self)
        self.input_a.setPlaceholderText("Пример: 1 3 5 -2 0 4 0 3")
        layout.addWidget(self.input_a)

        self.btn_calculate = QPushButton("Рассчитать массив B")
        self.btn_calculate.clicked.connect(self.calculate_b)
        layout.addWidget(self.btn_calculate)

        self.result_list = QListWidget(self)
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    def calculate_b(self):
        try:
            input_text = self.input_a.text()
            a = list(map(int, input_text.split()))

            if len(a) % 2 != 0:
                self.result_list.addItem("Массив A должен содержать четное количество элементов!")
                return

            b = calculate_b_array(a)

            self.result_list.clear()
            for value in b:
                self.result_list.addItem(f"{value}")
        except ValueError:
            self.result_list.clear()
            self.result_list.addItem("Ошибка! Введите правильные целые числа.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
