# Form implementation generated from reading ui file 'viginer.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.key_decipher_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.key_decipher_label.setObjectName("key_decipher_label")
        self.gridLayout.addWidget(self.key_decipher_label, 2, 1, 1, 1)
        self.text_edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 1, 0, 1, 1)
        self.result_decipher_browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.result_decipher_browser.setObjectName("result_decipher_browser")
        self.gridLayout.addWidget(self.result_decipher_browser, 6, 1, 1, 1)
        self.cipher_text_edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.cipher_text_edit.setObjectName("cipher_text_edit")
        self.gridLayout.addWidget(self.cipher_text_edit, 1, 1, 1, 1)
        self.cipher_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cipher_text.setObjectName("cipher_text")
        self.gridLayout.addWidget(self.cipher_text, 0, 1, 1, 1)
        self.key_word_cipher_edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.key_word_cipher_edit.setObjectName("key_word_cipher_edit")
        self.gridLayout.addWidget(self.key_word_cipher_edit, 3, 0, 1, 1)
        self.decipher_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.decipher_button.setObjectName("decipher_button")
        self.gridLayout.addWidget(self.decipher_button, 4, 1, 1, 1)
        self.cipher_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cipher_button.setObjectName("cipher_button")
        self.gridLayout.addWidget(self.cipher_button, 4, 0, 1, 1)
        self.result_decipher = QtWidgets.QLabel(self.gridLayoutWidget)
        self.result_decipher.setObjectName("result_decipher")
        self.gridLayout.addWidget(self.result_decipher, 5, 1, 1, 1)
        self.key_cipher = QtWidgets.QLabel(self.gridLayoutWidget)
        self.key_cipher.setObjectName("key_cipher")
        self.gridLayout.addWidget(self.key_cipher, 2, 0, 1, 1)
        self.text_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_label.setObjectName("text_label")
        self.gridLayout.addWidget(self.text_label, 0, 0, 1, 1)
        self.result_cipher_browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.result_cipher_browser.setObjectName("result_cipher_browser")
        self.gridLayout.addWidget(self.result_cipher_browser, 6, 0, 1, 1)
        self.key_word_decipher_edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.key_word_decipher_edit.setObjectName("key_word_decipher_edit")
        self.gridLayout.addWidget(self.key_word_decipher_edit, 3, 1, 1, 1)
        self.result_cipher = QtWidgets.QLabel(self.gridLayoutWidget)
        self.result_cipher.setObjectName("result_cipher")
        self.gridLayout.addWidget(self.result_cipher, 5, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 7, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Viginer"))
        self.key_decipher_label.setText(_translate("MainWindow", "Key word"))
        self.cipher_text.setText(_translate("MainWindow", "Cipher text"))
        self.decipher_button.setText(_translate("MainWindow", "Decipher"))
        self.cipher_button.setText(_translate("MainWindow", "Cipher"))
        self.result_decipher.setText(_translate("MainWindow", "Result decipher"))
        self.key_cipher.setText(_translate("MainWindow", "Key word"))
        self.text_label.setText(_translate("MainWindow", "Text"))
        self.result_cipher.setText(_translate("MainWindow", "Result cipher"))
        self.error_label.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
