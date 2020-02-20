# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import math

class Ui_OtherWindow(object):
    def __init__(self,count1,count2,count3,count4,count5,count6,expected1,expected2,expected3,expected4,expected5,expected6,
                 area1,area2,area3,area4,area5,area6):
        self.count1=count1
        self.count2=count2
        self.count3=count3
        self.count4=count4
        self.count5=count5
        self.count6=count6
        self.expected1=expected1
        self.expected2=expected2
        self.expected3=expected3
        self.expected4=expected4
        self.expected5=expected5
        self.expected6=expected6
        self.area1=area1
        self.area2=area2
        self.area3=area3
        self.area4=area4
        self.area5=area5
        self.area6=area6
        
    def calculate_density(self):
        density1=(int(self.count1)+int(self.expected1))/(int(self.area1))
        density2=(int(self.count2)+int(self.expected2))/(int(self.area2))
        density3=(int(self.count3)+int(self.expected3))/(int(self.area3))
        density4=(int(self.count4)+int(self.expected4))/(int(self.area4))
        density5=(int(self.count5)+int(self.expected5))/(int(self.area5))
        density6=(int(self.count6)+int(self.expected6))/(int(self.area6))
        v_ff=1.34 #max speed at full freedom
        gamma=1.913 #empirically derived fit parameter
        Dmax=5.4 #crowd density at which no movement is possible
#we calculate speed for different regions
        v1=v_ff*(1-math.exp(-gamma*((1/density1)-(1/Dmax))))
        v2=v_ff*(1-math.exp(-gamma*((1/density2)-(1/Dmax))))
        v3=v_ff*(1-math.exp(-gamma*((1/density3)-(1/Dmax))))
        v4=v_ff*(1-math.exp(-gamma*((1/density4)-(1/Dmax))))
        v5=v_ff*(1-math.exp(-gamma*((1/density5)-(1/Dmax))))
        v6=v_ff*(1-math.exp(-gamma*((1/density6)-(1/Dmax))))             
        return density1,density2,density3,density4,density5,density6,v1,v2,v3,v4,v5,v6
    def predict(self):        
        density1,density2,density3,density4,density5,density6,v1,v2,v3,v4,v5,v6=self.calculate_density()
        low='L'
        high='H'
        medium='M'
        lowspeed='S'
        medspeed='Me'
        highspeed='F'
        list1=[]
        list2=[]
        list3=[]
        Oc=[]
        speedlist=[]
        i=1
        v_ff=1.34 #max speed at full freedom
        gamma=1.913 #empirically derived fit parameter
        Dmax=5.4
        while(i<6):
            for x in range(0,3):
                var=random.randint(1,200)
                density=var/30
        
                speed=v_ff*(1-math.exp(-gamma*((1/density)-(1/Dmax))))
                if(speed<=0.5):
                    speedlist.append(lowspeed)
                elif(speed>0.5 and speed<=1):
                    speedlist.append(medspeed)
                elif(speed>1):
                    speedlist.append(highspeed)
        # Oc=list1+list2+list3
                i+=1
        #print(speedlist)
        p_ss=0.2
        p_sme=0.7
        p_sf=0.1
        p_meme=0.3
        p_mes=0.3
        p_mef=0.4
        p_ff=0.2
        p_fs=0.3
        p_fme=0.5

#Initial Probabilities
        p_s=0.33
        p_m=0.5
        p_f=0.16
#Emission probabilities
        p_sl=0.2
        p_sm=0.2
        p_sh=0.6
        p_mel=0.2
        p_mem=0.7
        p_meh=0.1
        p_fl=0.8
        p_fm=0.1
        p_fh=0.1
