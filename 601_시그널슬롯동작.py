from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sys

class 시그널슬롯동작(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        self.count = 0 
        btn = QPushButton('클릭')
        btn.clicked.connect(self.changeLabel) 

        self.label = QLabel(f"{self.count} 번 눌렸습니다.")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn)
        self.setLayout(vbox)
      
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Signal and Slot')
        self.show()
  
    def changeLabel(self): 
        self.count += 1
        self.label.setText(f"{self.count} 번 눌렸습니다.")

app = QApplication(sys.argv)
실행인스턴스 = 시그널슬롯동작()
app.exec_()
