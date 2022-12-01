import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = self.leMine.text()
        print(a)
        
        b = random() # 여기 문제
        c = ""
        if b > 0.5 :
            c = "짝"
        else :
            c = "홀"
        
        self.leCom.setText(c)
        
        if a == c :
            self.leResult.setText("이김")
        else :
            self.leResult.setText("짐")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()