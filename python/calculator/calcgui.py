# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 343, 170))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 2, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 5, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 7, 0, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 7, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 7, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_del = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.gridLayout.addWidget(self.pushButton_del, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 5, 0, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 7, 2, 1, 1)
        self.pushButton_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.gridLayout.addWidget(self.pushButton_mult, 2, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 341, 23))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 20))
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
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_del.setText(_translate("MainWindow", "CE"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_mult.setText(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
