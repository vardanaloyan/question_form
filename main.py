#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore



class Hello(QtGui.QWidget):
    enterPressed = QtCore.pyqtSignal()

    def __init__(self):
        super(Hello, self).__init__()
        self.initUI()
        
    def initUI(self):               
        self.setWindowTitle('Hello')  
        self.lout = QtGui.QFormLayout()  
        self.text = QtGui.QTextEdit("Hello Every one this is awesome GUI")
        self.text.setReadOnly(True)
        self.lout.addRow("", self.text)
        self.setLayout(self.lout)

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.enterPressed.emit()
        print event.key()


class Buttons(QtGui.QWidget):
    def __init__(self):
        super(Buttons, self).__init__()
        self.initUI()
        
    def initUI(self):               
        self.btn1 = QtGui.QPushButton("Question 1")
        self.btn2 = QtGui.QPushButton("Question 2")
        self.btn3 = QtGui.QPushButton("Question 3")
        self.btn4 = QtGui.QPushButton("Question 4")
        self.btn5 = QtGui.QPushButton("Question 5")
        self.btn6 = QtGui.QPushButton("Question 6")

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 0, 2)
        self.grid.addWidget(self.btn4, 1, 0)
        self.grid.addWidget(self.btn5, 1, 1)
        self.grid.addWidget(self.btn6, 1, 2)
        self.setLayout(self.grid)



class Question1(QtGui.QWidget):
    def __init__(self):
        super(Question1, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout() 
        self.question = QtGui.QTextEdit(u"The kinetic energy of a moving object is given by the formula KE=(1/2)mv**2. Where m is object’s mass and v is the velocity.") 
        self.question.setReadOnly(1)
        self.lout.addRow("Question 1", self.question)
        self.vline = QtGui.QLineEdit()
        self.lout.addRow("v", self.vline)

        self.mline = QtGui.QLineEdit()
        self.lout.addRow("m", self.mline)

        self.resline = QtGui.QLineEdit()
        self.resline.setReadOnly(1)
        self.lout.addRow("Result", self.resline)

        self.calcBtn = QtGui.QPushButton("Calculate")
        self.calcBtn.clicked.connect(self.Calculate)
        self.lout.addRow("btn", self.calcBtn)

        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)

    def Calculate(self):
        try:
            v = float(self.vline.text())
            m = float(self.mline.text())
            E = 0.5*m*v**2
            self.resline.setText("{} Jouls".format(E))
        except Exception as ex:
            self.resline.setText(ex)

class Question2(QtGui.QWidget):
    def __init__(self):
        super(Question2, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout()  
        self.lout.addRow("simple2", QtGui.QLineEdit())
        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)

class Question3(QtGui.QWidget):
    def __init__(self):
        super(Question3, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout()  
        self.lout.addRow("simple3", QtGui.QLineEdit())
        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)

class Question4(QtGui.QWidget):
    def __init__(self):
        super(Question4, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout()  
        self.lout.addRow("simple4", QtGui.QLineEdit())
        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)


class Question5(QtGui.QWidget):
    def __init__(self):
        super(Question5, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout()  
        self.lout.addRow("simple5", QtGui.QLineEdit())
        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)

class Question6(QtGui.QWidget):
    def __init__(self):
        super(Question6, self).__init__()
        self.initUI()
        
    def initUI(self):               
        # self.setWindowTitle('Question1')  
        self.lout = QtGui.QFormLayout()  
        self.lout.addRow("simple6", QtGui.QLineEdit())
        self.backBtn = QtGui.QPushButton("Back")
        self.lout.addRow("btn", self.backBtn)

        self.setLayout(self.lout)

class MainWin(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWin, self).__init__()
        self.initUI()

    def initialState(self):
        self.display(1)

    def display(self,i):
        self.Stack.setCurrentIndex(i)

    def initUI(self):               
        self.setWindowTitle('Question Form')

        self.Stack = QtGui.QStackedWidget(self)

        self.q1 = Question1()
        self.q1.backBtn.clicked.connect(self.initialState)
        self.q2 = Question2()
        self.q2.backBtn.clicked.connect(self.initialState)
        self.q3 = Question3()
        self.q3.backBtn.clicked.connect(self.initialState)
        self.q4 = Question4()
        self.q4.backBtn.clicked.connect(self.initialState)
        self.q5 = Question5()
        self.q5.backBtn.clicked.connect(self.initialState)
        self.q6 = Question6()
        self.q6.backBtn.clicked.connect(self.initialState)

        self.hello = Hello()
        self.hello.enterPressed.connect(lambda: self.display(1))

        self.buttons = Buttons()
        self.buttons.btn1.clicked.connect(lambda: self.display(2))
        self.buttons.btn2.clicked.connect(lambda: self.display(3))
        self.buttons.btn3.clicked.connect(lambda: self.display(4))
        self.buttons.btn4.clicked.connect(lambda: self.display(5))
        self.buttons.btn5.clicked.connect(lambda: self.display(6))
        self.buttons.btn6.clicked.connect(lambda: self.display(7))

        self.Stack.addWidget(self.hello)
        self.Stack.addWidget(self.buttons)
        self.Stack.addWidget(self.q1)
        self.Stack.addWidget(self.q2)
        self.Stack.addWidget(self.q3)
        self.Stack.addWidget(self.q4)
        self.Stack.addWidget(self.q5)
        self.Stack.addWidget(self.q6)

        self.setCentralWidget(self.Stack)
        self.display(0)
        self.move(500,500)
        self.show()
        


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWin()
    # ex = Question1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
