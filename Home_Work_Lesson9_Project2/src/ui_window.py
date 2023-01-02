from PyQt5 import QtCore, QtGui, QtWidgets
from funcs import download_video_to_the_folder,download_audio

class Ui_Downloader(object):
    def setupUi(self, Downloader):
        Downloader.setObjectName("Downloader")
        Downloader.setMinimumSize(QtCore.QSize(400, 500))
        Downloader.setMaximumSize(QtCore.QSize(400, 500))
        Downloader.setMouseTracking(False)
        Downloader.setStyleSheet("background-color: rgb(137, 148, 131);")
        self.centralwidget = QtWidgets.QWidget(Downloader)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setEnabled(True)
        self.main_label.setGeometry(QtCore.QRect(80, 20, 241, 41))
        self.main_label.setSizeIncrement(QtCore.QSize(10, 10))
        self.main_label.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.main_label.setFont(font)
        self.main_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_label.setAcceptDrops(False)
        self.main_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_label.setAutoFillBackground(False)
        self.main_label.setStyleSheet("background-color: rgb(90, 99, 12);")
        self.main_label.setFrameShape(QtWidgets.QFrame.Box)
        self.main_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_label.setLineWidth(1)
        self.main_label.setMidLineWidth(2)
        self.main_label.setScaledContents(False)
        self.main_label.setObjectName("main_label")

        #----------URL LABEL--------------------#

        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setEnabled(True)
        self.url_label.setGeometry(QtCore.QRect(20, 90, 111, 41))
        self.url_label.setSizeIncrement(QtCore.QSize(10, 10))
        self.url_label.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.url_label.setFont(font)
        self.url_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.url_label.setAcceptDrops(False)
        self.url_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.url_label.setAutoFillBackground(False)
        self.url_label.setStyleSheet("background-color: rgb(90, 99, 12);")
        self.url_label.setFrameShape(QtWidgets.QFrame.Box)
        self.url_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.url_label.setLineWidth(1)
        self.url_label.setMidLineWidth(2)
        self.url_label.setScaledContents(False)
        self.url_label.setObjectName("url_label")

        
        #----------------END URL LABLE--------------------#


        #----------------Button open path to a folder--------------------#

        self.button_path_to_folder = QtWidgets.QPushButton(self.centralwidget)
        self.button_path_to_folder.setGeometry(QtCore.QRect(29, 160, 341, 41))
        self.button_path_to_folder.setSizeIncrement(QtCore.QSize(10, 10))
        self.button_path_to_folder.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(20)
        font.setBold(True)
        self.button_path_to_folder.setFont(font)
        self.button_path_to_folder.setStyleSheet("background-color: rgb(26, 135, 138);")
        self.button_path_to_folder.setObjectName("button_path_to_folder")

        self.button_path_to_folder.clicked.connect(self.choose_folder)
        

        #----------------END   Button open path to a folder--------------------#
        

        self.show_path_to_folder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.show_path_to_folder.setGeometry(QtCore.QRect(30, 210, 341, 41))
        self.show_path_to_folder.setStyleSheet("background-color: rgb(18, 12, 15);\n"
"")
        self.show_path_to_folder.setObjectName("show_path_to_folder")

        
        
        #---------------URL LINE START--------------------------------#
        self.url_line = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url_line.setGeometry(QtCore.QRect(140, 90, 231, 41))
        self.url_line.setStyleSheet("background-color: rgb(18, 12, 15);")
        self.url_line.setObjectName("url_line")


         #---------------URL LINE END--------------------------------#


       
        #--------------------START RADIOBUTTON VIDEO-----------------------#
        self.radioButton_video = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_video.setGeometry(QtCore.QRect(40, 270, 81, 31))
        self.radioButton_video.setStyleSheet("color: rgb(19, 26, 91);")
        self.radioButton_video.setObjectName("radioButton_video")

        #--------------------END RADIOBUTTON VIDEO-----------------------#

        #--------------------START RADIOBUTTON AUDIO-----------------------#
        self.radioButton_audio = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_audio.setGeometry(QtCore.QRect(40, 310, 81, 31))
        self.radioButton_audio.setStyleSheet("color: rgb(19, 26, 91);\n"
"")
        self.radioButton_audio.setObjectName("radioButton_audio")

        #--------------------END RADIOBUTTON AUDIO-----------------------#
        self.button_group = QtWidgets.QButtonGroup(self.centralwidget)
        self.button_group.addButton(self.radioButton_video)
        self.button_group.addButton(self.radioButton_audio)
        #--------------------START BUTTON START---------------------------#
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(30, 350, 341, 41))
        self.button_start.setSizeIncrement(QtCore.QSize(10, 10))
        self.button_start.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(20)
        font.setBold(True)
        self.button_start.setFont(font)
        self.button_start.setStyleSheet("background-color: rgb(26, 135, 138);")
        self.button_start.setObjectName("button_start")

        self.button_start.clicked.connect(self.start_download)

        #---------------------END BUTTON START------------------------------#

        #---------------------START PROGRESS BAR-----------------------------#
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 420, 341, 51))
        self.progressBar.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        Downloader.setCentralWidget(self.centralwidget)
         #---------------------END PROGRESS BAR-----------------------------#
        self.retranslateUi(Downloader)
        QtCore.QMetaObject.connectSlotsByName(Downloader)


    def retranslateUi(self, Downloader):
        _translate = QtCore.QCoreApplication.translate
        Downloader.setWindowTitle(_translate("Downloader", "Downloader"))
        self.main_label.setText(_translate("Downloader", "          Downloader"))
        self.url_label.setText(_translate("Downloader", "  URL =>"))
        self.button_path_to_folder.setText(_translate("Downloader", "Choose a folder"))
        self.radioButton_video.setText(_translate("Downloader", "    Video"))
        self.radioButton_audio.setText(_translate("Downloader", "    Audio"))
        self.button_start.setText(_translate("Downloader", "Start"))


    def start_download(self):
        url = self.url_line.toPlainText()
        sent_to_folder = self.show_path_to_folder.toPlainText()
        group = self.button_group.checkedId()
        if group == -2:
            download_video_to_the_folder(url,sent_to_folder)
        else:
            download_audio(url,sent_to_folder)
        
    def choose_folder(self):
      choose_folder = QtWidgets.QFileDialog.getExistingDirectory()
      self.show_path_to_folder.insertPlainText(choose_folder)
      




