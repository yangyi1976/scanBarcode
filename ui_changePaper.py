# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePaper.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePaperDlg(object):
    def setupUi(self, ChangePaperDlg):
        ChangePaperDlg.setObjectName("ChangePaperDlg")
        ChangePaperDlg.setEnabled(True)
        ChangePaperDlg.resize(1280, 768)
        ChangePaperDlg.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(ChangePaperDlg)
        self.groupBox.setGeometry(QtCore.QRect(80, 120, 1051, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 85, 0);\n"
" \n"
" \n"
" \n"
"\n"
"font: 24pt \"微软雅黑\";\n"
"font-weight:bold;\n"
" ")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 91, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 85, 0);\n"
"font: 30pt \"微软雅黑\";\n"
"font-weight:bold;")
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.comboBadID = QtWidgets.QComboBox(self.groupBox)
        self.comboBadID.setGeometry(QtCore.QRect(110, 60, 431, 61))
        self.comboBadID.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBadID.setStyleSheet("color: rgb(53, 53, 53);\n"
"background-color: rgb(240, 240, 240);\n"
"border:1px solid rgb(200, 200,200);\n"
"font: 30pt \"黑体\";\n"
"\n"
"text-align: center;\n"
"\n"
"font-weight:bold;")
        self.comboBadID.setEditable(False)
        self.comboBadID.setObjectName("comboBadID")
        self.label_badnum = QtWidgets.QLabel(self.groupBox)
        self.label_badnum.setEnabled(True)
        self.label_badnum.setGeometry(QtCore.QRect(600, 50, 151, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_badnum.sizePolicy().hasHeightForWidth())
        self.label_badnum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_badnum.setFont(font)
        self.label_badnum.setStyleSheet("color: rgb(255, 85, 0);\n"
"font: 30pt \"微软雅黑\";\n"
"font-weight:bold;")
        self.label_badnum.setTextFormat(QtCore.Qt.PlainText)
        self.label_badnum.setIndent(0)
        self.label_badnum.setObjectName("label_badnum")
        self.lcdBadNum = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdBadNum.setGeometry(QtCore.QRect(810, 29, 200, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdBadNum.setFont(font)
        self.lcdBadNum.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcdBadNum.setDigitCount(3)
        self.lcdBadNum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdBadNum.setObjectName("lcdBadNum")
        self.groupBox_2 = QtWidgets.QGroupBox(ChangePaperDlg)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 300, 1051, 401))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("\n"
"color: rgb(75, 226, 110);\n"
" \n"
"font: 24pt \"微软雅黑\";\n"
"font-weight:bold;\n"
" \n"
" ")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 81, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 30pt \"微软雅黑\";\n"
"font-weight:bold")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.label_NewNum = QtWidgets.QLabel(self.groupBox_2)
        self.label_NewNum.setEnabled(True)
        self.label_NewNum.setGeometry(QtCore.QRect(610, 30, 141, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_NewNum.sizePolicy().hasHeightForWidth())
        self.label_NewNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_NewNum.setFont(font)
        self.label_NewNum.setStyleSheet("font: 32pt \"微软雅黑\";\n"
"font-weight:bold;")
        self.label_NewNum.setTextFormat(QtCore.Qt.PlainText)
        self.label_NewNum.setIndent(0)
        self.label_NewNum.setObjectName("label_NewNum")
        self.lcdNewNum = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNewNum.setGeometry(QtCore.QRect(750, 60, 271, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNewNum.sizePolicy().hasHeightForWidth())
        self.lcdNewNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdNewNum.setFont(font)
        self.lcdNewNum.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcdNewNum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNewNum.setStyleSheet("")
        self.lcdNewNum.setDigitCount(3)
        self.lcdNewNum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNewNum.setObjectName("lcdNewNum")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 501, 271))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(31, 31, 31);")
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(490)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(31)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(27)
        self.comboNewID = QtWidgets.QComboBox(self.groupBox_2)
        self.comboNewID.setGeometry(QtCore.QRect(110, 60, 431, 61))
        self.comboNewID.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboNewID.setStyleSheet("color: rgb(53, 53, 53);\n"
"background-color: rgb(240, 240, 240);\n"
"border:1px solid rgb(200, 200,200);\n"
"font: 30pt \"黑体\";\n"
"\n"
"text-align: center;\n"
"\n"
"font-weight:bold;")
        self.comboNewID.setEditable(False)
        self.comboNewID.setObjectName("comboNewID")
        self.btnEnd = QtWidgets.QPushButton(ChangePaperDlg)
        self.btnEnd.setEnabled(True)
        self.btnEnd.setGeometry(QtCore.QRect(420, 710, 131, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnEnd.setFont(font)
        self.btnEnd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnEnd.setStyleSheet("#btnEnd { \n"
"font: 20pt \'微软雅黑\';\n"
"background-color: #67C23A;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4px;border:1px solid #aaa }\n"
"#btnEnd:Pressed {background-color: #66EE23;}")
        self.btnEnd.setObjectName("btnEnd")
        self.btnCannotScan = QtWidgets.QPushButton(ChangePaperDlg)
        self.btnCannotScan.setGeometry(QtCore.QRect(620, 710, 201, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCannotScan.setFont(font)
        self.btnCannotScan.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCannotScan.setStyleSheet("#btnCannotScan { \n"
"font: 20pt \'微软雅黑\';\n"
"background-color: #67C23A;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4px;border:1px solid #aaa }\n"
"#btnCannotScan:Pressed {background-color: #66EE23;}")
        self.btnCannotScan.setObjectName("btnCannotScan")
        self.layoutWidget = QtWidgets.QWidget(ChangePaperDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(75, 50, 561, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 28pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.lineEditBadLingID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditBadLingID.setEnabled(False)
        self.lineEditBadLingID.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEditBadLingID.setFont(font)
        self.lineEditBadLingID.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditBadLingID.setStyleSheet("color: rgb(53, 53, 53);\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"font: 32pt \"黑体\";\n"
"\n"
"text-align: center;\n"
"\n"
"font-weight:bold;\n"
"")
        self.lineEditBadLingID.setObjectName("lineEditBadLingID")
        self.horizontalLayout.addWidget(self.lineEditBadLingID)
        self.lb_endChangeTips = QtWidgets.QLabel(ChangePaperDlg)
        self.lb_endChangeTips.setGeometry(QtCore.QRect(650, 20, 481, 101))
        self.lb_endChangeTips.setStyleSheet("font: 36pt \"Arial\";\n"
"color: rgb(0, 255, 127);\n"
"background-color: rgb(85, 85, 127);\n"
"font-weight:bold;\n"
"border-radius:6px;\n"
"")
        self.lb_endChangeTips.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_endChangeTips.setObjectName("lb_endChangeTips")
        self.groupBox.raise_()
        self.layoutWidget.raise_()
        self.groupBox_2.raise_()
        self.btnEnd.raise_()
        self.btnCannotScan.raise_()
        self.lb_endChangeTips.raise_()

        self.retranslateUi(ChangePaperDlg)
        QtCore.QMetaObject.connectSlotsByName(ChangePaperDlg)
        ChangePaperDlg.setTabOrder(self.lineEditBadLingID, self.comboBadID)
        ChangePaperDlg.setTabOrder(self.comboBadID, self.lcdBadNum)
        ChangePaperDlg.setTabOrder(self.lcdBadNum, self.lcdNewNum)
        ChangePaperDlg.setTabOrder(self.lcdNewNum, self.btnCannotScan)
        ChangePaperDlg.setTabOrder(self.btnCannotScan, self.btnEnd)

    def retranslateUi(self, ChangePaperDlg):
        _translate = QtCore.QCoreApplication.translate
        ChangePaperDlg.setWindowTitle(_translate("ChangePaperDlg", "Dialog"))
        self.groupBox.setTitle(_translate("ChangePaperDlg", "损 纸："))
        self.label_10.setText(_translate("ChangePaperDlg", "ID："))
        self.label_badnum.setText(_translate("ChangePaperDlg", "张 数："))
        self.groupBox_2.setTitle(_translate("ChangePaperDlg", "替换纸："))
        self.label_3.setText(_translate("ChangePaperDlg", "ID："))
        self.label_NewNum.setText(_translate("ChangePaperDlg", "张 数："))
        self.btnEnd.setText(_translate("ChangePaperDlg", "结束换纸"))
        self.btnCannotScan.setText(_translate("ChangePaperDlg", "手工录入损纸"))
        self.label_11.setText(_translate("ChangePaperDlg", "令 号："))
        self.lineEditBadLingID.setPlaceholderText(_translate("ChangePaperDlg", "0000000000000000"))
        self.lb_endChangeTips.setText(_translate("ChangePaperDlg", "已完成换纸"))


