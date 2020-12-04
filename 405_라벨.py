import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class 라벨(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_1 = QLabel(self)
        label_1.setText('라벨 1')
        label_1.setAlignment(Qt.AlignLeft)

        label_2 = QLabel('라벨 2', self)
        label_2.setAlignment(Qt.AlignRight)

        label_3 = QLabel('라벨 3', self)

        font_1 = label_1.font()
        font_1.setPointSize(15)
        font_1.setItalic(True)

        font_2 = label_2.font()
        font_2.setPointSize(20)
        font_2.setFamily('Helveltica')

        font_3 = label_3.font()
        font_3.setPointSize(30)
        font_3.setBold(True)

        label_1.setFont(font_1)
        label_2.setFont(font_2)
        label_3.setFont(font_3)

        vbox = QVBoxLayout()
        vbox.addWidget(label_1)
        vbox.addWidget(label_2)
        vbox.addWidget(label_3, alignment=Qt.AlignCenter)
        
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QLabel')
        self.show()
        
app = QApplication(sys.argv)
실행인스턴스 = 라벨()
app.exec_()

