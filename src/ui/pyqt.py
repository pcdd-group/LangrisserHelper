# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 253)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo.ico"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_sweep = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_sweep.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_sweep.setFont(font)
        self.pushButton_sweep.setAutoFillBackground(False)
        self.pushButton_sweep.setStyleSheet("")
        self.pushButton_sweep.setCheckable(False)
        self.pushButton_sweep.setObjectName("pushButton_sweep")
        self.verticalLayout.addWidget(self.pushButton_sweep)
        self.pushButton_task = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_task.setFont(font)
        self.pushButton_task.setStyleSheet("")
        self.pushButton_task.setObjectName("pushButton_task")
        self.verticalLayout.addWidget(self.pushButton_task)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Langrisser Helper"))
        self.pushButton_sweep.setText(_translate("MainWindow", "扫荡秘境"))
        self.pushButton_task.setText(_translate("MainWindow", "每日任务"))
