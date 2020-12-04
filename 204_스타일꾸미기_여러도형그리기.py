import sys

from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
import random

class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.pyqtUI()

    def pyqtUI(self):        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('도형그리기')
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawFigure(paint)
        paint.end()

    def drawFigure(self, paint):
        paint.setBrush(QColor(10, 255, 40))
        paint.setPen(QPen(QColor(Qt.red)))
        paint.drawRect(20, 30, 100, 100)

        paint.setBrush(QColor(10, 255, 40))
        paint.setPen(QPen(QColor(Qt.red)))
        paint.drawRoundedRect(150, 20, 100, 100, 30, 30)

        paint.setBrush(QBrush(Qt.CrossPattern))
        paint.drawRoundedRect(300, 100, 100, 100, 10, 10)

        paint.setBrush(QColor(Qt.darkGreen))
        paint.setPen(QPen(QColor(Qt.red), 2, Qt.DotLine))
        #paint.drawEllipse(150, 200, 180, 180)
        paint.drawEllipse(150, 200, 180, 220)  # 180 : width, 220 : height

app = QApplication(sys.argv)
exc = myapp()
app.exec_()