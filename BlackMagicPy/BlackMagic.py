from PyQt5.QtWidgets import QApplication
from BlackMagicPy.gui import mainWindow
from BlackMagicPy.layouts.stylesheets import style_resources
from BlackMagicPy.utils import utils
from pathlib import Path
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stylePath = str(Path.cwd()) + '\\layouts\\stylesheets\\dark.qss'
    utils.toggle_stylesheet(stylePath)
    win = mainWindow.MainWindow()
    win.show()
    sys.exit(app.exec())


