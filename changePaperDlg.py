import sys
from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import  QFont
from PyQt5.QtWidgets import QApplication,   QMessageBox, QDialog, QTableWidgetItem
from PyQt5.QtCore import  Qt,pyqtSlot
from ui_changePaper import Ui_ChangePaperDlg
from scanThread import ScanBarThread
from scanBarcodeDBAPI import scanBarcodeDB
from config import Config
from scanUtil import checkBarCode

class ChangePaperDlg(QDialog):
    def __init__(self,dbip,dbuser,dbpassword,database,parent=None):
        super().__init__(parent)
        self.ui=Ui_ChangePaperDlg()
        self.ui.setupUi(self)
        self.setWindowTitle("换纸操作")
        self.setWindowFlags(Qt.Drawer|Qt.MSWindowsFixedSizeDialogHint)  #只显示关闭图标，并固定窗口大小。
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAutoFillBackground(True)


        self.ui.comboBadID.setEditable(True)
        self.ui.comboBadID.setFocus(True)
        self.ui.lb_endChangeTips.setHidden(True)
        self.btnCannotScan_toggle=False

        #database config
        self.dbip = dbip
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.database = database

        self.isRun = True
        self.badCount = 0
        self.newCount = 0
        self.lingID = ""
        self.operator = ""
        self.enableCount=True
        self.startChange=False
        self.newPaperSet=[]
        # self.badBarcode=[]

        # self.initScanUsbPort('com3', 'com4')
        if not self.initDB():
            print("DB init fail!")
            self.isRun = False
            return False
        self.closeThisWindow=Config.openChangepaper
        self.goodPaperIn=Config.goodPaperIn

        self.ui.comboBadID.editTextChanged.connect(self.editcombox)
        # self.ui.comboNewID.currentIndexChanged.connect(self.currentIndexChanged)
        self.ui.comboBadID.lineEdit().returnPressed.connect(self.returnPressed)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer1 = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.blinkLabel)  # 计时结束调用 方法
        self.timer1.timeout.connect(self.blinkLabel1)  # 计时结束调用 方法

        # p = QPalette()
        # p.setColor(QPalette.Background, Qt.black)
        # p.setColor(QPalette.WindowText, Qt.red)
        # # p.setColor(QPalette.Text, Qt.red)
        # # p.setColor(QPalette.ButtonText, Qt.red)
        # self.setPalette(p)
        qss = "QDialog#ChangePaperDlg{background-color:black;}"
        # qss = "QWidget#mainWindow{border-image:url(background.png);}"
        self.setStyleSheet(qss)


    def initScanUsbPort(self, comA, comB):
        """
        初始化扫描端口和扫描守护线程
        :param comA:  好纸串口A
        :param comB:  损纸串口B
        :return:
        """
        comPortGood= comA
        comPortBad = comB
        if not self.initDB():
            print("DB init fail!")
            self.isRun = False
            return False

        # try:
        #     self.scanPortBad = ScanBarThread(comPortBad, 'bad')  # B口扫描线程
        #     self.scanPortBad.scanBar.connect(self.scanBadPaper)  # 关联槽函数，并接受扫描到的坏品条码数据
        # except IOError as err:
        #     QMessageBox.information(self, '错误', '扫描%s串口不能连接' % comPortBad)

        try:
            self.scanPortGood = ScanBarThread(comPortGood, 'good')  # A口扫描线程
            self.scanPortGood.scanBar.connect(self.changePaper)  # 关联槽函数，并接受扫描到的条码数据
        except IOError as err:
            QMessageBox.about(self, '错误', '扫描-%s串口不能连接' % comPortGood)
        #启动线程
        # self.scanPortBad.start()
        self.scanPortGood.start()

    def setMySql(self,dbip,dbuser,dbpassword,database):
        self.dbip=dbip
        self.dbuser=dbuser
        self.dbpassword=dbpassword
        self.database=database

    def initDB(self):
        '''
        初始化数据库，成功，返回True
        :return:
        '''
        self.barcodeDB = scanBarcodeDB()
        # 连接本地sqlite
        self.db = self.barcodeDB.getConnDB()
        if (self.db is None):
            QMessageBox.information(self, '错误', '缓存无法连接，可能损坏，请先修复！')
            return False
        # 设置远程mysql
        self.barcodeDB.setSqlServer(self.dbip, self.dbuser, self.dbpassword, self.database)
        self.mysqldb = self.barcodeDB.getConnSqlDB()
        if (self.mysqldb is None):
            QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网线；如若不行，连接数据库管理员！！')
            return False
        return True

    def setOperator(self,userName):
        self.operator=userName


    def scanBadPaper(self,badCode,type):
        '''
        扫描损纸，判断远程数据库里是否有，有则删之，并获取lingID
        :return:
        '''

        idx = self.ui.comboNewID.findText(badCode)
        if idx != -1:
            newCount = self.ui.comboNewID.count()
            self.ui.lcdNewNum.display(newCount - 1)
            self.ui.comboNewID.removeItem(idx)
            return

        lingID=self.barcodeDB.queryLingID(self.mysqldb,badCode)
        if lingID is None:
            QMessageBox.information(self, '注意', '没有查询到该产品的条码,请检查此条码正确与否！！')
            return False
        else:
            idx = self.ui.comboBadID.findText(badCode)
            if idx==-1:
                self.ui.lb_endChangeTips.setHidden(False)
                self.ui.lb_endChangeTips.setText("换纸状态...")
                self.ui.comboBadID.addItem(badCode)
                self.ui.lineEditBadLingID.setText(lingID)
                self.badCount+=1
                self.ui.lcdBadNum.display(self.badCount)
                self.startChange=True

            self.ui.comboBadID.setCurrentText(badCode)
            return True

    def getComboxAllText(self,combox):
        badBarcode=[]
        for i in range(combox.count()):
            codeList=combox.itemText(i)
            badBarcode.append(codeList)
        return  badBarcode

    def changePaper(self,newCode,type):
        '''
        使用串口扫描录入更换的新纸
        :param newCode:新纸ID
        :param type:
        :return:
        '''
        if self.startChange is False or self.ui.comboBadID.count()==0:
            return
        #先判断是否该条码已经扫描过 ,!=-1 表示该条码已经扫描过
        if self.ui.comboNewID.findText(newCode) !=-1 :
            self.ui.comboNewID.setCurrentText(newCode)
            return
        #判断该条码是否在损纸框中已经扫了，有就删除,其他动作不操作。
        badidx=self.ui.comboBadID.findText(newCode)
        if badidx!=-1:
            self.badCount-=1
            self.ui.comboBadID.removeItem(badidx)
            self.ui.lcdBadNum.display(self.badCount)
            return

        self.ui.comboNewID.addItem(newCode)
        self.newCount += 1

        self.ui.lcdNewNum.display(self.newCount)
        mainLingID=self.ui.lineEditBadLingID.text()
        scantime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paper=(newCode,'good',scantime,self.operator,'0000',mainLingID,'整令')
        self.newPaperSet.append(paper)
        self.ui.comboNewID.setCurrentText(newCode)
        #需要删除本地sqlite里的newCode记录，以避免上传到远程数据库
        self.barcodeDB.delPaper(self.db,newCode)
        if self.newCount==self.badCount:  #换纸，写入数据库、更新整令的令号、删除损纸
            r= self.barcodeDB.insertOrUpdate(self.mysqldb,tuple(self.newPaperSet))
            if r:
                r=self.barcodeDB.updateLingID(self.mysqldb,newCode,mainLingID)  #使用最后一张纸的ID进行
                if r:
                    badBarCodeSet=self.getComboxAllText(self.ui.comboBadID)
                    self.barcodeDB.delByMatchBarcode(self.mysqldb,tuple(badBarCodeSet))

            # 结束换纸
            self.startChange=False
            # 清除纸张显示
            self.clearPaperDisplay()
            # self.ui.lb_endChangeTips.setHidden(False)
            self.ui.lb_endChangeTips.setText("完成本令换纸")

    def changePaperByUsb(self, newCode):
        '''
        使用usb口扫描录入更换的新纸
        :param newCode:新纸ID
        :param type:
        :return:
        '''
        if self.startChange is False or self.ui.comboBadID.count() == 0:  #未开始换
            return
        # # 先判断是否该条码已经扫描过 ,!=-1 表示该条码已经扫描过
        # if self.ui.comboNewID.findText(newCode) != -1:
        #     self.ui.comboNewID.setCurrentText(newCode)
        #     return
        # 判断该条码是否在损纸框中已经扫了，其他动作不操作。可能扫到不需要换的纸了。但实际不可能你
        badidx = self.ui.comboBadID.findText(newCode)
        if badidx != -1:

            return

        # self.ui.comboNewID.addItem(newCode)
        self.newCount += 1
        self.ui.lcdNewNum.display(self.newCount)
        item=QTableWidgetItem(newCode)
        item.setTextAlignment(Qt.AlignHCenter)
        item.setFont(QFont('微软雅黑', 27, QFont.Black))
        rowNum=self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowNum)
        self.ui.tableWidget.setItem(rowNum,0,item)

        mainLingID = self.ui.lineEditBadLingID.text()
        scantime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paper = (newCode, 'good', scantime, self.operator, '0000', mainLingID, '整令','更换好纸')
        self.newPaperSet.append(paper)
        self.ui.comboNewID.setCurrentText(newCode)
        # 需要删除本地sqlite里的newCode记录，以避免上传到远程数据库
        self.barcodeDB.delPaper(self.db, newCode)
        if self.newCount == self.badCount:  # 换纸，写入数据库、更新整令的令号、删除损纸
            r = self.barcodeDB.insertOrUpdate(self.mysqldb, tuple(self.newPaperSet))
            if r:
                r = self.barcodeDB.updateLingID(self.mysqldb, newCode, mainLingID)  # 使用最后一张纸的ID进行
                if r:
                    badBarCodeSet = self.getComboxAllText(self.ui.comboBadID)
                    self.barcodeDB.delByMatchBarcode(self.mysqldb, tuple(badBarCodeSet))

            # 结束换纸
            self.startChange = False
            # 清除纸张显示
            self.clearPaperDisplay()
            # self.ui.lb_endChangeTips.setHidden(False)
            self.ui.lb_endChangeTips.setText("完成本令换纸")
            self.ui.comboBadID.setEditable(True)
            self.ui.comboBadID.setFocus(True)

    def clearPaperDisplay(self):
        '''
        用于结束换纸后，清除控件的值
        :return:
        '''
        self.newCount=0
        self.badCount=0
        self.newPaperSet = []
        self.ui.comboBadID.clear()
        self.ui.comboNewID.clear()
        self.ui.lcdNewNum.display(0)
        self.ui.lcdBadNum.display(0)




    @pyqtSlot()
    def on_btnCannotScan_clicked(self):
        '''
        无法扫描损纸，需手工录入条码
        :return:
        '''
        qtCss='''
            color: rgb(53, 53, 53);
            border:1px solid rgb(200, 200,200);
            font: 30pt "黑体";
            text-align: center;
            font-weight:bold;
            '''
        # self.ui.btnCannotScan.setFocus(True)


        if self.btnCannotScan_toggle==False:  #可手工编辑
            self.ui.btnCannotScan.setText("确定")
            self.btnCannotScan_toggle=True
            qtCss+="background-color: rgb(255,255,255);"
            self.ui.comboBadID.setStyleSheet(qtCss)
            self.ui.comboBadID.setEditable(True)
            self.ui.comboBadID.lineEdit().returnPressed.connect(self.returnPressed)  #只能在启用编辑后才可以将此信号绑定
            self.ui.comboBadID.setFocus(True)
            self.ui.comboBadID.lineEdit().setStyleSheet(qtCss)

        else: #录入状态
            qtCss += "background-color: rgb(240, 240, 240);"
            self.ui.comboBadID.setStyleSheet(qtCss)
            self.ui.btnCannotScan.setText("手工录入损纸")
            self.btnCannotScan_toggle=False
            badID = self.ui.comboBadID.lineEdit().text()
            self.ui.comboBadID.setEditable(False)
            print("输入：", badID)
            idx=self.ui.comboBadID.findText(badID)
            if idx==-1 and badID !="":  #录入的没有在列表里，就添加
                # self.ui.comboBadID.addItem(badID)
                self.scanBadPaper(badID,'bad')
            c=self.ui.comboBadID.count()
            self.ui.comboBadID.setCurrentIndex(c-1)  #将添加的显示出来。

    @pyqtSlot()
    def on_lineEditBadID_editingFinished(self):
        # self.ui.btnCannotScan.setFocus(True)
        print("损纸 ID 录入")
        # if self.lineEdit.isModified():
        #     print(self.lineEdit.text())
        #     print("Editing Finished")
        # self.lineEdit.setModified(False)



    def recoverlineEditStyle(self):
        qtCss = '''
                    color: rgb(53, 53, 53);
                    background-color: rgb(240, 240, 240);
                    border:none;
                    font: 30pt "黑体";
                    text-align: center;
                    font-weight:bold;
                    '''
        self.ui.lineEditBadID.setStyleSheet(qtCss)

    def destroyScanThread(self):

        print("换纸窗口，终止扫描线程===")
        # 终止扫描守护线程
        # self.scanPortA.terminate()
        # self.scanPortB.terminate()
        self.scanPortGood.isStop = True
        # self.scanPortBad.isStop = True
        # 释放com口
        self.scanPortGood.comPort.com.close()
        # self.scanPortBad.comPort.com.close()
        # 退出线程
        self.scanPortGood.exit()
        # self.scanPortBad.exit()
        # 删除进程变量
        del self.scanPortGood
        # del self.scanPortBad

    def currentIndexChanged(self):
        # badId = self.ui.comboBadID.currentText()
        #
        #
        # # lingID=self.barcodeDB.queryLingID(self.mysqldb,badCode)
        # lingID = 1
        # if lingID is None:
        #     QMessageBox.information(self, '注意', '没有查询到该产品的条码,请检查此条码正确与否！！')
        #     idx = self.ui.comboBadID.currentIndex()
        #     self.ui.comboBadID.removeItem(idx)
        # else:
        #     idx = self.ui.comboBadID.findText(badId)
        #     # print(self.ui.comboBadID.count())
        #     print("idx:", idx)
        #     if idx == self.ui.comboBadID.count() - 1 and badId != "":
        #         self.badCount += 1
        #         self.ui.lcdBadNum.display(self.badCount)
        #
        # self.ui.comboBadID.lineEdit().selectAll()
        idx = self.ui.comboNewID.currentIndex()
        self.ui.comboNewID.setCurrentIndex(idx)
        QMessageBox.information(self,"tishi",str(idx))

    def editcombox(self):
        '''
        编辑框一旦录入字符就执行该函数，去除编辑框里的空格
        :return:
        '''

        # 可以去除编辑空里的空格
        self.enableCount = True
        str =self.ui.comboBadID.lineEdit().text().strip()
        self.ui.comboBadID.setEditText(str )
        idx = self.ui.comboBadID.findText(str)
        # self.ui.comboBadID.setCurrentIndex(idx)  此处用这句编辑会有问题
        if idx!=-1:  #找到有重复的
            self.enableCount=False
            self.ui.comboBadID.lineEdit().selectAll()

    def editNewcombox(self):
        '''
        编辑框一旦录入字符就执行该函数，去除编辑框里的空格
        :return:
        '''

        # 可以去除编辑空里的空格
        self.enableNewCount = True
        str = self.ui.comboNewID.lineEdit().text().strip()
        self.ui.comboNewID.setEditText(str)
        idx = self.ui.comboNewID.findText(str)
        # self.ui.comboNewID.setCurrentIndex(idx)  此处用这句编辑会有问题
        if idx!=-1:   #找到有重复的
            self.enableNewCount=False

            self.ui.comboNewID.lineEdit().selectAll()

    def returnPressed(self):
        '''
        损纸编辑框回车时候执行，选中编辑框里的字符。注意：回车添加字符到列表框，是自动添加，不是在此函数里处理
        :return:
        '''

        # self.ui.comboBadID.lineEdit().clear()
        badId=self.ui.comboBadID.currentText()
        print("return pressed:", badId)


        if badId.lower()==self.closeThisWindow.lower():
            self.on_btnEnd_clicked()
            return
        elif (badId.lower()== self.goodPaperIn.lower())  and  self.startChange :  #进入扫描好纸模式
            self.ui.comboNewID.setEditable(True)
            self.ui.comboNewID.setFocus(True)
            qtCss = '''
                        color: rgb(53, 53, 53);
                        border:1px solid rgb(200, 200,200);
                        font: 30pt "黑体";
                        text-align: center;
                        font-weight:bold;
                        background-color: rgb(255,255,255);
                        '''
            self.ui.comboNewID.setStyleSheet(qtCss)
            idx = self.ui.comboBadID.currentIndex()
            self.ui.comboBadID.removeItem(idx)
            self.ui.comboNewID.editTextChanged.connect(self.editNewcombox)
            self.ui.comboNewID.lineEdit().returnPressed.connect(self.returnPressedNewEdit)
            return

        if  not checkBarCode(badId):  #未通过验证规则
            idx = self.ui.comboBadID.currentIndex()
            self.ui.comboBadID.removeItem(idx)
            QMessageBox.information(self, '注意', '不是产品条码！！')
            self.ui.comboBadID.setFocus(True)
            self.ui.comboBadID.lineEdit().selectAll()
            return
        #先判断该条码是否已经在新纸框里出现，有则删除，不操作其他
        idx=self.ui.comboNewID.findText(badId)
        if idx !=-1:
            self.newCount-=1
            self.ui.lcdNewNum.display(self.newCount)
            self.ui.comboNewID.removeItem(idx)
            #由于编辑框扫描时候，会将自己也加入框中，所以也要删除刚扫描的条码
            idx = self.ui.comboBadID.currentIndex()
            self.ui.comboBadID.removeItem(idx)
            return

        lingID=self.barcodeDB.queryLingID(self .mysqldb,badId)  #查询令号

        if lingID!=self.ui.lineEditBadLingID.text() and lingID is not None and self.startChange :
            self.ui.lb_endChangeTips.setText("不是同一令！")
            idx = self.ui.comboBadID.currentIndex()
            self.ui.comboBadID.removeItem(idx)
            self.ui.comboBadID.setFocus(True)
            return
        # lingID = 1
        if lingID is None:
            QMessageBox.information(self, '注意', '没有查询到该产品的条码,请检查此条码正确与否！！')
            idx = self.ui.comboBadID.currentIndex()
            self.ui.comboBadID.removeItem(idx)
        else:
            idx = self.ui.comboBadID.findText(badId)
            print(self.ui.comboBadID.count() )
            print("idx:",idx)
            # if idx == (self.ui.comboBadID.count()-1)  :
            if self.enableCount:
                    self.ui.lb_endChangeTips.setHidden(False)
                    self.ui.lb_endChangeTips.setText("换纸中...")
                    self.ui.lineEditBadLingID.setText(lingID)
                    self.badCount += 1
                    self.ui.lcdBadNum.display(self.badCount)
                    self.startChange = True
                    self.ui.tableWidget.clear()
                    self.ui.tableWidget.setRowCount(0)
                    self.ui.comboNewID.clear()
                    self.ui.comboNewID.setEditable(False)

        self.enableCount = False

        self.ui.comboBadID.setCurrentText(badId)
        self.ui.comboBadID.lineEdit().selectAll()
        # print("press returns")
        pass

    def returnPressedNewEdit(self):
        newId = self.ui.comboNewID.currentText()
        # idx  =  self.ui.comboNewID.findText(newId)
        if  not checkBarCode(newId):  #未通过验证规则
            idx = self.ui.comboNewID.currentIndex()
            self.ui.comboNewID.removeItem(idx)
            QMessageBox.information(self, '注意', '不是产品条码！！')
            self.ui.comboNewID.setFocus(True)
            self.ui.comboNewID.lineEdit().selectAll()
            return
        print("New combx:",self.ui.comboNewID.count())

        if self.enableNewCount:
            self.changePaperByUsb(newId)
        self.enableNewCount = False
        self.ui.comboNewID.setCurrentText(newId)
        self.ui.comboNewID.lineEdit().selectAll()

    @pyqtSlot()
    def on_btnEnd_clicked(self):
        print("closed ...")
        # self.destroyScanThread()
        self.close()


        # self.timer.start(400)  # 设置计时间隔并启动,1秒
        # time.sleep(0.2)
        # self.timer1.start(400)

    def blinkLabel1(self):

        print("timer...")
        self.ui.lb_endChangeTips.setHidden(False)
        QApplication.processEvents()


    def blinkLabel(self):
        print("timer1...")
        self.badCount += 1
        self.ui.lb_endChangeTips.setHidden(True)
        QApplication.processEvents()
        if self.badCount==4:
            self.timer.stop()
            self.timer1.stop()
            self.badCount=0


    def closeEvent(self, event):
        print("changePaperDlg exit：",event)
        # self.destroyScanThread()
        # QCoreApplication.instance().quit()



if __name__=="__main__":
    app=QApplication(sys.argv)
    changePaperDlg=ChangePaperDlg('127.0.1.1','root','password','paperbarcode')
    # changePaperDlg.setMySql('127.0.0.1','root','password','paperbarcode')
    if changePaperDlg.isRun:
        changePaperDlg.show()
    sys.exit(app.exec_())