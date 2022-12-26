from PyQt5 import QtCore, QtGui, QtWidgets
from funcs import get_path_to_folder_download_video,user_input_link,download_video_to_the_folder


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(91, 126, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 137, 181, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 150, 40))
        self.label.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(76, 132, 64);\n"
"color: rgb(252, 255, 76);\n"
"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(140, 310, 150, 40))
        self.Start.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"background-color: rgb(252, 68, 48);\n"
"alternate-background-color: rgb(203, 33, 66);")
        self.Start.setObjectName("Start")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(120, 140, 193, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(120, 200, 193, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Video downloader"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.commandLinkButton.setText(_translate("MainWindow", "URL"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Path to folder"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

