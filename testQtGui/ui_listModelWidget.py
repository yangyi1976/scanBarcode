# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listModelWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(816, 414)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(50, 170, 301, 201))
        self.listView.setObjectName("listView")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(490, 160, 281, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btnList_Append = QtWidgets.QPushButton(Form)
        self.btnList_Append.setGeometry(QtCore.QRect(70, 50, 78, 24))
        self.btnList_Append.setObjectName("btnList_Append")
        self.btnList_Insert = QtWidgets.QPushButton(Form)
        self.btnList_Insert.setGeometry(QtCore.QRect(210, 50, 78, 24))
        self.btnList_Insert.setObjectName("btnList_Insert")
        self.btnList_Delete = QtWidgets.QPushButton(Form)
        self.btnList_Delete.setGeometry(QtCore.QRect(70, 120, 78, 24))
        self.btnList_Delete.setObjectName("btnList_Delete")
        self.btnList_Clear = QtWidgets.QPushButton(Form)
        self.btnList_Clear.setGeometry(QtCore.QRect(210, 120, 78, 24))
        self.btnList_Clear.setObjectName("btnList_Clear")
        self.btnText_Display = QtWidgets.QPushButton(Form)
        self.btnText_Display.setGeometry(QtCore.QRect(500, 120, 251, 31))
        self.btnText_Display.setObjectName("btnText_Display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnList_Append.setText(_translate("Form", "????????????"))
        self.btnList_Insert.setText(_translate("Form", "?????????"))
        self.btnList_Delete.setText(_translate("Form", "?????????"))
        self.btnList_Clear.setText(_translate("Form", "????????????"))
        self.btnText_Display.setText(_translate("Form", "??????????????????StringList"))
