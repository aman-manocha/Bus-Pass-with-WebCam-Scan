import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(10,30,1300,700)
        self.setWindowTitle("Bus Pass System")
        self.setWindowIcon(QtGui.QIcon('bus_icon.png'))
        self.home()
        
    def home(self):
        btn = QtGui.QPushButton("Admin Login", self)
        btn2 = QtGui.QPushButton("User Login", self)
        btn3 = QtGui.QPushButton("Logout", self)

        #btn.resize(100,50)
        btn.move(500,500)
        
        #btn2.resize(100,50)
        btn2.move(700,500)

        #btn3.resize(100,50)
        btn3.move(1100,50)

        btn3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()
