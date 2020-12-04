import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
                            QVBoxLayout, QSpinBox, QDoubleSpinBox

class 스핀박스(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(1000000)
        self.spinbox.setSingleStep(1000)

        self.label2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.valueChange)

        self.label3 = QLabel('QDoubleSpinBox')
        self.dSpinbox = QDoubleSpinBox()
        self.dSpinbox.setSingleStep(0.5)
        self.dSpinbox.setSuffix('달러')
        self.dSpinbox.setDecimals(1)
        self.label4 = QLabel('0')

        self.dSpinbox.valueChanged.connect(self.valueChange2)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.dSpinbox)
        vbox.addWidget(self.label4)

        self.setLayout(vbox)        

        self.setWindowTitle('QSpinBox, QDoubleSpinBox')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def valueChange(self):
        self.label2.setText(f'{self.spinbox.value()}원 ->' +
                            f'{round(self.spinbox.value()/1191, 2)}달러')

    def valueChange2(self):
        self.label4.setText(f'{self.dSpinbox.value()}달러 -> '+ 
                            f'{round(self.dSpinbox.value()*1191, 2)}원')
        
app = QApplication(sys.argv)
실행인스턴스 = 스핀박스()
app.exec_()
