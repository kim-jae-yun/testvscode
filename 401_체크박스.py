import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt5.QtCore import Qt

class 체크박스(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cbox = QCheckBox('체크박스1', self)
        self.cbox.move(40, 30)

        self.cbox.stateChanged.connect(self.chageBox1) # 함수를 연결시켜 놓는 것

        self.cbox2 = QCheckBox('체크박스2', self)
        self.cbox2.move(150, 30)        

        self.cbox2.stateChanged.connect(self.chageBox2)   # stateChanged : 시그널이 발생한다고 함 : 6장에서 배움

        self.result = QLabel('체크 박스를 선택해주세요.', self)
        self.result.setFixedWidth(300)
        self.result.move(40, 100)

        self.cbox2.toggle()
        # - text() 체크 박스의 라벨 텍스트를 반환
        # - setText() 체크 박스의 라벨 텍스트를 설정
        # - isChecked()체크 박스의 상태를 반환 (True/False)
        # - checkState() 체크 박스의 상태를 반환 (2/1/0) (선택/변경없음/해제)
        # - toggle() 체크 박스의 상태를 변경

        self.setWindowTitle('QCheckBOx')
        self.setGeometry(300, 300, 400, 300)
        self.show() 

    def chageBox1(self, state):
        print(state)              # state : 체크가 되면 2, 체크가 안되면 2이 표시된다.
        # if state == Qt.Checked:
        if state == 2:
            self.result.setText('체크박스1이 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')

    def chageBox2(self, state):
        if state == Qt.Checked:
            self.result.setText('체크박스2가 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')

           

app = QApplication(sys.argv)
실행인스턴스 = 체크박스()
app.exec_()

