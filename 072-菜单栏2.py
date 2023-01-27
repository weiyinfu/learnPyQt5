import sys

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Menu - Geekscoders.com")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        self.create_menu()

    def create_menu(self):
        main_menu = self.menuBar()
        fileMenu = main_menu.addMenu("File")

        newAction = QAction(QIcon('images/new.png'), "New", self)
        newAction.setShortcut("Ctrl+N")
        fileMenu.addAction(newAction)

        saveAction = QAction(QIcon('images/save.png'), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        fileMenu.addSeparator()

        copyAction = QAction(QIcon('images/copy.png'), "Copy", self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)

        exitAction = QAction(QIcon('images/exit.png'), "Exit", self)
        exitAction.triggered.connect(self.close_window)

        fileMenu.addAction(exitAction)

    def close_window(self):
        self.close()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
