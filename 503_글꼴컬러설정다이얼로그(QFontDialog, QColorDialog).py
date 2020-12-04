from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,\
                            QLabel, QFontDialog, QColorDialog, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys

class 글꼴컬러설정다이얼로그(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        self.label = QLabel('안녕하세요! 제주코딩베이스 캠프 PyQt5 강좌 입니다!', self)
        self.label.setAlignment(Qt.AlignCenter) 

        btn1 = QPushButton('폰트 선택', self)
        btn1.clicked.connect(self.showFont) 

        color = QColor(Qt.black) 

        self.colorFrame = QFrame(self)
        self.colorFrame.setStyleSheet(
            f'background-color: {color.name()};')
            
        btn2 = QPushButton('색상 선택', self)
        btn2.clicked.connect(self.showColor) 

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn1)
        vbox.addWidget(self.colorFrame)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        self.setWindowTitle('QFont, QColor Dialog')
        self.setGeometry(300, 300, 450, 300)
        self.show()

    def showFont(self):
        font, flag = QFontDialog.getFont()

        if flag: 
            self.label.setFont(font)
        else:
            self.label.setText("선택 되지 않았어요! 다시 한번 선택해주세요!")

    def showColor(self):
        color = QColorDialog.getColor() 

        if color.isValid(): 
            self.colorFrame.setStyleSheet(f'background-color: {color.name()}')
           
        else: 
            self.colorFrame.setStyleSheet("image : url(img/weniv-licat.png)")

app = QApplication(sys.argv)
실행인스턴스 = 글꼴컬러설정다이얼로그()
app.exec_()
