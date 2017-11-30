import sys
from PySide2 import QtCore, QtGui, QtWidgets

def hello():
    print ('Hello World')

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    button = QtWidgets.QPushButton('Hello')
    button.clicked.connect(hello)
    button.show()
    sys.exit(app.exec_())
