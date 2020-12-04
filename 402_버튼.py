import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon

class 버튼(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn_1 = QPushButton(self)
        btn_1.setText('버튼1')
        btn_1.setEnabled(True)

        btn_2 = QPushButton('&Button2', self)  # Alt + B 를 입력하면 단축키가 된다.
        btn_2.setText('버튼2')
        btn_2.setEnabled(True)

        btn_3 = QPushButton('버튼3', self)
        btn_3.setIcon(QIcon('img\weniv-licat.png'))
        btn_3.move(50, 200)
        btn_3.setFixedSize(150, 50)

        btn_2.toggle()     # 표현이 실행될 때 시작되어 있는 상태로 실행할 수 있는 메서드이다.

        hbox = QHBoxLayout()
        hbox.addWidget(btn_1)
        hbox.addWidget(btn_2)
        hbox.addWidget(btn_3)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('QCheckBOx')
        self.show() 

    

           

app = QApplication(sys.argv)
실행인스턴스 = 버튼()
app.exec_()

