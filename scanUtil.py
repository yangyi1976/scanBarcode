from config import Config

def checkBarCode(code):

    if not code.isnumeric():  # 不是数字，返回否
        return  False

    if Config.barcodebytes=='-1': #不做验证
        return True

    if str(len(code))!=Config.barcodebytes:  #长度
        return False
    i = map(int, code)
    s=sum(i)
    if s%10==0 : #满足长度，且所有数字之和个位为0
        return True