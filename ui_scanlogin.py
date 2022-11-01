# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanlogin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScanLoginDlg(object):
    def setupUi(self, ScanLoginDlg):
        ScanLoginDlg.setObjectName("ScanLoginDlg")
        ScanLoginDlg.resize(880, 503)
        ScanLoginDlg.setAutoFillBackground(False)
        ScanLoginDlg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QtWidgets.QWidget(ScanLoginDlg)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 240, 761, 188))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_usercode = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.le_usercode.setFont(font)
        self.le_usercode.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.le_usercode.setStyleSheet("color:rgb(0, 0, 127);\n"
"background-color: rgb(240, 240, 240);\n"
"border-style:groove;\n"
"border-bottom:1px solid rgb(0, 0, 127);\n"
" \n"
" ")
        self.le_usercode.setText("")
        self.le_usercode.setFrame(True)
        self.le_usercode.setAlignment(QtCore.Qt.AlignCenter)
        self.le_usercode.setReadOnly(False)
        self.le_usercode.setObjectName("le_usercode")
        self.gridLayout.addWidget(self.le_usercode, 1, 1, 1, 1)
        self.lb_loginBar = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_loginBar.sizePolicy().hasHeightForWidth())
        self.lb_loginBar.setSizePolicy(sizePolicy)
        self.lb_loginBar.setMaximumSize(QtCore.QSize(150, 120))
        self.lb_loginBar.setText("")
        self.lb_loginBar.setPixmap(QtGui.QPixmap("img/barblue.jpg"))
        self.lb_loginBar.setScaledContents(False)
        self.lb_loginBar.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_loginBar.setObjectName("lb_loginBar")
        self.gridLayout.addWidget(self.lb_loginBar, 1, 0, 1, 1)
        self.lb_userName = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_userName.sizePolicy().hasHeightForWidth())
        self.lb_userName.setSizePolicy(sizePolicy)
        self.lb_userName.setMaximumSize(QtCore.QSize(598, 110))
        self.lb_userName.setStyleSheet("color:rgb(0, 0, 127);\n"
"font: 40pt \"黑体\";\n"
"")
        self.lb_userName.setText("")
        self.lb_userName.setTextFormat(QtCore.Qt.PlainText)
        self.lb_userName.setPixmap(QtGui.QPixmap("img/user.jpg"))
        self.lb_userName.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_userName.setObjectName("lb_userName")
        self.gridLayout.addWidget(self.lb_userName, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(ScanLoginDlg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1019, 232))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/back_bar.jpg"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.loginBtn = QtWidgets.QPushButton(ScanLoginDlg)
        self.loginBtn.setGeometry(QtCore.QRect(280, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.closeBtn = QtWidgets.QPushButton(ScanLoginDlg)
        self.closeBtn.setGeometry(QtCore.QRect(440, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")

        self.retranslateUi(ScanLoginDlg)
        QtCore.QMetaObject.connectSlotsByName(ScanLoginDlg)

    def retranslateUi(self, ScanLoginDlg):
        _translate = QtCore.QCoreApplication.translate
        ScanLoginDlg.setWindowTitle(_translate("ScanLoginDlg", "Dialog"))
        self.le_usercode.setPlaceholderText(_translate("ScanLoginDlg", "请扫描用户条码登录"))
        self.loginBtn.setText(_translate("ScanLoginDlg", "登录"))
        self.closeBtn.setText(_translate("ScanLoginDlg", "关闭"))


