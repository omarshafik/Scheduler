# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LiveSimulation.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
import math
import PyQt5
import time
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty, QSequentialAnimationGroup, QTimer
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFrame
from Scheduler import Scheduler
from proccessClass import Proccess


class TextLabel(QtWidgets.QLabel):
    def txt(self):
        try:
            return self.text()
        except:
            return ""

    def setTxt(self, str1):
        self.setText(str1)
    txt = QtCore.pyqtProperty(str, fget=txt, fset=setTxt)


class Ui_LiveSimulation(object):
    def setupUi(self, MainWindow, prefs):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProcessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ProcessTable.setGeometry(QtCore.QRect(30, 50, 471, 251))
        self.ProcessTable.setObjectName("ProcessTable")
        self.ProcessTable.setColumnCount(0)
        self.ProcessTable.setRowCount(0)
        self.newProcesccBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newProcesccBtn.setGeometry(QtCore.QRect(530, 210, 91, 31))
        self.newProcesccBtn.setObjectName("newProcesccBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 111, 20))
        self.label.setObjectName("label")
        self.insertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.insertBtn.setGeometry(QtCore.QRect(640, 210, 111, 31))
        self.insertBtn.setObjectName("insertBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(530, 260, 91, 31))
        self.stopBtn.setObjectName("stopBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(640, 260, 111, 31))
        self.clearBtn.setObjectName("clearBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 370, 121, 20))
        self.label_2.setObjectName("label_2")
        self.runningLabel = QtWidgets.QLabel(self.centralwidget)
        self.runningLabel.setGeometry(QtCore.QRect(130, 410, 71, 61))
        self.runningLabel.setObjectName("runningLabel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(476, 370, 91, 20))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(253, 360, 41, 161))
        self.line.setStyleSheet("color: rgb(239, 41, 41);\n"
                                "color: rgb(239, 41, 41);\n"
                                "font: 24pt \"Ubuntu\";\n"
                                "border-color: rgb(239, 41, 41);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.arrivalTime = 0
        self.pro_list = []
        self.output = []
        self.output_list = []
        self.readyQueue = []
        self.RunningGroup = QSequentialAnimationGroup()
        self.timer = QTimer()
        self.remaining = 0

        self.timer.timeout.connect(self.SetRunningLabel)
        self.stopBtn.clicked.connect(self.StopSimulation)
        self.newProcesccBtn.clicked.connect(self.insertRow)
        self.insertBtn.clicked.connect(self.ReadProccessTable)
        self.clearBtn.clicked.connect(self.ClearAll)

        self.algorithm = prefs["algorithm"]
        self.cnt = 2
        if self.algorithm == "Priority" or self.algorithm == "SJF":
            self.preemptive = prefs["preemptive"]
        if self.algorithm == "Priority":
            self.cnt = 3
        if self.algorithm == "Round Robin":
            self.quatum = prefs["time"]
        self.ProcessTable.setColumnCount(self.cnt)
        self.runningLabel.setStyleSheet("color: rgb(0, 0 , 0);\n"
                                        "background-color: rgb(200, 50, 30);")
        self.runningLabel.setAlignment(Qt.AlignCenter)
        self.ProcessTable.setHorizontalHeaderLabels(
            ["Name", "Duration", "Priority"])
        self.ProcessTable.setColumnWidth(0, 470/self.cnt)
        self.ProcessTable.setColumnWidth(1, 450/self.cnt)
        self.ProcessTable.setColumnWidth(2, 450/self.cnt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Simulation"))
        self.newProcesccBtn.setText(_translate("MainWindow", "New Process"))
        self.label.setText(_translate("MainWindow", "Processes Table"))
        self.insertBtn.setText(_translate("MainWindow", "Insert Selection"))
        self.stopBtn.setText(_translate("MainWindow", "Stop/Start"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Running Process"))
        self.runningLabel.setText(_translate("MainWindow", "NOP"))
        self.label_4.setText(_translate("MainWindow", "Ready Queue"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def StopSimulation(self):
        if not self.timer.isActive():
            self.timer.start(1000)
        else:
            self.timer.stop()

    def ClearAll(self):
        self.pro_list.clear()
        self.output.clear()
        self.output_list.clear()
        self.ProcessTable.setRowCount(0)
        for i in range(len(self.readyQueue)):
            self.readyQueue[i].clear()
            self.readyQueue[i].hide()
        self.readyQueue.clear()
        self.timer.stop()
        self.runningLabel.setText("NOP")

    def insertRow(self):
        self.ProcessTable.insertRow(self.ProcessTable.rowCount())

    def ReadProccessTable(self):
        rows = sorted(set(index.row() for index in
                          self.ProcessTable.selectedIndexes()))

        for row in rows:
            name = str(self.ProcessTable.item(row, 0).text())
            duration = int(self.ProcessTable.item(row, 1).text())
            priority = 0
            if self.algorithm == "Priority":
                priority = int(self.ProcessTable.item(row, 2).text())
            if name and duration > 0 and priority >= 0:
                for x in range(len(self.pro_list)):
                    if self.pro_list[x].name == name:
                        self.pro_list[x].duration += duration
                        break
                else:
                    self.pro_list.append(
                        Proccess(self.arrivalTime, duration, name, priority))

        self.setOutputs()
        # self.setReadyQueue()
        self.SetRunningLabel()

    def setOutputs(self):
        self.output.clear()
        self.output_list.clear()
        pList = copy.deepcopy(self.pro_list)
        if self.algorithm == "Priority" and self.preemptive:
            self.output = Scheduler().priority_preemptive(pList)
        elif self.algorithm == "Priority" and not self.preemptive:
            self.output = Scheduler().priority_nonpreemptive(pList)
        elif self.algorithm == "SJF" and self.preemptive:
            self.output = Scheduler().SJF_Preemptive(pList)
        elif self.algorithm == "SJF" and not self.preemptive:
            self.output = Scheduler().SJF_nonPreemptive(pList)
        elif self.algorithm == "Round Robin":
            self.output = Scheduler().roundRobin(pList, self.quatum)

        if len(self.output):
            prev_tSlot = self.output[0]
            duration = 0
            for tSlot in self.output:
                if(tSlot != prev_tSlot):
                    self.output_list.append(
                        {"Name": prev_tSlot, "duration": duration})
                    duration = 0
                duration += 1
                prev_tSlot = tSlot
            self.output_list.append({"Name": prev_tSlot, "duration": duration})

    def SetRunningLabel(self):

        brk = False
        self.setReadyQueue()
        for x in range(len(self.pro_list)):
            if self.pro_list[x].name == self.output[0]:
                self.pro_list[x].duration -= 1
                if self.pro_list[x].duration == 0:
                    self.pro_list.remove(self.pro_list[x])
                brk = True
                break
        if brk:
            self.runningLabel.setText(
                self.output[0]+"\n"+str(self.output_list[0]["duration"]))
            self.setOutputs()
            self.timer.start(1000)
        else:
            self.runningLabel.setText("NOP")

    def setReadyQueue(self):

        H = 20
        x = 320
        styles = {}
        for i in range(len(self.readyQueue)):
            self.readyQueue[i].clear()
            self.readyQueue[i].hide()
        self.readyQueue.clear()
        i = 0
        for burst in self.output_list:
            if burst == self.output_list[0]:
                continue
            if len(self.output_list) > 1:
                width = 450/(len(self.output_list)-1)
                self.readyQueue.append(QtWidgets.QLabel(
                    self.centralwidget))
                self.readyQueue[i].setGeometry(x, 410, width, H)
                self.readyQueue[i].setText(burst["Name"])
                self.readyQueue[i].setAlignment(Qt.AlignCenter)
                self.readyQueue[i].show()
                self.readyQueue.append(QtWidgets.QLabel(
                    self.centralwidget))
                self.readyQueue[i+1].setGeometry(x, 410+H, width, H)
                self.readyQueue[i+1].setText(str(burst["duration"]))
                self.readyQueue[i+1].setAlignment(Qt.AlignCenter)
                self.readyQueue[i+1].show()
                if not burst["Name"] in styles:
                    styles[burst["Name"]] = "background-color: rgb("+str((120+i*50) %
                                                                         256)+", "+str((90+i*70) % 256)+", "+str((220+i*40) % 256)+");"
                self.readyQueue[i].setStyleSheet(styles[burst["Name"]])
                self.readyQueue[i+1].setStyleSheet(styles[burst["Name"]])
                x += width
                i += 2
