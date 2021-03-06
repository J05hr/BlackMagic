from PyQt5 import uic
from pathlib import Path


reldir = str(Path.cwd())
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\dataViewWindow.ui')


class DataViewWindow(BaseClass, FormClass):
    def __init__(self):
        super(DataViewWindow, self).__init__()
        self.setupUi(self)