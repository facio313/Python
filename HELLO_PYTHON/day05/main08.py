import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from sympy.printing.llvmjitcode import ll

form_class = uic.loadUiType("main08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        f = int(self.le_f.text())
        l = int(self.le_l.text())
        txt = ""
        for i in range(f - 1, l) :
            for k in range(0, f) :
                txt += "★"
            f += 1
            txt += "\n"
        self.pte.setPlainText(txt)   
        
    # def drawStar(self, cnt):
    #     ret = ""
    #     for i in range(cnt) :
    #         ret += "*"
    #     ret += "\n"
    #     return ret
    #
    # def myclick(self):
    #     f = self.le_f.text()
    #     l = self.le_l.text()
    #     ff = int(f)
    #     ll = int(l)
    #     print(ff, ll)
    #     txt = ""
    #
    #     for i in range(ff, ll) :
    #         txt += self.drawStar(i)
    #     self.pte.setPlainText(txt)
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()