# Oc=['L','L','M','H','M','H']
        probabilities=[]
        condition=[]
        if speedlist[0]=='F':
            probabilities.append((p_s*p_fl,p_m*p_mel,p_f*p_fl))
        elif speedlist[0]=='Me':
            probabilities.append((p_s*p_sm,p_m*p_mem,p_f*p_fm))
        else:
            probabilities.append((p_s*p_sh,p_m*p_meh,p_f*p_fh))
        for i in range(1,len(speedlist)):
            prev_slow,prev_medium,prev_fast=probabilities[-1]
            if speedlist[i]=='F': #For more crowd
                now_slow=max(prev_slow*p_ss*p_sl, prev_medium*p_mes*p_sl, prev_fast*p_fs*p_sl)
                now_medium=max(prev_slow*p_sme*p_mel, prev_medium*p_meme*p_mel, prev_fast*p_fme*p_mel)
                now_fast=max(prev_slow*p_sf*p_fl, prev_medium*p_mef*p_fl , prev_fast*p_ff*p_fl)
                probabilities.append((now_slow,now_medium,now_fast))
            elif speedlist[i]=='Me': #for medium crowd
                now_slow=max(prev_slow*p_ss*p_sm, prev_medium*p_mes*p_sm, prev_fast*p_fs*p_sm)
                now_medium=max(prev_slow*p_sme*p_mem, prev_medium*p_meme*p_mem, prev_fast*p_fme*p_mem)
                now_fast=max(prev_slow*p_sf*p_fm, prev_medium*p_mef*p_fm , prev_fast*p_ff*p_fm)
                probabilities.append((now_slow,now_medium,now_fast))
            else: #for less crowd
                now_slow=max(prev_slow*p_ss*p_sh, prev_medium*p_mes*p_sh, prev_fast*p_fs*p_sh)
                now_medium=max(prev_slow*p_sme*p_meh, prev_medium*p_meme*p_meh, prev_fast*p_fme*p_meh)
                now_fast=max(prev_slow*p_sf*p_fh, prev_medium*p_mef*p_fh , prev_fast*p_ff*p_fh)
                probabilities.append((now_slow,now_medium,now_fast))
        print(probabilities)
        for p in probabilities:
            if(p[0]>p[1] and p[0]>p[2]):
                condition.append('High Crowd')
            elif(p[1]>p[0] and p[1]>p[2]):
                condition.append('Medium Crowd')
            else:
                condition.append('Less crowd')
        return condition[len(condition)-1],probabilities
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(557, 325)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 191, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 140, 301, 21))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 47, 13))
        self.label_2.setObjectName("label_2")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(10, 220, 521, 61))
        self.textEdit2.setObjectName("textEdit2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.density1 = QtWidgets.QTextEdit(self.centralwidget)
        self.density1.setGeometry(QtCore.QRect(30, 30, 101, 21))
        self.density1.setObjectName("density1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 47, 13))
        self.label_4.setObjectName("label_4")
        self.density2 = QtWidgets.QTextEdit(self.centralwidget)
        self.density2.setGeometry(QtCore.QRect(200, 30, 104, 21))
        self.density2.setObjectName("density2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 10, 47, 13))
        self.label_5.setObjectName("label_5")
        self.density3 = QtWidgets.QTextEdit(self.centralwidget)
        self.density3.setGeometry(QtCore.QRect(390, 30, 104, 21))
        self.density3.setObjectName("density3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 47, 13))
        self.label_6.setObjectName("label_6")
        self.density4 = QtWidgets.QTextEdit(self.centralwidget)
        self.density4.setGeometry(QtCore.QRect(30, 90, 104, 21))
        self.density4.setObjectName("density4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 70, 47, 13))
        self.label_7.setObjectName("label_7")
        self.density5 = QtWidgets.QTextEdit(self.centralwidget)
        self.density5.setGeometry(QtCore.QRect(200, 90, 104, 21))
        self.density5.setObjectName("density5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 70, 47, 13))
        self.label_8.setObjectName("label_8")
        self.density6 = QtWidgets.QTextEdit(self.centralwidget)
        self.density6.setGeometry(QtCore.QRect(390, 90, 104, 21))
        self.density6.setObjectName("density6")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        density1,density2,density3,density4,density5,density6,speed1,speed2,speed3,speed4,speed5,speed6=self.calculate_density()
        self.density1.setText(str(density1)+","+str(speed1))
        self.density2.setText(str(density2)+","+str(speed2))
        self.density3.setText(str(density3)+","+str(speed3))
        self.density4.setText(str(density4)+","+str(speed4))
        self.density5.setText(str(density5)+","+str(speed5))
        self.density6.setText(str(density6)+","+str(speed6))
        message,prob=self.predict()
        self.textEdit.setText(str(prob))
        self.textEdit2.setText(str(message))
        
        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.label.setText(_translate("OtherWindow", "Predicted Crowd for the regions above"))
        self.label_2.setText(_translate("OtherWindow", "Warning"))
        self.label_3.setText(_translate("OtherWindow", "Density 1"))
        self.label_4.setText(_translate("OtherWindow", "Density 2"))
        self.label_5.setText(_translate("OtherWindow", "Density 3"))
        self.label_6.setText(_translate("OtherWindow", "Density 4"))
        self.label_7.setText(_translate("OtherWindow", "Density 5"))
        self.label_8.setText(_translate("OtherWindow", "Density 6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
