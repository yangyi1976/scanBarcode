import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDialog, QComboBox, QPushButton,QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
#子类化qcombobox，便于控制失去焦点事件
class Mycombox(QComboBox):
    def focusOutEvent(self, QFocusEvent):
        print("lost focus in QMycombobox")

class Demo(QDialog):
    choice = 'a'
    choice_list = ['a','b', 'c', 'd', 'e']

    def __init__(self):
        super(Demo, self).__init__()

        self.combobox_1 = Mycombox(self)                   # 1
        # self.combobox_1=QComboBox(self)
        self.combobox_2 = QFontComboBox(self)               # 2
        self.combobox_1.setEditable(True)
        self.lineedit = QLineEdit(self)                     # 3

        self.btn=QPushButton(self)
        self.btn.setText('按钮')
        self.btn1 = QPushButton(self)
        self.btn1.setText('按钮1')
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.combobox_init()
        self.count=1
    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.v_layout.addWidget(self.combobox_2)
        self.v_layout.addWidget(self.lineedit)
        self.v_layout.addWidget(self.btn)
        self.v_layout.addWidget(self.btn1)
        self.setLayout(self.v_layout)

    def combobox_init(self):
        self.combobox_1.addItem(str(4))
        self.combobox_1.addItem(self.choice)              # 4
        self.combobox_1.addItems(self.choice_list)        # 5
        self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        # self.combobox_1.currentTextChanged.connect(lambda: self.on_combobox_func(self.combobox_1))  # 7

        self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))
        # self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

        self.combobox_1.editTextChanged.connect(self.editcombox)
        # self.btn.clicked.connect(self.additem)
        self.btn1.clicked.connect(self.on_btn_clicked)
        self.combobox_1.lineEdit().returnPressed.connect(self.returnPressed)

    def returnPressed(self):
        print("edit press return!")


    def on_btn_clicked(self):
        print("closed")
        for i in  range(self.combobox_1.count()):
            print(self.combobox_1.itemText(i))
        # self.combobox_1.setCurrentText('d')
        self.combobox_1.setCurrentIndex(5)
        self.combobox_1.clear()
        # self.close()


    def additem(self):
        print("additem....")
        self.count+=2
        self.combobox_1.addItem(str(self.count))
        print(str(self.count))
        c=self.combobox_1.count()
        print(self.combobox_1.setCurrentIndex(c-1))

    def editcombox(self):
        #可以去除编辑空里的空格
        # str =self.combobox_1.lineEdit().text()
        # self.combobox_1.setEditText(str.strip())
        print("editing combox!")


    def on_combobox_func(self, combobox):                                                             # 8
        if combobox == self.combobox_1:
            print("current Index changed")
            str=combobox.lineEdit().text()
            combobox.setEditText(str.strip())
            # combobox.addItem(str.strip()+"==")
            QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText().strip()))
        else:
            self.lineedit.setFont(combobox.currentFont())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())