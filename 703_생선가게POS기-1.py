import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class 생선가게POS기(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.s = ''
        self.하나 = QPushButton('1')
        self.하나.clicked.connect(lambda:self.clickedNum('1'))

        self.더하기 = QPushButton('+')
        self.더하기.clicked.connect(lambda:self.clickedNum('+'))

        self.셋 = QPushButton('3')
        self.셋.clicked.connect(lambda:self.clickedNum('3'))

        self.등호 = QPushButton('=')
        self.등호.clicked.connect(self.calc)

        세로정렬 = QHBoxLayout() 
        세로정렬.addWidget(self.하나) 
        세로정렬.addWidget(self.더하기)
        세로정렬.addWidget(self.셋)
        세로정렬.addWidget(self.등호)
       
        self.setLayout(세로정렬)
        
        self.setWindowTitle("계산기")
        self.show()
        
    def clickedNum(self, text):
        self.s += text
        print(self.s)

    def calc(self):
        print(eval(self.s))
        self.s = ''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 생선가게POS기()
    app.exec_()
