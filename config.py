from configparser import ConfigParser


def getCfgData():
    ini_file = "scan.ini"
    cfg = ConfigParser()
    # 读取文件内容
    cfg.read(ini_file)
    return cfg

class Config:
    cfgdata = getCfgData()
    # 数据库配置
    mysqlCfg = dict(cfgdata.items('mysql'))
    codeCommand = dict(cfgdata.items('codecommand'))
    com = dict(cfgdata.items('com'))
    util= dict(cfgdata.items('scanutil'))

    # 远程数据库参数
    dbIP = mysqlCfg['host']
    dbuser = mysqlCfg['user']
    dbpassword = mysqlCfg['password']
    database = mysqlCfg['database']
    # 串口
    comPortGood = com['comportgood']
    #条码命令
    openChangepaper=codeCommand['openchangepaper']
    closeMainWin=codeCommand['closemainwin']
    changeOperator=codeCommand['changeoperator']
    goodPaperIn=codeCommand['goodpaperin']
    pickupPaper=codeCommand['pickuppaper']
    #检测
    barcodebytes=util['barcodebytes']
    papermaxcount=util['papermaxcount']
    comInstall=util['cominstall']

if __name__ == '__main__':
    print(Config.openChangepaper)
    print(Config.dbuser)
    print(Config.pickupPaper)