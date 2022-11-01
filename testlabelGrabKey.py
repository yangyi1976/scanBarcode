from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QLineEdit
import sys
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap


class Label(QLabel):
    def keyPressEvent(self, QKeyEvent):  # 键盘某个键被按下时调用
        #参数1  控件
        if QKeyEvent.key()== Qt.Key_A:  #判断是否按下了A键
            #key()  是普通键
            print('按下了A键')
            self.setText("A")

        if QKeyEvent.modifiers()==Qt.ControlModifier and QKeyEvent.key()== Qt.Key_A:#两键组合
            #modifiers()   判断修饰键
            #Qt.NoModifier   没有修饰键
            #Qt.ShiftModifier    Shift键被按下
            #Qt.ControlModifier    Ctrl键被按下
            #Qt.AltModifier      Alt键被按下
            print('按下了Ctrl-A键')

        if QKeyEvent.modifiers() == Qt.ControlModifier|Qt.ShiftModifier and QKeyEvent.key() == Qt.Key_A:  # 三键组合
            print('按下了Ctrl+Shift+A键')



class win(QWidget): #创建一个类，为了集成控件
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.setWindowTitle('事件学习')
        self.num=0
        self.label=Label('标签',self)
        self.label.resize(100,100)
        self.label.move(100,100)
        # self.label.grabKeyboard()   #控件开始捕获键盘
        self.edit=QLineEdit(self)
        self.label.resize(100,100)
        self.edit.setText("11111")
        # self.edit.grabKeyboard()
        self.childwin=Label(self)
        # 只有控件开始捕获键盘，控件的键盘事件才能收到消息



    def keyPressEvent(self, evt):
        print("press", evt.key())
        if evt.key() == Qt.Key_Return:
            print("press ===========a")
            self.label.setText("hui che")


if __name__=='__main__':
    app=QApplication(sys.argv)  #创建应用
    w=win()
    w.show()
    sys.exit(app.exec_())
