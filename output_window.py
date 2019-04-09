# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from Priority import Scheduler
from proccessClass import Proccess

proccess_list = {Proccess(0, 5, "U1", 5), Proccess(
    2, 4, "U2", 3), Proccess(5, 5, "U3", 1), Proccess(5, 1, "U4", 2)}
ProccessCount = 4

output = Scheduler().priority_preemptive(proccess_list)

prevSlot = output[0]
output_list = []
duration = 0
for slot in output:
    if(slot != prevSlot):
        output_list.append({"Name": prevSlot, "duration": duration})
        duration = 0
    duration += 1
    prevSlot = slot
output_list.append({"Name": prevSlot, "duration": duration})

print(output)
print(output_list)


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
            QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.Gantt = QtWidgets.QTableWidget(self.centralwidget)
        self.Gantt.setGeometry(QtCore.QRect(35, 481, 741, 51))
        self.Gantt.setObjectName("Gantt")
        self.Gantt.setColumnCount(0)
        self.Gantt.setRowCount(0)
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

        self.modToInput()

    def modToInput(self):
        self.Gantt.setColumnCount(len(output_list))
        self.Gantt.setRowCount(2)
        ganttWidth = 741
        slotWidth = math.floor(ganttWidth / len(output)) - 1
        i = 0
        self.Gantt.verticalHeader().hide()
        self.Gantt.horizontalHeader().hide()
        self.Gantt.setRowHeight(0, self.Gantt.height()/2 - 1)
        self.Gantt.setRowHeight(1, self.Gantt.height()/2)
        for item in output_list:
            self.Gantt.setColumnWidth(i, slotWidth*item["duration"])
            self.Gantt.setItem(0, i, QTableWidgetItem(item["Name"]))
            self.Gantt.setItem(1, i, QTableWidgetItem(str(item["duration"])))
            i += 1
        self.Gantt.setColumnWidth(i-1, (slotWidth)*item["duration"] + 1)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())