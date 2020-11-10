from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton
from pathlib import Path
from BlackMagicPy.gui import manualCWindow, autoCWindow, dataViewWindow


reldir = str(Path.cwd())
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\mainWindow.ui')


class MainWindow(BaseClass, FormClass):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.mcwin = manualCWindow.ManualCWindow()
        self.acwin = autoCWindow.AutoCWindow()
        self.dvwin = dataViewWindow.DataViewWindow()
        self.setupUi(self)

        self.manualCbutton = self.findChild(QPushButton, 'manualCbutton')
        self.manualCbutton.clicked.connect(self.manualCbuttonCallBack)

        self.autoCbutton = self.findChild(QPushButton, 'autoCbutton')
        self.autoCbutton.clicked.connect(self.autoCbuttonCallBack)

        self.dataViewButton = self.findChild(QPushButton, 'dataViewButton')
        self.dataViewButton.clicked.connect(self.dataViewButtonCallBack)

    def manualCbuttonCallBack(self):
        self.mcwin.show()

    def autoCbuttonCallBack(self):
        self.acwin.show()

    def dataViewButtonCallBack(self):
        self.dvwin.show()
