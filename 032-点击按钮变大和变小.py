import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        def get_small(*args, **kwargs):
            self.width -= 10
            self.setGeometry(300, 300, self.width, self.height)

        def get_big(*args, **kwargs):
            print(args, kwargs)
            self.width += 10
            self.setGeometry(300, 300, self.width, self.height)

        big = QPushButton('变大', self)
        big.clicked.connect(get_big)
        big.resize(big.sizeHint())
        big.move(50, 50)

        small = QPushButton('变小', self)
        small.clicked.connect(get_small)
        small.resize(small.sizeHint())
        small.move(150, 50)

        self.setGeometry(300, 300, self.width, self.height)
        self.setWindowTitle('变大变小')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
