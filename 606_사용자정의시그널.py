from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QPushButton, QLabel, QMainWindow 
from PyQt5.QtCore import Qt, pyqtSignal, QObject 
import sys

class Signal(QObject):
    closeProgram = pyqtSignal()
    addText = pyqtSignal()

class 사용자정의시그널(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):
        self.signal1 = Signal()
        self.signal1.closeProgram.connect(self.close)

        '''
        앞에서 사용했던 예제
        btn = QPushButton('클릭')
        btn.clicked.connect(self.changeLabel) #changeLabel은 슬롯(slot)
        '''

        self.label1 = QLabel('시그널을 알아볼까요?', self)
        self.label1.setFixedSize(300, 20)
        self.label1.move(40, 100)

        self.signal2 = Signal()
        self.signal2.addText.connect(self.changelabel)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mouseDoubleClickEvent(self, event):
        self.signal1.closeProgram.emit()

    def mousePressEvent(self, event):
        self.signal2.addText.emit()

    def changelabel(self):
        self.label1.setText('마우스가 눌렸습니다!')

    def close(self):
        super().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 사용자정의시그널()
    app.exec_()
