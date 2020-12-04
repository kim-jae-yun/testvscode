from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys

class 입력다이얼로그(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        btn = QPushButton('프로그램 종료',self)
        btn.clicked.connect(self.close)  
        btn.move(20, 50)

        btn2 = QPushButton("에러 발생",self)
        btn2.move(130,50)
        btn2.clicked.connect(self.critical)

        btn3 = QPushButton("경고 발생",self)
        btn3.move(240,50)
        btn3.clicked.connect(self.warning)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 350, 200)
        self.show()

    def close(self): 

        question = QMessageBox.question(self, '질문 메세지 창',\
                               '정말 종료하시겠습니까?',\
                               QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        
        if question == QMessageBox.Yes: 
            super().close()
          
    def critical(self):
        cri = QMessageBox.critical(self, '에러 창',\
                               '심각한 에러가 생겼습니다.',\
                               QMessageBox.Help| QMessageBox.Reset | QMessageBox.Apply)

    def warning(self):
        warn = QMessageBox.warning(self, "경고 창",\
                               '에러가 날 수 있는 문제가 생겼습니다.',\
                               QMessageBox.Ok|QMessageBox.Retry|QMessageBox.Ignore)
    
app = QApplication(sys.argv)
실행인스턴스 = 입력다이얼로그()
app.exec_()
