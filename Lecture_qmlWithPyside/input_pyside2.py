#-'''- coding: utf-8 -'''-

import sys
from PySide2 import QtCore, QtGui, QtQuick

app = QtGui.QGuiApplication(sys.argv)
view = QtQuick.QQuickView()
url = QtCore.QUrl('qml/input_pyside2.qml')
view.setSource(url)

root = view.rootObject()
inputButton = root.findChild(QtCore.QObject,"inputbutton")
inputButton.clicked.connect(lambda: print("clicked button"))
textinput = root.findChild(QtCore.QObject,"textinput")
textinput.accepted.connect(lambda:QtGui.Clear(root, textinput.property('text')))

view.show()
sys.exit(app.exec_())
