# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(989, 619)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 50, 291, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 150, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 290, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 380, 53, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.firstname = QtGui.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(600, 150, 113, 22))
        self.firstname.setObjectName(_fromUtf8("firstname"))
        self.mobile = QtGui.QLineEdit(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(600, 380, 141, 21))
        self.mobile.setObjectName(_fromUtf8("mobile"))
        self.emailid = QtGui.QLineEdit(self.centralwidget)
        self.emailid.setGeometry(QtCore.QRect(600, 410, 181, 22))
        self.emailid.setObjectName(_fromUtf8("emailid"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 440, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.psw = QtGui.QLineEdit(self.centralwidget)
        self.psw.setGeometry(QtCore.QRect(600, 440, 141, 22))
        self.psw.setEchoMode(QtGui.QLineEdit.Password)
        self.psw.setObjectName(_fromUtf8("psw"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 470, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cnfrmpsw = QtGui.QLineEdit(self.centralwidget)
        self.cnfrmpsw.setGeometry(QtCore.QRect(600, 470, 141, 22))
        self.cnfrmpsw.setEchoMode(QtGui.QLineEdit.Password)
        self.cnfrmpsw.setObjectName(_fromUtf8("cnfrmpsw"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 500, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_pic = QtGui.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(70, 160, 241, 231))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Users/sanya/Desktop/Bus-Pass-with-WebCam-Scan-aman-manocha-patch-1/bus_icon.png")))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(470, 320, 53, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 180, 61, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lastname = QtGui.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(600, 180, 113, 22))
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.male_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.male_radioButton.setGeometry(QtCore.QRect(600, 220, 95, 20))
        self.male_radioButton.setObjectName(_fromUtf8("male_radioButton"))
        self.district = QtGui.QComboBox(self.centralwidget)
        self.district.setGeometry(QtCore.QRect(600, 320, 91, 22))
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
        self.female_radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.female_radioButton_2.setGeometry(QtCore.QRect(670, 220, 95, 20))
        self.female_radioButton_2.setObjectName(_fromUtf8("female_radioButton_2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 220, 53, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 260, 53, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 410, 53, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.adhar = QtGui.QLineEdit(self.centralwidget)
        self.adhar.setGeometry(QtCore.QRect(600, 350, 141, 22))
        self.adhar.setObjectName(_fromUtf8("adhar"))
        self.date_comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.date_comboBox_2.setGeometry(QtCore.QRect(600, 260, 41, 22))
        self.date_comboBox_2.setObjectName(_fromUtf8("date_comboBox_2"))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.date_comboBox_2.addItem(_fromUtf8(""))
        self.month_comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.month_comboBox_3.setGeometry(QtCore.QRect(640, 260, 73, 22))
        self.month_comboBox_3.setObjectName(_fromUtf8("month_comboBox_3"))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.month_comboBox_3.addItem(_fromUtf8(""))
        self.year_comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.year_comboBox_4.setGeometry(QtCore.QRect(710, 260, 73, 22))
        self.year_comboBox_4.setObjectName(_fromUtf8("year_comboBox_4"))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.year_comboBox_4.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(470, 350, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.address = QtGui.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(600, 290, 191, 22))
        self.address.setObjectName(_fromUtf8("address"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SIGNUP PORTAL", None))
        self.label_2.setText(_translate("MainWindow", "First Name", None))
        self.label_3.setText(_translate("MainWindow", "Address", None))
        self.label_4.setText(_translate("MainWindow", "Mobile", None))
        self.label_5.setText(_translate("MainWindow", "Password", None))
        self.label_6.setText(_translate("MainWindow", "Confirm password", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.label_7.setText(_translate("MainWindow", "District", None))
        self.label_8.setText(_translate("MainWindow", "Last Name", None))
        self.male_radioButton.setText(_translate("MainWindow", "Male", None))
        self.district.setItemText(0, _translate("MainWindow", "New Delhi", None))
        self.district.setItemText(1, _translate("MainWindow", "North Delhi", None))
        self.district.setItemText(2, _translate("MainWindow", "North West Delhi", None))
        self.district.setItemText(3, _translate("MainWindow", "West Delhi", None))
        self.district.setItemText(4, _translate("MainWindow", "South Delhi", None))
        self.district.setItemText(5, _translate("MainWindow", "South West Delhi", None))
        self.district.setItemText(6, _translate("MainWindow", "North East Delhi", None))
        self.district.setItemText(7, _translate("MainWindow", "Central Delhi    ", None))
        self.district.setItemText(8, _translate("MainWindow", "East Delhi    ", None))
        self.district.setItemText(9, _translate("MainWindow", "Shahdara", None))
        self.district.setItemText(10, _translate("MainWindow", "South East Delhi", None))
        self.female_radioButton_2.setText(_translate("MainWindow", "Female", None))
        self.label_9.setText(_translate("MainWindow", "Gender", None))
        self.label_10.setText(_translate("MainWindow", "D.O.B", None))
        self.label_11.setText(_translate("MainWindow", "Email id", None))
        self.date_comboBox_2.setItemText(0, _translate("MainWindow", "1", None))
        self.date_comboBox_2.setItemText(1, _translate("MainWindow", "2", None))
        self.date_comboBox_2.setItemText(2, _translate("MainWindow", "3", None))
        self.date_comboBox_2.setItemText(3, _translate("MainWindow", "4", None))
        self.date_comboBox_2.setItemText(4, _translate("MainWindow", "5", None))
        self.date_comboBox_2.setItemText(5, _translate("MainWindow", "6", None))
        self.date_comboBox_2.setItemText(6, _translate("MainWindow", "7", None))
        self.date_comboBox_2.setItemText(7, _translate("MainWindow", "8", None))
        self.date_comboBox_2.setItemText(8, _translate("MainWindow", "9", None))
        self.date_comboBox_2.setItemText(9, _translate("MainWindow", "10", None))
        self.date_comboBox_2.setItemText(10, _translate("MainWindow", "11", None))
        self.date_comboBox_2.setItemText(11, _translate("MainWindow", "12", None))
        self.date_comboBox_2.setItemText(12, _translate("MainWindow", "13", None))
        self.date_comboBox_2.setItemText(13, _translate("MainWindow", "14", None))
        self.date_comboBox_2.setItemText(14, _translate("MainWindow", "15", None))
        self.date_comboBox_2.setItemText(15, _translate("MainWindow", "16", None))
        self.date_comboBox_2.setItemText(16, _translate("MainWindow", "17", None))
        self.date_comboBox_2.setItemText(17, _translate("MainWindow", "18", None))
        self.date_comboBox_2.setItemText(18, _translate("MainWindow", "19", None))
        self.date_comboBox_2.setItemText(19, _translate("MainWindow", "20", None))
        self.date_comboBox_2.setItemText(20, _translate("MainWindow", "21", None))
        self.date_comboBox_2.setItemText(21, _translate("MainWindow", "22", None))
        self.date_comboBox_2.setItemText(22, _translate("MainWindow", "23", None))
        self.date_comboBox_2.setItemText(23, _translate("MainWindow", "24", None))
        self.date_comboBox_2.setItemText(24, _translate("MainWindow", "25", None))
        self.date_comboBox_2.setItemText(25, _translate("MainWindow", "26", None))
        self.date_comboBox_2.setItemText(26, _translate("MainWindow", "27", None))
        self.date_comboBox_2.setItemText(27, _translate("MainWindow", "28", None))
        self.date_comboBox_2.setItemText(28, _translate("MainWindow", "29", None))
        self.date_comboBox_2.setItemText(29, _translate("MainWindow", "30", None))
        self.date_comboBox_2.setItemText(30, _translate("MainWindow", "31", None))
        self.month_comboBox_3.setItemText(0, _translate("MainWindow", "JAN", None))
        self.month_comboBox_3.setItemText(1, _translate("MainWindow", "FEB", None))
        self.month_comboBox_3.setItemText(2, _translate("MainWindow", "MAR", None))
        self.month_comboBox_3.setItemText(3, _translate("MainWindow", "APR", None))
        self.month_comboBox_3.setItemText(4, _translate("MainWindow", "MAY", None))
        self.month_comboBox_3.setItemText(5, _translate("MainWindow", "JUNE", None))
        self.month_comboBox_3.setItemText(6, _translate("MainWindow", "JULY", None))
        self.month_comboBox_3.setItemText(7, _translate("MainWindow", "AUG", None))
        self.month_comboBox_3.setItemText(8, _translate("MainWindow", "SEPT", None))
        self.month_comboBox_3.setItemText(9, _translate("MainWindow", "OCT", None))
        self.month_comboBox_3.setItemText(10, _translate("MainWindow", "NOV", None))
        self.month_comboBox_3.setItemText(11, _translate("MainWindow", "DEC", None))
        self.year_comboBox_4.setItemText(0, _translate("MainWindow", "1950", None))
        self.year_comboBox_4.setItemText(1, _translate("MainWindow", "1951", None))
        self.year_comboBox_4.setItemText(2, _translate("MainWindow", "1952", None))
        self.year_comboBox_4.setItemText(3, _translate("MainWindow", "1953", None))
        self.year_comboBox_4.setItemText(4, _translate("MainWindow", "1954", None))
        self.year_comboBox_4.setItemText(5, _translate("MainWindow", "1955", None))
        self.year_comboBox_4.setItemText(6, _translate("MainWindow", "1956", None))
        self.year_comboBox_4.setItemText(7, _translate("MainWindow", "1957", None))
        self.year_comboBox_4.setItemText(8, _translate("MainWindow", "1958", None))
        self.year_comboBox_4.setItemText(9, _translate("MainWindow", "1959", None))
        self.year_comboBox_4.setItemText(10, _translate("MainWindow", "1960", None))
        self.year_comboBox_4.setItemText(11, _translate("MainWindow", "1961", None))
        self.year_comboBox_4.setItemText(12, _translate("MainWindow", "1962", None))
        self.year_comboBox_4.setItemText(13, _translate("MainWindow", "1963", None))
        self.year_comboBox_4.setItemText(14, _translate("MainWindow", "1964", None))
        self.year_comboBox_4.setItemText(15, _translate("MainWindow", "1965", None))
        self.year_comboBox_4.setItemText(16, _translate("MainWindow", "1966", None))
        self.year_comboBox_4.setItemText(17, _translate("MainWindow", "1967", None))
        self.year_comboBox_4.setItemText(18, _translate("MainWindow", "1968", None))
        self.year_comboBox_4.setItemText(19, _translate("MainWindow", "1969", None))
        self.year_comboBox_4.setItemText(20, _translate("MainWindow", "1970", None))
        self.year_comboBox_4.setItemText(21, _translate("MainWindow", "1971", None))
        self.year_comboBox_4.setItemText(22, _translate("MainWindow", "1972", None))
        self.year_comboBox_4.setItemText(23, _translate("MainWindow", "1973", None))
        self.year_comboBox_4.setItemText(24, _translate("MainWindow", "1974", None))
        self.year_comboBox_4.setItemText(25, _translate("MainWindow", "1975", None))
        self.year_comboBox_4.setItemText(26, _translate("MainWindow", "1976", None))
        self.year_comboBox_4.setItemText(27, _translate("MainWindow", "1977", None))
        self.year_comboBox_4.setItemText(28, _translate("MainWindow", "1978", None))
        self.year_comboBox_4.setItemText(29, _translate("MainWindow", "1979", None))
        self.year_comboBox_4.setItemText(30, _translate("MainWindow", "1980", None))
        self.year_comboBox_4.setItemText(31, _translate("MainWindow", "1981", None))
        self.year_comboBox_4.setItemText(32, _translate("MainWindow", "1982", None))
        self.year_comboBox_4.setItemText(33, _translate("MainWindow", "1983", None))
        self.year_comboBox_4.setItemText(34, _translate("MainWindow", "1984", None))
        self.year_comboBox_4.setItemText(35, _translate("MainWindow", "1985", None))
        self.year_comboBox_4.setItemText(36, _translate("MainWindow", "1986", None))
        self.year_comboBox_4.setItemText(37, _translate("MainWindow", "1987", None))
        self.year_comboBox_4.setItemText(38, _translate("MainWindow", "1988", None))
        self.year_comboBox_4.setItemText(39, _translate("MainWindow", "1989", None))
        self.year_comboBox_4.setItemText(40, _translate("MainWindow", "1990", None))
        self.year_comboBox_4.setItemText(41, _translate("MainWindow", "1991", None))
        self.year_comboBox_4.setItemText(42, _translate("MainWindow", "1992", None))
        self.year_comboBox_4.setItemText(43, _translate("MainWindow", "1993", None))
        self.year_comboBox_4.setItemText(44, _translate("MainWindow", "1994", None))
        self.year_comboBox_4.setItemText(45, _translate("MainWindow", "1995", None))
        self.year_comboBox_4.setItemText(46, _translate("MainWindow", "1996", None))
        self.year_comboBox_4.setItemText(47, _translate("MainWindow", "1997", None))
        self.year_comboBox_4.setItemText(48, _translate("MainWindow", "1998", None))
        self.year_comboBox_4.setItemText(49, _translate("MainWindow", "1999", None))
        self.label_12.setText(_translate("MainWindow", "Aadhar no.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

