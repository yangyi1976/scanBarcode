import sys
from PyQt5.QtWidgets import  QApplication,QWidget,QAbstractItemView
from PyQt5.QtCore import pyqtSlot,QStringListModel,Qt,QModelIndex
from testQtGui.ui_listModelWidget import Ui_Form

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.__province=["北京","上海","天津","河北","山东","四川","重庆","广东","河南"]
        self.model=QStringListModel(self)
        self.model.setStringList(self.__province)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)

    @pyqtSlot()
    def   on_btnList_Append_clicked(self):
        print("Append")
        lastRow=self.model.rowCount()
        self.model.insertRow(lastRow)
        index=self.model.index(lastRow,0)
        self.model.setData(index,"newItem广西",Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)

    @pyqtSlot()
    def on_btnList_Insert_clicked(self):
        index=self.ui.listView.currentIndex()
        self.model.insertRow(index.row())
        self.model.setData(index,"insert海南",Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)

    @pyqtSlot()
    def on_btnList_Delete_clicked(self):
        index=self.ui.listView.currentIndex()
        self.model.removeRow(index.row())

    @pyqtSlot()
    def on_btnList_Clear_clicked(self):
        count=self.model.rowCount()
        print(count)
        self.model.removeRows(0,count)

    @pyqtSlot()
    def on_btnText_Display_clicked(self):
        strList=self.model.stringList()
        self.ui.plainTextEdit.clear()
        for text in strList:
            self.ui.plainTextEdit.appendPlainText(text)

    def on_listView_clicked(self,index):
        print("当前项index：row=%d ,column=%d" %(index.row(),index.column()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec())