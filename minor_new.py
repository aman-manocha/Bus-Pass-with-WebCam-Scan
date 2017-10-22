# -*- coding: utf-8 -*-
import DB_manager as db
import sys
# Form implementation generated from reading ui file 'minor1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from signup import Ui_MainWindow
import apitest

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BUSPASSSYSTEM(QtGui.QDialog):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.dbu = db.DatabaseUtility('buspass', 'information')
        self.setupUi(self)
        self.confirm = None
        
    def openwindow(self):
        self.window=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setObjectName(_fromUtf8("BUSPASSSYSTEM"))
        BUSPASSSYSTEM.resize(684, 652)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        BUSPASSSYSTEM.setFont(font)
        self.centralwidget = QtGui.QWidget(BUSPASSSYSTEM)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.buyrenew_label = QtGui.QLabel(self.centralwidget)
        self.buyrenew_label.setGeometry(QtCore.QRect(400, 250, 151, 51))
        self.buyrenew_label.setObjectName(_fromUtf8("buyrenew_label"))
        self.loginbtn = QtGui.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(380, 420, 101, 28))
        self.loginbtn.setObjectName(_fromUtf8("loginbtn"))
        #######################button event#######################
        #self.loginbtn.clicked.connect(self.Loginbtn)
        ###########################################################
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 559, 72))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.name_label = QtGui.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(360, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.name_lineEdit = QtGui.QLineEdit(self)
        self.name_lineEdit.setGeometry(QtCore.QRect(470, 320, 121, 22))
        ########## NAME VALIDATION######################
        regex=QtCore.QRegExp("[a-z-A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)
        self.name_lineEdit.setValidator(validator)
        ####################################
        self.name_lineEdit.setText(_fromUtf8(""))
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.psw_label = QtGui.QLabel(self.centralwidget)
        self.psw_label.setGeometry(QtCore.QRect(360, 360, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.psw_label.setFont(font)
        self.psw_label.setObjectName(_fromUtf8("psw_label"))
        self.psw_lineEdit = QtGui.QLineEdit(self)
        self.psw_lineEdit.setGeometry(QtCore.QRect(470, 360, 121, 22))
        self.psw_lineEdit.setAutoFillBackground(False)
        self.psw_lineEdit.setText(_fromUtf8(""))
        self.psw_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.psw_lineEdit.setObjectName(_fromUtf8("psw_lineEdit"))
        self.dnthv_label = QtGui.QLabel(self.centralwidget)
        self.dnthv_label.setGeometry(QtCore.QRect(390, 480, 231, 41))
        self.dnthv_label.setObjectName(_fromUtf8("dnthv_label"))
        self.signupbtn = QtGui.QPushButton(self.centralwidget)
        self.signupbtn.setGeometry(QtCore.QRect(360, 540, 101, 28))
        self.signupbtn.setObjectName(_fromUtf8("signupbtn"))
         #######################button event#######################
        self.signupbtn.clicked.connect(self.openwindow)
        ###########################################################
        self.cancelbtn = QtGui.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(490, 420, 93, 28))
        self.cancelbtn.setObjectName(_fromUtf8("cancelbtn"))
        self.label_pic = QtGui.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(30, 160, 101, 121))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 241, 231))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("bus_icon.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 540, 111, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #######################button event#######################
        self.pushButton.clicked.connect(self.run_apitest)
        ###########################################################
        #BUSPASSSYSTEM.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BUSPASSSYSTEM)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #BUSPASSSYSTEM.setStatusBar(self.statusbar)

        self.retranslateUi(BUSPASSSYSTEM)
        QtCore.QMetaObject.connectSlotsByName(BUSPASSSYSTEM)

    def run_apitest(self):
        apitest.main(sys.argv)

    def retranslateUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setWindowTitle(_translate("BUSPASSSYSTEM", "MainWindow", None))
        self.buyrenew_label.setText(_translate("BUSPASSSYSTEM", "Buy/Renew pass?", None))
        self.loginbtn.setText(_translate("BUSPASSSYSTEM", "login", None))
        self.label_2.setText(_translate("BUSPASSSYSTEM", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">BUS PASS SYSTEM</span></p></body></html>", None))
        self.name_label.setText(_translate("BUSPASSSYSTEM", "NAME", None))
        self.psw_label.setText(_translate("BUSPASSSYSTEM", "PASSWORD", None))
        self.dnthv_label.setText(_translate("BUSPASSSYSTEM", "Don\'t have an account?", None))
        self.signupbtn.setText(_translate("BUSPASSSYSTEM", "Sign up", None))
        self.cancelbtn.setText(_translate("BUSPASSSYSTEM", "Cancel", None))
        self.pushButton.setText(_translate("BUSPASSSYSTEM", "Google Signup", None))
    @QtCore.pyqtSignature("on_cancelbtn_clicked()")
    def Cancelbtn(self):
        self.close()
        
    @QtCore.pyqtSignature("on_loginbtn_clicked()")
    def Loginbtn(self):
        NAME = self.name_lineEdit.text()
        PASSWORD = self.psw_lineEdit.text()
        #print('%s'%NAME)
        if not NAME:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing')
        elif not PASSWORD:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(NAME, PASSWORD)

    def AttemptLogin(self, NAME, PASSWORD):
        
        t = self.dbu.GetTable()
        print (t)
        for col in t:
            if NAME == col[1]:
                if PASSWORD == col[3]:
                    QtGui.QMessageBox.information(self, 'Guess What?', 'Success!!')
                    #QtGui.QMessageBox.warning(self, 'Guess What?', 'incorrect credentials') 
                    self.close()
                else:
                    QtGui.QMessageBox.warning(self, 'Guess What?', 'incorrect credentials')
                    #QtGui.QMessageBox.information(self, 'Guess What?', 'Success!!') 
                    return
            else:
                QtGui.QMessageBox.warning(self, 'Guess What?', 'incorrect credentials')
    @QtCore.pyqtSignature("on_signbtn_clicked()")
    def NewUser_btn(self):
        self.newUser = Ui_Register(self.dbu)
        self.newUser.show() 


if __name__ == "__main__":
    #import sys
    app = QtGui.QApplication(sys.argv)
    BUSPASSSYSTEM = QtGui.QMainWindow()
    fp = Ui_BUSPASSSYSTEM()
    fp.setupUi(BUSPASSSYSTEM)
    fp.show()
    sys.exit(app.exec_())
