import sys,time

from  PyQt5.QtWidgets import QApplication ,QDialog
from PyQt5.QtCore import Qt
from ui_infoTip import  Ui_infoTipDlg


class InfoTipDlg(QDialog):


    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_infoTipDlg()
        self.ui.setupUi(self)
        #不显示对话框的标题栏和边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # self.topWindow=parent
        # self.grabKeyboard()  # 窗口捕获键盘事件
        self.ui.lineEdit_tip.setText("消息提示:")
        # self.ui.lineEdit_tip.setFocus(True)
        self.ui.lineEdit_tip.returnPressed.connect(self.returnPressed)

    def setAlertText(self,str):
        self.ui.lineEdit_tip.setText(str)

    def setTopWindow(self,top):  #传递进来顶层父窗口
        self.topWindow=top


    def showEvent(self,event):
        print("info dlg show")
        # self.ui.lineEdit_tip.setFocus(True)
        if hasattr(self.topWindow,"scanPortGood"):  #判断是否已经初始化了串口线程类
            self.topWindow.releasePort()        #释放主线程的串口，停止扫描
        pass

    def returnPressed(self):
        print("info return press")
        if hasattr(self.topWindow, "scanPortGood"):
            self.topWindow.startComPort()        #启动主线程的串口扫描
        self.close()




if __name__=="__main__":
    app=QApplication(sys.argv)
    scanTipDlg=InfoTipDlg()
    scanTipDlg.show()
    sys.exit(app.exec_())