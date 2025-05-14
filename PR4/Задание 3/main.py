import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QLineEdit
)
from PySide6.QtGui import QFont


class SearchInSortedArray(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PR4|Задание 3")
        self.setGeometry(100, 100, 700, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.title = QLabel("Поиск числа в отсортированном массиве из 100 случайных элементов")
        self.title.setFont(QFont("Arial", 13))
        self.layout.addWidget(self.title)

        self.input_label = QLabel("Введите целое число:")
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.search_button = QPushButton("Найти число")
        self.search_button.clicked.connect(self.search_number)
        self.layout.addWidget(self.search_button)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def search_number(self):
        try:
            search_value = int(self.input_field.text())
            raw_array = [random.randint(0, 200) for _ in range(100)]
            sorted_array = self.selection_sort(raw_array.copy())

            found_indexes = [i for i, x in enumerate(sorted_array) if x == search_value]

            if found_indexes:
                result = (
                    f"Массив (отсортированный):\n{sorted_array}\n\n"
                    f"Число {search_value} найдено на позициях: {found_indexes}"
                )
            else:
                lesser_values = [x for x in sorted_array if x < search_value]
                if lesser_values:
                    nearest = lesser_values[-1]
                    result = (
                        f"Массив (отсортированный):\n{sorted_array}\n\n"
                        f"Число {search_value} не найдено.\n"
                        f"Ближайшее меньшее число: {nearest}"
                    )
                else:
                    result = (
                        f"Массив (отсортированный):\n{sorted_array}\n\n"
                        f"Число {search_value} не найдено.\n"
                        f"В массиве нет меньших значений."
                    )

            self.result_label.setText(result)

        except ValueError:
            self.result_label.setText("Ошибка: введите корректное целое число.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchInSortedArray()
    window.show()
    sys.exit(app.exec())
