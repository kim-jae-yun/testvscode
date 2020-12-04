from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
import json
import requests

class 표위젯(QWidget):  
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.table = QTableWidget(150, 5, self)
        header = ['종목', '전일 종가', '변동가', '변동률', '시가']

        bithumbUrl = 'https://api.bithumb.com/public/ticker/ALL_KRW' 
        # 빗썸 오픈 API : https://apidocs.bithumb.com/docs/ticker 참고
        data = json.loads(requests.get(bithumbUrl).text)

        # print(data)
        for index, coin in enumerate(data['data']):  # data에서 data항목만 뽑아서 순서를 정해 줌
            if coin == 'date':
                break
            self.table.setItem(index, 0, QTableWidgetItem(coin)) 
            self.table.setItem(index, 1, QTableWidgetItem(data['data']\
                                         [coin]['prev_closing_price']+'원'))  # 전일종가
            self.table.setItem(index, 2, QTableWidgetItem(data['data']\
                                         [coin]['fluctate_24H']+'원'))        # 최근24시간 변동가
            self.table.setItem(index, 3, QTableWidgetItem(data['data']\
                                         [coin]['fluctate_rate_24H']+" %"))   # 최근24시간 변동률
            self.table.setItem(index, 4, QTableWidgetItem(data['data']\
                                         [coin]['opening_price']+"원"))       # 시가
        
        self.table.setHorizontalHeaderLabels(header)
        self.table.cellClicked.connect(self.showCellPosition)

        self.label = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 300, 720, 500)
        self.show()

    def showCellPosition(self):
        행 = self.table.currentColumn()
        열 = self.table.currentRow()
        self.label.setText(f'{행} 행, {열} 열입니다.')
    
app = QApplication(sys.argv)
실행인스턴스 = 표위젯()
app.exec_()
