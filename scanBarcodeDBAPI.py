from datetime import datetime


from  PyQt5.QtSql import QSqlDatabase,QSqlQuery
from  PyQt5.QtWidgets import QApplication


class scanBarcodeDB(object):
    """
    数据库操作类
    """
    def createDB(self):
        """
        创建并初始化sqlite文件
        :return: 成功返回True
        """
        db=QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./DB/paperLocalDB.db')
        if not db.open():
            print('无法与数据库建立连接')
            return False
        query=QSqlQuery()
        query.exec('create table papercode(barcode varchar(20),type varchar(4),time timestamp ,'
                   'operator varchar(10),sheetNumber int,lingNumber int,state varchar(4))')

        query.exec('insert into papercode values("0000000000","good","2022-08-01 12:00:00","张三",20,499,"零头")')
        print("success")
        db.close()
        return True


    def getConnDB(self):
        """
        创建并打开sqlite数据库文件。
        :return: 返回数据库实例db
        """
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./DB/paperLocalDB.db')
        if not db.open():
            return None
        else:
            return db

    def setSqlServer(self,ip,user,pwd,dbname):
        self.sqlip=ip
        self.sqluser=user
        self.sqlpwd=pwd
        self.sqldbname=dbname

    def getConnSqlDB(self):
        sqlDB=QSqlDatabase.addDatabase('QMYSQL',"mysql57conn")  #E:\MYSQL\MYSQL 5.7
        sqlDB.setHostName(self.sqlip)
        sqlDB.setDatabaseName(self.sqldbname)
        sqlDB.setUserName(self.sqluser)
        sqlDB.setPassword(self.sqlpwd)
        sqlDB.setPort(3306)
        sqlDB.setConnectOptions( 'MYSQL_OPT_CONNECT_TIMEOUT=30')
        if not sqlDB.open():
            print("can not connect db")
            # QMessageBox.information(self, '错误', '远程数据库无法打开，请先检查网络；如若不行，连接数据库管理员！！')
            return None
        else:
            return sqlDB


    def getUserInfo(self,db,userCode):
        """
        根据用户条码从表paperuser获取用户数据
        :param db:
        :param userCode: 用户条码
        :return:
        """
        query = QSqlQuery(db)
        query.prepare('''select * from paperuser where usercode=:code''')
        query.bindValue(":code",userCode)
        query.exec()
        query.first()
        if (not query.isValid()):
            return None
        userInfo = query.record()
        return userInfo

    def addPaperRecord(self,db,paperInfo):
        """
        写入一条扫描记录
        :param db:
        :param paperInfo: 字典，纸张记录字段
        :return: 添加执行成功，返回True。
        """
        query=QSqlQuery(db)
        query.prepare('''insert into papercode values(:code,:type,:time,:operator,:sheetNum,:lingNum,:lingID,:mainLingID,:state,:info) ''')
        query.bindValue(":code",paperInfo["code"])
        query.bindValue(":type",paperInfo["type"])
        query.bindValue(":time",paperInfo["time"])
        query.bindValue(":operator",paperInfo["operator"])
        query.bindValue(":sheetNum",0)
        query.bindValue(":lingNum",paperInfo["lingNum"])
        query.bindValue(":lingID",0)
        query.bindValue(":mainLingID", 0)
        query.bindValue(":state",paperInfo["state"])
        query.bindValue(":info", "")
        print(query.executedQuery())
        return query.exec()



    def queryPaperInfo(self,db,code):
        """
        根据条码查询是否存在该条码记录，是，就返回该记录。返回记录为字典
        :param db:
        :param code:
        :return: 记录result
        """
        query=QSqlQuery(db)
        query.prepare('''select * from papercode where barcode=:code''')
        query.bindValue(":code",code)
        query.exec()
        query.first()
        if (not query.isValid()):
            return None
        result=query.record()
        return result

    def queryLingID(self,db,code):
        """
        根据条码查询是否存在该条码记录，是，就返回纸的令号
        :param db:
        :param code:
        :return: 查询到的损纸的令号
        """
        query=QSqlQuery(db)
        query.prepare('''select * from papercode where barcode=:code''')
        query.bindValue(":code",code)
        query.exec()
        query.first()
        if (not query.isValid()):
            return None
        result=query.record()
        return result.value("mainLingID")

    def queryRemainingLastPaperInfo(self,db,operator):
        """
        查询零头的好、坏纸类型最后一张纸的信息
        :param db:
        :param state:
        :param operator:
        :return:
        """
        query = QSqlQuery(db)
        query.prepare(''' SELECT barcode,type,count(*),lingNum,max(time)  FROM papercode 
                        where operator=:operator and state='零头' group by type ''')
        query.bindValue(":operator", operator)
        # query.bindValue(":state",state)
        query.exec()
        result={"bad":None,"good":None}
        while query.next():
            result[query.value(1)]=query.record()  #将查询到的按type放入字典
        # print("字典1",result['good'].value(2))
        # print("字典1", result['good'].value(0))
        # print("字典2", result['bad'].value(2))
        # print("字典2", result['bad'].value(0))
        return result





    def queryPackageSet(self,db,state):
        """
        查询状态为整令的纸张 返回 记录集的列表
        :param db:
        :return:
        """
        query = QSqlQuery(db)
        query.prepare(''' select  * from papercode where state=:state ''')
        query.bindValue(":state" , state)
        query.exec()

        # 下面计算查询到的记录集的条数
        # query.last()
        # recNum = query.at()+1
        # if recNum <2:     #小于500张，返回none
        #     return None
        #
        # query.first()
        # query.previous()
        packageSet = []
        while (query.next()):
            recList=(query.value(0),query.value(1),query.value(2),query.value(3) ,
                     query.value(4),query.value(5),query.value(6),query.value(7),query.value(8),query.value(9))
            packageSet.append(recList)
        return packageSet

    def queryLocalPaperNum(self,db,operator):
        """
        按照操作者查询本地是否有零头以及整令数量
        :param db:
        :return:
        """
        ""
        query = QSqlQuery(db)
        query.prepare(''' SELECT count(*),state,operator FROM papercode  where operator=:operator group by state ''')
        query.bindValue(":operator", operator)
        query.exec()
        paperInfo = {"零头":0,"整令":0} #纸张状态数量字典

        while (query.next()):

            paperInfo[query.value(1)] = query.value(0)
        return paperInfo


    def acountSheetNum(self,db,type):
        """
        统计该类型的数量
        :param type:
        :return: 返回该类型的数量
        """
        query = QSqlQuery(db)
        query.prepare(''' select  count(*) from papercode where type=:type''')
        query.bindValue(":type", type)
        query.exec()
        # rec = query.size()   QtSqlite 驱动不支持size方法
        recNum=query.value(0)
        return recNum

    def countSheetNumBetweenTime(self,db,startTime,endTime,mainLingID):
        query = QSqlQuery(db)
        # query.prepare(''' select  count(*) from papercode where time between :startTime and :endTime ''')
        # query.bindValue(":startTime", startTime)
        # query.bindValue(":endTiime",endTime)
        # query.bindValue(":mainLingID",mainLingID)
        # r=query.exec()
        sqlStr="select  count(*) from papercode where time between '"+startTime+"' and '"+endTime+"'  and mainLingID='"+mainLingID+"'"
        r=query.exec(sqlStr)

        query.first()
        if r == False:
            raise Exception(query.lastError().text())
        recNum = query.value(0)
        return recNum

    def delPaper(self,db,code):
        """
        删除指定条码
        :param db:
        :param code: 条码
        :return: 删除成功，返回True
        """
        query=QSqlQuery(db)
        query.prepare(''' delete from papercode where barcode=:code''')
        query.bindValue(":code",code)
        return query.exec()

    def delPaperByState(self,db,state):
        """
        根据纸张状态，删除为整令的纸张记录
        :param state:
        :return:
        """
        query = QSqlQuery(db)
        query.prepare(''' delete from papercode where state=:state''')
        query.bindValue(":state", state)
        return query.exec()

    def delPaperByType(self,db,type):
        """
        根据纸张状态，删除为整令的纸张记录
        :param state:
        :return:
        """
        query = QSqlQuery(db)
        query.prepare(''' delete from papercode where type=:type''')
        query.bindValue(":type", type)
        return query.exec()

    def delByMatchBarcode(self,db,barCodeSet):
        '''
        根据传入的一批纸张ID，删除这些paper 记录
        :param barCodeSet: 元组，批量条码
        :return:
        '''

        query = QSqlQuery(db)
        sqlStr = "delete from papercode where barcode in "
        if len(barCodeSet)==1:
            sqlStr=sqlStr+"(\'"+barCodeSet[0]+"\')"
        else:
            sqlStr = sqlStr+str(barCodeSet)
        r = query.exec(sqlStr)
        if r is False:
            raise Exception(query.lastError().text())


    def updateLingID(self,db,lastPaperId,mainLingID):
        query = QSqlQuery(db)
        sqlstr="update papercode set lingID=:lingID where mainLingID=:mainLingID"
        query.prepare(sqlstr)
        query.bindValue(":lingID",lastPaperId)
        query.bindValue(":mainLingID", mainLingID)
        r = query.exec()
        query.finish()
        return r

    def updateStateByTpye(self,db,type,lingID,operator):
        """
        根据纸张类型,操作人，更改纸张状态为----整令
        :param db:
        :param Type:
        :return:
        """
        query=QSqlQuery(db)
        sqlstr="update papercode set state=:state ,lingID=:lingID,mainLingID=:mainLingID where type=:type and operator=:operator and state = '零头'"
        query.prepare(sqlstr)
        query.bindValue(":type",type)
        query.bindValue(":lingID",lingID)
        query.bindValue(":mainLingID",lingID)
        query.bindValue(":state","整令")
        query.bindValue(":operator",operator)
        r=query.exec()
        query.finish()
        return r

    def uploadDataset(self,db,sqlDB,state):
        """
        将本地sqlite上传--->MySql服务器,两个barcode表的字段个数和顺序要一样，上传完删除本地记录。
        :param db: 本地sqlite
        :param sqlDB: MySql server
        :param type:
        :return:
        """

        datasetTuple = tuple(self.queryPackageSet(db,state)) #查询到状态为整令的记录集，转换成元组
        if len(datasetTuple)<500:   #如果<500,没查到，返回，不操作。
            return True
        query = QSqlQuery(sqlDB)
        sqlStr='insert into papercode values'
        datasetTuple=map(str,datasetTuple)
        datasetTuple=','.join(datasetTuple)
        sqlStr=sqlStr + datasetTuple
        r=query.exec(sqlStr)
        # "此处应该抛出下面的错误。"
        if r==False:
            raise Exception(query.lastError().text())
        else:
            #删除已经上传的记录
            r=self.delPaperByState(db,state)
            return r


    def insertOrUpdate(self,db,newPaperSet,mainLingID=None,operator=None):
        '''
        用于换纸操作，按照主键barcode判断，如果有，就更新mainLingID与operator字段，否则就全新插入
        :param db:
        :param newPaperSet: 要插入的新纸,二维元组。
        :param mainLingID: 主令号
        :param operator: 操作人
        :return:
        '''
        query = QSqlQuery(db)
        sqlStr="INSERT INTO papercode (barcode,type,time,operator,lingID,mainLingID,state,info) values"
        datasetTuple = map(str, newPaperSet)
        datasetTuple = ','.join(datasetTuple)
        sqlStr = sqlStr + datasetTuple
        sqlStr=sqlStr+" ON duplicate KEY UPDATE mainLingID=values(mainLingID),operator=values(operator)"
        r = query.exec(sqlStr)
        if r==False:
            raise Exception(query.lastError().text())
        return r
    def insertByLoopinsert(self,db):
        """
        批量插入利用单语句inser循环
        :param db:
        :return:
        """
        query = QSqlQuery(db)

        start = datetime.now()
        for i in range(1,20):
            query.prepare('''insert into papercode values(:code,:type,:time,:operator,:sheetNum,:lingNum,:state,:info) ''')
            query.bindValue(":code", i * 217)
            query.bindValue(":type", 'bad')
            query.bindValue(":time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            query.bindValue(":operator", '世纪之光 ' + str(i))
            query.bindValue(":sheetNum", i)
            query.bindValue(":lingNum", i)
            query.bindValue(":state", '整令')
            query.bindValue(":info","")
            r=query.exec()

            if(not r ):
                print("wrong,rownum",i)
                print(query.lastError().text())
        end = datetime.now()
        print("end", end - start)


    def insertBatch(self,db):

        """
        批量生成记录插入数据库方式一，利用将数据集的每一列变成列表，在执行execBatch，速度慢！
        :param db:
        :return:
        """
        query = QSqlQuery(db)
        sqlStr = 'insert into papercode values(?,?,?,?,?,?,?)'
        query.prepare(sqlStr)
        code=[]
        type=[]
        operator=[]
        sheetNum=[]
        lingNum = []
        time = []
        state = []
        for i in range(1,2000):
            code.append(i*2210)
            type.append('bad')
            time.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            operator.append('九九归一 '+str(i))
            sheetNum.append(i)
            lingNum.append(i)
            state.append("整令")
        query.addBindValue(code)
        query.addBindValue(type)
        query.addBindValue(time)
        query.addBindValue(operator)
        query.addBindValue(sheetNum)
        query.addBindValue(lingNum)
        query.addBindValue(state)
        start=datetime.now()
        r=query.execBatch()
        end=datetime.now()
        if(r):
            print("end",end-start)
            query.finish()
        else:
            print("wrong")
            print(query.lastError().text())


    def insertLongValues(self,sqldb):
        """
        批量生成记录插入数据库方式二，构建一个长的values数据字符串，速度超快！
        :param sqldb:
        :return:
        """

        value=" (77600,'good', '2022-10-14','选纸1',212,212,0,0,'零头','')"
        for i in range(1,497):
            code=i * 1122
            type='good'
            time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            operator='选纸1'   # + str(i)
            sheetNum=i
            lingNum=i
            lingID=0
            mainLingID=0
            state="零头"
            info=""
            value=value+","+str((code,type,time,operator,sheetNum,lingNum,lingID,mainLingID,state,info))
        query = QSqlQuery(sqldb)
        sqlStr = 'insert into papercode values'

        sqlStr = sqlStr + value
        start = datetime.now()

        r = query.exec(sqlStr)
        end = datetime.now()
        print(sqlStr)
        if (r):
            print("end", end - start)
            query.finish()
        else:
            print("wrong")
            print(query.lastError().text())

    def disableRunByTime(self,db,operator):
        """
        判断本地数据库里的零头记录的日期是否与当天一致，或者是否查到记录
        返回False，不允许运行程序，必须等待远程数据库恢复正常。
        :param db:
        :return:
        """
        query=QSqlQuery(db)
        sqlStr="select time from papercode where  operator=:operator order  by time DESC "  #降序
        query.prepare(sqlStr)
        query.bindValue(":operator",operator)
        #能查到记录，并且获取最新的时间

        if query.exec() and query.first():
            rectime = query.value(0)
            recday = datetime.strptime(rectime, '%Y-%m-%d %H:%M:%S')
            # today=datetime.now().strftime("%d") #当前时间的天。
            today = datetime.now()
            n = today - recday  #天数差

            # if n.days == 0: # 当天

            if (n.days*24 + n.seconds/3600)<  8:  # <8个小时，认为是当天，可以继续扫描,返回False
                return False
            else:
                return True
        else:
            return True

    def closeDb(self,db):
        '''
            关闭数据库连接
        '''
        db.close()



import sys


if __name__ =='__main__':

    # db=scanBarcodeDB()
    # db.createDB()
    app = QApplication(sys.argv)
    print(QSqlDatabase.drivers())

    dbo=scanBarcodeDB()
    # dbo.setSqlServer('127.0.0.1','root','password','paperbarcode')
    # sqlitedb =dbo.getConnSqlDB()
    sqlitedb=dbo.getConnDB()
    if   sqlitedb.open():
        print("open is ok")
        # dbo.insertByLoopinsert(sqlitedb)
        dbo.insertLongValues(sqlitedb)
        # dbo.insertBatch(sqlitedb)
        # paperdic=dbo.queryRemainingLastPaperInfo( sqlitedb, '长江之水 188')
        # print(paperdic)
        dbo.closeDb(sqlitedb)
        print("close")
    else:

        print("not open")
    # print(sqlDB)
    # print(sqlDB.lastError().text())


    sys.exit(app.exec_())