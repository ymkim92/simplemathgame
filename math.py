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

NUM_GAME_DONE = 10

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

        # register timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showlcd)
        self.timer.start(1000)
        self.time = 0
        self.showlcd()

        self.correct = 0
        self.wrong = 0

        
    def initUI(self):      

        fontsize = 40
        self.setFont(QtGui.QFont("Droid", fontsize, QtGui.QFont.Normal))
        self.setFixedSize(500, 300)

        # Time
        self.label_time = QtGui.QLabel('Time', self)
        self.label_time.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Normal))
        self.label_time.setStyleSheet('color: blue')
        self.label_time.move(50, 20)

        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setGeometry(120, 13, 100, 50)

        self.label_o = QtGui.QLabel(self)
        self.label_o.move(220, 200)
        self.pixmap_empty = QtGui.QPixmap("png/empty.png")
        self.pixmap_correct = QtGui.QPixmap("png/correct-blue.png")
        self.pixmap_wrong = QtGui.QPixmap("png/wrong-red.png")
        self.label_o.setPixmap(self.pixmap_empty)

        self.label_score = QtGui.QLabel('0', self)
        self.label_score.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Normal))
        self.label_score.setStyleSheet('color: Green')
        self.label_score.move(300, 230)

        #########################################################################
        # Question line
        #########################################################################
        self.label1 = QtGui.QLabel('1', self)
        self.label1.move(100, 100)

        self.label2 = QtGui.QLabel('+', self)
        self.label2.move(150, 100)

        self.le = QtGui.QLineEdit(self)
        self.le.installEventFilter(self)
        self.le.setMaximumWidth(100)
        self.le.setFixedWidth(70)
        self.le.move(210, 100)
        
        self.label3 = QtGui.QLabel('=', self)
        self.label3.move(300, 100)

        self.label4 = QtGui.QLabel('1', self)
        self.label4.move(350, 100)
        #########################################################################

        self.set_question(random.randint(3, 8), 1, 10)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Math Game for Gawon')
        self.show()

        self.showDialog('')
 
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
                        self.label_o.setPixmap(self.pixmap_correct)

                        #self.label_o.setPixmap(pixmap)
                        QtCore.QTimer.singleShot(1000, lambda: self.label_o.setPixmap(self.pixmap_empty))

                        self.correct += 1
                        self.label_score.setText(str(self.correct))
                        if self.correct >= NUM_GAME_DONE:
                            self.correct = 0
                            self.wrong = 0
                            self.showDialog("Correct %d answers and wrong %d answer(s).\nIt took %d seconds.\n\n" %(NUM_GAME_DONE, self.wrong, self.time))
                    else:
                        print "Wrong"
                        self.label_o.setPixmap(self.pixmap_wrong)

                        #self.label_o.setPixmap(pixmap)
                        QtCore.QTimer.singleShot(1000, lambda: self.label_o.setPixmap(self.pixmap_empty))
                        self.wrong += 1
                    self.le.setText('')
                    self.set_question(random.randint(1, 9), 1, 10)
                                                                             

        return QtGui.QWidget.eventFilter(self, widget, event)

    def check_answer(self):
        try:
            if int(self.label4.text()) == int(self.label1.text()) + int(self.le.text()):
                return True;
            else:
                return False;

        except:
            return False;

    def showDialog(self, str_end):
        # Timer stop

        # Display dialog box
        display_string = str_end + "Do you want to start a new game?"
        reply = QtGui.QMessageBox.question(self, 'Game Dialog',
            display_string, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

        if reply == QtGui.QMessageBox.Yes:
            # Timer start
            self.time = 0
            self.label_score.setText("0")
            pass
        else:
            sys.exit(-1)


    def showlcd(self):
        text = "%02d:%02d" %(self.time/60, self.time%60)
        self.lcd.display(text)
        self.time += 1

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
