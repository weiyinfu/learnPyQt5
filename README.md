# 学习PyQt的必要性
* Python的GUI库可用的不多，tkinter等简单库基本上都是歧途
* 想做一些给自己用的GUI工具，想把过去的一些python代码封装成GUI工具
* 不想为了做GUI去跨语言调用，学习任何一门语言都应该掌握一下这门语言的GUI开发
* PyQt的官方文档实在是太漂亮了
* flutter、electron编译出来的应用都太大了，至少几十兆。使用Python做的GUI很小。

# Qt是什么？
Qt是一个巨无霸，是最著名的C++库之一。它什么东西都想自己做，例如QMake、网络库、JSON库等。   
同时代的MFC等已经被淘汰了，而Qt却以其跨平台特性称为C++中的最佳GUI库。  

PyQt6 和 PySide6 都是用于调用 Qt6 API 的Python库，使用它们可以轻松在Python语言中创建基于Qt的GUI程序；PyQt6 和 PySide6 最大的不同表现在发行许可上；

PyQt6 是由 Riverbank Computing 公司的Phil Thompson开发，出现的比较早；它采用 GPLv3 许可证和商业许可证发布；这表示你如果使用 PyQt6 ，则必须将你的代码进行开源；如果要闭源，则需要购买商业许可；

PySide6 是 Qt 官方的库，亲儿子，出现的时间要比 PyQt 晚的多，这也是很多人知道 PyQt 不知道 PySide 的原因；但随着版本的迭代， PySide6 越来越强大，作者更看好 PySide ；

PySide6 采用 LGPL 许可发布，这意味着只要你以调用动态链接库的形式使用 Qt ，你可以以任何形式（商业、非商业、开源、非开源）发布你的程序；


# QDesktopWidget弃用
QDesktopWidget and QApplication::desktop()
QDesktopWidget was already deprecated in Qt 5, and has been removed in Qt 6, together with QApplication::desktop().

QScreen provides equivalent functionality to query for information about available screens, screen that form a virtual desktop, and screen geometries.

Use QWidget::setScreen() to create a QWidget on a specific display; note that this does not move a widget to a screen in a virtual desktop setup.

Then use:

    cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
# 问题记录
mac平台升级12之后无法显示PyQt5的窗口，使用PyQt6则一切正常。  
或者使用PyQt5=5.13也能够解决问题。  
https://clay-atlas.com/us/blog/2021/10/12/macos-en-big-sur-pyqt5-window-cannnot-be-showed/

QAction,QIcon在QtGui包下面。  

浏览器模块在PyQt6里面移除掉了，需要手动安装浏览器模块：`pip install PyQt6-WebEngine`

`from PyQt6.QtWebEngineWidgets import QWebEngineView`

# 安装
安装PyQt6：
pip install PyQt6

安装PyQt6 web引擎：
pip install PyQt6-WebEngine

安装PyQt6工具，之后可以使用pyqt6designer
pip install pyqt6-tools
# TODO
练习QT：实现记事本，实现Mac桌面工具，实现聊天工具

# 参考文档
http://code.py40.com/pyqt5/14.html  
https://doc.qt.io/qtforpython/contents.html  
https://doc.bccnsoft.com/docs/PyQt5/

Qt6视频教程
https://geekscoders.com/courses/pyqt6-tutorials/lessons/how-to-create-qmenu-in-pyqt6/