# Практическая работа №5

### Тема: Поиск элементов массива

### Цель: приобрести навыки составления программ с использованием одномерных массивов

#### Задачи:

> * повторить структуру операторов ввода-вывода и использование циклов, вложенных циклов
> * повторить синтаксис оператора инициализации и ввода-вывода массивов;
> * повторить основные библиотечные файлы, подключаемые при выполнении программ;
> * усовершенствовать навыки составления программ с одномерными массивами.

#### Задание

> В массиве все элементы, стоящие после нечетных, заменить на 0.

#### Контрольный пример

> Ввожу размер массива
> Получаю массив нужного размера, где первые элементы после нечетных равны нулю.

#### Системный анализ

> Входные данные: `Integer n`
> Промежуточные данные: `Array array`, `Array result_array`
> Выходные данные: `String result`

#### Блок-схема

![block.drawio.png](src/block.drawio.png)

#### Код программы

```python
import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit
)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
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
            for i in range(len(result_array) - 1):
                if result_array[i] % 2 != 0:
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

```

#### Результат работы программы

![screen.png](src/screen.png)

#### Вывод по проделанной работе

![cat.gif](../cat.gif)