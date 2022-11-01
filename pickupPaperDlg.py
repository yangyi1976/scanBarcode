import sys

from PyQt5.QtCore import  QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import  QColor
from PyQt5.QtWidgets import QApplication,   QMessageBox, QDialog
from PyQt5.QtCore import  Qt
from ui_pickuppaper import Ui_PickupPaperDlg

from scanBarcodeDBAPI import scanBarcodeDB
from config import Config


class PickupPaperDlg(QDialog):
    def __init__(self,dbip,dbuser,dbpassword,database,parent=None):
        super().__init__(parent)
        self.ui=Ui_PickupPaperDlg()
        self.ui.setupUi(self)
        self.setWindowTitle("挑出未扫描纸")
        self.setWindowFlags(Qt.Drawer|Qt.MSWindowsFixedSizeDialogHint)  #只显示关闭图标，并固定窗口大小。


        # self.ui.lineEdit_firstID.setReadOnly(True)
        self.ui.lineEdit_firstID.setFocus(True)
        self.ui.lineEdit_endID.setReadOnly(True)
        self.isRun=True

        # database config
        self.dbip = dbip
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.database = database

        self.closeThisWindow=Config.pickupPaper
        self.strUsbScanCode =""
        self.firstPaperTime=""
        self.endPaperTime=""
        if not self.initDB():
            print("DB init fail!")
            self.isRun = False
            return False

        qss = "QDialog#PickupPaperDlg{background-color:black;}"
        self.setStyleSheet(qss)
        # self.grabKeyboard()
        # self.ui.lineEdit_firstID.returnPressed.connect(self.firstEditPressed)

    def initDB(self):
        '''
        初始化数据库，成功，返回True
        :return:
        '''
        self.barcodeDB = scanBarcodeDB()
        # 设置远程mysql
        self.barcodeDB.setSqlServer(self.dbip, self.dbuser, self.dbpassword, self.database)
        self.mysqldb = self.barcodeDB.getConnSqlDB()
        if (self.mysqldb is None):
            QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网线；如若不行，连接数据库管理员！！')
            return False
        return True
    # def firstEditPressed(self):
    #     firstPaperID=self.ui.lineEdit_firstID.text()
    #     if firstPaperID.lower()==self.closeThisWindow.lower():
    #         self.close()
    #         return
    def setTopWindow(self, top):
        self.topWindow = top

    def showEvent(self, event):
        if not hasattr(self,"topWindow")  :
            return
        self.topWindow.releaseKeyboard()
        self.grabKeyboard()

        pass

    def keyPressEvent(self, event):
        # if self.ui.lineEdit_bad.text() !="":
        #     self.ui.lineEdit_bad.clear()

        if event.key()!=Qt.Key_Return   :
            self.strUsbScanCode+=event.text()
            print("from pikcup:",self.strUsbScanCode)
        else:
            #判断是否触发操作命令码
            if self.strUsbScanCode.lower()== self.closeThisWindow.lower():
                self.strUsbScanCode = ""
                self.releaseKeyboard()
                self.close()
                return
            if self.ui.lineEdit_firstID.isEnabled():
                self.ui.lineEdit_firstID.setText(self.strUsbScanCode)
                self.blinkWin("first")
                result=self.barcodeDB.queryPaperInfo(self.mysqldb,self.strUsbScanCode)
                if result is None:
                    self.ui.lb_firstTip.setText("未查到此张产品ID！")
                    self.ui.lineEdit_firstID.setFocus()
                    self.ui.lineEdit_firstID.selectAll()
                    self.strUsbScanCode = ""
                    return
                self.ui.lb_firstTip.setText("")
                self.firstPaperTime=result.value("time").toString("yyyy-MM-dd hh:mm:ss")
                self.firstPaperLingId=result.value("mainLingID")
                self.ui.lineEdit_endID.setReadOnly(False)
                self.ui.lineEdit_endID.setEnabled(True)
                self.ui.lineEdit_endID.setFocus(True)
                self.ui.lineEdit_firstID.setEnabled(False)
                #查询数据库的操作时间
                self.strUsbScanCode = ""
            elif self.ui.lineEdit_endID.isEnabled():
                self.ui.lineEdit_endID.setText(self.strUsbScanCode)
                self.blinkWin("end")
                result = self.barcodeDB.queryPaperInfo(self.mysqldb, self.strUsbScanCode)
                if result is None:
                    self.ui.lb_endTip.setText("未查到此张产品ID！")
                    self.ui.lineEdit_endID.setFocus()
                    self.ui.lineEdit_endID.selectAll()
                    self.strUsbScanCode = ""
                    return
                self.ui.lb_endTip.setText("")
                self.ui.lineEdit_firstID.setEnabled(True)
                self.ui.lineEdit_firstID.setFocus(True)
                self.ui.lineEdit_endID.setEnabled(False)
                result = self.barcodeDB.queryPaperInfo(self.mysqldb, self.strUsbScanCode)
                self.endPaperTime = result.value("time").toString("yyyy-MM-dd hh:mm:ss")
                self.endPaperLingId = result.value("mainLingID")

                if(self.firstPaperLingId !=self.endPaperLingId):
                    QMessageBox.information(self,"错误","不是同一令纸！")
                    self.strUsbScanCode = ""
                    return
                #交换首末张。一令纸上面的张时间是晚入库，所以按时间而言首张其实是末张
                self.firstPaperTime,self.endPaperTime=self.endPaperTime,self.firstPaperTime
                self.num=self.barcodeDB.countSheetNumBetweenTime(self.mysqldb,self.firstPaperTime,self.endPaperTime,self.firstPaperLingId)
                print("数量：",self.num)
                self.ui.lcd_betweenCount.display(self.num)
                self.strUsbScanCode = ""

    def _set_color(self, col):

        # 调色板方式绘制背景动画颜色
        # palette = self.palette()
        # palette.setColor(self.backgroundRole(), col)
        #
        # self.setPalette(palette)
        # =========================
        # 样式表方式绘制背景动画颜色
        qss = '''
                color: rgb(195, 0, 0);
                font: 22pt \"微软雅黑\";
                text-align: center;
                font-weight:bold;
                '''
        if self.blinkType=="first":
            self.ui.lineEdit_firstID.setStyleSheet(qss + "background-color:" + col.name())
        else :
            self.ui.lineEdit_endID.setStyleSheet(qss+"color:rgb(0, 250, 0);background-color:"+col.name())

    color = pyqtProperty(QColor, fset=_set_color)   #定义动画颜色属性

    def blinkWin(self,type):

        self.anim = QPropertyAnimation(self, b"color")
        # anim.setTargetObject(self.ui.lineEdit_good)
        self.anim.setDuration(400)
        self.anim.setLoopCount(2)
        if type == 'first':
            self.blinkType='first'
            self.anim.setStartValue(QColor(0, 0, 0))
        else:
            self.blinkType='end'
            self.anim.setStartValue(QColor(0, 0, 0))

        # self.anim.setEndValue(QColor( 240,  240, 240))
        # self.anim.setEndValue(self.palette().color(self.backgroundRole()))

        self.anim.setEndValue(QColor(255,255,255))
        self.anim.start()


if __name__=="__main__":
    app=QApplication(sys.argv)
    pickupPaperDlg=PickupPaperDlg('127.0.1.1','root','password','paperbarcode')
    if pickupPaperDlg.isRun:
        pickupPaperDlg.show()
    sys.exit(app.exec_())