# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProccessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ProccessTable.setGeometry(QtCore.QRect(180, 160, 425, 83))
        self.ProccessTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ProccessTable.setEditTriggers(
            QtWidgets.QAbstractItemView.AllEditTriggers)
        self.ProccessTable.setShowGrid(True)
        self.ProccessTable.setWordWrap(True)
        self.ProccessTable.setCornerButtonEnabled(True)
        self.ProccessTable.setObjectName("ProccessTable")
        self.ProccessTable.setColumnCount(4)
        self.ProccessTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(3, item)
        self.ProccessTable.horizontalHeader().setVisible(True)
        self.ShowHideBtn = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.ShowHideBtn.setGeometry(QtCore.QRect(300, 340, 166, 25))
        self.ShowHideBtn.setStandardButtons(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
        self.ShowHideBtn.setObjectName("ShowHideBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 440, 121, 20))
        self.label.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.ProccessTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "P1"))
        item = self.ProccessTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P2"))
        item = self.ProccessTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.ProccessTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.ProccessTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.ProccessTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
