import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
                            QCalendarWidget, QPushButton
from PyQt5.QtCore import Qt, QDate

class 시간날짜편집기(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.cal = QCalendarWidget() 
        self.cal.setGridVisible(True)          # 격자표시 설정
        self.cal.setDateRange(QDate(2020, 1, 1), QDate.currentDate()) 
        self.cal.clicked[QDate].connect(self.PastDate)  

        self.label1 = QLabel(self)
        self.date = self.cal.selectedDate() 
        self.label1.setText(self.date.toString())

        self.label2 = QLabel(self) 
        previousBtn = QPushButton('이전 달')
        previousBtn.clicked.connect(self.preMonth)
        nextBtn = QPushButton('다음 달')
        nextBtn.clicked.connect(self.nextMonth)

        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(previousBtn)
        vbox.addWidget(nextBtn)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 500, 400)
        self.show()

    def PastDate(self, date):  
        self.label1.setText(date.toString()) 
        self.label2.setText(f'2020년 1월 1일부터 {QDate(2020,1,1).daysTo(date)}일이 지났습니다.') 

    def preMonth(self):
        self.cal.showPreviousMonth()

    def nextMonth(self):
        self.cal.showNextMonth()
    
app = QApplication(sys.argv)
실행인스턴스 = 시간날짜편집기()
app.exec_()
