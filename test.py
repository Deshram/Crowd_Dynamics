# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#

#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from test2 import Ui_OtherWindow
import time
import random
from PyQt5.QtCore import QTimer

class Ui_MainWindow(object):
    
    def getValue(self):
            random1 = random.randint(0,100)
            random2= random.randint(0,100)
            random3= random.randint(0,100)
            random4= random.randint(0,100)
            random5= random.randint(0,100)
            random6= random.randint(0,100)
            random7= random.randint(0,100)
            random8= random.randint(0,100)
            random9= random.randint(0,100)
            random10= random.randint(0,100)
            random11= random.randint(0,100)
            random12= random.randint(0,100)
            self.count1.setText(str(random1))
            self.count2.setText(str(random2))
            self.count3.setText(str(random3))
            self.count4.setText(str(random4))
            self.count5.setText(str(random5))
            self.count6.setText(str(random6)) 
            self.expected1.setText(str(random7))
            self.expected2.setText(str(random8))
            self.expected3.setText(str(random9))
            self.expected4.setText(str(random10))
            self.expected5.setText(str(random11))
            self.expected6.setText(str(random12))      
    def openWindow(self):

        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OtherWindow(self.count1.toPlainText(),self.count2.toPlainText(),self.count3.toPlainText(),self.count4.toPlainText(),self.count5.toPlainText(),self.count6.toPlainText(),self.expected1.toPlainText(),
                               self.expected2.toPlainText(),self.expected3.toPlainText(),self.expected4.toPlainText(),self.expected5.toPlainText(),
                               self.expected6.toPlainText(),self.area1.toPlainText(),self.area2.toPlainText(),self.area3.toPlainText(),self.area4.toPlainText(),self.area5.toPlainText(),
                               self.area6.toPlainText())
        self.ui.setupUi(self.window)
        self.window.show()
        
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 81, 20))
        self.label.setObjectName("label")
        
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(280, 470, 211, 41))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.openWindow)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 43, 31, 20))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 0, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 821, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 390, 811, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.count1 = QtWidgets.QTextEdit(self.centralwidget)
        self.count1.setGeometry(QtCore.QRect(60, 40, 104, 21))
        self.count1.setObjectName("count1")
        
        self.count1.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 80, 31, 20))
        self.label_3.setObjectName("label_3")
        self.area1 = QtWidgets.QTextEdit(self.centralwidget)
        self.area1.setGeometry(QtCore.QRect(60, 80, 104, 21))
        self.area1.setObjectName("area1")
        self.areaint1=30
        self.area1.setText(str(self.areaint1))
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(473, 0, 20, 401))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.train_arrives = QtWidgets.QLabel(self.centralwidget)
        self.train_arrives.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.train_arrives.setObjectName("train_arrives")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 141, 16))
        self.label_5.setObjectName("label_5")
        self.expected1 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected1.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.expected1.setObjectName("expected1")
        
        self.expected1.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 40, 47, 13))
        self.label_6.setObjectName("label_6")
        self.count2 = QtWidgets.QTextEdit(self.centralwidget)
        self.count2.setGeometry(QtCore.QRect(320, 40, 104, 21))
        self.count2.setObjectName("count2")
        
        self.count2.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
    
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 80, 47, 13))
        self.label_7.setObjectName("label_7")
        self.area2 = QtWidgets.QTextEdit(self.centralwidget)
        self.area2.setGeometry(QtCore.QRect(320, 80, 104, 21))
        self.area2.setObjectName("area2")
        
        self.areaint2=35
        self.area2.setText(str(self.areaint2))
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 120, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 140, 141, 16))
        self.label_9.setObjectName("label_9")
        self.expected2 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected2.setGeometry(QtCore.QRect(240, 160, 151, 31))
        self.expected2.setObjectName("expected2")
        
        self.expected2.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(620, 20, 47, 13))
        self.label_26.setObjectName("label_26")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(520, 50, 47, 13))
        self.label_10.setObjectName("label_10")
        self.count3 = QtWidgets.QTextEdit(self.centralwidget)
        self.count3.setGeometry(QtCore.QRect(600, 50, 104, 21))
        self.count3.setObjectName("count3")
        
        self.count3.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 90, 47, 13))
        self.label_11.setObjectName("label_11")
        self.area3 = QtWidgets.QTextEdit(self.centralwidget)
        self.area3.setGeometry(QtCore.QRect(600, 90, 104, 21))
        self.area3.setObjectName("area3")
        
        self.areaint3=35
        self.area3.setText(str(self.areaint3))
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(510, 120, 81, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 140, 141, 16))
        self.label_13.setObjectName("label_13")
        self.expected3 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected3.setGeometry(QtCore.QRect(510, 160, 161, 31))
        self.expected3.setObjectName("expected3")
        
        self.expected3.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(80, 220, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(330, 220, 47, 13))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(590, 220, 47, 13))
        self.label_29.setObjectName("label_29")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 240, 31, 20))
        self.label_14.setObjectName("label_14")
        self.count4 = QtWidgets.QTextEdit(self.centralwidget)
        self.count4.setGeometry(QtCore.QRect(70, 240, 104, 21))
        self.count4.setObjectName("count4")
        
        self.count4.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 270, 31, 20))
        self.label_15.setObjectName("label_15")
        self.area4 = QtWidgets.QTextEdit(self.centralwidget)
        self.area4.setGeometry(QtCore.QRect(70, 270, 104, 21))
        self.area4.setObjectName("area4")
        
        self.areaint4=30
        self.area4.setText(str(self.areaint4))
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 300, 81, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 320, 141, 16))
        self.label_17.setObjectName("label_17")
        self.expected4 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected4.setGeometry(QtCore.QRect(20, 350, 151, 31))
        self.expected4.setObjectName("expected4")
        
        self.expected4.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 240, 31, 20))
        self.label_18.setObjectName("label_18")
        self.count5 = QtWidgets.QTextEdit(self.centralwidget)
        self.count5.setGeometry(QtCore.QRect(310, 240, 104, 21))
        self.count5.setObjectName("count5")
        
        self.count5.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(250, 270, 31, 20))
        self.label_19.setObjectName("label_19")
        self.area5 = QtWidgets.QTextEdit(self.centralwidget)
        self.area5.setGeometry(QtCore.QRect(310, 270, 104, 21))
        self.area5.setObjectName("area5")
        
        self.areaint5=40
        self.area5.setText(str(self.areaint5))
        
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(250, 300, 81, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(250, 320, 141, 16))
        self.label_21.setObjectName("label_21")
        self.expected5 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected5.setGeometry(QtCore.QRect(250, 350, 151, 31))
        self.expected5.setObjectName("expected5")
        
        self.expected5.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(520, 240, 31, 20))
        self.label_22.setObjectName("label_22")
        self.count6 = QtWidgets.QTextEdit(self.centralwidget)
        self.count6.setGeometry(QtCore.QRect(570, 240, 104, 21))
        self.count6.setObjectName("count6")
        
        self.count6.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(520, 270, 31, 20))
        self.label_23.setObjectName("label_23")
        self.area6 = QtWidgets.QTextEdit(self.centralwidget)
        self.area6.setGeometry(QtCore.QRect(570, 270, 104, 21))
        self.area6.setObjectName("area6")
        
        self.areaint6=35
        self.area6.setText(str(self.areaint6))
        
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(510, 300, 81, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(510, 320, 141, 16))
        self.label_25.setObjectName("label_25")
        self.expected6 = QtWidgets.QTextEdit(self.centralwidget)
        self.expected6.setGeometry(QtCore.QRect(510, 350, 151, 31))
        self.expected6.setObjectName("expected6")
        
        self.expected6.setText("0")
        self.qTimer = QTimer()
        self.qTimer.setInterval(5000)
        self.qTimer.timeout.connect(self.getValue)
        self.qTimer.start()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "AREA1"))
        self.label_2.setText(_translate("MainWindow", "Count"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Area"))
        self.train_arrives.setText(_translate("MainWindow", "Train arrives:"))
        self.label_5.setText(_translate("MainWindow", "Expected people to deboard"))
        self.label_4.setText(_translate("MainWindow", "AREA 2"))
        self.label_6.setText(_translate("MainWindow", "Count"))
        self.label_7.setText(_translate("MainWindow", "Area"))
        self.label_8.setText(_translate("MainWindow", "Train arrives:"))
        self.label_9.setText(_translate("MainWindow", "Expected people to deboard"))
        self.label_26.setText(_translate("MainWindow", "AREA 3"))
        self.label_10.setText(_translate("MainWindow", "Count"))
        self.label_11.setText(_translate("MainWindow", "Area"))
        self.label_12.setText(_translate("MainWindow", "Train arrives:"))
        self.label_13.setText(_translate("MainWindow", "Expected people to deboard"))
        self.label_27.setText(_translate("MainWindow", "AREA 4"))
        self.label_28.setText(_translate("MainWindow", "AREA 5"))
        self.label_29.setText(_translate("MainWindow", "AREA 6"))
        self.label_14.setText(_translate("MainWindow", "Count"))
        self.label_15.setText(_translate("MainWindow", "Area"))
        self.label_16.setText(_translate("MainWindow", "Train arrives:"))
        self.label_17.setText(_translate("MainWindow", "Expected people to deboard"))
        self.label_18.setText(_translate("MainWindow", "Count"))
        self.label_19.setText(_translate("MainWindow", "Area"))
        self.label_20.setText(_translate("MainWindow", "Train arrives:"))
        self.label_21.setText(_translate("MainWindow", "Expected people to deboard"))
        self.label_22.setText(_translate("MainWindow", "Count"))
        self.label_23.setText(_translate("MainWindow", "Area"))
        self.label_24.setText(_translate("MainWindow", "Train arrives:"))
        self.label_25.setText(_translate("MainWindow", "Expected people to deboard"))
        # while(True):
        #     random_number = random.randint(0,100)
        #     self.count1.setText(str(random_number))
        #     time.sleep(2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    MainWindow.show()
    sys.exit(app.exec_())
