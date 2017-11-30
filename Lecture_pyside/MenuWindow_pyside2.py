import sys
from PySide2 import QtCore, QtGui, QtWidgets
class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Menu Window");    self.setGeometry(300, 200, 300, 300)
        self.statusBar = QtWidgets.QStatusBar();    self.setStatusBar(self.statusBar)
        self.fileMenu = self.menuBar().addMenu("F&ile")
        self.helpMenu = self.menuBar().addMenu("Help")
        self.openAction = QtWidgets.QAction("&Open", self,
                         shortcut=QtGui.QKeySequence.Open, statusTip="Open File",
                         triggered=self.openFile)
        self.exitAction = QtWidgets.QAction(QtGui.QIcon('application-exit.png'), "E&xit", self,
                         shortcut="Ctrl+Q", statusTip="Exit Application",
                         triggered=self.close)
        self.fileMenu.addAction(self.openAction);    self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction);        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exitAction)
        self.textedit = QtWidgets.QTextEdit(self);    self.setCentralWidget(self.textedit)
    def newFile(self):
        self.textedit.setText('Make New File \n')
    def openFile(self):
        self.filename, self.filtername = QtWidgets.QFileDialog.getOpenFileName(self)
        self.textedit.setText(open(self.filename).read())

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv);    ew = MenuWindow()
    ew.show();        sys.exit(app.exec_())
