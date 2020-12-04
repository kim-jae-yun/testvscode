from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class 이벤트함수(QWidget):  
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):        
        self.label = QLabel('키를 입력하세요 \n\n ESC: 종료\
                            \n F11: 위젯 300, 300위치로 옮기기\
                            \n F1: 라벨 텍스트 변경 \n 0: 위젯 100,100위치로 옮기기\
                            \n 1: 위젯 추가')

        self.label2 = QLabel()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label,alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.label2)

        self.setLayout(self.vbox)
        self.setWindowTitle('Reimplementing Event Handler')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def keyPressEvent(self,event):
        
        if event.key() == Qt.Key_Escape: 
            self.close()  

        elif event.key() == Qt.Key_F11:
            self.move(300, 300) 
            self.label.setText('키 입력하세요 \n\nESC: 종료 \nF11: 위젯 300, 300위치로 옮기기 \nF1: 라벨 텍스트 변경 \n0: 위젯 100,100위치로 옮기기 \n1: 위젯 추가')
        
        elif event.key() == Qt.Key_F1: 
            self.label.setText("F1이 눌렸어요! 되돌아가길 원하시면 0번을 눌러주세요")
        
        elif event.key() == Qt.Key_0:
            self.move(100,100)
            self.label.setText('키 입력하세요 \n\nESC: 종료 \nF11: 위젯 300, 300위치로 옮기기 \nF1: 라벨 텍스트 변경 \n0: 위젯 100,100위치로 옮기기 \n1: 위젯 추가')

    def keyReleaseEvent(self,event):

        if event.key() == Qt.Key_1: 
            # self.label2.setText('키가 눌렀다 떼어졌어요!')
            self.label2 = QLabel('키가 눌렀다 떼어졌어요!')
            self.vbox.addWidget(self.label2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    실행인스턴스 = 이벤트함수()
    app.exec_()
