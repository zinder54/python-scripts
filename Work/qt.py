from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300,300)
    win.setWindowTitle("kiwa testing")

    win.show()
    sys.exit(app.exec_())

window() 
##pycui5 -x qt.ui -o qt.py   <<this turns the ui file from qtdesigner into a usable python file
