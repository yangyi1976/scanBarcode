# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pickuppaper.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PickupPaperDlg(object):
    def setupUi(self, PickupPaperDlg):
        PickupPaperDlg.setObjectName("PickupPaperDlg")
        PickupPaperDlg.resize(1099, 619)
        self.lineEdit_firstID = QtWidgets.QLineEdit(PickupPaperDlg)
        self.lineEdit_firstID.setGeometry(QtCore.QRect(220, 200, 411, 71))
        self.lineEdit_firstID.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 32pt \"黑体\";\n"
"text-align: center;\n"
"\n"
"font-weight:bold;")
        self.lineEdit_firstID.setObjectName("lineEdit_firstID")
        self.lineEdit_endID = QtWidgets.QLineEdit(PickupPaperDlg)
        self.lineEdit_endID.setGeometry(QtCore.QRect(230, 450, 401, 71))
        self.lineEdit_endID.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 32pt \"黑体\";\n"
"text-align: center;\n"
"\n"
"font-weight:bold;")
        self.lineEdit_endID.setObjectName("lineEdit_endID")
        self.label_10 = QtWidgets.QLabel(PickupPaperDlg)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 181, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(" \n"
"font: 34pt \"黑体\";\n"
"color: rgb(0, 255, 0);\n"
"font-weight:bold;")
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(PickupPaperDlg)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(10, 450, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(" \n"
"font: 34pt \"黑体\";\n"
"color: rgb(0, 255, 0);\n"
"font-weight:bold;")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(PickupPaperDlg)
        self.groupBox_2.setGeometry(QtCore.QRect(650, 130, 441, 461))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("\n"
"color: rgb(75, 226, 110);\n"
"")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lcd_betweenCount = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcd_betweenCount.setGeometry(QtCore.QRect(20, 70, 411, 350))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_betweenCount.sizePolicy().hasHeightForWidth())
        self.lcd_betweenCount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_betweenCount.setFont(font)
        self.lcd_betweenCount.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcd_betweenCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd_betweenCount.setStyleSheet("color: rgb(0, 255, 0);")
        self.lcd_betweenCount.setDigitCount(3)
        self.lcd_betweenCount.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_betweenCount.setObjectName("lcd_betweenCount")
        self.line = QtWidgets.QFrame(PickupPaperDlg)
        self.line.setGeometry(QtCore.QRect(60, 100, 1011, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(PickupPaperDlg)
        self.label.setGeometry(QtCore.QRect(310, 20, 491, 81))
        self.label.setStyleSheet("font: 75 36pt \"微软雅黑\";\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.lb_firstTip = QtWidgets.QLabel(PickupPaperDlg)
        self.lb_firstTip.setGeometry(QtCore.QRect(230, 290, 391, 41))
        self.lb_firstTip.setStyleSheet("font: 30pt \"黑体\";\n"
"color: rgb(255, 0, 0);\n"
" ")
        self.lb_firstTip.setText("")
        self.lb_firstTip.setObjectName("lb_firstTip")
        self.lb_endTip = QtWidgets.QLabel(PickupPaperDlg)
        self.lb_endTip.setGeometry(QtCore.QRect(240, 530, 391, 41))
        self.lb_endTip.setStyleSheet("font: 30pt \"黑体\";\n"
"color: rgb(255, 0, 0);\n"
" ")
        self.lb_endTip.setText("")
        self.lb_endTip.setObjectName("lb_endTip")

        self.retranslateUi(PickupPaperDlg)
        QtCore.QMetaObject.connectSlotsByName(PickupPaperDlg)

    def retranslateUi(self, PickupPaperDlg):
        _translate = QtCore.QCoreApplication.translate
        PickupPaperDlg.setWindowTitle(_translate("PickupPaperDlg", "Dialog"))
        self.label_10.setText(_translate("PickupPaperDlg", "首张ID："))
        self.label_11.setText(_translate("PickupPaperDlg", "末张ID："))
        self.groupBox_2.setTitle(_translate("PickupPaperDlg", "预期张数："))
        self.label.setText(_translate("PickupPaperDlg", "拣 出 未 扫 码 纸 张  "))


