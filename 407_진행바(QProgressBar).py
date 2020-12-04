import sys
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QPushButton

class 진행바(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.bar1 = QProgressBar(self)
        self.bar1.setOrientation(Qt.Vertical)  #Horizontal
        self.bar1.setGeometry(50, 50, 50, 300) # (x, y, width, height)

        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(150, 200, 250, 30) # (x, y, width, height)
        self.bar2.setRange(0, 50)

        self.label1 = QLabel(f'이 바의 범위는 {self.bar2.minimum()} 부터 {self.bar2.maximum()} 입니다.', self)
        self.label1.move(170, 240)

        self.label2 = QLabel('이 곳에 첫 번째 바의 값이 나옵니다.', self)
        self.label2.move(50, 360)

        self.btn = QPushButton('시작', self)
        self.btn.move(50, 390)
        self.btn.clicked.connect(self.runTimer)

        self.value = 0
        self.timer = QBasicTimer()
        self.bar1.valueChanged.connect(self.changeValue)        

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('QProgressBar')
        self.show()  

    def runTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('시작')
        else:
            self.timer.start(self.bar1.maximum(), self)
            self.btn.setText('중지')
    
    def timerEvent(self, event):
        if self.value >= self.bar1.maximum():
            self.timer.stop()
            self.btn.setText('완료')
            return
        self.value += 1
        self.bar1.setValue(self.value)
    
    def changeValue(self):
        self.label2.setText(str(self.bar1.value()))
         
        
app = QApplication(sys.argv)
실행인스턴스 = 진행바()
app.exec_()
