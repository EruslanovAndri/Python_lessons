from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QPushButton,QTabBar
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('Video downloader from YouTube')
    win.setGeometry(100,100,500,500)
    win.setStyleSheet('background-color:pink;')

    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    layout.addLayout(layout)

    main_text = QtWidgets.QLabel(win)
    main_text.setText('Are you ready for download new video from YouTube?')
    main_text.move(80,40)
    main_text.adjustSize()

    btn = QtWidgets.QPushButton(win)
    btn.move(100,150)
    btn.setText('Start')
    btn.setFixedWidth(200)

    bar = QTabBar(win)
    bar.move(100,100)
    bar.adjustSize()
    


    win.show()
    sys.exit(app.exec_())
window()