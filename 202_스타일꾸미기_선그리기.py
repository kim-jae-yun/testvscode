import sys

from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt

class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.pyqtUI()

    def pyqtUI(self):        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('QPainter!')
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawLine(paint)
        paint.end()

    def drawLine(self, paint):
        pen = QPen(Qt.blue, 4, Qt.SolidLine)
        paint.setPen(pen)
        paint.drawLine(100, 40, 400, 40)

        pen.setStyle(Qt.DashLine)
        pen.setColor(Qt.yellow)
        paint.setPen(pen)
        paint.drawLine(100, 80, 400, 80)
               
        pen.setStyle(Qt.DashDotLine)
        pen.setColor(Qt.red)
        paint.setPen(pen)
        paint.drawLine(100, 120, 400, 120)

        pen.setStyle(Qt.DashDotDotLine)
        pen.setColor(Qt.darkMagenta)
        paint.setPen(pen)
        paint.drawLine(100, 160, 400, 160)

        pen.setStyle(Qt.DotLine)
        pen.setColor(Qt.darkGreen)
        pen.setWidth(2)
        paint.setPen(pen)        
        paint.drawLine(100, 200, 400, 200)        

        pen.setStyle(Qt.CustomDashLine)  # 내가 직접 제작하는 라인
        pen.setDashPattern([4, 4, 6, 4]) # Dash, 공간, Dash, 공간
        pen.setColor(Qt.darkGray)
        pen.setWidth(8)
        paint.setPen(pen)
        paint.drawLine(100, 240, 400, 240)

app = QApplication(sys.argv)
exc = myapp()
app.exec_()