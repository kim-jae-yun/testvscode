import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import urllib.request

class 그림위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.img = QPixmap()    
        # url ='http://www.paullab.co.kr/images/logo_weniv.png'
        url = 'http://paullab.co.kr/images/logo_weniv.png'
        webImg = urllib.request.urlopen(url).read()
        # print(webImg)
        self.img.loadFromData(webImg) # Text로 가져온 값들을 조립하는 과정이 있어야함
       
        self.label_img = QLabel()  
        self.label_img.setPixmap(self.img)
        self.label_img.setAlignment(Qt.AlignCenter)
        self.label_size = QLabel(f'가로 : {self.img.width()}/세로 : {self.img.height()}')  
        self.label_size.setAlignment(Qt.AlignCenter)

        loadBtn = QPushButton('이미지 변경')
        loadBtn.clicked.connect(self.changeImage)

        saveBtn = QPushButton('저장')
        saveBtn.clicked.connect(self.saveImage)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_img)
        vbox.addWidget(self.label_size)
        vbox.addWidget(loadBtn)
        vbox.addWidget(saveBtn)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.setGeometry(300, 300, 400, 300)
        self.show()   
   
    def changeImage(self):
        self.img.load('img/weniv-mura.png')
        self.label_img.setPixmap(self.img)
        self.label_size.setText(f'가로 : {self.img.width()}/세로 : {self.img.height()}') 

    def saveImage(self):
        self.img = self.label_img.pixmap() 
        self.img.save('저장된 이미지.png')
        
app = QApplication(sys.argv)
실행인스턴스 = 그림위젯()
app.exec_()
