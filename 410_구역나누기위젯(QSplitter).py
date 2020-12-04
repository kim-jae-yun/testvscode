import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QHBoxLayout

class 구역나누기위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        top = QWidget(self)
        top.setStyleSheet('background-color : red;')

        middle = QWidget(self)
        middle.setStyleSheet('background-color : green;'
                             'border-radius : 10px;')

        bottom_left = QWidget(self)
        bottom_left.setStyleSheet('background-color : blue;'
                                  'border-style : solid;'
                                  'border-width : 3px;'
                                  'border-color : black;')
        
        bottom_right = QWidget(self)
        bottom_right.setStyleSheet('background-color : gray;'
                                  'border-style : outset;'
                                  'border-width : 4px;'
                                  'border-color : red;')

        split1 = QSplitter(Qt.Horizontal)
        split1.addWidget(bottom_left)
        split1.addWidget(bottom_right)

        split2 = QSplitter(Qt.Vertical)
        split2.addWidget(top)
        split2.addWidget(middle)
        split2.addWidget(split1)
        
        hbox.addWidget(split2)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('QSplitter')
        self.show()
        
app = QApplication(sys.argv)
실행인스턴스 = 구역나누기위젯()
app.exec_()
