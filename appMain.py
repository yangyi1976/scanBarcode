import sys,time,os

from datetime import datetime

from PyQt5.QtWidgets import QApplication,  QMainWindow,  QDialog, QDesktopWidget,qApp
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, Qt, pyqtSlot
from ui_scanBarcode import  Ui_MainWindow
from PyQt5.QtGui import QColor
from configparser import ConfigParser

from config import Config
from scanThread import ScanBarThread
from scanBarcodeDBAPI import scanBarcodeDB
from changePaperDlg import  ChangePaperDlg
from scanLoginDlg import ScanLoginDlg
from scanOperatorTipDlg import ScanOperatorTipDlg
from infoTipDlg import  InfoTipDlg
from changeOperatorTipDlg import ChangeOperatorTipDlg
from pickupPaperDlg import  PickupPaperDlg
from scanUtil import checkBarCode


class MyAppMain(QMainWindow):
    good_count=0
    bad_count=0
    goodPack_count=1
    badPack_count=1

    def __init__(self,userName,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_goodPack.setText(str(self. goodPack_count))
        self.ui.lineEdit_badPack.setText(str(self.badPack_count))
        self.ui.lcdCount_good.display(self.good_count)
        self.ui.lcdCount_bad.display(self.bad_count)
        # self.showMaximized()        #启动窗口时最大化
        self.setWindowTitle("选纸扫描系统")
        self.setAutoFillBackground(True)


        self.grabKeyboard()  #窗口捕获键盘事件
        self.strUsbScanCode = ""
        self.ui.lineEdit_bad.setEnabled(True)
        # self.ui.lineEdit_bad.setFocusPolicy(Qt.StrongFocus)
        # self.ui.lineEdit_bad.setFocus(True)   #不能设置为焦点，否则，键盘按下事件会被编辑框自己捕捉，由于lineedit控件没有回车键信号，
        # 所以不能响应回车操作。除非自定义编辑框，并重载键盘按下事件。

        # self.setStyleSheet("background-color:#ff00ff")
        # self.setStyleSheet("color:#00ff00")
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        p.setColor(self.foregroundRole(), Qt.red)
        self.setPalette(p)
        #窗口居中
        self.moveCenter()

        self.searchClick = False

        #配置文件
        # cfgdata=self.getCfgData()
        # #数据库配置
        # mysqlCfg=dict(cfgdata.items('mysql'))
        # self.codeCommand=dict(cfgdata.items('codecommand'))
        # self.com=dict(cfgdata.items('com'))
        #远程数据库参数
        self.dbIP = Config.dbIP  #mysqlCfg['host']
        self.dbuser = Config.dbuser #mysqlCfg['user']
        self.dbpassword = Config.dbpassword #mysqlCfg['password']
        self.database = Config.database  #mysqlCfg['database']
        #串口
        comPortGood= Config.comPortGood  #self.com['comportgood']
        # comPortBad='com4'

        self.paperInfo = {}
        self.operator=userName
        self.ui.lb_operator.setText(userName)

        qApp.setStyleSheet('''QMessageBox {background-color: red;font:28pt \"微软雅黑\"}''')
        self.infoTipDlg=InfoTipDlg( )

        #命令条码
        self.openChangepaper=Config.openChangepaper # self.codeCommand['openchangepaper']
        self.closeMainWin=Config.closeMainWin  # self.codeCommand['closemainwin']
        self.changeOperator=Config.changeOperator # self.codeCommand['changeoperator']
        self.pickupPaper=Config.pickupPaper
        #声明数据库链接实例
        self.codeDB=scanBarcodeDB()
        self.db=self.codeDB.getConnDB()
        # self.db=None
        if (self.db is None):
            # QMessageBox.information(self, '错误', '缓存无法连接，可能损坏，请先修复！')
            self.displayTipDlg('缓存数据库无法连接，可能损坏，请先修复！')


        self.codeDB.setSqlServer(self.dbIP,self.dbuser,self.dbpassword,self.database)
        self.sqldb =self.codeDB.getConnSqlDB()
        if(self.sqldb is None):
            # QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网线!'+
            #                                     '当天如已开始扫描，可以继续进行。')
            self.displayTipDlg('远程数据库无法打开! 如已开始扫描，可继续进行。')
            # 查到当天零头记录，可以继续扫描。如果没有查到，或者不是当天记录，则不允许继续扫描。
            if  self.codeDB.disableRunByTime(self.db,self.operator):
                # QMessageBox.information(self, '错误','系统暂停扫描!')
                self.displayTipDlg('系统暂停扫描!')
                return
            else: #继续扫描，存在本地，显示零头的信息。
                self.displayRemainingLastPaperInfo(True)
        else:
            #不是当天操作，令数从1开始计数
            if self.codeDB.disableRunByTime(self.db, self.operator):
                # 先删除坏仓的数据
                self.codeDB.delPaperByType(self.db, "bad")
                self.displayRemainingLastPaperInfo(False)
            else: #是当天操作， 显示零头的令数
                self.displayRemainingLastPaperInfo(True)

            #判断本地是否有整令要上传,上传后删除本地记录。
            try:
                r = self.codeDB.uploadDataset(self.db, self.sqldb, '整令')
                if not r:
                    # QMessageBox.information(self, '错误', '删除本地已上传的记录集出错')
                    self.displayTipDlg('删除本地已上传的记录集出错')
            except Exception as e:
                 # QMessageBox.information(self, '错误', '上传批量数据出错:\n %s \n %s' % (e.args[0], datetime.now()))
                 self.displayTipDlg('上传批量数据出错:\n %s \n %s' % (e.args[0], datetime.now()))
        if Config.comInstall.lower() == 'true':
            try:
                self.scanPortGood=ScanBarThread(comPortGood,'good')           #实例好仓条码扫描线程，传入类型
                self.scanPortGood.scanBar.connect(self.inputBarCode)   #关联槽函数，并接受扫描到的条码数据
            except IOError as err:
                # QMessageBox.information(self, '错误', '好仓-%s串口不能连接' %comPortGood)
                # self.infoMessageBox.setText('好仓-%s串口不能连接' %comPortGood)
                self.displayTipDlg('好仓-%s串口不能连接' %comPortGood)
        # try:
        #     self.scanPortBad = ScanBarThread(comPortBad, 'bad')  # 实例坏仓条码扫描线程
        #     self.scanPortBad.scanBar.connect(self.inputBarCode)  # 关联槽函数，并接受扫描到的坏品条码数据
        # except IOError as err:
        #     QMessageBox.about(self, '错误', '坏仓-%s串口不能连接' %comPortBad)

        # self.ui.lineEdit_bad.returnPressed.connect(self.lineEditReturnPressed)
        # self.ui.lineEdit_bad.editingFinished.connect(self.editingFinished)
        # self.ui.lineEdit_bad.textChanged.connect(self.textChanged)

        # 自定义消息提示弹出窗


    def getCfgData(self ):
        ini_file = "scan.ini"
        db_name = "mysql"

        cfg = ConfigParser()
        # 读取文件内容
        cfg.read(ini_file)

        return cfg
        # cfg.items()返回list，元素为tuple
        db_cfg = dict(cfg.items(db_name))

        # # 连接数据库
        # con = MySQL.connect(**db_cfg)
        # con.close()
        # 打印参数
        print(db_cfg['user'])

        return cfg


    def displayTipDlg(self,str):
        self.releaseKeyboard()
        self.infoTipDlg.setAlertText(str)
        self.infoTipDlg.setTopWindow(self)
        self.infoTipDlg.exec()
        self.grabKeyboard()




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

    def textChanged(self):


        print('text changed:',self.ui.lineEdit_bad.text())

    def displayRemainingLastPaperInfo(self,displayPckNum):
        '''
        查询本地是否有零头，并显示零头数量
        :param displayPckNum:
        :return:
        '''
        remainingtlastDic = self.codeDB.queryRemainingLastPaperInfo(self.db, self.operator)
        if remainingtlastDic['good']:
            self.ui.lineEdit_good.setText(remainingtlastDic['good'].value(0))  # 取条码
            self.ui.lcdCount_good.display(remainingtlastDic['good'].value(2))  # 取零头纸张数量
            self.good_count = remainingtlastDic['good'].value(2)
            if displayPckNum: #当天，需要显示令数
                self.ui.lineEdit_goodPack.setText(str(remainingtlastDic['good'].value(3)))
            else:
                self.ui.lineEdit_goodPack.setText("1")
        if remainingtlastDic['bad']:
            self.ui.lineEdit_bad.setText(remainingtlastDic['bad'].value(0))  # 取条码
            self.ui.lcdCount_bad.display(remainingtlastDic['bad'].value(2))  # 取零头纸张数量
            self.bad_count = remainingtlastDic['bad'].value(2)
            if displayPckNum:  # 当天，需要显示令数
                self.ui.lineEdit_badPack.setText(str(remainingtlastDic['bad'].value(3)))
            else:
                self.ui.lineEdit_badPack.setText("1")


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
        if self.blinkType=="bad":
            self.ui.gBoxCount_bad.setStyleSheet(qss + "background-color:" + col.name())
        else :
            self.ui.gBoxCount_good.setStyleSheet(qss+"color:rgb(0, 250, 0);background-color:"+col.name())

    color = pyqtProperty(QColor, fset=_set_color)   #定义动画颜色属性

    def blinkWin(self,type):

        # anim = QPropertyAnimation(self, b"color")
        # # anim.setTargetObject(self.ui.lineEdit_good)
        # anim.setDuration(600)
        # anim.setLoopCount(2)
        # if type=='good':
        #     anim.setStartValue(QColor(0, 255, 0))
        # else:
        #     anim.setStartValue(QColor(255, 0, 0))
        #
        # anim.setEndValue(QColor(240, 240, 240))
        # anim.start()
        # ========================================
        self.anim = QPropertyAnimation(self, b"color")
        # anim.setTargetObject(self.ui.lineEdit_good)
        self.anim.setDuration(400)
        self.anim.setLoopCount(2)
        if type == 'good':
            self.blinkType='good'
            self.anim.setStartValue(QColor(0, 255, 0))
        else:
            self.blinkType='bad'
            self.anim.setStartValue(QColor(255, 0, 0))

        # self.anim.setEndValue(QColor( 240,  240, 240))
        self.anim.setEndValue(self.palette().color(self.backgroundRole()))
        self.anim.start()

    def setPaperInfo(self,code,type,operator,lingNum,state):
        self.paperInfo["code"]=code
        self.paperInfo["type"]=type
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.paperInfo["time"]=time
        self.paperInfo["operator"]=operator
        # self.paperInfo["sheetNum"]=sheetNum
        self. paperInfo["lingNum"]=lingNum
        self.paperInfo["state"]=state
        # print(time)
        # print(lingNum)

    def lineEditReturnPressed(self):
        print("lineEditReturnpress")
        self.ui.lineEdit_bad.setText("111")

    def editingFinished(self):
        # if self.ui.lineEdit_bad.text() !="":
        #     self.ui.lineEdit_bad.clear()
        
        print("edit..",self.ui.lineEdit_bad.text())
        # self.ui.lineEdit_bad.setFocus(True)
        # self.ui.lineEdit_bad.selectAll()

    # def keyPressEvent(self, event):
    #     print("scan:",event.key())

    def keyPressEvent(self, event):
        # if self.ui.lineEdit_bad.text() !="":
        #     self.ui.lineEdit_bad.clear()

        if event.key()!=Qt.Key_Return   :
            self.strUsbScanCode+=event.text()
            print("from main:",self.strUsbScanCode)
        else:
            #判断是否触发操作命令码
            if self.strUsbScanCode.lower()==self.openChangepaper.lower():
                self.strUsbScanCode = ""
                self.on_btnChangePaper_clicked()  #打开换纸界面
                return
            elif self.strUsbScanCode.lower()==self.pickupPaper.lower(): #打开拣出未扫描纸界面
                self.strUsbScanCode=""
                self.releaseKeyboard()
                self.openPickupPaper()
                return
            elif self.strUsbScanCode.lower()==self.closeMainWin.lower(): #关闭主界面
                self.strUsbScanCode = ""
                self.releaseKeyboard()
                self.close()
                os.system('shutdown -s -t 5')
            elif self.strUsbScanCode.lower()==self.changeOperator.lower(): #切换用户
                self.strUsbScanCode = ""
                self.changeOperatorName()
                return
            elif not checkBarCode(self.strUsbScanCode):
                self.strUsbScanCode = ""
                self.displayTipDlg('不是产品条码')
                return
            self.ui.lineEdit_bad.setText(self.strUsbScanCode)
            self.inputBarCode(self.strUsbScanCode, "bad")
            self.strUsbScanCode=""
            self.ui.lineEdit_bad.clearFocus()
            print("press return")

    def openPickupPaper(self):
        # self.releaseKeyboard()
        pickupPaperDlg=PickupPaperDlg(self.dbIP, self.dbuser, self.dbpassword, self.database, self)

        pickupPaperDlg.setAttribute(Qt.WA_DeleteOnClose)
        pickupPaperDlg.closeThisWindow=self.pickupPaper
        pickupPaperDlg.setTopWindow(self)
        pickupPaperDlg.exec()

        self.grabKeyboard()
        # 重新启动扫描线程
        # if hasattr(self, 'scanPortGood'):
        #     # self.scanPortBad.comPort.com.open()
        #     # self.scanPortBad.start()
        #     self.scanPortGood.comPort.com.open()
        #     self.scanPortGood.start()

    def changeOperatorName(self):
        if self.good_count!= 500:
            self.displayTipDlg("未满500张，不能切换用户。"+str(self.good_count)+"张")
            return
        changeOperator=ChangeOperatorTipDlg()
        if   hasattr(self, 'scanPortGood') :
            self.scanPortGood.isStop = True
        self.releaseKeyboard()
        if changeOperator.exec()==QDialog.Accepted:
            self.operator=changeOperator.getUserName()
            self.ui.lb_operator.setText(self.operator)
            if hasattr(self, 'scanPortGood'):
                self.scanPortGood.start()
            self.grabKeyboard()
      

        pass

    # 将串口条码数据写入文本框中
    def inputBarCode(self,strBarcode,type):
        """
        将纸质条码数据写入数据库，并更新界面信息。先判断是否为查询状态，再判断记录是否有该纸张。
        :param strBarcode: 条码
        :param type: 好坏品类型
        :return:
        """
        maxCount=int(Config.papermaxcount)

        if not checkBarCode(strBarcode):  #条码格式未通过检测
            return

        if self.searchClick == True:
            result = self.codeDB.queryPaperInfo(self.db, strBarcode)
            self.searchType(strBarcode, result)
            return
        # 判断条码数据是否已经在数据库中
        result = self.codeDB.queryPaperInfo(self.db, strBarcode)
        mysqlResult=self.codeDB.queryPaperInfo(self.sqldb, strBarcode)
        # 如果查询到该记录，且类型一致，无操作。
        if result:
            if (type == result.value("type")):
                return
        if mysqlResult:
            if (type == mysqlResult.value("type")):
                return

        if type=='good':
            print("GOOD input-================", strBarcode)
            self.good_count+=1               # 张数+1

            if self.good_count==maxCount:           # 达到500张计数，令包+1,同时张数置为1
                try:
                    #获取第500张(每令最后一张)的条码作为令ID
                    # lingID=self.ui.lineEdit_good.text()   #此句是当>500时，取上一张（第500张）作为最后一张
                    lingID=strBarcode
                    #存储第500张
                    goodpack_count = int(self.ui.lineEdit_goodPack.text())
                    self.setPaperInfo(strBarcode, type, self.operator, goodpack_count, '零头')
                    self.storePaper(self.paperInfo, result)

                    # 纸张状态置为整令
                    self.codeDB.updateStateByTpye(self.db,type,lingID,self.operator)
                    # 上传状态为整令的数据到数据库服务器
                    r=self.codeDB.uploadDataset(self.db, self.sqldb,'整令')
                    if not r:
                        # QMessageBox.information(self, '错误', '删除本地已上传的记录集出错')
                        self.displayTipDlg('删除本地已上传的记录集出错!')

                    # "处理出错后的数据，标记是否为整令"
                except Exception as e:
                    # QMessageBox.information(self, '错误', '上传批量数据出错:\n %s \n %s' % (e.args[0],datetime.now()))
                    self.displayTipDlg('上传批量数据出错:\n %s \n %s' % (e.args[0],datetime.now()))


                # 满500，弹出提示刷人员窗口，停止扫描操作
                self.releasePort()
                self.releaseKeyboard()
                scanTipDlg=ScanOperatorTipDlg(self)
                scanTipDlg.setUserName(self.operator)
                scanTipDlg.exec()
                self.operator=scanTipDlg.getUserName()
                self.ui.lb_operator.setText(self.operator)
                self.startComPort()
                self.grabKeyboard()
                # goodpack_count=int(self.ui.lineEdit_goodPack.text())
                # goodpack_count+=1         # 令计数+1
                self.ui.lineEdit_good.setText(str(strBarcode))
                self.ui.lcdCount_good.display(self.good_count)
                self.ui.lineEdit_goodPack.setText(str(goodpack_count))
                # self.good_count = 0       # 纸张计数从启始值0开始
            else:
                if self.good_count>maxCount:
                    self.good_count=1   #重置为1
                    goodpack_count = int(self.ui.lineEdit_goodPack.text())
                    goodpack_count += 1  # 令计数+1
                    self.ui.lineEdit_goodPack.setText(str(goodpack_count))

                self.ui.lineEdit_good.setText(str(strBarcode))
                self.ui.lcdCount_good.display(self.good_count)
                goodpack_count = int(self.ui.lineEdit_goodPack.text())
                # self.blinkWin('good')
                self.setPaperInfo(strBarcode, type, self.operator, goodpack_count, '零头')
                self.storePaper(self.paperInfo, result)

        else:
            print("BAD input-================", strBarcode)
            self.bad_count+=1
            if self.bad_count>15000:
                try:
                    # 获取第500张(每令最后一张)的条码作为令ID
                    lingID = self.ui.lineEdit_good.text()
                    # 纸张状态置为整令
                    self.codeDB.updateStateByTpye(self.db, type,lingID, self.operator)
                    # 上传状态为整令的数据到数据库服务器，<500，不上传
                    r = self.codeDB.uploadDataset(self.db, self.sqldb, '整令')
                    if not r:
                        # QMessageBox.information(self, '错误', '删除本地已上传的记录集出错')
                        self.displayTipDlg('删除本地已上传的记录集出错!')

                except Exception as e:
                    # QMessageBox.information(self, '错误', '上传批量数据出错:\n %s \n %s' % (e.args[0], datetime.now()))
                    self.displayTipDlg('上传批量数据出错:\n %s \n %s' % (e.args[0], datetime.now()))

                badpack_count = int(self.ui.lineEdit_badPack.text())
                badpack_count += 1
                self.bad_count = 1
                self.ui.lcdCount_bad.display(1)
                self.ui.lineEdit_bad.setText(str(strBarcode))
                self.ui.lineEdit_badPack.setText(str(badpack_count))
            else:
                self.ui.lineEdit_bad.setText(str(strBarcode))
                self.ui.lcdCount_bad.display(self.bad_count)
                badpack_count = int(self.ui.lineEdit_badPack.text())
            self.setPaperInfo(strBarcode, type, self.operator,  badpack_count, '零头')
            self.storePaper(self.paperInfo,result)
        return


    def storePaper(self,paperInfo,result):
        """
        根据type以及是否查询到记录，进行增加记录、删除记录、或无操作。
        :param paperInfo:
        :return: True,增加了记录，Fasle无操作
        """
        papertype=paperInfo["type"]
        barcode=paperInfo["code"]
        if (result is None):
            self.blinkWin(papertype)
            self.codeDB.addPaperRecord(self.db, paperInfo)  # 无此条码，增加一条记录
            return True
        else:
            #有记录，且类型不一致，则删除原类型记录，更新界面，并按新type进行存储。

            if papertype!=result.value("type"):

                #修改界面的纸张数量与令数量
                if(papertype=='good'):
                    self.bad_count -= 1

                    self.ui.lineEdit_bad.setText('0000000000000000')
                    self.ui.lcdCount_bad.display(self.bad_count)
                else:
                    self.good_count -= 1
                    self.ui.lineEdit_good.setText('0000000000000000')
                    self.ui.lcdCount_good.display(self.good_count)

                self.codeDB.delPaper(self.db, barcode)   #删除
                self.codeDB.addPaperRecord(self.db,paperInfo)
                #可以显示删掉后最近时间即最上张的条码，暂不使用
                # lastPaper = self.codeDB.queryRemainingLastPaperInfo(self.db, self.operator)
                # self.ui.lineEdit_bad.setText(lastPaper['bad'].value(0))
                # self.ui.lineEdit_good.setText(lastPaper['good'].value(0))
                self.blinkWin(papertype)
            return True

    def closeEvent(self, event):
        # os.system("shutdown -s -t 10")  # 执行关机命令,即在点关闭按钮，执行关闭事件，不关机，确保只有扫条码命令关机
        self.codeDB.closeDb(self.db)
        self.codeDB.closeDb(self.sqldb)
        self.releasePort()
        event.accept()



        # 默认直接调用QMessageBox.question 弹出询问的方法
        # reply = QMessageBox.question(self,  '本程序', "是否要退出程序？",
        #                                        QMessageBox.Yes | QMessageBox.No,
        #                                        QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     event.accept()
        #     self.codeDB.closeDb(self.db)
        #     self.close()
        #
        # else:
        #     event.ignore()
        #     # 最小化到托盘
        #     # self.setWindowFlags( Qt.SplashScreen |  Qt.FramelessWindowHint)
        #     # self.showMinimized()

    @pyqtSlot()
    def on_btnSearch_clicked(self):
        """
        进入查询状态，扫描结果只能显示在搜索框里。
        :return:
        """
        self.ui.textEdit_search.setEnabled(True)
        self.ui.textEdit_search.setFocus(True)
        self.searchClick=True

    @pyqtSlot()
    def on_btnSetup_clicked(self):
        print("setup:::::::::::::::::::")



    @pyqtSlot()
    def on_btnChangePaper_clicked(self):
        '''
        换纸操作按钮
        :return:
        '''
        #s释放串口
        self.releasePort()
        self.releaseKeyboard()  #释放键盘监听
        changePpDlg=ChangePaperDlg(self.dbIP,self.dbuser,self.dbpassword,self.database,self)
        changePpDlg.setAttribute(Qt.WA_DeleteOnClose)
        changePpDlg.setOperator(self.operator) #传入操作人员
        changePpDlg.closeThisWindow=self.openChangepaper
        #
        if changePpDlg.isRun:
            changePpDlg.exec()

        print("changPaper closed")
        # self.ui.lineEdit_bad.setFocus(True)
        self.grabKeyboard()
        # 重新启动扫描线程
        if hasattr(self, 'scanPortGood'):
            # self.scanPortBad.comPort.com.open()
            # self.scanPortBad.start()
            self.scanPortGood.comPort.com.open()
            self.scanPortGood.start()


    def startComPort(self):
        '''
        打开串口，并启动串口扫描线程
        :return:
        '''
        if hasattr(self, 'scanPortGood'):
            self.scanPortGood.comPort.com.open()
            self.scanPortGood.start()


    def releasePort(self):
        # 停止扫描线程
        if   hasattr(self, 'scanPortGood'):   # and not hasattr(self, 'scanPortB'):
            self.scanPortGood.isStop = True
            # self.scanPortBad.isStop = True
            # 关闭（释放）串口
            # self.scanPortBad.comPort.com.close()
            self.scanPortGood.comPort.com.close()
            # 退出线程
            # self.scanPortBad.exit()
            self.scanPortGood.exit()


    def searchType(self,code,result):
        '''
        显示查询的条码，及对应的类型，并设置颜色。由扫描程序调用
        :param code:
        :param searchType:
        :return:
        '''
        if(result is None):
            searchText="无此条码"
            textColor="rgb(0,0,240)"
        else:
            searchType= result.value("type")
            searchText = "好品" if searchType == "good" else "坏品"
            textColor="rgb(0, 255, 0);" if searchType=="good" else "rgb(53, 53, 53);"
        qssStyle='''
            font: 40pt "黑体";
            text-align: center;
            padding:15px 0;
            font-weight:bold;
            '''+ "color:"+textColor
        print(qssStyle)
        self.ui.label_paperType.setStyleSheet(qssStyle)
        self.ui.textEdit_search.setStyleSheet(qssStyle)
        self.ui.textEdit_search.setText(code)
        self.ui.label_paperType.setText(searchText)
        self.ui.textEdit_search.setEnabled(False)
        self.searchClick = False
        return

if  __name__=="__main__":
    app=QApplication(sys.argv)

    #
    # appMain = MyAppMain('选纸1')
    # # cfgdata=appMain.getCfgData()
    #
    # appMain.show()
    # appMain.scanPortGood.start()
    # appMain.scanPortBad.start()

    time.sleep(4)

    loginDlg = ScanLoginDlg()
    loginDlg.dbIP=Config.dbIP
    loginDlg.dbuser=Config.dbuser
    loginDlg.dbpassword = Config.dbpassword
    loginDlg.database = Config.database

    if loginDlg.exec()==QDialog.Accepted:

        userName=loginDlg.getUserName()
        appMain = MyAppMain(userName)
        appMain.ui.lb_operator.setText(userName)
        appMain.show()
        if   hasattr( appMain, 'scanPortGood'): # and not hasattr( appMain, 'scanPortB'):
            appMain.scanPortGood.start()
            # appMain.scanPortBad.start()
            print("scaning。。。。 ")
        else:
            print("no com,stop scaning")
    else:
        print("close login")
        loginDlg.destroy()


    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # mainWin = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainWin)
    # widget.show()
    # sys.exit(app.exec_())



