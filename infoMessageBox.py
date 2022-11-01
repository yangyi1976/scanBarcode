from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import Qt

class InfoMessageBox(QMessageBox):
    def __init__(self, parent=None):

        super(InfoMessageBox, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("消息")
        self.resize(800, 400)
        self.setMaximumSize(800,400)

        parent.releaseKeyboard()   #父窗口释放键盘监听
        self.topWindow=parent

    def showEvent(self,event):
        if hasattr(self.topWindow,"scanPortGood"):  #判断是否已经初始化了串口线程类
            self.topWindow.releasePort()
        print("show ======")



    def closeEvent(self, QCloseEvent):
        self.topWindow.grabKeyboard()  #父窗口恢复键盘监听
        # self.topWindow.scanPortGood.comPort.com.open()
        # self.topWindow.scanPortGood.start()