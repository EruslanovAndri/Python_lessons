from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QComboBox,QFileDialog,QPushButton,QVBoxLayout
import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()   

    window.setGeometry(200,200,400,500)
    window.setWindowTitle('Downlader')
    window.setFixedSize(400,500)

    headTitle = QtWidgets.QLabel(window)
    headTitle.setText('Downloader')
    headTitle.setGeometry(160,0,100,100)
    headTitle.move(165,20)
    headTitle.adjustSize()

    urlTitle = QtWidgets.QLabel(window)
    urlTitle.setText('Enter URL')
    urlTitle.setGeometry(160,50,200,30)
    urlTitle.move(165,50)
    urlTitle.adjustSize()
    

    urlLink = QtWidgets.QLineEdit(window)
    urlLink.setGeometry(50,80,300,30)


    pathFolder = QtWidgets.QLabel(window)
    pathFolder.setText('Path to the folder')
    pathFolder.move(160,150)
    pathFolder.adjustSize()


    video = QtWidgets.QRadioButton(window)
    video.setGeometry(50,200,150,150)
    video.setText('Download video')

    audio = QtWidgets.QRadioButton(window)
    audio.setGeometry(50,250,150,150)
    audio.setText('Download audio')




    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()

    