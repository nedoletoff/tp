# Form implementation generated from reading ui file 'main_design.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menulab1 = QtWidgets.QMenu(self.menubar)
        self.menulab1.setObjectName("menulab1")
        self.menulab1_2 = QtWidgets.QMenu(self.menulab1)
        self.menulab1_2.setObjectName("menulab2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionp2_2 = QtGui.QAction(MainWindow)
        self.actionp2_2.setObjectName("actionp2_2")
        self.actionp1_1 = QtGui.QAction(MainWindow)
        self.actionp1_1.setObjectName("actionp1_1")
        self.actionp1_2 = QtGui.QAction(MainWindow)
        self.actionp1_2.setObjectName("actionp1_2")
        self.menulab1_2.addAction(self.actionp1_1)
        self.menulab1_2.addAction(self.actionp1_2)
        self.menulab1.addAction(self.menulab1_2.menuAction())
        self.menulab1.addAction(self.actionp2_2)
        self.menubar.addAction(self.menulab1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menulab1.setTitle(_translate("MainWindow", "labs"))
        self.menulab1_2.setTitle(_translate("MainWindow", "lab1"))
        self.actionp2_2.setText(_translate("MainWindow", "lab2"))
        self.actionp1_1.setText(_translate("MainWindow", "part 1"))
        self.actionp1_2.setText(_translate("MainWindow", "part 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())