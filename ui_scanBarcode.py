# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanBarcode.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(310, 20, 701, 55))
        self.label_14.setStyleSheet(" font: 75 30pt \"微软雅黑\";\n"
"color: rgb(255, 255, 0);\n"
"font-weight:bold;\n"
"\n"
" \n"
" ")
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gBoxCount_bad = QtWidgets.QGroupBox(self.centralwidget)
        self.gBoxCount_bad.setGeometry(QtCore.QRect(750, 160, 601, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gBoxCount_bad.sizePolicy().hasHeightForWidth())
        self.gBoxCount_bad.setSizePolicy(sizePolicy)
        self.gBoxCount_bad.setStyleSheet("\n"
"font:  22pt \"微软雅黑\";\n"
"font-weight:bold;\n"
"color: rgb(255, 85, 0);")
        self.gBoxCount_bad.setAlignment(QtCore.Qt.AlignCenter)
        self.gBoxCount_bad.setObjectName("gBoxCount_bad")
        self.lcdCount_bad = QtWidgets.QLCDNumber(self.gBoxCount_bad)
        self.lcdCount_bad.setGeometry(QtCore.QRect(10, 60, 500, 350))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.lcdCount_bad.sizePolicy().hasHeightForWidth())
        self.lcdCount_bad.setSizePolicy(sizePolicy)
        self.lcdCount_bad.setMinimumSize(QtCore.QSize(0, 0))
        self.lcdCount_bad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdCount_bad.setFont(font)
        self.lcdCount_bad.setStyleSheet("color: rgb(255, 0, 0);\n"
"border:none;")
        self.lcdCount_bad.setDigitCount(3)
        self.lcdCount_bad.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdCount_bad.setProperty("value", 100.0)
        self.lcdCount_bad.setProperty("intValue", 100)
        self.lcdCount_bad.setObjectName("lcdCount_bad")
        self.groupBox_4 = QtWidgets.QGroupBox(self.gBoxCount_bad)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 410, 411, 161))
        self.groupBox_4.setStyleSheet("font:  16pt \"微软雅黑\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_bad = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_bad.setEnabled(False)
        self.lineEdit_bad.setGeometry(QtCore.QRect(10, 50, 391, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bad.sizePolicy().hasHeightForWidth())
        self.lineEdit_bad.setSizePolicy(sizePolicy)
        self.lineEdit_bad.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEdit_bad.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lineEdit_bad.setStyleSheet("color: rgb(251, 251, 251);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25pt \"Arial Black\";\n"
" \n"
"border:none;\n"
"color: rgb(0, 0, 0);\n"
"text-align: center;\n"
"font-weight:bold;\n"
"")
        self.lineEdit_bad.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_bad.setObjectName("lineEdit_bad")
        self.groupBox_2 = QtWidgets.QGroupBox(self.gBoxCount_bad)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 410, 161, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("font:  16pt \"微软雅黑\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_badPack = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_badPack.setEnabled(False)
        self.lineEdit_badPack.setGeometry(QtCore.QRect(20, 30, 131, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_badPack.sizePolicy().hasHeightForWidth())
        self.lineEdit_badPack.setSizePolicy(sizePolicy)
        self.lineEdit_badPack.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_badPack.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lineEdit_badPack.setStyleSheet("border:none;\n"
"background-color: rgb(0,0,0);\n"
"font: 80pt \"黑体\";\n"
"color: rgb(249, 83, 0);\n"
"\n"
"")
        self.lineEdit_badPack.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_badPack.setObjectName("lineEdit_badPack")
        self.gBoxCount_good = QtWidgets.QGroupBox(self.centralwidget)
        self.gBoxCount_good.setGeometry(QtCore.QRect(10, 160, 731, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gBoxCount_good.sizePolicy().hasHeightForWidth())
        self.gBoxCount_good.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gBoxCount_good.setFont(font)
        self.gBoxCount_good.setStyleSheet("color: rgb(85, 255, 0);\n"
"font:  22pt \"微软雅黑\";\n"
"font-weight:bold;")
        self.gBoxCount_good.setAlignment(QtCore.Qt.AlignCenter)
        self.gBoxCount_good.setObjectName("gBoxCount_good")
        self.lcdCount_good = QtWidgets.QLCDNumber(self.gBoxCount_good)
        self.lcdCount_good.setGeometry(QtCore.QRect(10, 40, 600, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.lcdCount_good.sizePolicy().hasHeightForWidth())
        self.lcdCount_good.setSizePolicy(sizePolicy)
        self.lcdCount_good.setMinimumSize(QtCore.QSize(0, 0))
        self.lcdCount_good.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdCount_good.setFont(font)
        self.lcdCount_good.setStyleSheet("\n"
"color: rgb(0, 250, 0);\n"
"border:none;\n"
"\n"
"")
        self.lcdCount_good.setDigitCount(3)
        self.lcdCount_good.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdCount_good.setProperty("value", 500.0)
        self.lcdCount_good.setProperty("intValue", 500)
        self.lcdCount_good.setObjectName("lcdCount_good")
        self.groupBox_3 = QtWidgets.QGroupBox(self.gBoxCount_good)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 410, 461, 161))
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font:  16pt \"微软雅黑\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_good = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_good.setGeometry(QtCore.QRect(30, 60, 421, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_good.sizePolicy().hasHeightForWidth())
        self.lineEdit_good.setSizePolicy(sizePolicy)
        self.lineEdit_good.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEdit_good.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lineEdit_good.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25pt \"Arial Black\";\n"
" \n"
"border:none;\n"
"color: rgb(0, 0, 0);\n"
"text-align: center;\n"
"font-weight:bold;\n"
"")
        self.lineEdit_good.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_good.setObjectName("lineEdit_good")
        self.gBoxLingNum_good = QtWidgets.QGroupBox(self.gBoxCount_good)
        self.gBoxLingNum_good.setGeometry(QtCore.QRect(500, 410, 211, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gBoxLingNum_good.sizePolicy().hasHeightForWidth())
        self.gBoxLingNum_good.setSizePolicy(sizePolicy)
        self.gBoxLingNum_good.setMaximumSize(QtCore.QSize(16777215, 170))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.gBoxLingNum_good.setFont(font)
        self.gBoxLingNum_good.setStyleSheet("color: rgb(255, 255, 255);\n"
"font:  16pt \"微软雅黑\";\n"
"")
        self.gBoxLingNum_good.setObjectName("gBoxLingNum_good")
        self.lineEdit_goodPack = QtWidgets.QLineEdit(self.gBoxLingNum_good)
        self.lineEdit_goodPack.setEnabled(False)
        self.lineEdit_goodPack.setGeometry(QtCore.QRect(30, 40, 141, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_goodPack.sizePolicy().hasHeightForWidth())
        self.lineEdit_goodPack.setSizePolicy(sizePolicy)
        self.lineEdit_goodPack.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_goodPack.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lineEdit_goodPack.setStyleSheet("border:none;\n"
"color: rgb(0, 255, 0);\n"
"\n"
"font:90pt \"黑体\";\n"
"\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_goodPack.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_goodPack.setObjectName("lineEdit_goodPack")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 80, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setStyleSheet("font: 30pt \"Agency FB\";\n"
"color: rgb(255, 255, 0);\n"
"font-weight;bold;\n"
"")
        self.label_15.setObjectName("label_15")
        self.lb_operator = QtWidgets.QLabel(self.centralwidget)
        self.lb_operator.setGeometry(QtCore.QRect(260, 80, 271, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_operator.sizePolicy().hasHeightForWidth())
        self.lb_operator.setSizePolicy(sizePolicy)
        self.lb_operator.setStyleSheet("color:#ffffff;\n"
"font: 30pt \"Agency FB\";\n"
"font-weight:bold;")
        self.lb_operator.setObjectName("lb_operator")
        self.btnChangePaper = QtWidgets.QPushButton(self.centralwidget)
        self.btnChangePaper.setGeometry(QtCore.QRect(1010, 90, 121, 51))
        self.btnChangePaper.setStyleSheet("font: 25pt \"微软雅黑 light\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.846591, x2:0.949, y2:0.0568182, stop:0 rgba(100, 100, 100, 255), stop:0.994318 rgba(243, 243, 243, 255));\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
" \n"
"")
        self.btnChangePaper.setObjectName("btnChangePaper")
        self.btnSetup = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetup.setGeometry(QtCore.QRect(1170, 90, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetup.sizePolicy().hasHeightForWidth())
        self.btnSetup.setSizePolicy(sizePolicy)
        self.btnSetup.setMaximumSize(QtCore.QSize(200, 90))
        self.btnSetup.setStyleSheet("\n"
"font: 25pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.846591, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(243, 243, 243, 255));")
        self.btnSetup.setObjectName("btnSetup")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 140, 1321, 16))
        self.line.setStyleSheet("border-bottom: 1px solid #fff;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_14.raise_()
        self.layoutWidget.raise_()
        self.gBoxCount_bad.raise_()
        self.label_15.raise_()
        self.lb_operator.raise_()
        self.btnChangePaper.raise_()
        self.btnSetup.raise_()
        self.line.raise_()
        self.gBoxCount_good.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_14.setText(_translate("MainWindow", "钞 纸 人 工 选 纸 条 码 扫 描 系 统"))
        self.gBoxCount_bad.setTitle(_translate("MainWindow", "坏纸仓计数"))
        self.groupBox_4.setTitle(_translate("MainWindow", "坏纸条码："))
        self.lineEdit_bad.setPlaceholderText(_translate("MainWindow", "0000000000000000"))
        self.groupBox_2.setTitle(_translate("MainWindow", "令数"))
        self.lineEdit_badPack.setPlaceholderText(_translate("MainWindow", "00"))
        self.gBoxCount_good.setTitle(_translate("MainWindow", "好纸仓计数"))
        self.groupBox_3.setTitle(_translate("MainWindow", "好纸条码："))
        self.lineEdit_good.setPlaceholderText(_translate("MainWindow", "0000000000000000"))
        self.gBoxLingNum_good.setTitle(_translate("MainWindow", "令数"))
        self.lineEdit_goodPack.setPlaceholderText(_translate("MainWindow", "00"))
        self.label_15.setText(_translate("MainWindow", "操作人员："))
        self.lb_operator.setText(_translate("MainWindow", "张三"))
        self.btnChangePaper.setText(_translate("MainWindow", "换 纸"))
        self.btnSetup.setText(_translate("MainWindow", "设置"))


