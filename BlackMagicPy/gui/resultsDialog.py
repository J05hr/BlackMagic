from PyQt5 import uic
from pathlib import Path


reldir = str(Path.cwd())
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\resultsDialog.ui')


class ResultsDialog(BaseClass, FormClass):
    def __init__(self):
        super(ResultsDialog, self).__init__()
        self.setupUi(self)

