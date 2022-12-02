import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("main09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        # self.pb0.clicked.connect(self.myclick)
        # self.pb1.clicked.connect(self.myclick)
        # self.pb2.clicked.connect(self.myclick)
        # self.pb3.clicked.connect(self.myclick)
        # self.pb4.clicked.connect(self.myclick)
        # self.pb5.clicked.connect(self.myclick)
        # self.pb6.clicked.connect(self.myclick)
        # self.pb7.clicked.connect(self.myclick)
        # self.pb8.clicked.connect(self.myclick)
        # self.pb9.clicked.connect(self.myclick)
        
        self.pbCall.clicked.connect(self.call)
    
    def myclick(self):
        self.sender().text()
        
    # def myclick(self):
    #     str_new = self.sender().text()
    #     str_old = self.le.text()
    #
    #     self.le.setText(str_old + str_new)
        
    def call(self):
        QMessageBox.question(None, "calling", self.le.text() + '로 전화거는 중', QMessageBox.Yes, QMessageBox.NoButton)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()