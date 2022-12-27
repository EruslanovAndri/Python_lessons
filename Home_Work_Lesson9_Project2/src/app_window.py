from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QComboBox,QFileDialog,QPushButton,QVBoxLayout
import sys
from funcs import get_path_to_folder_download_video,user_input_link


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()   
    # Main window
    window.setGeometry(200,200,400,500)
    window.setWindowTitle('Downlader')
    window.setFixedSize(400,500)
    # Head Title
    headTitle = QtWidgets.QLabel(window)
    headTitle.setText('Downloader')
    headTitle.setGeometry(160,0,100,100)
    headTitle.move(165,20)
    headTitle.adjustSize()
    # URL Title
    urlTitle = QtWidgets.QLabel(window)
    urlTitle.setText('Enter URL')
    urlTitle.setGeometry(160,50,200,30)
    urlTitle.move(165,50)
    urlTitle.adjustSize()
    # URL Link string
    urlLink = QtWidgets.QLineEdit(window)
    urlLink.setGeometry(50,80,300,30)
    # Push button to open path to folder
    button = QtWidgets.QPushButton(window)
    button.setText('Choose path to a folder')
    button.setGeometry(100,150,170,50)
    button.adjustSize()
    # Information label 
    label = QtWidgets.QLabel(window)
    label.setText('Choose a folder')
    label.adjustSize()
    label.setGeometry(50,200,200,40)

    # RadioButton video
    video = QtWidgets.QRadioButton(window)
    video.setGeometry(50,200,150,150)
    video.setText('Download video')

    # RadioButton audio
    audio = QtWidgets.QRadioButton(window)
    audio.setGeometry(50,250,150,150)
    audio.setText('Download audio')

    # Connection Push button for choosing folder
    # button.clicked.connect(lambda:clicker(label))
    button.clicked.connect(lambda:pathToFolder(label))

    window.show()
    sys.exit(app.exec_())

#-------------------------------Functions----------------------------------------------#
    # Method connect push button to open the folder with information label 
# def clicker(file):
#     fileName = QtWidgets.QFileDialog.getOpenFileName(file,'Open File','','ALL Files (*);;Python Files (*.py)')
#     if fileName:
#         file.setText(fileName[0])
def pathToFolder(folder):
    folderName = QFileDialog.getExistingDirectory(folder,'Select Directory')
    if folderName:
        folder.setText(folderName[0])
    


if __name__ == '__main__':
    application()

    