# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 90, 361, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selected_scheduler = QtWidgets.QComboBox(
            self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selected_scheduler.setFont(font)
        self.selected_scheduler.setObjectName("selected_scheduler")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.horizontalLayout.addWidget(self.selected_scheduler)
        self.preemptive = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.preemptive.setFont(font)
        self.preemptive.setObjectName("preemptive")
        self.horizontalLayout.addWidget(self.preemptive)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(90, 190, 341, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.no_process = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.no_process.setObjectName("no_process")
        self.horizontalLayout_2.addWidget(self.no_process)
        self.Select = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Select.setFont(font)
        self.Select.setObjectName("Select")
        self.horizontalLayout_2.addWidget(self.Select)
        self.time_slice = QtWidgets.QLineEdit(self.centralwidget)
        self.time_slice.setGeometry(QtCore.QRect(240, 270, 113, 25))
        self.time_slice.setObjectName("time_slice")
        self.lb_time = QtWidgets.QLabel(self.centralwidget)
        self.lb_time.setGeometry(QtCore.QRect(90, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_time.setFont(font)
        self.lb_time.setObjectName("lb_time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.hide_show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Scheduler"))
        self.selected_scheduler.setItemText(
            0, _translate("MainWindow", "FCFS"))
        self.selected_scheduler.setItemText(
            1, _translate("MainWindow", "Round Robin"))
        self.selected_scheduler.setItemText(2, _translate("MainWindow", "SJF"))
        self.selected_scheduler.setItemText(
            3, _translate("MainWindow", "Priority"))
        self.preemptive.setText(_translate("MainWindow", "Preemptive"))
        self.label_2.setText(_translate("MainWindow", "Number of process"))
        self.Select.setText(_translate("MainWindow", "Select"))
        self.lb_time.setText(_translate("MainWindow", "Time slice"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.selected_scheduler.activated.connect(self.hide_show)

    def get_scheduler(self):
        index = self.selected_scheduler.currentIndex()
        return index

    def hide_show(self):
        i = self.get_scheduler()
        if i == 0:
            self.preemptive.hide()
            self.time_slice.hide()
            self.lb_time.hide()
        elif i == 1:
            self.preemptive.hide()
            self.time_slice.show()
            self.lb_time.show()
        elif i == 2:
            self.preemptive.show()
            self.time_slice.hide()
            self.lb_time.hide()
        elif i == 3:
            self.preemptive.show()
            self.time_slice.hide()
            self.lb_time.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
