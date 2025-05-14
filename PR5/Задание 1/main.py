import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit
)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PR5|Задание 1")
        self.setGeometry(100, 100, 600, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Введите количество элементов массива:")
        self.layout.addWidget(self.label)

        self.n_input = QLineEdit()
        self.layout.addWidget(self.n_input)

        self.button = QPushButton("Сгенерировать и обработать массив")
        self.button.clicked.connect(self.process_array)
        self.layout.addWidget(self.button)

        self.result = QLabel("")
        self.result.setWordWrap(True)
        self.layout.addWidget(self.result)

    def process_array(self):
        try:
            n = int(self.n_input.text())
            array = [random.randint(1, 20) for _ in range(n)]
            result_array = array.copy()
            for i in range(len(array) - 1):
                if array[i] % 2 != 0:
                    result_array[i + 1] = 0
            self.result.setText(
                f"Исходный массив:\n{array}\n\nОбработанный массив:\n{result_array}"
            )
        except:
            self.result.setText("Ошибка: введите корректное число элементов.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
