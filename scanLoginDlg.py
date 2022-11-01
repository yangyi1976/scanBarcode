import os
import  sys
from config import Config
from  PyQt5.QtWidgets import QApplication,QMessageBox,QDialog
from PyQt5.QtCore import QCoreApplication,Qt,pyqtSlot
from ui_scanlogin import Ui_ScanLoginDlg
from scanThread import ScanBarThread
from scanBarcodeDBAPI import scanBarcodeDB
import time

class ScanLoginDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_ScanLoginDlg()
        self.ui.setupUi(self)
        self.setWindowTitle("扫描用户条码登陆")
        self.setWindowFlags(Qt.Drawer|Qt.MSWindowsFixedSizeDialogHint)  #只显示关闭图标，并固定窗口大小。
        self.setAutoFillBackground(True)

        # self.initScanUsbPort('com3','com4')
        self.userName=""
        self.userCode=""
        self.strUsbScanCode = ""

        # 远程数据库参数
        # self.dbIP = ""
        # self.dbuser = ""
        # self.dbpassword = ""
        # self.database = ""
        self.dbIP = Config.dbIP
        self.dbuser = Config.dbuser
        self.dbpassword = Config.dbpassword
        self.database = Config.database
        # 串口
        comPortGood = ""
         #关闭窗口条码命令
        self.closeMainWin = "1"
        if not self.initDB():
            print("DB init fail!")
            self.close()
        self.grabKeyboard()

    def initScanUsbPort(self, comA, comB):
        """
        初始化扫描端口和扫描守护线程
        :param comA:  串口A
        :param comB:  串口B
        :return:
        """
        comPortA = comA
        comPortB = comB
        if not self.initDB():
            print("DB init fail!")
            return

        try:
            self.scanPortA = ScanBarThread(comPortA, 'good')  # A口扫描线程
            self.scanPortA.scanBar.connect(self.userLogin)  # 关联槽函数，并接受扫描到的条码数据
        except IOError as err:
            QMessageBox.information(self, '错误', '扫描%s串口不能连接' % comPortA)

        try:
            self.scanPortB = ScanBarThread(comPortB, 'bad')  # B口扫描线程
            self.scanPortB.scanBar.connect(self.userLogin)  # 关联槽函数，并接受扫描到的坏品条码数据
        except IOError as err:
            QMessageBox.about(self, '错误', '扫描-%s串口不能连接' % comPortB)
        #启动线程
        self.scanPortA.start()
        # self.scanPortB.start()

    def initDB(self):
        '''
        初始化数据库，成功，返回True
        :return:
        '''
        self.codeDB = scanBarcodeDB()
        #连接本地sqlite
        self.db = self.codeDB.getConnDB()
        if (self.db is None):
            QMessageBox.information(self, '错误', '缓存无法连接，可能损坏，请先修复！')
            return False
        #设置远程mysql
        self.codeDB.setSqlServer(self.dbIP,self.dbuser,self.dbpassword,self.database)
        self.mysqldb = self.codeDB.getConnSqlDB()
        if (self.mysqldb is None):

            QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网线；如若不行，请联系数据库管理员！！',
                                     QMessageBox.Yes ,QMessageBox.Yes)
            return False
        return True

    def keyPressEvent(self, event):
        if event.key() != Qt.Key_Return:
            self.strUsbScanCode += event.text()
            print(self.strUsbScanCode)
        else:
            # 判断是否触发操作命令码
            if self.strUsbScanCode.lower() == self.closeMainWin.lower():  # 关闭主界面
                self.strUsbScanCode = ""
                self.releaseKeyboard()
                print("close==")
                self.close()
                os.system('shutdown -s -t 5')

            self.userLogin(self.strUsbScanCode)
            self.strUsbScanCode = ""
            # self.ui.le_usercode.clearFocus()
            print("login window return pressed....")


    def userLogin(self,userCode):
        '''
        扫描线程信号触发，显示扫描的用户名称，触发登录操作按钮
        :param userCode:
        :return:
        '''
        self.userInfo = self.getUserInfo(userCode)
        if self.userInfo is None:
            self.ui.le_usercode.setText("无此用户")
            return
        userName=self.getUserName()
        self.ui.le_usercode.setText(userName)
        #实时刷新界面
        QApplication.processEvents()
        self.userCode=userCode
        time.sleep(0.5)
        self.releaseKeyboard()
        self.accept()
        # self.on_loginBtn_clicked()


    def getUserInfo(self,userCode):
        userInfo=self.codeDB.getUserInfo(self.mysqldb,userCode)
        return  userInfo

    def getUserName(self):
        return self.userInfo.value("userName")


    @pyqtSlot()
    def on_loginBtn_clicked(self):
        userCode=self.ui.le_usercode.text()
        self.userInfo = self.getUserInfo(userCode)

        if self.userInfo is None:
            QMessageBox.information(self, '注意', '无此用户,请重新尝试或者添加用户！')
            self.ui.le_usercode.setText("")
        else:

            userName=self.userInfo.value("userName")
            print("@class:scanLoginDlg.%s 登录成功" % userName)
            print("@class:scanLoginDlg.销毁扫描守护线程，释放扫描com端口")
            self.destroyScanThread()
            if not hasattr(self,'scanPortA') and not hasattr(self,'scanPortB'):
                self.accept()

    def destroyScanThread(self):
        print("登录窗口，终止扫描线程===")
        #终止扫描守护线程
        # self.scanPortA.terminate()
        # self.scanPortB.terminate()
        self.scanPortA.isStop=True
        self.scanPortB.isStop = True
        # 释放com口
        self.scanPortA.comPort.com.close()
        self.scanPortB.comPort.com.close()
        #退出线程
        self.scanPortA.exit()
        self.scanPortB.exit()
        #删除进程变量
        del self.scanPortA
        del self.scanPortB

    @pyqtSlot()
    def on_closeBtn_clicked(self):
        self.close()
        # self.destroyScanThread()


    def closeEvent(self, event):
        print("exit：",event)
        self.releaseKeyboard()
        event.rejected()
        QCoreApplication.instance().quit()





if __name__=="__main__":
    app=QApplication(sys.argv)
    loginDlg=ScanLoginDlg()
    loginDlg.exec()
    sys.exit(app.exec_())
