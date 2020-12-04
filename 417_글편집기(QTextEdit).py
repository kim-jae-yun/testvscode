import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class 글편집기(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.label1 = QLabel('텍스트 편집기')
        self.text_edit = QTextEdit()
        
        self.text_edit.setAcceptRichText(False)
        self.label2 = QLabel('글자수를 세어볼까요?')
        btn_clear = QPushButton('내용 지우기') 
        btn_color = QPushButton('빨간색으로 변경')

        btn_clear.clicked.connect(self.clear_text)  
        btn_color.clicked.connect(self.change_color)  
        self.text_edit.textChanged.connect(self.check_text_lengh)  

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.label2)
        vbox.addWidget(btn_clear)
        vbox.addWidget(btn_color)

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def check_text_lengh(self):
        text = self.text_edit.toPlainText()  
        self.label2.setText(f'글자수는 : {len(text)} 입니다.')

    def clear_text(self):
        self.text_edit.clear() 

    def change_color(self):
        self.text_edit.setTextColor(QColor(252, 32, 12))
    
app = QApplication(sys.argv)
실행인스턴스 = 글편집기()
app.exec_()
