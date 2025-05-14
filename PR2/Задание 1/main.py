import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import Qt


class ArrayProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PR2|Задание 1")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Введите массив вещественных чисел через пробел:")
        self.layout.addWidget(self.input_label)

        self.input_line = QLineEdit()
        self.layout.addWidget(self.input_line)

        self.process_button = QPushButton("Обработать")
        self.process_button.clicked.connect(self.process_array)
        self.layout.addWidget(self.process_button)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def process_array(self):
        try:
            array = list(map(float, self.input_line.text().split()))

            zero_count = sum(1 for x in array if x == 0)

            min_index = array.index(min(array))
            sum_after_min = sum(array[min_index + 1:])

            sorted_by_abs = sorted(array, key=abs)

            result_text = (
                f"Количество нулей: {zero_count}\n"
                f"Сумма после минимального элемента: {sum_after_min}\n"
                f"Массив, отсортированный по модулю: {sorted_by_abs}"
            )

            self.result_label.setText(result_text)

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите корректные числа через пробел!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayProcessor()
    window.show()
    sys.exit(app.exec())
