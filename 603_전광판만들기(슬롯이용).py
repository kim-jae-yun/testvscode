from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication,\
                            QPushButton, QLabel
from PyQt5.QtCore import Qt, QCoreApplication
import sys

class 전광판만들기(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        lcd = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)

        self.slider.valueChanged.connect(lcd.display) 
        self.slider.valueChanged.connect(self.setValue)

        btn1 = QPushButton('초기화')
        btn2 = QPushButton('종료')

        btn1.clicked.connect(self.changeValue)  
        btn2.clicked.connect(self.exitProgram)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(self.slider, alignment=Qt.AlignCenter)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Signal and Slot')
        self.show()
    
    def changeValue(self):
        self.slider.setValue(0)
        self.label.setText(str(self.slider.value()))

    def setValue(self):
        self.label.setText(str(self.slider.value()))

    def exitProgram(self):
        QCoreApplication.instance().quit()
        # super().close() 이것도 사용가능

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 전광판만들기()
    app.exec_()
