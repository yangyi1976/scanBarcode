import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QEvent
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout, QFormLayout)
from testKeypress import DemoKeyboardEvent



class MyLineEdit(QLineEdit):
    def __init__(self, id, parent=None):
        super(MyLineEdit, self).__init__(parent)
        self.id = id

    # 焦点进入事件
    def focusInEvent(self, evt):
        print('输入焦点在:', self.id)
        QLineEdit.focusInEvent(self, evt)

    # 焦点离开事件
    def focusOutEvent(self, evt):
        print(self.id, ':失去输入焦点')
        QLineEdit.focusOutEvent(self, evt)

    def keyPressEvent(self, evt):
        print("press MyLineeidt")


class FocusSetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(FocusSetDemo, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5:焦点设置演示')
        # 设置窗口大小
        self.resize(400, 600)

        self.initUi()



    def initUi(self):
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(10)

        btnChangeFocus = QPushButton('将焦点设置到编辑框2')
        btnChangeFocus.clicked.connect(self.onButtonChangeFocus)

        self.lineEdit1 = MyLineEdit(1)
        self.lineEdit2 = QLineEdit()

        # self.keyboardGrabber()  #让主窗口监听键盘事件


        fLayout = QFormLayout()
        fLayout.addRow('编辑框1', self.lineEdit1)
        fLayout.addRow('编辑框2', self.lineEdit2)

        mainLayout.addWidget(btnChangeFocus)
        mainLayout.addLayout(fLayout)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.red)
        self.setPalette(palette)

    def onButtonChangeFocus(self):
        self.lineEdit2.setFocus()

        # mainWidget = QWidget()
        # mainWidget.setWindowTitle("abc")
        #
        # ledit=QLineEdit()
        # mainWidget.addWidget(ledit)

        # window = DemoKeyboardEvent()

        pass


    def focusInEvent(self, evt):
        print('输入焦点在:', self.id)


    def keyPressEvent(self, evt):
        print("press",evt.key())
        if evt.key()==Qt.Key_Return:
            print("press ===========a")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FocusSetDemo()
    window.show()
    sys.exit(app.exec())
