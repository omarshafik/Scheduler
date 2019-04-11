# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scheduler(object):
    def setupUi(self, scheduler):
        scheduler.setObjectName("scheduler")
        scheduler.resize(540, 316)
        self.centralwidget = QtWidgets.QWidget(scheduler)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 259, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selected_scheduler = QtWidgets.QComboBox(self.centralwidget)
        self.selected_scheduler.setGeometry(QtCore.QRect(140, 60, 259, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selected_scheduler.setFont(font)
        self.selected_scheduler.setObjectName("selected_scheduler")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.preemptive = QtWidgets.QCheckBox(self.centralwidget)
        self.preemptive.setGeometry(QtCore.QRect(260, 30, 259, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.preemptive.setFont(font)
        self.preemptive.setObjectName("preemptive")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 173, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(170, 170, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.go.setFont(font)
        self.go.setObjectName("go")
        self.lb_time = QtWidgets.QLabel(self.centralwidget)
        self.lb_time.setGeometry(QtCore.QRect(140, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_time.setFont(font)
        self.lb_time.setObjectName("lb_time")
        self.no_process = QtWidgets.QSpinBox(self.centralwidget)
        self.no_process.setGeometry(QtCore.QRect(320, 100, 48, 26))
        self.no_process.setObjectName("no_process")
        self.t_slice = QtWidgets.QSpinBox(self.centralwidget)
        self.t_slice.setGeometry(QtCore.QRect(320, 130, 48, 26))
        self.t_slice.setObjectName("t_slice")
        scheduler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(scheduler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        scheduler.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(scheduler)
        self.toolBar.setObjectName("toolBar")
        scheduler.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(scheduler)
        QtCore.QMetaObject.connectSlotsByName(scheduler)

    def retranslateUi(self, scheduler):
        _translate = QtCore.QCoreApplication.translate
        scheduler.setWindowTitle(_translate("scheduler", "Process Scheduler"))
        self.label.setText(_translate("scheduler", " Scheduler"))
        self.selected_scheduler.setItemText(0, _translate("scheduler", "FCFS"))
        self.selected_scheduler.setItemText(1, _translate("scheduler", "Round Robin"))
        self.selected_scheduler.setItemText(2, _translate("scheduler", "SJF"))
        self.selected_scheduler.setItemText(3, _translate("scheduler", "Priority"))
        self.preemptive.setText(_translate("scheduler", "Preemptive"))
        self.label_2.setText(_translate("scheduler", "Number of process"))
        self.go.setText(_translate("scheduler", "done"))
        self.lb_time.setText(_translate("scheduler", "Time slice"))
        self.toolBar.setWindowTitle(_translate("scheduler", "toolBar"))
        self.selected_scheduler.activated.connect(self.hide_show)
        #self.no_process.valueChanged.connect(self.on_click)
       # self.t_slice.valueChanged.connect(self.get_t_slice)
        self.go.clicked.connect(self.on_click)
        self.preemptive.hide()
        self.t_slice.hide()
        self.lb_time.hide()
      
    

    
    def get_scheduler(self):
        index = self.selected_scheduler.currentIndex()
        return index
    def on_click(self):
        data ={"algorithim":self.selected_scheduler.currentText(),"Number":self.no_process.value(), "time":self.t_slice.value(), "preemptive":self.preemptive.isChecked()}
        print(data)

    
    def hide_show(self):
        i = self.get_scheduler()
        if i == 0:
            self.preemptive.hide()
            self.t_slice.hide()
            self.lb_time.hide()
        elif i == 1:
            self.preemptive.hide()
            self.t_slice.show()
            self.lb_time.show()
        elif i == 2:
            self.preemptive.show()
            self.t_slice.hide()
            self.lb_time.hide()
        elif i == 3:
            self.preemptive.show()
            self.t_slice.hide()
            self.lb_time.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scheduler = QtWidgets.QMainWindow()
    ui = Ui_scheduler()
    ui.setupUi(scheduler)
    scheduler.show()
    sys.exit(app.exec_())
