import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class 선택단추(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn_1 = QRadioButton(self)
        btn_1.setText('버튼1')
        btn_1.move(60, 50)

        btn_2 = QRadioButton('&Button2', self)  # Alt + B 를 입력하면 단축키가 된다.
        btn_2.setText('버튼2')
        btn_2.setChecked(True)
        btn_2.move(60, 80)

        btn_3 = QRadioButton('버튼3', self)        
        btn_3.move(60, 110)
        btn_3.setAutoExclusive(False)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QRadioButton')
        self.show()

app = QApplication(sys.argv)
실행인스턴스 = 선택단추()
app.exec_()

