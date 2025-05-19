import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton
)
from PySide6.QtGui import QFont


class SelectionSortApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 600, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.instructions = QLabel("Введите массив чисел (через пробел или запятую):")
        self.instructions.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.instructions)

        self.input_area = QTextEdit()
        self.input_area.setFont(QFont("Courier New", 10))
        self.layout.addWidget(self.input_area)

        self.sort_button = QPushButton("Сортировать методом выбора")
        self.sort_button.clicked.connect(self.sort_array)
        self.layout.addWidget(self.sort_button)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

    def sort_array(self):
        try:
            text = self.input_area.toPlainText()
            raw_numbers = text.replace(",", " ").split()
            array = [int(num) for num in raw_numbers]

            sorted_array = self.selection_sort(array.copy())

            self.result_label.setText(
                f"Исходный массив: {array}\n"
                f"Отсортированный: {sorted_array}"
            )
        except Exception as e:
            self.result_label.setText(f"Ошибка: {str(e)}")

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectionSortApp()
    window.show()
    sys.exit(app.exec())
