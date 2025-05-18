from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLineEdit, QLabel, QTextEdit)


class FractionUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()

        self.input_label = QLabel("Введите дроби (через пробел, формат: a/b):")
        self.input_field = QLineEdit()
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_field)

        self.calculate_button = QPushButton("Вычислить произведение")
        main_layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат:")
        self.result_field = QTextEdit()
        self.result_field.setReadOnly(True)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_field)

        self.setLayout(main_layout)
