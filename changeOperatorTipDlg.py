import sys,time

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import Qt

from scanBarcodeDBAPI import scanBarcodeDB
from ui_changeOperatorTip import Ui_ChangeOperatorTipDlg
from  config  import Config


class ChangeOperatorTipDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_ChangeOperatorTipDlg()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.lineEdit_operatorCode.setFocus(True)
        self.ui.lineEdit_operator.setText("")
        self.operatorCode="6918163020886"
        # self.grabKeyboard()  # 窗口捕获键盘事件

        self.userName = ""
        self.userCode = ""
        self.strUsbScanCode = ""

        self.dbIP = Config.dbIP
        self.dbuser = Config.dbuser
        self.dbpassword = Config.dbpassword
        self.database = Config.database
        if not self.initDB():
            print("DB init fail!")
            self.close()
        self.closeMainWin=Config.closeMainWin
        self.ui.lineEdit_operatorCode.returnPressed.connect(self.returnPressed)

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

    def returnPressed(self):
        operatorCode=self.ui.lineEdit_operatorCode.text()

        if operatorCode.lower()==self.closeMainWin.lower():
            self.close()
        else:
            # self.ui.lineEdit_operatorCode.clear()
            # self.ui.lineEdit_operatorCode.setText("人员码不对")
            # QApplication.processEvents()
            # time.sleep(0.5)
            # self.ui.lineEdit_operatorCode.clear()
            self.changeOperator( operatorCode)


        # print(operatorCode)
        pass
    def changeOperator(self,userCode):
        '''
        扫描线程信号触发，显示扫描的用户名称，触发登录操作按钮
        :param userCode:
        :return:
        '''
        self.userInfo = self.getUserInfo(userCode)
        if self.userInfo is None:
            self.ui.lineEdit_operator.setText("无此用户")
            time.sleep(0.5)
            self.ui.lineEdit_operatorCode.clear()
            return
        userName=self.getUserName()
        self.ui.lineEdit_operator.setText(userName)
        #实时刷新界面
        QApplication.processEvents()
        self.userCode=userCode
        time.sleep(0.5)

        self.accept()
        # self.on_loginBtn_clicked()


    def getUserInfo(self,userCode):
        userInfo=self.codeDB.getUserInfo(self.mysqldb,userCode)
        return  userInfo

    def getUserName(self):
        return self.userInfo.value("userName")

if __name__=="__main__":
    app=QApplication(sys.argv)
    scanTipDlg=ChangeOperatorTipDlg()
    scanTipDlg.show()
    sys.exit(app.exec_())