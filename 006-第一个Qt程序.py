import sys

from PyQt6.QtWidgets import *

"""
创建一个app，然后app.exec()就会一直运行着。
在这个运行之前，创建一个主窗口并显示出来
"""
app = QApplication(sys.argv)
# 创建主窗口
x = QMainWindow()
x.setWindowTitle('常用工具')
# 设置窗口大小900*600
x.resize(900, 600)
x.show()
# 运行应用，并监听事件
sys.exit(app.exec())
