import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = int(self.le.text())
        result = ""
        for i in range(1, 10) :
            result += "{} * {} = {}".format(a, i, a*i) + "\n"
            # f"{a}*{i}={result}" python 3.5부터 생김
        self.tv.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()