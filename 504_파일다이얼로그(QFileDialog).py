from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QFileDialog,\
                            QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from pathlib import Path  

class 파일다이얼로그(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        self.textEdit = QTextEdit("이곳에 파일 내용이 들어갑니다.")
        self.label = QLabel("이곳에는 그림이 들어갑니다.")

        btn_open = QPushButton('파일 불러오기')
        btn_open.clicked.connect(self.loadFile)
        btn_img = QPushButton('이미지 불러오기')
        btn_img.clicked.connect(self.loadImg)
        vbox = QVBoxLayout()
        vbox.addWidget(self.textEdit)
        vbox.addWidget(btn_open)

        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(btn_img)

        self.setLayout(vbox)
        self.setGeometry(300, 100, 600, 800)
        self.setWindowTitle('QFileDialog')
        self.show()

    def loadFile(self):

        Openfile = QFileDialog.getOpenFileName(self,\
                   '파일 열기', './', filter="Python Files(*.py)")
        
        if Openfile[0]:
            f = open(Openfile[0], 'r', encoding='utf-8')
            with f:  
                data = f.read()  
                self.textEdit.setText(data) 

    def loadImg(self):
        home_dir = str(Path.home()) 

        Openfile = QFileDialog.getOpenFileName(
            self, "이미지 열기", directory=home_dir, filter="Images (*.png *.jpg)")

        self.label.setPixmap(QPixmap(Openfile[0]))

app = QApplication(sys.argv)
실행인스턴스 = 파일다이얼로그()
app.exec_()
