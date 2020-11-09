from PyQt5 import uic
from pathlib import Path
from PyQt5.QtWidgets import *
from BlackMagicPy.gui import resultsDialog


reldir = str(Path.cwd())
baseDataDir = '\\data'
FormClass, BaseClass = uic.loadUiType(reldir + '\\layouts\\manualCWindow.ui')


class ManualCWindow(BaseClass, FormClass):
    def __init__(self):
        super(ManualCWindow, self).__init__()
        self.browseDialog = None
        self.resultsDialog = None
        self.dataFname = None
        self.trainingData = None
        self.testingData = None
        self.trainingModel = None
        self.setupUi(self)

        self.curDirLabel = self.findChild(QLabel, 'curDirLabel')
        self.curDirLabel.setText('\\..' + baseDataDir)

        self.trainPercentSpin = self.findChild(QSpinBox, 'trainPercentSpin')
        self.sellBelowSpin = self.findChild(QDoubleSpinBox, 'sellBelowSpin')
        self.buyAboveSpin = self.findChild(QDoubleSpinBox, 'buyAboveSpin')
        self.movingAvgSpin = self.findChild(QSpinBox, 'movingAvgSpin')

        self.browseButton = self.findChild(QPushButton, 'browseButton')
        self.browseButton.clicked.connect(self.browseButtonCallBack)

        self.runCButton = self.findChild(QPushButton, 'runCButton')
        self.runCButton.clicked.connect(self.runCButtonCallBack)

        self.dataListWidget = self.findChild(QListWidget, 'dataListWidget')
        self.dataListWidget.clicked.connect(self.dataSelectedCallBack)
        self.dataDir = reldir + baseDataDir
        self.updateListView()

    def updateListView(self):
        if self.dataDir:
            pobj = Path(self.dataDir)
            for fname in pobj.iterdir():
                self.dataListWidget.addItem(str(fname.name))

    def browseButtonCallBack(self):
        self.dataListWidget.clear()
        self.browseDialog = QFileDialog()
        self.dataDir = self.browseDialog.getExistingDirectory(self, "Choose Data Directory", self.dataDir, self.browseDialog.ShowDirsOnly)
        self.updateListView()

    def runCButtonCallBack(self):
        self.runCButton.setEnabled(False)
        self.runCButton.setText("Running...")

        self.resultsDialog = resultsDialog.ResultsDialog()
        self.resultsDialog.show()
        self.resultsDialog.finished.connect(self.resultsDialogFinishedCallback)

    def resultsDialogFinishedCallback(self):
        self.runCButton.setEnabled(True)
        self.runCButton.setText("Run Classification")

    def dataSelectedCallBack(self):
        self.dataFname = self.dataListWidget.selectedItems()
        self.runCButton.setEnabled(True)
