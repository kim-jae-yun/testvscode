import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
                            QTimeEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime

class 시간날짜편집기(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        label = QLabel('QTimeEdit')
        label.setAlignment(Qt.AlignCenter)

        time = QTimeEdit(self)
        time.setTime(QTime.currentTime())
        time.setTimeRange(QTime(00, 00, 00), QTime.currentTime())
        time.setDisplayFormat('a:hh:mm:ss.zzz')

        label2 = QLabel('QDateEdit')
        label2.setAlignment(Qt.AlignCenter)

        self.date_edit = QDateEdit(self)
        self.date_edit.setDate(QDate.currentDate()) 
        self.date_edit.setDateRange(QDate(2000, 1, 1), QDate.currentDate())
        # self.date_edit.setDisplayFormat('yyyy년 MMMM d일')
        self.date_edit.dateChanged.connect(self.dateChange)        

        self.label3 = QLabel('이곳에 QDateEdit에서 선택된 값이 나타납니다.')
        self.label3.setAlignment(Qt.AlignCenter)        

        label4 = QLabel('QDateTimeEdit')
        label4.setAlignment(Qt.AlignCenter)

        label5 = QLabel(self)
        label5.setAlignment(Qt.AlignCenter)
        label5.setText(f'QDateTime \n 현재 시간은 {QDateTime.currentDateTime().toString("yyyy년 MMMM d일 ap hh시 mm분 ss초.zzz")} 입니다.')

        dt_edit = QDateTimeEdit(self)
        dt_edit.setDateTimeRange(QDateTime(2020, 1, 1, 00, 00, 00),\
                                 QDateTime(2021, 1, 1, 00, 00, 00))
        dt_edit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(time)
        vbox.addWidget(label2)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        vbox.addWidget(dt_edit)

        self.setLayout(vbox)

        self.setWindowTitle('QTime, QDateEdit, QDateTimeEdit')
        self.setGeometry(300, 300, 400, 300)
        self.show()   
    
    def dateChange(self):     
        self.label3.setText(self.date_edit.date().toString('yyyy년 MMMM d일'))        

app = QApplication(sys.argv)
실행인스턴스 = 시간날짜편집기()
app.exec_()
