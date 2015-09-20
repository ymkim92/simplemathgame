#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial 

In this example, we receive data from
a QtGui.QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys, random
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        fontsize = 40
        layout = QtGui.QHBoxLayout(self)

        self.label1 = QtGui.QLabel('1', self)
        font = self.label1.font()
        font.setPointSize(fontsize)
        self.label1.setFont(font)
        layout.addWidget(self.label1)

        self.label2 = QtGui.QLabel('+', self)
        font = self.label2.font()
        font.setPointSize(fontsize)
        self.label2.setFont(font)
        layout.addWidget(self.label2)

        self.le = QtGui.QLineEdit(self)
        self.le.installEventFilter(self)
        font = self.le.font()
        font.setPointSize(fontsize)
        self.le.setFont(font)
        self.le.setMaximumWidth(100)
        self.le.setFixedWidth(100)
        layout.addWidget(self.le)
        
        self.label3 = QtGui.QLabel('=', self)
        font = self.label3.font()
        font.setPointSize(fontsize)
        self.label3.setFont(font)
        layout.addWidget(self.label3)

        self.label4 = QtGui.QLabel('1', self)
        font = self.label4.font()
        font.setPointSize(fontsize)
        self.label4.setFont(font)
        layout.addWidget(self.label4)

        self.set_question(random.randint(3, 8), 1, 10)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Math Game for Gawon')
        self.show()
 
    def set_question(self, first, plus, result):
        self.label1.setText(str(first))
        if plus :
            self.label2.setText('+')
        else:
            self.label2.setText('-')

        self.label4.setText(str(result))

    def eventFilter(self, widget, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            widget is self.le):
            key = event.key()
            if key == QtCore.Qt.Key_Escape:
                self.le.setText('')
            else:
                if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                    if self.check_answer():
                        print "Good"
                    else:
                        print "Wrong"
                    self.le.setText('')
                    self.set_question(random.randint(1, 9), 1, 10)
                                                                             

        return QtGui.QWidget.eventFilter(self, widget, event)

    def check_answer(self):
        if int(self.label4.text()) == int(self.label1.text()) + int(self.le.text()):
            return True;
        else:
            return False;

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
