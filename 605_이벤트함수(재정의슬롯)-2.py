from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class 이벤트함수(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        x = 0
        y = 0

        self.location = f"x좌표는 : {x}, y좌표는 : {y}" 
        self.label1 = QLabel(self.location, self)
        self.label1.setFont(QFont("Decorative",20))
        self.label2 = QLabel("마우스를 클릭 또는 더블클릭 해보세요")

        self.setMouseTracking(True) 

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.setLayout(self.vbox)
        self.setWindowTitle('Reimplementing Event Handler2')
        self.setGeometry(300, 300, 400, 300)
        self.show()
   
    def mousePressEvent(self, event):
        self.label2.setText('마우스를 클릭했습니다.')

    def mouseDoubleClickEvent(self, event):
        self.label2.setText('마우스를 더블클릭했습니다.')

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        location = 'x좌표는 : {0}, y좌표는 : {1}'.format(x, y) 

        self.label1.setText(location)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 이벤트함수()
    app.exec_()
