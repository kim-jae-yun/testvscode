import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDial

class 다이얼위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dial = QDial(self)
        self.dial.move(30, 20)

        self.dial2 = QDial(self)
        self.dial2.move(200, 20)
        self.dial2.setRange(0, 50)
        self.dial2.setNotchesVisible(True)

        self.label1 = QLabel('다이얼 1값', self)
        self.label1.move(40, 130)
        self.label2 = QLabel('다이얼 2값', self)
        self.label2.move(210, 130)

        btn = QPushButton('기본값으로 되돌리기', self)
        btn.move(150, 200)

        self.dial.valueChanged.connect(self.chageValue)
        self.dial2.valueChanged.connect(self.chageValue)

        btn.clicked.connect(self.btn_clicked)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('QDial')
        self.show()

    def btn_clicked(self):
        self.dial.setValue(0)
        self.dial2.setValue(0)

    def chageValue(self):
        self.label1.setText(str(self.dial.value()))
        self.label2.setText(str(self.dial2.value()))
        
app = QApplication(sys.argv)
실행인스턴스 = 다이얼위젯()
app.exec_()
