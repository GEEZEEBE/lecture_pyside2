#-'''- coding: utf-8 -'''-

import sys
from PySide2 import QtCore, QtGui, QtQuick

app = QtGui.QGuiApplication(sys.argv)
view = QtQuick.QQuickView()
url = QtCore.QUrl('input.qml')
view.setSource(url)

root = view.rootObject()
#/button = root.findChild(QtCore.QObject,"inputButton")
inputButton = root.findChild(QtCore.QObject,"inputbutton")
inputButton.clicked.connect(lambda: print("clicked button"))
textinput = root.findChild(QtCore.QObject,"textinput")
textinput.accepted.connect(lambda: Clear(root, textinput.property('text')))

view.show()
sys.exit(app.exec_())
