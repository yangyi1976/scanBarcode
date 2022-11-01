# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanOperatorTip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScanOperatorTipDlg(object):
    def setupUi(self, ScanOperatorTipDlg):
        ScanOperatorTipDlg.setObjectName("ScanOperatorTipDlg")
        ScanOperatorTipDlg.resize(1025, 537)
        ScanOperatorTipDlg.setStyleSheet(" \n"
"background-color: rgb(0, 214, 0);")
        self.lineEdit_operator = QtWidgets.QLineEdit(ScanOperatorTipDlg)
        self.lineEdit_operator.setGeometry(QtCore.QRect(360, 300, 301, 101))
        self.lineEdit_operator.setStyleSheet("border:none;\n"
"font: 87 40pt \"Arial Black\";\n"
"font-weight:bold;\n"
"")
        self.lineEdit_operator.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_operator.setObjectName("lineEdit_operator")
        self.textEdit = QtWidgets.QTextEdit(ScanOperatorTipDlg)
        self.textEdit.setGeometry(QtCore.QRect(130, 110, 781, 101))
        self.textEdit.setStyleSheet("\n"
"font: 40pt \"Arial Black\";\n"
"font-weight:bold;\n"
"border:none;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_operatorCode = QtWidgets.QLineEdit(ScanOperatorTipDlg)
        self.lineEdit_operatorCode.setGeometry(QtCore.QRect(170, 220, 431, 51))
        self.lineEdit_operatorCode.setStyleSheet("border:none;\n"
"font: 40pt \"Arial Black\";\n"
"border-bottom:2px solid #000;\n"
"color: #000021;\n"
" ")
        self.lineEdit_operatorCode.setObjectName("lineEdit_operatorCode")
        self.label = QtWidgets.QLabel(ScanOperatorTipDlg)
        self.label.setGeometry(QtCore.QRect(640, 200, 251, 81))
        self.label.setStyleSheet("font: 40pt \"Arial Black\";\n"
"color: #000021;\n"
"font-weight:bold;\n"
"border:none;")
        self.label.setObjectName("label")

        self.retranslateUi(ScanOperatorTipDlg)
        QtCore.QMetaObject.connectSlotsByName(ScanOperatorTipDlg)

    def retranslateUi(self, ScanOperatorTipDlg):
        _translate = QtCore.QCoreApplication.translate
        ScanOperatorTipDlg.setWindowTitle(_translate("ScanOperatorTipDlg", "Form"))
        self.textEdit.setHtml(_translate("ScanOperatorTipDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:40pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#000021;\">本令纸已满500张，请刷人员卡:  </span></p></body></html>"))
        self.label.setText(_translate("ScanOperatorTipDlg", "进行确认。"))


