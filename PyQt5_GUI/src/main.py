import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.resize(500,500) # set size of the dlg main window
        self.setFixedSize(500,500)
        
        self.ledText = QLineEdit('Text',self) # create line for writing text
        self.ledText.move(200,50) 

        self.btnUpdate = QPushButton('Update main title',self) # create button 
        self.btnUpdate.move(190,100)
        self.btnUpdate.clicked.connect(self.event_btn_update_clicked) # connect button with method 


    def event_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())