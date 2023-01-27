import sys
from os.path import *

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

folder = dirname(abspath(__file__))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        iconPath = join(folder, 'web.png')
        print(iconPath)
        self.setWindowIcon(QIcon(iconPath))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
