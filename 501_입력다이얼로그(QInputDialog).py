from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
import sys

class 입력다이얼로그(QWidget):  
    def __init__(self):
        super().__init__()
        self.day = ['월', '화', '수', '목', '금']
        self.initUI()

    def initUI(self):        
        self.btn1 = QPushButton('이름 입력', self)
        self.btn1.move(30, 30)
        self.btn1.clicked.connect(self.showDialog1)

        self.btn2 = QPushButton('요일 선택', self)
        self.btn2.move(30, 80)
        self.btn2.clicked.connect(self.showDialog2)

        self.btn3 = QPushButton('일자 선택', self)
        self.btn3.move(30, 130)
        self.btn3.clicked.connect(self.showDialog3)

        self.label1 = QLabel('이곳에 이름이 표시됩니다.', self)
        self.label1.move(130, 35)
        self.label1.setFixedSize(150, 20)

        self.label2 = QLabel('이곳에 요일이 표시됩니다.', self)
        self.label2.move(130, 85)
        self.label2.setFixedSize(150, 20)

        self.label3 = QLabel('이곳에 날짜가 표시됩니다.', self)
        self.label3.move(130, 135)
        self.label3.setFixedSize(150, 20)

        self.setWindowTitle('QInputDialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog1(self):
        text, flag = QInputDialog.getText(self, '입력창', '이름을 입력하세요.')
        if flag:
            self.label1.setText(str(text))

    def showDialog2(self):
        text, flag = QInputDialog.getItem(self, '리스트 호출 입력창',\
                                                '요일을 선택하세요', self.day)
        if flag:
            self.label2.setText(str(text))

    def showDialog3(self):
        number, flag = QInputDialog.getInt(self, "요일 선택 창",\
                                                 "요일을 선택하세요", min=1, max=31)
        if flag:
            self.label3.setText(str(number)+"일")
    
app = QApplication(sys.argv)
실행인스턴스 = 입력다이얼로그()
app.exec_()
