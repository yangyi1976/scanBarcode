# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoTip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoTipDlg(object):
    def setupUi(self, infoTipDlg):
        infoTipDlg.setObjectName("infoTipDlg")
        infoTipDlg.resize(977, 234)
        infoTipDlg.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.lineEdit_tip = QtWidgets.QLineEdit(infoTipDlg)
        self.lineEdit_tip.setGeometry(QtCore.QRect(40, 30, 921, 131))
        self.lineEdit_tip.setStyleSheet("font: 87 28pt \"Arial Black\";\n"
"font-weight:bold;\n"
"border:none;\n"
" ")
        self.lineEdit_tip.setObjectName("lineEdit_tip")

        self.retranslateUi(infoTipDlg)
        QtCore.QMetaObject.connectSlotsByName(infoTipDlg)

    def retranslateUi(self, infoTipDlg):
        _translate = QtCore.QCoreApplication.translate
        infoTipDlg.setWindowTitle(_translate("infoTipDlg", "Dialog"))
        self.lineEdit_tip.setText(_translate("infoTipDlg", "消息提示"))


