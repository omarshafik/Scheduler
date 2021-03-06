import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from new_output_window import Ui_OutputWindow
from SimulationWindow import Ui_LiveSimulation


class Ui_scheduler(object):
    def setupUi(self, scheduler):
        scheduler.setObjectName("scheduler")
        scheduler.resize(540, 316)
        self.centralwidget = QtWidgets.QWidget(scheduler)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 60, 259, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selected_scheduler = QtWidgets.QComboBox(self.centralwidget)
        self.selected_scheduler.setGeometry(QtCore.QRect(140, 100, 259, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selected_scheduler.setFont(font)
        self.selected_scheduler.setObjectName("selected_scheduler")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.selected_scheduler.addItem("")
        self.preemptive = QtWidgets.QCheckBox(self.centralwidget)
        self.preemptive.setGeometry(QtCore.QRect(260, 70, 259, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.preemptive.setFont(font)
        self.preemptive.setObjectName("preemptive")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 173, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(160, 210, 90, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.go.setFont(font)
        self.go.setObjectName("go")
        self.goLive = QtWidgets.QPushButton(self.centralwidget)
        self.goLive.setGeometry(QtCore.QRect(280, 210, 90, 27))
        self.goLive.setFont(font)
        self.goLive.setObjectName("goLive")
        self.lb_time = QtWidgets.QLabel(self.centralwidget)
        self.lb_time.setGeometry(QtCore.QRect(140, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_time.setFont(font)
        self.lb_time.setObjectName("lb_time")
        self.no_process = QtWidgets.QSpinBox(self.centralwidget)
        self.no_process.setGeometry(QtCore.QRect(320, 140, 48, 26))
        self.no_process.setMaximum(100000)
        self.no_process.setObjectName("no_process")
        self.t_slice = QtWidgets.QSpinBox(self.centralwidget)
        self.t_slice.setGeometry(QtCore.QRect(320, 170, 48, 26))
        self.t_slice.setObjectName("t_slice")

        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(110, 30, 440, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.error.setFont(font)
        self.error.setObjectName("error")

        scheduler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(scheduler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        scheduler.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(scheduler)
        self.toolBar.setObjectName("toolBar")
        scheduler.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.error.hide()
        self.goLive.clicked.connect(self.on_click_live)

        self.retranslateUi(scheduler)
        QtCore.QMetaObject.connectSlotsByName(scheduler)

    def retranslateUi(self, scheduler):
        _translate = QtCore.QCoreApplication.translate
        scheduler.setWindowTitle(_translate("scheduler", "Process Scheduler"))
        self.label.setText(_translate("scheduler", " Scheduler"))
        self.selected_scheduler.setItemText(0, _translate("scheduler", "FCFS"))
        self.selected_scheduler.setItemText(
            1, _translate("scheduler", "Round Robin"))
        self.selected_scheduler.setItemText(2, _translate("scheduler", "SJF"))
        self.selected_scheduler.setItemText(
            3, _translate("scheduler", "Priority"))
        self.preemptive.setText(_translate("scheduler", "Preemptive"))
        self.label_2.setText(_translate("scheduler", "Number of process"))
        self.go.setText(_translate("scheduler", "Done"))
        self.goLive.setText(_translate("scheduler", "Live"))
        self.lb_time.setText(_translate("scheduler", "Time slice"))
        self.toolBar.setWindowTitle(_translate("scheduler", "toolBar"))
        self.selected_scheduler.activated.connect(self.hide_show)
        self.go.clicked.connect(self.on_click)
        self.preemptive.hide()
        self.t_slice.hide()
        self.lb_time.hide()

    def get_scheduler(self):
        index = self.selected_scheduler.currentIndex()
        return index

    def on_click(self):
        process_no = self.no_process.value()
        time_slice = self.t_slice.value()
        scheduler = self.selected_scheduler.currentText()
        data = {"algorithm": scheduler, "Number": process_no,
                "time": time_slice, "preemptive": self.preemptive.isChecked()}
        if(process_no == 0):
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate(
                "scheduler", "<font color='red'>Number of processes must be greater than 0 </font>"))
            self.error.show()
        elif(time_slice == 0 and scheduler == "Round Robin"):
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate(
                "scheduler", "<font color='red'> Time slice must be greater than 0 </font>"))
            self.error.show()
        else:
            self.error.hide()
            self.OutputWindow = QtWidgets.QMainWindow()
            self.outui = Ui_OutputWindow(data)
            self.outui.setupUi(self.OutputWindow, data)
            self.OutputWindow.show()

    def on_click_live(self):
        time_slice = self.t_slice.value()
        scheduler = self.selected_scheduler.currentText()
        data = {"algorithm": scheduler,
                "time": time_slice, "preemptive": self.preemptive.isChecked()}

        if(time_slice == 0 and scheduler == "Round Robin"):
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate(
                "scheduler", "<font color='red'> Time slice must be greater than 0 </font>"))
            self.error.show()
        # elif not scheduler == "Round Robin":
        else:
            self.error.hide()
            self.LiveSimulation = QtWidgets.QMainWindow()
            self.outui = Ui_LiveSimulation()
            self.outui.setupUi(self.LiveSimulation, data)
            self.LiveSimulation.show()

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
