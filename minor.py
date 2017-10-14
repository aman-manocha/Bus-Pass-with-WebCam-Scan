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
        BUSPASSSYSTEM.resize(676, 554)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        BUSPASSSYSTEM.setFont(font)
        self.centralwidget = QtGui.QWidget(BUSPASSSYSTEM)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 200, 151, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 101, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 671, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 250, 121, 22))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 290, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 290, 121, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 390, 231, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 430, 101, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 330, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        BUSPASSSYSTEM.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BUSPASSSYSTEM)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BUSPASSSYSTEM.setStatusBar(self.statusbar)

        self.retranslateUi(BUSPASSSYSTEM)
        QtCore.QMetaObject.connectSlotsByName(BUSPASSSYSTEM)

    def retranslateUi(self, BUSPASSSYSTEM):
        BUSPASSSYSTEM.setWindowTitle(_translate("BUSPASSSYSTEM", "MainWindow", None))
        self.label.setText(_translate("BUSPASSSYSTEM", "already a member? ", None))
        self.pushButton.setText(_translate("BUSPASSSYSTEM", "login", None))
        self.label_2.setText(_translate("BUSPASSSYSTEM", "BUS PASS SYSTEM", None))
        self.label_3.setText(_translate("BUSPASSSYSTEM", "NAME", None))
        self.label_4.setText(_translate("BUSPASSSYSTEM", "PASSWORD", None))
        self.label_5.setText(_translate("BUSPASSSYSTEM", "Don\'t have an account?", None))
        self.pushButton_2.setText(_translate("BUSPASSSYSTEM", "Sign up", None))
        self.pushButton_3.setText(_translate("BUSPASSSYSTEM", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BUSPASSSYSTEM = QtGui.QMainWindow()
    ui = Ui_BUSPASSSYSTEM()
    ui.setupUi(BUSPASSSYSTEM)
    BUSPASSSYSTEM.show()
    sys.exit(app.exec_())

