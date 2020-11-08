from PyQt5 import uic
from pathlib import Path


reldir = str(Path.cwd())
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\manualCWindow.ui')


class ManualCWindow(BaseClass, FormClass):
    def __init__(self):
        super(ManualCWindow, self).__init__()
        self.setupUi(self)
