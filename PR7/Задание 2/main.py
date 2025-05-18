import sys
import random
from collections import Counter
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QHBoxLayout, QMessageBox
)


class RemoveCommonDuplicates(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление общих повторяющихся элементов")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("Размер массива A")
        self.input_b = QLineEdit()
        self.input_b.setPlaceholderText("Размер массива B")
        input_layout.addWidget(self.input_a)
        input_layout.addWidget(self.input_b)
        layout.addLayout(input_layout)

        self.button = QPushButton("Сгенерировать и обработать")
        self.button.clicked.connect(self.process)
        layout.addWidget(self.button)

        self.list_a = QListWidget()
        layout.addWidget(QLabel("Массив A (исходный):"))
        layout.addWidget(self.list_a)

        self.list_b = QListWidget()
        layout.addWidget(QLabel("Массив B:"))
        layout.addWidget(self.list_b)

        self.list_result = QListWidget()
        layout.addWidget(QLabel("Массив A (после удаления):"))
        layout.addWidget(self.list_result)

        self.setLayout(layout)

    def process(self):
        try:
            size_a = int(self.input_a.text())
            size_b = int(self.input_b.text())
            if size_a <= 0 or size_b <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите положительные числа для размеров массивов.")
            return

        A = [random.randint(1, 9) for _ in range(size_a)]
        B = [random.randint(1, 9) for _ in range(size_b)]

        self.list_a.clear()
        self.list_a.addItems(map(str, A))

        self.list_b.clear()
        self.list_b.addItems(map(str, B))

        count_a = Counter(A)
        count_b = Counter(B)

        result = [x for x in A if not (count_a[x] >= 2 and count_b[x] >= 2)]

        self.list_result.clear()
        self.list_result.addItems(map(str, result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RemoveCommonDuplicates()
    window.show()
    sys.exit(app.exec())
