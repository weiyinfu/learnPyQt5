import sys

from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
# 创建主窗口
x = QMainWindow()
x.setWindowTitle('常用工具')
# 设置窗口大小900*600
x.resize(1300, 700)
x.show()
# 运行应用，并监听事件
sys.exit(app.exec_())
