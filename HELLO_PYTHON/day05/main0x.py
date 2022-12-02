import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main0x.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        no1 = (int)(random()*9+1);
        no2 = (int)(random()*9+1);
        no3 = (int)(random()*9+1);
        
        while no1 == no2 or no2 == no3 or no3 == no1 :
            no2 = (int)(random()*9+1);
            no3 = (int)(random()*9+1);
        
        
        self.num1 = str(no1)
        self.num2 = str(no2)
        self.num3 = str(no3)
        
        number = self.num1 + self.num2 + self.num3
        print(number)
        
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        myNumber = self.le.text()
    
        s = 0;
        b = 0;
        
        if myNumber.find(self.num1) != -1 :
            if myNumber.find(self.num1, 0) == 0 :
                s += 1
            else :
                b += 1

        if myNumber.find(self.num2) != -1 :
            if myNumber.find(self.num2, 1) == 1 :
                s += 1
            else :
                b += 1
        if myNumber.find(self.num3) != -1 :
            if myNumber.find(self.num3, 2) == 2 :
                s += 1
            else :
                b += 1

        str_old = self.te.toPlainText()
        str_new = myNumber + " " + str(s) + "S " + str(b) + "B\n"
                
        self.te.setText(str_new + str_old)
        
        if s == 3 and b == 0 :
            QMessageBox.question(None, "결과", "추카추카", QMessageBox.Yes, QMessageBox.NoButton)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()