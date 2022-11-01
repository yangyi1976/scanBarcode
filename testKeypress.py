import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QApplication, QWidget


class DemoKeyboardEvent(QWidget):
    def __init__(self, parent=None):
        super(DemoKeyboardEvent, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: 键盘按键事件演示')
        # 设置窗口大小
        self.resize(400, 320)

        self.key = ''

    # 重绘窗口事件
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont(self.font().family(), 36))
        painter.setPen(QPen(Qt.blue))
        painter.setRenderHint(QPainter.TextAntialiasing)

        # 居中绘制文本信息
        painter.drawText(self.rect(), Qt.AlignCenter, self.key)

        # 键盘按键事件

    def keyPressEvent(self, event):
        self.key = ''
        if event.key() == Qt.Key_Home:
            self.key = 'Home'
        elif event.key() == Qt.Key_End:
            self.key = 'End'
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageDown"
            else:
                self.key = "PageDown"
        elif Qt.Key_0 <= event.key() <= Qt.Key_9:
            self.key = event.text()
        elif Qt.Key_A <= event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()

        # 如果key有字符，不为空，则绘制字符
        if self.key:
            self.update()
        # 否则就继续监视这个事件
        # else:
            # QWidget.keyPressEvent(self, event)

    # Tab键由于涉及焦点切换，不会传递给keyPressEvent，因此，需要在这里重新定义。
    def event(self, event):
        # 如果有按键按下，并且按键是tab键
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            self.key = "Tab"
            self.update()
            return True
        return QWidget.event(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoKeyboardEvent()
    window.show()
    sys.exit(app.exec())
