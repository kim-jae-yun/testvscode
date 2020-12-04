import sys
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider

class 슬라이더위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slide = QSlider(Qt.Vertical, self)
        slide.setGeometry(200, 50, 100, 200)
        slide.setTickPosition(QSlider.TicksLeft)  # Tick을 표시하지 않을 것인지, 왼쪽, 오른쪽, 양쪽에 표시할 거냐?
        '''
        - `setTickPosition` 를 활용해 수직, 수평 막대를 설정할 수 있습니다. 아래와 같이 int값으로도 표시할 수 있습니다.
        - *setTickPosition(0) = setTickPosition(QSlider.NoTicks) 틱을 표시하지 않음*
        - *setTickPosition(1) = setTickPosition(QSlider.TicksAbove) 틱을 수평슬라이더 위쪽에 표시*
        - *setTickPosition(2) = setTickPosition(QSlider.TicksBelow) 틱을 수평슬라이더 아래쪽에 표시*
        - *setTickPosition(3) = setTickPosition(QSlider.TicksBothSides) 틱을 수평슬라이더 양쪽에 표시*
        - *setTickPosition(TicksAbove) = setTickPosition(QSlider.TicksLeft) 틱을 수직슬라이더 왼쪽에 표시*
        - *setTickPosition(TicksBelow) = setTickPosition(QSlider.TicksRight) 틱을 수직슬라이더 오른쪽에 표시*
        - valueChanged[int] : 슬라이더가 움직이면 즉, 여기서는 값이 바뀌면 시그널을 보내 changeValue와 연결
        - setPixmap(QPixmap(사진 위치))
        - adjustSize() : 사이즈 자동 맞춤
        '''
        slide.valueChanged[int].connect(self.changeValue)

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('img/mute.png'))
        self.img.adjustSize()
        self.img.move(30, 70)

        self.label = QLabel(f'범위 : {slide.minimum()} ~ {slide.maximum()}', self)
        self.label.move(50, 200)

        self.label2 = QLabel(self)
        self.label2.move(50, 250)
        self.label2.setFixedWidth(30)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('QSlider')
        self.show()  

    def changeValue(self, value):
        self.label2.setText(str(value))
        if value == 0:
            self.img.setPixmap(QPixmap('img/mute.png'))
        elif 0 < value <= 30:
            self.img.setPixmap(QPixmap('img/min.png'))
        elif 30 < value <= 80:
            self.img.setPixmap(QPixmap('img/medium.png'))
        else:
            self.img.setPixmap(QPixmap('img/max.png'))
    
         
        
app = QApplication(sys.argv)
실행인스턴스 = 슬라이더위젯()
app.exec_()
