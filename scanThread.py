
from PyQt5.QtCore  import QThread
from PyQt5.QtCore import pyqtSignal
from getComPort import ComPort


class ScanBarThread(QThread):
    scanBar = pyqtSignal(str,str)  # 自定义扫描条码信号

    def __init__(self,com,scanType,parent=None):
        super().__init__(parent)
        try:
            self.comPort=ComPort(com)  #声明串口
        except IOError as ioerr:       #抛出串口异常
             raise ioerr

        self.scanType=scanType     #扫描纸仓类型

    def __del__(self):

        del self.comPort
        print("del scanPort")



    def run(self):
        self.isStop=False
        while not self.isStop:  #主线程会将此标志设置为Tru
            # self.sleep(1)
            strCode=self.comPort.getBarCode()

            print("waiting:",strCode)
            if strCode !=-1:
                print("@(class:scanThread)扫描获取条码:", strCode.strip())
                if self.scanType=='good':
                    self.scanBar.emit(strCode.strip(),'good')
                else:
                    self.scanBar.emit(strCode.strip(),'bad')
        self.isStop=False
