import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        arr = []
        for i in range(0, 6) :
            arr.append(int(random()*45 + 1))
            for j in range(0, i) :
                if arr[i] == arr[j] :
                    arr[i].append(int(random()*45 + 1))
                else :
                    pass

                    
        for k in range(0, 5) :
            for l in range(k, 6) :
                a = arr[k]
                b = arr[l]
                if a > b :
                    arr[k] = b
                    arr[l] = a
        
        print(arr)
                    
        self.le1.setText(str(arr[0]))
        self.le2.setText(str(arr[1]))
        self.le3.setText(str(arr[2]))
        self.le4.setText(str(arr[3]))
        self.le5.setText(str(arr[4]))
        self.le6.setText(str(arr[5]))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()