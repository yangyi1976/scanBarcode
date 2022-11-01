import sys
from  PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import  QtWidgets
from PyQt5.QtCore import QRect


class Ui_MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        #窗口大小
        self.resize(800, 600)
        #定义按钮
        self.pushButton = QtWidgets.QPushButton(self)
        #设置按钮位置(x,y,width,height)
        self.pushButton.setGeometry(QRect(10, 240, 93, 28))
        #设置按钮内容
        self.pushButton.setText("button")
        #设置按钮对象名（不是显示内容
        self.pushButton.setObjectName("pushButton")
        #设置按钮圆角
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px; border: 2px groove gray;border-style: outset;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
