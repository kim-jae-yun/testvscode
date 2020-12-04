import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        insert = QPushButton('insert')
        home = QPushButton('home')
        pageUp = QPushButton('pageUp')
        delete = QPushButton('delete')
        end = QPushButton('end')
        pageDown = QPushButton('pageDown')
        keyboard = QPushButton('keyboard')

        grid = QGridLayout()
        # grid.setSpacing(15)
        grid.setSpacing(5)

        grid.addWidget(insert, 0, 0)
        grid.addWidget(home, 0, 1)
        grid.addWidget(pageUp, 0, 2)

        grid.addWidget(delete, 1, 0)
        grid.addWidget(end, 1, 1)
        grid.addWidget(pageDown, 1, 2)

        grid.addWidget(keyboard, 2, 0, 2, 3, alignment=Qt.AlignCenter) # keyboard : 추가할위젯, 2:행, 0:열, 2:확장시킬행, 3:확장시킬열
        
        self.setLayout(grid)
        self.setWindowTitle('box Position')
        self.setGeometry(300, 300, 400, 300)
        self.show()    

app = QApplication(sys.argv)
실행인스턴스 = myapp()
app.exec_()

