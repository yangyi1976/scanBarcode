import sys,time

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt

from config import Config
from scanBarcodeDBAPI import scanBarcodeDB
from ui_scanOperatorTip import Ui_ScanOperatorTipDlg


class ScanOperatorTipDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_ScanOperatorTipDlg()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.moveCenter()
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
        self.closeMainWin = Config.closeMainWin
        self.ui.lineEdit_operatorCode.returnPressed.connect(self.returnPressed)

    def initDB(self):
        '''
        初始化数据库，成功，返回True
        :return:
        '''
        self.codeDB = scanBarcodeDB()
        # 连接本地sqlite
        self.db = self.codeDB.getConnDB()
        if (self.db is None):
            QMessageBox.information(self, '错误', '缓存无法连接，可能损坏，请先修复！')
            return False
        # 设置远程mysql
        self.codeDB.setSqlServer(self.dbIP, self.dbuser, self.dbpassword, self.database)
        self.mysqldb = self.codeDB.getConnSqlDB()
        if (self.mysqldb is None):
            QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网线；如若不行，请联系数据库管理员！！',
                                    QMessageBox.Yes, QMessageBox.Yes)
            return False
        return True
    def returnPressed(self):
        operatorCode=self.ui.lineEdit_operatorCode.text()

        # if operatorCode==self.operatorCode:
        #     self.close()
        # else:
        #     self.ui.lineEdit_operatorCode.clear()
        #     self.ui.lineEdit_operatorCode.setText("人员码不对")
        #     QApplication.processEvents()
        #     time.sleep(0.5)
        #     self.ui.lineEdit_operatorCode.clear()
        # # print(operatorCode)

        self.changeOperator(operatorCode)

    def changeOperator(self, userCode):
        '''
        usb扫描用户码，可以切换不同用户返回。
        :param userCode:
        :return:
        '''
        self.userInfo = self.getUserInfo(userCode)
        if self.userInfo is None:
            self.ui.lineEdit_operator.setText("无此用户")
            time.sleep(0.5)
            self.ui.lineEdit_operatorCode.clear()
            return
        userName = self.getUserName()
        self.ui.lineEdit_operator.setText(userName)
        # 实时刷新界面
        QApplication.processEvents()
        self.userCode = userCode
        time.sleep(0.5)
        self.accept()

    def getUserInfo(self,userCode):
        userInfo=self.codeDB.getUserInfo(self.mysqldb,userCode)
        return  userInfo

    def getUserName(self):
        return self.userInfo.value("userName")

    def setUserName(self,userName):
        self.userName=userName
        self.ui.lineEdit_operator.setText(userName)

    def moveCenter(self):
        '''
        将窗体移到屏幕中心
        :return:
        '''
        # 得到窗体的框架信息
        frQr = self.frameGeometry()
        # 得到桌面中心
        cp = QDesktopWidget().availableGeometry().center()
        # 框架中心与桌面中心对齐
        frQr.moveCenter(cp)
        # 自身窗体的左上角与框架左上角对齐
        self.move(frQr.topLeft())
if __name__=="__main__":
    app=QApplication(sys.argv)
    scanTipDlg=ScanOperatorTipDlg()
    scanTipDlg.show()
    sys.exit(app.exec_())