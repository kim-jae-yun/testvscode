import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class 옵션선택창(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('옵션을 선택해주세요.', self) 
        self.label.move(20, 80)
        self.label.setFixedSize(300,20)

        self.cbox = QComboBox(self) 
        self.cbox.addItem('Option 1') 
        self.cbox.addItem('Option 2')
        self.cbox.addItem('Option 3')
        self.cbox.addItem('Option 4')

        self.cbox.move(40,40)

        self.cbox.activated[str].connect(self.clicked)
        
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def clicked(self): 
        index = str(self.cbox.currentIndex()) 
        text = str(self.cbox.currentText())  
        # self.label.setText("아이템의 " + index + "번째에 있는 "+ text + "를 선택했습니다.") 
        self.label.setText(f"아이템의 {index}번째에 있는 {text}를 선택했습니다.") 
        self.adjustSize()    # adjustSize : 라벨크기를 자동조절, 이경우는 창크기도 같이 조절될 수 있다.
        
app = QApplication(sys.argv)
실행인스턴스 = 옵션선택창()
app.exec_()

