import sys
from PySide2 import QtCore, QtGui, QtWidgets

class SlotWidget(QtWidgets.QWidget):
  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.roiLabel = QtWidgets.QLabel('Rate of Interest')
    self.yrsLabel = QtWidgets.QLabel('No. of Years')

    self.roiSpin = QtWidgets.QSpinBox()
    self.roiSpin.setMinimum(1)
    self.roiSpin.setMaximum(15)
    self.yrsSpin = QtWidgets.QSpinBox()
    self.yrsSpin.setMinimum(1)
    self.yrsSpin.setMaximum(20)
    
    self.roiDial = QtWidgets.QDial()
    self.roiDial.setNotchesVisible(True)
    self.roiDial.setMaximum(15)
    self.roiDial.setMinimum(1)
    self.roiDial.setValue(1)
    self.yrsSlide = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    self.yrsSlide.setMaximum(20)
    self.yrsSlide.setMinimum(1)

    self.myGridLayout = QtWidgets.QGridLayout()

    self.myGridLayout.addWidget(self.roiLabel, 0, 0)
    self.myGridLayout.addWidget(self.yrsLabel, 1, 0)
    self.myGridLayout.addWidget(self.roiSpin, 0, 1)
    self.myGridLayout.addWidget(self.yrsSpin, 1, 1)
    self.myGridLayout.addWidget(self.roiDial, 0, 2)
    self.myGridLayout.addWidget(self.yrsSlide, 1, 2)

    self.setLayout(self.myGridLayout)
    self.setWindowTitle("A simple EMI calculator")

    self.roiDial.valueChanged.connect(self.roiSpin.setValue)
    self.connect(self.roiSpin, QtCore.SIGNAL("valueChanged(int)"), self.roiDial.setValue)
    self.yrsSlide.valueChanged.connect(self.yrsSpin.setValue)
    self.connect(self.yrsSpin, QtCore.SIGNAL("valueChanged(int)"), self.yrsSlide,QtCore.SLOT("setValue(int)"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = SlotWidget()
    win.show()
    sys.exit(app.exec_())
      