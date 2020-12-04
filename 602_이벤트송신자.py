from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sys

class 이벤트송신자(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        self.btn1 = QPushButton("버튼 1" )
        self.btn2 = QPushButton("버튼 2" )

        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2.clicked.connect(self.buttonClicked)

        self.label = QLabel('누가 시그널을 보냈을까?')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label,alignment=Qt.AlignCenter)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Event Sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.label.setText(sender.text() + '이 보냈습니다.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 이벤트송신자()
    app.exec_()
