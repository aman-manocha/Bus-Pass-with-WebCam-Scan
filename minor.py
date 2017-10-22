# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setObjectName(_fromUtf8("BUSPASSSYSTEM"))
        BUSPASSSYSTEM.resize(735, 657)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        BUSPASSSYSTEM.setFont(font)
        self.centralwidget = QtGui.QWidget(BUSPASSSYSTEM)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.alredy_label = QtGui.QLabel(self.centralwidget)
        self.alredy_label.setGeometry(QtCore.QRect(420, 170, 151, 51))
        self.alredy_label.setObjectName(_fromUtf8("alredy_label"))
        self.loginbtn = QtGui.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(380, 310, 101, 28))
        self.loginbtn.setObjectName(_fromUtf8("loginbtn"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 559, 72))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.name_label = QtGui.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(370, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.name_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.name_lineEdit.setGeometry(QtCore.QRect(480, 230, 121, 22))
        self.name_lineEdit.setText(_fromUtf8(""))
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.psw_label = QtGui.QLabel(self.centralwidget)
        self.psw_label.setGeometry(QtCore.QRect(340, 260, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.psw_label.setFont(font)
        self.psw_label.setObjectName(_fromUtf8("psw_label"))
        self.psw_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.psw_lineEdit.setGeometry(QtCore.QRect(480, 260, 121, 22))
        self.psw_lineEdit.setAutoFillBackground(False)
        self.psw_lineEdit.setText(_fromUtf8(""))
        self.psw_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.psw_lineEdit.setObjectName(_fromUtf8("psw_lineEdit"))
        self.dnthv_label = QtGui.QLabel(self.centralwidget)
        self.dnthv_label.setGeometry(QtCore.QRect(380, 370, 231, 31))
        self.dnthv_label.setObjectName(_fromUtf8("dnthv_label"))
        self.signupbtn = QtGui.QPushButton(self.centralwidget)
        self.signupbtn.setGeometry(QtCore.QRect(380, 410, 101, 28))
        self.signupbtn.setObjectName(_fromUtf8("signupbtn"))
        self.cancelbtn = QtGui.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(490, 310, 93, 28))
        self.cancelbtn.setObjectName(_fromUtf8("cancelbtn"))
        self.gsignupbtn = QtGui.QPushButton(self.centralwidget)
        self.gsignupbtn.setGeometry(QtCore.QRect(490, 410, 101, 28))
        self.gsignupbtn.setObjectName(_fromUtf8("gsignupbtn"))
        self.label_pic = QtGui.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(30, 160, 101, 121))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 190, 241, 231))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Users/sanya/Desktop/Bus-Pass-with-WebCam-Scan-aman-manocha-patch-1/bus_icon.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 581))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
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
        self.label_2.setText(_translate("BUSPASSSYSTEM", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">BUS PASS SYSTEM</span></p></body></html>", None))
        self.name_label.setText(_translate("BUSPASSSYSTEM", "NAME", None))
        self.psw_label.setText(_translate("BUSPASSSYSTEM", "PASSWORD", None))
        self.dnthv_label.setText(_translate("BUSPASSSYSTEM", "Don\'t have an account?", None))
        self.signupbtn.setText(_translate("BUSPASSSYSTEM", "Sign up", None))
        self.cancelbtn.setText(_translate("BUSPASSSYSTEM", "Cancel", None))
        self.gsignupbtn.setText(_translate("BUSPASSSYSTEM", "google signup", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BUSPASSSYSTEM = QtGui.QMainWindow()
    ui = Ui_BUSPASSSYSTEM()
    ui.setupUi(BUSPASSSYSTEM)
    BUSPASSSYSTEM.show()
    sys.exit(app.exec_())

