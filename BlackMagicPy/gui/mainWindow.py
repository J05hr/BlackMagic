from PyQt5 import uic
from pathlib import Path

reldir = str(Path.cwd())
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\mainWindow.ui')

class MainWindow(BaseClass, FormClass):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


