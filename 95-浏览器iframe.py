import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

"""
使用Qt实现的webviewer。  
这种webviewer存在很多问题：
* 需要flash的时候，没法安装flash
* 请求有些资源的时候会被block
"""
link_list = [
    {'name': '芳斯塔芙-生物科普', 'url': 'https://www.zhihu.com/people/irenecai/zvideos'},
    {'name': 'YouTube英语精选', 'url': 'https://www.zhihu.com/people/kan-man-hua-54/zvideos'},
    {'name': 'Linvo说宇宙', 'url': 'https://www.zhihu.com/people/linvosay/zvideos'},
    {'name': '妈咪说', 'url': 'https://space.bilibili.com/223146252?spm_id_from=333.337.search-card.all.click'},
]


# 创建主窗口
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('简易浏览器')
        # 设置窗口大小900*600
        self.resize(1300, 700)
        self.show()

        # 创建tabwidget（多标签页面）
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)

        for i in link_list:
            # 第一个tab页面
            self.webview = WebEngineView(self)  # self必须要有，是将主窗口作为参数，传给浏览器
            self.webview.load(QUrl(i['url']))
            self.create_tab(self.webview, i['name'])

    # 显示地址
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.webview.setUrl(q)

    # 创建tab页面
    def create_tab(self, webview, title):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, title)
        self.tabWidget.setCurrentWidget(self.tab)

        # 渲染到页面
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)

    # 关闭tab页面
    def close_Tab(self, index):
        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()  # 当只有1个tab时，关闭主窗口


# 创建浏览器，重写重写createwindow方法实现页面连接的点击跳转
class WebEngineView(QWebEngineView):

    def __init__(self, mainwindow, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow

    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)
        self.mainwindow.create_tab(new_webview, "新建页面")
        return new_webview


# 程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 创建主窗口
    browser = MainWindow()
    browser.show()
    # 运行应用，并监听事件
    sys.exit(app.exec_())
