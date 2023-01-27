import os
import sys

from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import *
from PyQt6.QtWebEngineCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import *


class WebEnginePage(QWebEnginePage):  # QWebEngineView
    def __init__(self, profile, parent=None):
        super().__init__(profile, parent)

    def contextMenuEvent(self, event):  # 算是一种折中的方法，因为其他的方法好像因为bug的原因不起作用
        self.menu = self.createStandardContextMenu()  # page().
        selectedText = self.selectedText()
        if selectedText:
            self.menu.addSeparator()
            self.menu.addAction('谷歌搜索', lambda: QDesktopServices.openUrl(QUrl(f'https://www.google.com/search?q={selectedText}')))
        self.menu.popup(event.globalPos())  # 这种貌似怪异的做法也不能改成show或pos；using menu.exec() might lead to consolle warnings and painting artifacts, so using popup() is better


class WebEngineView(QWebEngineView):  # QWebEngineView
    def __init__(self, parent=None):
        super().__init__(parent)

        self.webEngineProfile = QWebEngineProfile('EngkudictWebEngineProfile ')
        # self.webEngineProfile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        print(self.webEngineProfile.persistentCookiesPolicy(), self.webEngineProfile.isOffTheRecord())
        self.webpage = WebEnginePage(self.webEngineProfile)  # QWebEnginePage(self.webEngineProfile)
        # self.webpage.destroyed.connect(lambda obj: self.webEngineProfile.deleteLater())  #这种方式不行 If the profile is not the default profile, the caller must ensure that the profile stays alive for as long as the page does.
        self.setPage(self.webpage)
        self.webpage.load(QUrl('https://fanyi.baidu.com/'))

        # webEngineProfile = self.page().profile()
        # # webEngineProfile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        # print(webEngineProfile.persistentCookiesPolicy(), webEngineProfile.isOffTheRecord(), webEngineProfile.persistentStoragePath())  # Qt6 PersistentCookiesPolicy.NoPersistentCookies True=====Qt6  1 False
        # # self.load(QUrl('https://fanyi.baidu.com/'))
        # self.load(QUrl('https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile-1'))

    @Slot(QCloseEvent)
    def closeEvent(self, event):
        self.setPage(None)  # To avoid msg: Release of profile requested but WebEnginePage still not deleted. Expect troubles !  https://github.com/qutebrowser/qutebrowser/commit/e6ae8797e71a678bef97a13b9057e29442e0ef48
    # del self.webEngineProfile
    # self.webEngineProfile.deleteLater()  # A disk-based QWebEngineProfile should be destroyed on or before application exit, otherwise the cache and persistent data may not be fully flushed to disk.  https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile-1


if __name__ == "__main__":
    # QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 任务Qt6 不需要了Qt High DPI scaling is now activated by default; the default rounding policy is PassThrough
    # os.putenv("QT_ENABLE_HIGHDPI_SCALING", '1')
    os.putenv("QT_SCALE_FACTOR", '1.6')

    app = QApplication(sys.argv)
    webEngineView = WebEngineView()
    webEngineView.showMaximized()
    sys.exit(app.exec())
