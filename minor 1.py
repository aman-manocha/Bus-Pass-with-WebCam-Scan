# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import DB_manager as db
from PyQt4 import QtCore, QtGui
from signup import Ui_MainWindow
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

class Ui_BUSPASSSYSTEM(object):
    def openwindow(self):
        self.window=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def logincheck(self):
        print("login button clicked!")
    def signupcheck(self):
        print("signup button clicked!")
    def setupUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setObjectName(_fromUtf8("BUSPASSSYSTEM"))
        BUSPASSSYSTEM.resize(676, 554)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        BUSPASSSYSTEM.setFont(font)
        self.centralwidget = QtGui.QWidget(BUSPASSSYSTEM)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.alredy_label = QtGui.QLabel(self.centralwidget)
        self.alredy_label.setGeometry(QtCore.QRect(290, 200, 151, 51))
        self.alredy_label.setObjectName(_fromUtf8("alredy_label"))
        self.loginbtn = QtGui.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(290, 330, 101, 28))
        self.loginbtn.setObjectName(_fromUtf8("loginbtn"))
        #######################button event#######################
        self.loginbtn.clicked.connect(self.logincheck)
        ###########################################################
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 671, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.name_label = QtGui.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(230, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.name_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.name_lineEdit.setGeometry(QtCore.QRect(290, 250, 121, 22))
        self.name_lineEdit.setText(_fromUtf8(""))
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.psw_label = QtGui.QLabel(self.centralwidget)
        self.psw_label.setGeometry(QtCore.QRect(180, 290, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.psw_label.setFont(font)
        self.psw_label.setObjectName(_fromUtf8("psw_label"))
        self.psw_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.psw_lineEdit.setGeometry(QtCore.QRect(290, 290, 121, 22))
        self.psw_lineEdit.setObjectName(_fromUtf8("psw_lineEdit"))
        self.dnthv_label = QtGui.QLabel(self.centralwidget)
        self.dnthv_label.setGeometry(QtCore.QRect(280, 390, 231, 31))
        self.dnthv_label.setObjectName(_fromUtf8("dnthv_label"))
        self.signupbtn = QtGui.QPushButton(self.centralwidget)
        self.signupbtn.setGeometry(QtCore.QRect(290, 430, 101, 28))
        self.signupbtn.setObjectName(_fromUtf8("signupbtn"))
        #######################button event#######################
        self.signupbtn.clicked.connect(self.openwindow)
        self.signupbtn.clicked.connect(self.signupcheck)
        ###########################################################
        self.cancelbtn = QtGui.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(410, 330, 93, 28))
        self.cancelbtn.setObjectName(_fromUtf8("cancelbtn"))
        self.gsignupbtn = QtGui.QPushButton(self.centralwidget)
        self.gsignupbtn.setGeometry(QtCore.QRect(410, 430, 101, 28))
        self.gsignupbtn.setObjectName(_fromUtf8("gsignupbtn"))
        BUSPASSSYSTEM.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BUSPASSSYSTEM)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BUSPASSSYSTEM.setStatusBar(self.statusbar)

        self.retranslateUi(BUSPASSSYSTEM)
        QtCore.QMetaObject.connectSlotsByName(BUSPASSSYSTEM)

    def retranslateUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setWindowTitle(_translate("BUSPASSSYSTEM", "MainWindow", None))
        self.alredy_label.setText(_translate("BUSPASSSYSTEM", "already a member? ", None))
        self.loginbtn.setText(_translate("BUSPASSSYSTEM", "login", None))
        self.label_2.setText(_translate("BUSPASSSYSTEM", "<html><head/><body><p><span style=\" color:#00aaff;\">BUS PASS SYSTEM</span></p></body></html>", None))
        self.name_label.setText(_translate("BUSPASSSYSTEM", "NAME", None))
        self.psw_label.setText(_translate("BUSPASSSYSTEM", "PASSWORD", None))
        self.dnthv_label.setText(_translate("BUSPASSSYSTEM", "Don\'t have an account?", None))
        self.signupbtn.setText(_translate("BUSPASSSYSTEM", "Sign up", None))
        self.cancelbtn.setText(_translate("BUSPASSSYSTEM", "Cancel", None))
        self.gsignupbtn.setText(_translate("BUSPASSSYSTEM", "google signup", None))

   ''' @QtCore.pyqtSignature("on_loginbtn_clicked()")
    def Loginbtn(self):
        NAME = self.user_lineEdit.text()
        PASSWORD = self.password_lineEdit.text()
        if not NAME:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not PASSWORD:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(NAME, PASSWORD)

    def AttemptLogin(self, NAME, PASSWORD):
        
        t = self.dbu()
        print (t)
        for col in t:
            if NAME == col[1]:
                if PASSWORD == col[4]:
                    QtGui.QMessageBox.information(self, 'Success!!')
                    self.close()
                else:
                    QtGui.QMessageBox.warning(self, 'Password incorrect...')
                    return'''


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BUSPASSSYSTEM = QtGui.QMainWindow()
    ui = Ui_BUSPASSSYSTEM()  
    ui.setupUi(BUSPASSSYSTEM)
    BUSPASSSYSTEM.show()
    sys.exit(app.exec_())

