from PyQt4 import QtGui, QtCore
import sys
import Prime
import time

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        #self.setStyleSheet("background: white")
        self.home()
        
    def home(prime,self):

        widget = QtGui.QWidget()
        
        label = QtGui.QLabel("Hello", widget)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QtGui.QLabel(str(prime),widget)
        label2.setStyleSheet("font: 20pt Proxima Nova")

        v_layout = QtGui.QVBoxLayout(widget)
        v_layout.addWidget(label,0,QtCore.Qt.AlignCenter)
        v_layout.addWidget(label2,0,QtCore.Qt.AlignCenter)
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)
        self.show()

        time.sleep(1)

    def prime_updater(self):
        for i in Prime.obtain_range(100):
            if i is not None:
                self.home(i)

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
run()






Having issues with updating label2