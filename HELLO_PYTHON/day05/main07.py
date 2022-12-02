import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)
        
    def myclick(self):
        a = self.leMine.text()
        b = int(random()*3)
        c = ""
        
        if b == 0 :
            c = "가위"
        elif b == 1 :
            c = "바위"
        else :
            c = "보"
        self.leCom.setText(c)
            
        result = ""
        if a == c :
            result = "비김"
        elif (a == "가위" and c == "바위") or (a == "바위" and c == "보") or (a == "보" and c == "가위") :
            result = "짐"
        else :
            result = "이김"
        self.leResult.setText(result)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()