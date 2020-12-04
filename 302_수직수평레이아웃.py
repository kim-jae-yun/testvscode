import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1_img = QLabel()
        label1_img.setPixmap(QPixmap('img/weniv-licat.png'))
        label1 = QLabel('내 이름은 라이캣!')

        label2_img = QLabel()
        label2_img.setPixmap(QPixmap('img/weniv-mura.png'))
        label2 = QLabel('내 이름은 뮤라!')

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        vbox1.addWidget(label1_img)
        vbox1.addWidget(label1)

        vbox2.addWidget(label2_img)
        vbox2.addWidget(label2)
        
        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)
        self.setWindowTitle('box Position')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    

app = QApplication(sys.argv)
실행인스턴스 = myapp()
app.exec_()

