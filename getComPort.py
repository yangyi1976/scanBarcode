# encoding=utf-8
import serial

import time
class ComPort(object):
    def __init__(self,com_num):
        try:
            self.com=serial.Serial(com_num,115200)

        except(OSError,serial.SerialException):
             raise serial.SerialException

    # def __del__(self):
    #     """
    #     析构函数，释放串口
    #     :return:
    #     """
    #     # self.com.close()
    #     # print("closed com")

    def getBarCode(self):
        try:
            n=self.com.in_waiting

        except:
            print("inWaiting is error!!!!!")
            return -1
        if n != 0:
            print('get data from serial port:', n,self.com.port)
            # data = self.com.read(n+2)
            data=self.com.readline()
            strBarCode=data.decode('UTF-8')
            print('  data length:', len(data))
            self.com.reset_input_buffer()
            return strBarCode
        else:
            return -1

if __name__ == '__main__':
    com=ComPort('com3')
    com4=ComPort('com4')
    while True:
        code=com.getBarCode()
        code4=com4.getBarCode()
        if code!=-1:

            print(code)

        # print(1)







#  #==========================================
# if __name__ == '__main__':
#   com3 = serial.Serial('COM3', 115200)
#   # com4 = serial.Serial('COM4', 115200)
#
#   # com3.write('$$$$'.encode('UTF-8'))
#   # data = com3.read(4)
#
# while True:
#     n = com3.inWaiting()  # 获取接收到的数据长度
#
#     if n:
#       # 读取数据并将数据存入data
#       print(n)
#       data = com3.read(n+2)
#       # 输出接收到的数据
#       print('get data from serial port:', data.decode('UTF-8'))
#       # 显示data的类型，便于如果出错时检查错误
#       # print(type(data))
#
#
#     # print(data.decode('UTF-8'))
#     # data = com4.read(15)
#     # print(data)
#
