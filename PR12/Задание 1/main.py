import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QListWidget, QMessageBox
)


def product_subarray(d, k, s):
    if s - k + 1 != 3:
        raise ValueError("Подмассив должен содержать ровно 3 элемента")
    prod = 1
    for i in range(k, s + 1):
        prod *= d[i]
    return prod


class ArrayProductApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 500, 350)

        layout = QVBoxLayout()

        self.btn_generate = QPushButton("Сгенерировать массив из 10 элементов")
        self.btn_generate.clicked.connect(self.generate_array)
        layout.addWidget(self.btn_generate)

        self.list_array = QListWidget()
        layout.addWidget(QLabel("Массив d:"))
        layout.addWidget(self.list_array)

        self.btn_compute = QPushButton("Вычислить выражения")
        self.btn_compute.clicked.connect(self.compute_results)
        layout.addWidget(self.btn_compute)

        self.label_result = QLabel("")
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def generate_array(self):
        self.d = [random.randint(1, 10) for _ in range(10)]
        self.list_array.clear()
        self.list_array.addItems(map(str, self.d))
        self.label_result.setText("")

    def compute_results(self):
        if not hasattr(self, 'd'):
            QMessageBox.warning(self, "Внимание", "Сначала сгенерируйте массив.")
            return
        try:
            p1 = product_subarray(self.d, 1, 3)  # d[1]*d[2]*d[3]
            p2 = product_subarray(self.d, 4, 6)  # d[4]*d[5]*d[6]
            s3 = self.d[7] + self.d[8] + self.d[9]  # d[7]+d[8]+d[9]
        except IndexError:
            QMessageBox.critical(self, "Ошибка", "Массив должен содержать минимум 10 элементов.")
            return
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            return

        result_text = (
            f"Произведение d[1]*d[2]*d[3]: {p1}\n"
            f"Произведение d[4]*d[5]*d[6]: {p2}\n"
            f"Сумма d[7]+d[8]+d[9]: {s3}"
        )
        self.label_result.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayProductApp()
    window.show()
    sys.exit(app.exec())
