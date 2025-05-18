import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)


class IncreaseLastLongestRun(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 500, 350)

        layout = QVBoxLayout()

        self.input_n = QLineEdit()
        self.input_n.setPlaceholderText("Введите размер массива N")
        layout.addWidget(self.input_n)

        self.btn_generate = QPushButton("Сгенерировать массив и преобразовать")
        self.btn_generate.clicked.connect(self.process_array)
        layout.addWidget(self.btn_generate)

        self.list_original = QListWidget()
        layout.addWidget(QLabel("Исходный массив:"))
        layout.addWidget(self.list_original)

        self.list_result = QListWidget()
        layout.addWidget(QLabel("Преобразованный массив:"))
        layout.addWidget(self.list_result)

        self.setLayout(layout)

    def process_array(self):
        try:
            n = int(self.input_n.text())
            if n <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите корректное положительное число.")
            return

        arr = [random.randint(1, 10) for _ in range(n)]
        self.list_original.clear()
        self.list_original.addItems(map(str, arr))

        max_len = 1
        current_len = 1
        runs = []

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                current_len += 1
            else:
                runs.append((i - current_len, current_len))
                if current_len > max_len:
                    max_len = current_len
                current_len = 1
        runs.append((n - current_len, current_len))
        if current_len > max_len:
            max_len = current_len

        last_max_run = None
        for start, length in reversed(runs):
            if length == max_len:
                last_max_run = (start, length)
                break

        if last_max_run is not None:
            start, length = last_max_run
            for i in range(start, start + length):
                arr[i] += 1

        self.list_result.clear()
        self.list_result.addItems(map(str, arr))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IncreaseLastLongestRun()
    window.show()
    sys.exit(app.exec())
