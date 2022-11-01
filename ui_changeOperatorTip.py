# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeOperatorTip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeOperatorTipDlg(object):
    def setupUi(self, ChangeOperatorTipDlg):
        ChangeOperatorTipDlg.setObjectName("ChangeOperatorTipDlg")
        ChangeOperatorTipDlg.resize(1012, 338)
        ChangeOperatorTipDlg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit = QtWidgets.QTextEdit(ChangeOperatorTipDlg)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 701, 101))
        self.textEdit.setStyleSheet("\n"
"font: 40pt \"Arial Black\";\n"
"font-weight:bold;\n"
"border:none;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_operatorCode = QtWidgets.QLineEdit(ChangeOperatorTipDlg)
        self.lineEdit_operatorCode.setGeometry(QtCore.QRect(120, 200, 451, 51))
        self.lineEdit_operatorCode.setStyleSheet("border:none;\n"
"font: 40pt \"Arial Black\";\n"
"border-bottom:2px solid #000;\n"
"color: #000021;\n"
" ")
        self.lineEdit_operatorCode.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_operatorCode.setObjectName("lineEdit_operatorCode")
        self.lineEdit_operator = QtWidgets.QLineEdit(ChangeOperatorTipDlg)
        self.lineEdit_operator.setGeometry(QtCore.QRect(620, 170, 331, 101))
        self.lineEdit_operator.setStyleSheet("border:none;\n"
"font: 87 40pt \"Arial Black\";\n"
"font-weight:bold;\n"
"")
        self.lineEdit_operator.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_operator.setObjectName("lineEdit_operator")

        self.retranslateUi(ChangeOperatorTipDlg)
        QtCore.QMetaObject.connectSlotsByName(ChangeOperatorTipDlg)

    def retranslateUi(self, ChangeOperatorTipDlg):
        _translate = QtCore.QCoreApplication.translate
        ChangeOperatorTipDlg.setWindowTitle(_translate("ChangeOperatorTipDlg", "Form"))
        self.textEdit.setHtml(_translate("ChangeOperatorTipDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:40pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#000021;\">请刷人员卡进行切换操作人:  </span></p></body></html>"))


