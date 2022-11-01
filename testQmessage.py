
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, qApp, QMessageBox

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 200)
        button = QPushButton('Click me', self)
        qApp.setStyleSheet("QMessageBox QPushButton{background-color: blue;}")
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QMessageBox.information(self, 'Notification', 'Text', QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = App()
    widget.show()
    sys.exit(app.exec_())