import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, \
                            QCheckBox, QPushButton, QGridLayout, QVBoxLayout, \
                            QMenu, QLabel, QHBoxLayout

class 그룹박스(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        img = QPixmap('img/pyqt.png')
        label = QLabel()
        label.setPixmap(img) 
        label.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.addWidget(self.RadioGroup(), 0, 0)
        grid.addWidget(self.CheckGroup(), 1, 0)
        grid.addWidget(label, 0, 1, 2, 1)
        grid.addWidget(self.PushButtonGroup(), 2, 0, 2, 2)

        self.setLayout(grid)

        self.setWindowTitle('QGroupBox')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def RadioGroup(self):
        RadioGroupBox = QGroupBox('라디오 버튼 그룹')

        radio1 = QRadioButton('Radio 버튼 1')
        radio2 = QRadioButton('Radio 버튼 2')
        radio3 = QRadioButton('Radio 버튼 3')
        radio2.setChecked(True) 

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        RadioGroupBox.setLayout(vbox)

        return RadioGroupBox  

    def CheckGroup(self):
        CheckBoxGroup = QGroupBox('체크박스 그룹')
        CheckBoxGroup.setCheckable(True)   # False이면 하위 체크박스들도 체크가 불가능
        CheckBoxGroup.setChecked(False)

        checkbox1 = QCheckBox('체크박스1')
        checkbox1.setChecked(True)
        checkbox2 = QCheckBox('체크박스2')
        # checkbox3 = QCheckBox('체크박스3')

        tristatebox = QCheckBox('체크박스4')
        tristatebox.setTristate(True)   # setTristate : 3개의 값을 가진 체크박스를 생성, 체크/미체크/네모

        hbox = QHBoxLayout()

        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        # hbox.addWidget(checkbox3)
        hbox.addWidget(tristatebox)
        CheckBoxGroup.setLayout(hbox)

        return CheckBoxGroup

    def PushButtonGroup(self):
        PushButtonGroupBox = QGroupBox('푸시버튼 그룹')
        # PushButtonGroupBox.setAlignment(Qt.AlignCenter)
        PushButtonGroupBox.setAlignment(Qt.AlignLeft)
       
        PushButton = QPushButton('기본 버튼') 
        PushButton.setStyleSheet("color: green;"
                          "border-style: solid;"
                          "border-width: 3px;"
                          "background-color: beige;"
        )

        CheckedButton = QPushButton('체크 표시 버튼')
        CheckedButton.setCheckable(True) 
        CheckedButton.setChecked(True)  

        FlatButton = QPushButton('Flat 버튼')
        FlatButton.setFlat(True)

        PopupButton = QPushButton('팝업 창 버튼') 
        menu = QMenu(self) 
        menu.addAction('옵션 1')
        menu.addAction('옵션 2')
        PopupButton.setMenu(menu) 

        vbox = QVBoxLayout()
        vbox.addWidget(PushButton)
        vbox.addWidget(CheckedButton)
        vbox.addWidget(FlatButton)
        vbox.addWidget(PopupButton)
        PushButtonGroupBox.setLayout(vbox)

        return PushButtonGroupBox        
        
app = QApplication(sys.argv)
실행인스턴스 = 그룹박스()
app.exec_()
