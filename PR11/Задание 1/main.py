import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)


class SplitMatrixElements(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 600, 450)

        layout = QVBoxLayout()

        size_layout = QHBoxLayout()
        self.input_rows = QLineEdit()
        self.input_rows.setPlaceholderText("Количество строк")
        self.input_cols = QLineEdit()
        self.input_cols.setPlaceholderText("Количество столбцов")
        size_layout.addWidget(self.input_rows)
        size_layout.addWidget(self.input_cols)
        layout.addLayout(size_layout)

        self.btn_generate = QPushButton("Сгенерировать матрицу")
        self.btn_generate.clicked.connect(self.generate_matrix)
        layout.addWidget(self.btn_generate)

        self.label_matrix = QLabel("Исходная матрица:")
        layout.addWidget(self.label_matrix)
        self.table_matrix = QTableWidget()
        layout.addWidget(self.table_matrix)

        self.btn_split = QPushButton("Разделить элементы")
        self.btn_split.clicked.connect(self.split_elements)
        layout.addWidget(self.btn_split)

        self.label_pos_zero = QLabel("Положительные и нулевые элементы:")
        layout.addWidget(self.label_pos_zero)
        self.list_pos_zero = QListWidget()
        layout.addWidget(self.list_pos_zero)

        self.label_neg = QLabel("Отрицательные элементы:")
        layout.addWidget(self.label_neg)
        self.list_neg = QListWidget()
        layout.addWidget(self.list_neg)

        self.setLayout(layout)

    def generate_matrix(self):
        try:
            rows = int(self.input_rows.text())
            cols = int(self.input_cols.text())
            if rows <= 0 or cols <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите корректные размеры матрицы.")
            return

        self.matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

        self.display_table(self.table_matrix, self.matrix)

        self.list_pos_zero.clear()
        self.list_neg.clear()

    def split_elements(self):
        if not hasattr(self, 'matrix'):
            QMessageBox.warning(self, "Внимание", "Сначала сгенерируйте матрицу.")
            return

        pos_zero = []
        neg = []
        for row in self.matrix:
            for val in row:
                if val >= 0:
                    pos_zero.append(val)
                else:
                    neg.append(val)

        self.list_pos_zero.clear()
        self.list_pos_zero.addItems(map(str, pos_zero))

        self.list_neg.clear()
        self.list_neg.addItems(map(str, neg))

    def display_table(self, table, data):
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0
        table.setRowCount(rows)
        table.setColumnCount(cols)
        for i in range(rows):
            for j in range(cols):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitMatrixElements()
    window.show()
    sys.exit(app.exec())
