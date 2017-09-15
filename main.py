import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(10,30,1300,700)
        self.setWindowTitle("Bus Pass System")
        self.setWindowIcon(QtGui.QIcon())
        self.show()

app = QtGui.QApplication(sys.argv)

GUI = Window()
sys.exit(app.exec_())
