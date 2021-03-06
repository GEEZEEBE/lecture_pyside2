import sys
from PySide2 import QtCore, QtGui, QtWidgets

class SlotWidget(QtWidgets.QWidget):
  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.amtLabel = QtWidgets.QLabel('Loan Amount')
    self.roiLabel = QtWidgets.QLabel('Rate of Interest')
    self.yrsLabel = QtWidgets.QLabel('No. of Years')
    self.emiLabel = QtWidgets.QLabel('EMI per month')
    self.emiValue = QtWidgets.QLCDNumber()

    self.emiValue.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
    self.emiValue.setFixedSize(QtCore.QSize(130,30))
    self.emiValue.setDigitCount(8)

    self.amtText = QtWidgets.QLineEdit('10000')
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

    self.calculateButton = QtWidgets.QPushButton('Calculate EMI')

    self.myGridLayout = QtWidgets.QGridLayout()

    self.myGridLayout.addWidget(self.amtLabel, 0, 0)
    self.myGridLayout.addWidget(self.roiLabel, 1, 0)
    self.myGridLayout.addWidget(self.yrsLabel, 2, 0)
    self.myGridLayout.addWidget(self.amtText, 0, 1)
    self.myGridLayout.addWidget(self.roiSpin, 1, 1)
    self.myGridLayout.addWidget(self.yrsSpin, 2, 1)
    self.myGridLayout.addWidget(self.roiDial, 1, 2)
    self.myGridLayout.addWidget(self.yrsSlide, 2, 2)
    self.myGridLayout.addWidget(self.calculateButton, 3, 1)

    self.setLayout(self.myGridLayout)
    self.setWindowTitle("A simple EMI calculator")

    self.roiDial.valueChanged.connect(self.roiSpin.setValue)
    self.connect(self.roiSpin, QtCore.SIGNAL("valueChanged(int)"), self.roiDial.setValue)
    self.yrsSlide.valueChanged.connect(self.yrsSpin.setValue)

    self.connect(self.yrsSpin, QtCore.SIGNAL("valueChanged(int)"), self.yrsSlide,QtCore.SLOT("setValue(int)"))
    self.connect(self.calculateButton, QtCore.SIGNAL("clicked()"), self.showEMI)
  def showEMI(self):
    loanAmount = float(self.amtText.text())
    rateInterest = float( float (self.roiSpin.value() / 12) / 100)
    noMonths = int(self.yrsSpin.value() * 12)
    emi = (loanAmount * rateInterest) * ( ( ( (1 + rateInterest) ** noMonths ) / ( ( (1 + rateInterest) ** noMonths ) - 1) ))
    self.emiValue.display(emi)
    self.myGridLayout.addWidget(self.emiLabel, 4, 0)
    self.myGridLayout.addWidget(self.emiValue, 4, 2)

# define a new slot that receives and prints a string
def printText(text):
    print(text)

class CustomSignal(QtCore.QObject):
    # create a new signal
    mySignal = QtCore.Signal(str)
    
if __name__ == '__main__':
    try:
        myObject = CustomSignal()
        # connect signal and slot
        myObject.mySignal.connect(printText)
        # emit signal
        myObject.mySignal.emit("Hello, Universe!")
    except Exception:
        print(sys.exc_info()[1])
                
# if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    win = SlotWidget()
    win.show()
    sys.exit(app.exec_())
      