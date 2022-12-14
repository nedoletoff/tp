# Form implementation generated from reading ui file 'logParser.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import logging
from tkinter.filedialog import askopenfilename

from PyQt6 import QtCore, QtGui, QtWidgets

logging.basicConfig(
    filename="/home/nedoletoff/Documents/tp/sample.log",
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
log = logging.getLogger("ex")

class Ui_MainWindow(object):
    def __init__(self):
        self.filename = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 991, 741))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.date_edit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_edit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit.setObjectName("date_edit")
        self.gridLayout.addWidget(self.date_edit, 0, 4, 1, 1)
        self.find_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.find_button.setObjectName("find_button")
        self.gridLayout.addWidget(self.find_button, 0, 3, 1, 1)
        self.Signature_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Signature_edit.setObjectName("Signature_edit")
        self.gridLayout.addWidget(self.Signature_edit, 1, 0, 1, 2)
        self.gap_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gap_button.setObjectName("gap_button")
        self.gridLayout.addWidget(self.gap_button, 1, 3, 1, 1)
        self.text_browser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.text_browser_2.setObjectName("text_browser_2")
        self.gridLayout.addWidget(self.text_browser_2, 6, 0, 1, 5)
        self.open_file_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_file_button.setObjectName("open_file_button")
        self.gridLayout.addWidget(self.open_file_button, 0, 2, 1, 1)
        self.date_edit_2 = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_edit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit_2.setObjectName("date_edit_2")
        self.gridLayout.addWidget(self.date_edit_2, 1, 4, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 1, 2, 1, 1)
        self.Signature_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Signature_label.setObjectName("Signature_label")
        self.gridLayout.addWidget(self.Signature_label, 0, 0, 1, 2)
        self.plain_text_edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plain_text_edit.setObjectName("plain_text_edit")
        self.gridLayout.addWidget(self.plain_text_edit, 2, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_file_button.clicked.connect(self.openFile)
        self.clear_button.clicked.connect(self.clear)
        self.find_button.clicked.connect(self.find)

    def find(self):
        text = self.plain_text_edit.toPlainText()



    def openFile(self):
        try:
            self.filename = askopenfilename()
        except Exception as e:
            log.exception(e)
            return
        with open(self.filename) as file:
            text = file.read()
        self.text_browser_2.setText(text)

    def clear(self):
        self.plain_text_edit.clear()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.find_button.setText(_translate("MainWindow", "Find"))
        self.gap_button.setText(_translate("MainWindow", "Gap"))
        self.open_file_button.setText(_translate("MainWindow", "Open File"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.Signature_label.setText(_translate("MainWindow", "Signature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
