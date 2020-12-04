import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class 라벨(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.label = QLabel(self)
        self.label.move(30, 20)

        self.inputText = QLineEdit(self)
        self.inputText.move(30, 50)
        self.inputText.textChanged[str].connect(self.changed1)       
        self.inputText.returnPressed.connect(self.changeText) 

        self.label2 = QLabel(self)
        self.label2.move(30, 100)

        self.inputText2 = QLineEdit(self)
        self.inputText2.move(30, 130)
        self.inputText2.setEchoMode(2)  # setEchoMode : 2일때는 입력된 문자대신 비밀번호용 문자로 대체
                                        # 0 : 입력값을 그대로 표시 
                                        # 1 : 표시하지 않음
                                        # 3 : 입력시에는 문자로 표시하나 수정중에는 다른 문자로 표시  
        self.inputText2.textChanged[str].connect(self.changed2)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('QLabel')
        self.show()        

    def changed1(self, text):
        print(text)
        self.label.setText('편집중입니다. 마치려면 Enter키를 눌러주세요.')
        self.label.adjustSize()
        
    def changeText(self):
        # print(self.inputText.text())
        self.label.setText(self.inputText.text())

    def changed2(self, text):
        print(text)
        self.label2.setText(text)        
        self.label2.adjustSize()        
        
app = QApplication(sys.argv)
실행인스턴스 = 라벨()
app.exec_()
