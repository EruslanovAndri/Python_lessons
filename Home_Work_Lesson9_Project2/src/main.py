from ui_window import Ui_Downloader
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Downloader = QtWidgets.QMainWindow()
    ui = Ui_Downloader()
    ui.setupUi(Downloader)
    Downloader.show()
    sys.exit(app.exec_())
