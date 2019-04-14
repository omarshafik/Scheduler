# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
import math
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from Scheduler import Scheduler
from proccessClass import Proccess
from copy import deepcopy

# proccess_list = {Proccess(0, 5, "U1", 5), Proccess(
#     2, 4, "U2", 3), Proccess(5, 5, "U3", 1), Proccess(5, 1, "U4", 2)}
# ProccessCount = 4

# output = Scheduler().priority_nonpreemptive(proccess_list)

# prevSlot = output[0]
# output_list = []
# duration = 0
# for slot in output:
#     if(slot != prevSlot):
#         output_list.append({"Name": prevSlot, "duration": duration})
#         duration = 0
#     duration += 1
#     prevSlot = slot
# output_list.append({"Name": prevSlot, "duration": duration})

# print(output)
# print(output_list)

# pref = {"algorithm": "preemptive", "ProccessNum": 2}


class Ui_OutputWindow(object):
    def __init__(self, prefs):
        self.prefs = prefs

    def setupUi(self, MainWindow, x):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        if(x['algorithm'] == "Priority"):
            cols = 4
        else:
            cols = 3
        if(x['Number'] < 6):
            height = 25*x['Number']+23
            scroll = 0
        else:
            height = 148
            scroll = 14
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProccessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ProccessTable.setGeometry(
            QtCore.QRect(180, 160, 90*cols+25+scroll, height))
        self.ProccessTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ProccessTable.setEditTriggers(
            QtWidgets.QAbstractItemView.AllEditTriggers)
        self.ProccessTable.setShowGrid(True)
        self.ProccessTable.setWordWrap(True)
        self.ProccessTable.setCornerButtonEnabled(True)
        self.ProccessTable.setObjectName("ProccessTable")
        self.ProccessTable.setColumnCount(cols)
        self.ProccessTable.setRowCount(x['Number'])
        i = 0
        while(i < x['Number']):
            item = QtWidgets.QTableWidgetItem()
            self.ProccessTable.setVerticalHeaderItem(i, item)
            i = i + 1
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProccessTable.setHorizontalHeaderItem(2, item)
        if(x['algorithm'] == "Priority"):
            item = QtWidgets.QTableWidgetItem()
            self.ProccessTable.setHorizontalHeaderItem(3, item)
        self.ProccessTable.horizontalHeader().setVisible(True)
        self.Gantt = QtWidgets.QTableWidget(self.centralwidget)
        self.Gantt.setGeometry(QtCore.QRect(35, 481, 741, 51))
        self.Gantt.setObjectName("Gantt")
        self.Gantt.setColumnCount(0)
        self.Gantt.setRowCount(0)
        self.Gantt.horizontalHeader().setHighlightSections(False)
        self.ShowHideBtn = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.ShowHideBtn.setGeometry(QtCore.QRect(300, 340, 166, 25))
        self.ShowHideBtn.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.ShowHideBtn.setObjectName("ShowHideBtn")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 380, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(140, 425, 400, 25))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(185, 105, 440, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.error.setFont(font)
        self.error.setStyleSheet("color: red")
        self.error.setObjectName("error")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, x)

        self.Gantt.hide()
        self.label.hide()
        self.label2.hide()
        self.error.hide()
        self.ShowHideBtn.accepted.connect(self.SetGantt)
        self.ShowHideBtn.rejected.connect(self.ResetGantt)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Gantt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Gantt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def ReadProccessTable(self):
        prefs = self.prefs
        count = prefs["Number"]
        alg = prefs["algorithm"]
        pro_list = []
        error = ""
        for row in range(count):
            name = str(self.ProccessTable.item(row, 0).text())
            if(name == ""):
                error = "Process name is required"
                break
            arrival_time = self.ProccessTable.item(row, 1).text()
            duration = self.ProccessTable.item(row, 2).text()
            priority = "1"
            if(alg == "Priority"):
                priority = self.ProccessTable.item(row, 3).text()
            if(not arrival_time.isdigit()):
                error = name + " arrival time must be >= 0"
                break
            elif(not duration.isdigit()):
                error = name + " duration must be a postive integer"
                break
            elif(not priority.isdigit()):
                error = name + " priority must be a postive integer"
                break
            else:
                arrival_time = int(arrival_time)
                duration = int(duration)
                priority = int(priority)
            if(arrival_time < 0):
                error = name + " arrival time must be >= 0"
                break
            elif (duration <= 0):
                error = name + " duration must be a postive integer"
                break
            elif (priority <= 0):
                error = name + " priority must be a postive integer"
                break
            else:#name and arrival_time >= 0 and duration > 0 and priority >= 0:
                pro_list.append(
                    Proccess(int(arrival_time), int(duration), name, int(priority)))
        processes = []
        processes = deepcopy(pro_list)
        out = []
        out_list = []
        if(error == ""):
            if alg == "Priority" and prefs["preemptive"]:
                out = Scheduler().priority_preemptive(pro_list)
            elif alg == "Priority" and not prefs["preemptive"]:
                out = Scheduler().priority_nonpreemptive(pro_list)
            elif alg == "SJF" and prefs["preemptive"]:
                out = Scheduler().SJF_Preemptive(pro_list)
            elif alg == "SJF" and not prefs["preemptive"]:
                out = Scheduler().SJF_nonPreemptive(pro_list)
            elif alg == "Round Robin":
                out = Scheduler().roundRobin(pro_list, prefs["time"])

            prev_tSlot = out[0]
            duration = 0
            for tSlot in out:
                if(tSlot != prev_tSlot):
                    out_list.append({"Name": prev_tSlot, "duration": duration})
                    duration = 0
                duration += 1
                prev_tSlot = tSlot
            out_list.append({"Name": prev_tSlot, "duration": duration})
        return out, out_list , processes , error

    def ResetGantt(self):
        self.ProccessTable.setEditTriggers(
            QtWidgets.QAbstractItemView.AllEditTriggers)
        self.Gantt.clear()
        self.Gantt.hide()
        self.label.hide()
        self.label2.hide()
        self.error.hide()

    def SetGantt(self):
        self.ProccessTable.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        output, output_list, pro_list, error = self.ReadProccessTable()
        if(error != ""):
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate("MainWindow", error))
            self.error.show()
        else:
            avg_TAT = 0
            avg_WT = 0
            avg_TAT, avg_WT= Scheduler().average_TAT_WT(output, pro_list)
            self.Gantt.setColumnCount(len(output_list))
            self.Gantt.setRowCount(2)
            ganttWidth = self.Gantt.width()
            slotWidth = math.ceil(ganttWidth / len(output))
            i = 0
            self.Gantt.setFixedWidth(
                math.ceil(slotWidth*len(output)))
            self.Gantt.verticalHeader().hide()
            self.Gantt.horizontalHeader().hide()
            self.Gantt.setRowHeight(0, self.Gantt.height()/2 - 1)
            self.Gantt.setRowHeight(1, self.Gantt.height()/2)
            for item in output_list:
                self.Gantt.setColumnWidth(i, slotWidth*item["duration"] - 4)
                self.Gantt.setItem(0, i, QTableWidgetItem(item["Name"]))
                self.Gantt.setItem(1, i, QTableWidgetItem(str(item["duration"])))
                i += 1
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("MainWindow", " average waiting time = " + str(avg_WT)))
            self.label2.setText(_translate("MainWindow", " average turn around time = " + str(avg_TAT)))
            self.label.show()
            self.label2.show()
            self.Gantt.show()

    def retranslateUi(self, MainWindow, dict):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Output View"))
        i = 0
        while(i < dict['Number']):
            item = self.ProccessTable.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", "P"+str(i)))
            self.ProccessTable.setRowHeight(i, 25)
            i = i + 1
        item = self.ProccessTable.horizontalHeaderItem(0)
        self.ProccessTable.setColumnWidth(0, 90)
        item.setText(_translate("MainWindow", "Name"))
        item = self.ProccessTable.horizontalHeaderItem(1)
        self.ProccessTable.setColumnWidth(1, 90)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.ProccessTable.horizontalHeaderItem(2)
        self.ProccessTable.setColumnWidth(2, 90)
        item.setText(_translate("MainWindow", "Duration"))
        if(dict['algorithm'] == "Priority"):
            item = self.ProccessTable.horizontalHeaderItem(3)
            self.ProccessTable.setColumnWidth(3, 90)
            item.setText(_translate("MainWindow", "Priority"))
