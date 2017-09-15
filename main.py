import sys
from PyQt4 import QtGui

app =  QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(10,20,1300,700)
window.setWindowTitle("Bus Pass System")
window.show()
