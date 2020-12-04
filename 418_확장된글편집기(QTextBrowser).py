import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QTextBrowser, QLineEdit
from PyQt5.QtCore import Qt

class 확장된글편집기(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.addText)

        self.btn_add = QPushButton('입력')
        self.btn_add.clicked.connect(self.addText)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.append('일반 플래인 텍스트입니다.')

        self.tb.setAlignment(Qt.AlignCenter)
        self.btn_clear = QPushButton('지우기')
        self.btn_clear.clicked.connect(self.clearText)

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.btn_add)
        vbox.addWidget(self.btn_clear)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 400)
        self.show()

    def addText(self):
        text = self.line_edit.text()
        self.tb.append(text)
        self.line_edit.clear()

    def clearText(self):
        self.tb.clear()
    
app = QApplication(sys.argv)
실행인스턴스 = 확장된글편집기()
app.exec_()
