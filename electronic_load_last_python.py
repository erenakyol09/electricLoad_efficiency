# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/gitProject/v5_EL/electronic_load_last.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ELECTRONICLOAD(object):
    def setupUi(self, ELECTRONICLOAD):
        ELECTRONICLOAD.setObjectName("ELECTRONICLOAD")
        ELECTRONICLOAD.resize(1394, 915)
        ELECTRONICLOAD.setStyleSheet("background-color: rgb(0, 132, 193);")
        ELECTRONICLOAD.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(ELECTRONICLOAD)
        self.pushButton.setGeometry(QtCore.QRect(1280, 20, 93, 21))
        self.pushButton.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ELECTRONICLOAD)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 50, 93, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayoutWidget = QtWidgets.QWidget(ELECTRONICLOAD)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1070, 20, 165, 72))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser.setGeometry(QtCore.QRect(1070, 140, 301, 161))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(ELECTRONICLOAD)
        self.lineEdit.setGeometry(QtCore.QRect(1070, 110, 221, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(ELECTRONICLOAD)
        self.pushButton_3.setGeometry(QtCore.QRect(1300, 110, 71, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_15 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_15.setGeometry(QtCore.QRect(1070, 610, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_16.setGeometry(QtCore.QRect(1070, 650, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_18.setGeometry(QtCore.QRect(1090, 380, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_22.setGeometry(QtCore.QRect(1070, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_23.setGeometry(QtCore.QRect(1070, 450, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_24.setGeometry(QtCore.QRect(1070, 490, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_25.setGeometry(QtCore.QRect(1070, 530, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_26.setGeometry(QtCore.QRect(1070, 570, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_17 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_17.setGeometry(QtCore.QRect(1070, 730, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_20.setGeometry(QtCore.QRect(1070, 770, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_21.setGeometry(QtCore.QRect(1090, 700, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.tab1_load = QtWidgets.QTabWidget(ELECTRONICLOAD)
        self.tab1_load.setGeometry(QtCore.QRect(20, 20, 1021, 881))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tab1_load.setFont(font)
        self.tab1_load.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.tab1_load.setObjectName("tab1_load")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 70, 73, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 40, 73, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(100, 40, 131, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(100, 10, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 40, 101, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(250, 10, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 70, 131, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 70, 101, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(10, 130, 991, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(166, 190, 200);")
        self.label_32.setFrameShape(QtWidgets.QFrame.Box)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.pushButton_10.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 170, 91, 41))
        self.pushButton_11.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(300, 170, 91, 41))
        self.pushButton_12.setStyleSheet("background-color: rgb(112, 181, 200);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(780, 30, 221, 91))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(790, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.graphicsView = PlotWidget(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(10, 230, 491, 301))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(810, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(900, 160, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.graphicsView_2 = PlotWidget(self.tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 540, 491, 301))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = PlotWidget(self.tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(510, 230, 491, 301))
        self.graphicsView_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = PlotWidget(self.tab)
        self.graphicsView_4.setGeometry(QtCore.QRect(510, 540, 491, 301))
        self.graphicsView_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.tab1_load.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab1_load.addTab(self.tab_2, "")
        self.label_19 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_19.setGeometry(QtCore.QRect(1070, 810, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_27 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_27.setGeometry(QtCore.QRect(1070, 850, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.lcdNumber = QtWidgets.QLCDNumber(ELECTRONICLOAD)
        self.lcdNumber.setGeometry(QtCore.QRect(1070, 320, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setDigitCount(21)
        self.lcdNumber.setObjectName("lcdNumber")
        self.textBrowser_3 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_3.setGeometry(QtCore.QRect(1160, 410, 211, 41))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_4.setGeometry(QtCore.QRect(1160, 450, 211, 41))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_5.setGeometry(QtCore.QRect(1160, 490, 211, 41))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_6.setGeometry(QtCore.QRect(1160, 530, 211, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_7.setGeometry(QtCore.QRect(1160, 570, 211, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_8.setGeometry(QtCore.QRect(1160, 610, 211, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_9.setGeometry(QtCore.QRect(1160, 650, 211, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_10.setGeometry(QtCore.QRect(1160, 730, 211, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_11.setGeometry(QtCore.QRect(1160, 770, 211, 41))
        self.textBrowser_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_12.setGeometry(QtCore.QRect(1160, 810, 211, 41))
        self.textBrowser_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(ELECTRONICLOAD)
        self.textBrowser_13.setGeometry(QtCore.QRect(1160, 850, 211, 41))
        self.textBrowser_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.label_10 = QtWidgets.QLabel(ELECTRONICLOAD)
        self.label_10.setGeometry(QtCore.QRect(1140, 80, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.tab1_load.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.formLayoutWidget.raise_()
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.pushButton_3.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_19.raise_()
        self.label_27.raise_()
        self.lcdNumber.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_5.raise_()
        self.textBrowser_6.raise_()
        self.textBrowser_7.raise_()
        self.textBrowser_8.raise_()
        self.textBrowser_9.raise_()
        self.textBrowser_10.raise_()
        self.textBrowser_11.raise_()
        self.textBrowser_12.raise_()
        self.textBrowser_13.raise_()
        self.label_10.raise_()

        self.retranslateUi(ELECTRONICLOAD)
        self.tab1_load.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ELECTRONICLOAD)

    def retranslateUi(self, ELECTRONICLOAD):
        _translate = QtCore.QCoreApplication.translate
        ELECTRONICLOAD.setWindowTitle(_translate("ELECTRONICLOAD", "ELECTRONIC LOAD"))
        self.pushButton.setText(_translate("ELECTRONICLOAD", "CONNECT"))
        self.pushButton_2.setText(_translate("ELECTRONICLOAD", "STOP"))
        self.comboBox.setItemText(0, _translate("ELECTRONICLOAD", "COM4"))
        self.comboBox.setItemText(1, _translate("ELECTRONICLOAD", "COM5"))
        self.comboBox.setItemText(2, _translate("ELECTRONICLOAD", "COM6"))
        self.comboBox.setItemText(3, _translate("ELECTRONICLOAD", "COM7"))
        self.label.setText(_translate("ELECTRONICLOAD", "BaudRate"))
        self.comboBox_2.setItemText(0, _translate("ELECTRONICLOAD", "115200"))
        self.comboBox_2.setItemText(1, _translate("ELECTRONICLOAD", "57600"))
        self.comboBox_2.setItemText(2, _translate("ELECTRONICLOAD", "38400"))
        self.comboBox_2.setItemText(3, _translate("ELECTRONICLOAD", "19200"))
        self.comboBox_2.setItemText(4, _translate("ELECTRONICLOAD", "9600"))
        self.comboBox_2.setItemText(5, _translate("ELECTRONICLOAD", "1200"))
        self.label_2.setText(_translate("ELECTRONICLOAD", "PORT"))
        self.pushButton_3.setText(_translate("ELECTRONICLOAD", "SEND"))
        self.label_15.setText(_translate("ELECTRONICLOAD", "DC CURRENT"))
        self.label_16.setText(_translate("ELECTRONICLOAD", "DC VOLTAGE"))
        self.label_18.setText(_translate("ELECTRONICLOAD", "POWER ANALYZER"))
        self.label_22.setText(_translate("ELECTRONICLOAD", "P"))
        self.label_23.setText(_translate("ELECTRONICLOAD", "Vrms"))
        self.label_24.setText(_translate("ELECTRONICLOAD", "Irms"))
        self.label_25.setText(_translate("ELECTRONICLOAD", "pf"))
        self.label_26.setText(_translate("ELECTRONICLOAD", "FREQUENCY"))
        self.label_17.setText(_translate("ELECTRONICLOAD", "POWER"))
        self.label_20.setText(_translate("ELECTRONICLOAD", "VOLTAGE"))
        self.label_21.setText(_translate("ELECTRONICLOAD", "ELECTRONIC LOAD"))
        self.pushButton_4.setText(_translate("ELECTRONICLOAD", "SEND"))
        self.comboBox_3.setItemText(0, _translate("ELECTRONICLOAD", "A"))
        self.comboBox_3.setItemText(1, _translate("ELECTRONICLOAD", "B"))
        self.comboBox_3.setItemText(2, _translate("ELECTRONICLOAD", "C"))
        self.label_3.setText(_translate("ELECTRONICLOAD", "COMMAND"))
        self.comboBox_4.setItemText(0, _translate("ELECTRONICLOAD", "Constant Current"))
        self.comboBox_4.setItemText(1, _translate("ELECTRONICLOAD", "Constant Voltage"))
        self.comboBox_4.setItemText(2, _translate("ELECTRONICLOAD", "Constant Power"))
        self.comboBox_4.setItemText(3, _translate("ELECTRONICLOAD", "Constant Resistor"))
        self.label_4.setText(_translate("ELECTRONICLOAD", "MODE"))
        self.label_7.setText(_translate("ELECTRONICLOAD", "VALUE"))
        self.pushButton_5.setText(_translate("ELECTRONICLOAD", "SEND"))
        self.pushButton_6.setText(_translate("ELECTRONICLOAD", "SEND"))
        self.label_32.setText(_translate("ELECTRONICLOAD", "GRAPHICS"))
        self.pushButton_10.setText(_translate("ELECTRONICLOAD", "RUN"))
        self.pushButton_11.setText(_translate("ELECTRONICLOAD", "STOP"))
        self.pushButton_12.setText(_translate("ELECTRONICLOAD", "REFRESH"))
        self.textBrowser_2.setHtml(_translate("ELECTRONICLOAD", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("ELECTRONICLOAD", "Connected Device Info:"))
        self.label_9.setText(_translate("ELECTRONICLOAD", "TIME:"))
        self.tab1_load.setTabText(self.tab1_load.indexOf(self.tab), _translate("ELECTRONICLOAD", "Electronic Load"))
        self.tab1_load.setTabText(self.tab1_load.indexOf(self.tab_2), _translate("ELECTRONICLOAD", "Power Analyzer"))
        self.label_19.setText(_translate("ELECTRONICLOAD", "CURRENT"))
        self.label_27.setText(_translate("ELECTRONICLOAD", "RESISTOR"))

from pyqtgraph import PlotWidget
