import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget

class 탭버튼위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tab1 = QWidget() 
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        tabs = QTabWidget()
        
        tabs.addTab(self.tab1,'라이캣')
        tabs.addTab(self.tab2,'파이')
        tabs.addTab(self.tab3,'썬')
        tabs.setTabPosition(1)  # TabPosition : Tab이 표시되는 방향. 위쪽:0, 아래쪽:1, 왼쪽:2, 오른쪽:3, 기본=0 
        tabs.setTabShape(0)     # Shape : 모서리 라운드. 0: 작은원호, 1:큰원호/삼각형 모양에 접근, 기본=0

        tabs.tabBarClicked.connect(self.clickedTab)
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)
        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 400)
        self.show()

    def clickedTab(self,index): 
        if index == 0: 
            self.tab1.setStyleSheet('image : url(img/weniv-licat.png)')
        elif index == 1:
            self.tab2.setStyleSheet('image : url(img/weniv-pie.png)')
        else:
            self.tab3.setStyleSheet('image : url(img/weniv-sun.png)')
        
app = QApplication(sys.argv)
실행인스턴스 = 탭버튼위젯()
app.exec_()
