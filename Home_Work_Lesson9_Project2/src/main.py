from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QButtonGroup,QPushButton,QColorDialog
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300,300,400,400)
    win.setWindowTitle('My first window')
    win.setStyleSheet('background-color:grey;')

    label = QtWidgets.QLabel(win)
    label.setText('My first label')
    label.move(50,50)


    win.show()
    sys.exit(app.exec_())
window()

