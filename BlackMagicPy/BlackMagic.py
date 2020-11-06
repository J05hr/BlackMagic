from PyQt5.QtWidgets import QApplication
from BlackMagicPy.gui import mainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWindow.MainWindow()

    win.show()
    sys.exit(app.exec())
