from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from kiwaqt import Ui_MainWindow
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        OpenFile = QAction("&Open File", self)
        OpenFile.setShortcut("Ctrl+O")
        OpenFile.setStatusTip('Open File')
        OpenFile.triggered.connect(self.file_open)

        SaveFile = QAction("&Save File", self)
        SaveFile.setShortcut("Ctrl+S")
        SaveFile.setStatusTip('Save File')
        SaveFile.triggered.connect(self.save_file)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(OpenFile)
        fileMenu.addAction(SaveFile)


    def file_open(self):
        files, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()","","All Files (*);;python Files (*.py)")
        if files:
            print(files)
    def save_file(self):
        options = QFileDialog.Options()
        name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","Text Files (*.txt);;All Files (*)",
                                            options=options)
        if name:
            print(name)



def window():
    app = QApplication(sys.argv)
    application  = ApplicationWindow()
    application.setWindowTitle("kiwa testing")
    application.show()
    sys.exit(app.exec_())

window()
##pycui5 -x qt.ui -o qt.py   <<this turns the ui file from qtdesigner into a usable python file
