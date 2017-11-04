# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdetail.ui'
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

class Ui_editdetails(object):
    def setupUi(self, editdetails):
        editdetails.setObjectName(_fromUtf8("editdetails"))
        editdetails.resize(989, 619)
        self.centralwidget = QtGui.QWidget(editdetails)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.details = QtGui.QLabel(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(460, 50, 291, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.details.setFont(font)
        self.details.setObjectName(_fromUtf8("details"))
        self.enterfname = QtGui.QLabel(self.centralwidget)
        self.enterfname.setGeometry(QtCore.QRect(470, 150, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterfname.setFont(font)
        self.enterfname.setObjectName(_fromUtf8("enterfname"))
        self.enteradd = QtGui.QLabel(self.centralwidget)
        self.enteradd.setGeometry(QtCore.QRect(470, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enteradd.setFont(font)
        self.enteradd.setObjectName(_fromUtf8("enteradd"))
        self.entermobile = QtGui.QLabel(self.centralwidget)
        self.entermobile.setGeometry(QtCore.QRect(470, 280, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entermobile.setFont(font)
        self.entermobile.setObjectName(_fromUtf8("entermobile"))
        self.firstname = QtGui.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(600, 150, 113, 22))
        self.firstname.setObjectName(_fromUtf8("firstname"))
        self.mobile = QtGui.QLineEdit(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(600, 280, 141, 21))
        self.mobile.setMaxLength(32765)
        self.mobile.setObjectName(_fromUtf8("mobile"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 370, 131, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_pic = QtGui.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(70, 160, 241, 231))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setPixmap(QtGui.QPixmap(_fromUtf8("Bus-Pass-with-WebCam-Scan-aman-manocha-patch-1/bus_icon.png")))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.enterdistrict = QtGui.QLabel(self.centralwidget)
        self.enterdistrict.setGeometry(QtCore.QRect(470, 240, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterdistrict.setFont(font)
        self.enterdistrict.setObjectName(_fromUtf8("enterdistrict"))
        self.enterlname = QtGui.QLabel(self.centralwidget)
        self.enterlname.setGeometry(QtCore.QRect(470, 180, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterlname.setFont(font)
        self.enterlname.setObjectName(_fromUtf8("enterlname"))
        self.lastname = QtGui.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(600, 180, 113, 22))
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.district = QtGui.QComboBox(self.centralwidget)
        self.district.setGeometry(QtCore.QRect(600, 240, 91, 22))
        self.district.setObjectName(_fromUtf8("district"))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.addItem(_fromUtf8(""))
        self.district.setItemText(11, _fromUtf8(""))
        self.address = QtGui.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(600, 210, 191, 22))
        self.address.setObjectName(_fromUtf8("address"))
        editdetails.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(editdetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        editdetails.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(editdetails)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        editdetails.setStatusBar(self.statusbar)

        self.retranslateUi(editdetails)
        QtCore.QMetaObject.connectSlotsByName(editdetails)

    def retranslateUi(self, editdetails):
        editdetails.setWindowTitle(_translate("editdetails", "MainWindow", None))
        self.details.setText(_translate("editdetails", "EDIT DETAILS", None))
        self.enterfname.setText(_translate("editdetails", "First Name", None))
        self.enteradd.setText(_translate("editdetails", "Address", None))
        self.entermobile.setText(_translate("editdetails", "Mobile no.", None))
        self.pushButton.setText(_translate("editdetails", "UPDATE DETAILS", None))
        self.enterdistrict.setText(_translate("editdetails", "District", None))
        self.enterlname.setText(_translate("editdetails", "Last Name", None))
        self.district.setItemText(0, _translate("editdetails", "New Delhi", None))
        self.district.setItemText(1, _translate("editdetails", "North Delhi", None))
        self.district.setItemText(2, _translate("editdetails", "North West Delhi", None))
        self.district.setItemText(3, _translate("editdetails", "West Delhi", None))
        self.district.setItemText(4, _translate("editdetails", "South Delhi", None))
        self.district.setItemText(5, _translate("editdetails", "South West Delhi", None))
        self.district.setItemText(6, _translate("editdetails", "North East Delhi", None))
        self.district.setItemText(7, _translate("editdetails", "Central Delhi    ", None))
        self.district.setItemText(8, _translate("editdetails", "East Delhi    ", None))
        self.district.setItemText(9, _translate("editdetails", "Shahdara", None))
        self.district.setItemText(10, _translate("editdetails", "South East Delhi", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    editdetails = QtGui.QMainWindow()
    ui = Ui_editdetails()
    ui.setupUi(editdetails)
    editdetails.show()
    sys.exit(app.exec_())

