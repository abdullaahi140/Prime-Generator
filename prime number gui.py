from PyQt4 import QtGui, QtCore
import sys
import Prime
import time

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        #self.setStyleSheet("background: white")
        self.label_updater()
        
    def home(self,prime):

        self.widget = QtGui.QWidget()
        
        label = QtGui.QLabel("Prime Numbers", self.widget)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QtGui.QLabel(str(prime),self.widget)
        label2.setStyleSheet("font: 20pt Proxima Nova")
        
        v_layout = QtGui.QVBoxLayout(self.widget)
        v_layout.addWidget(label,0,QtCore.Qt.AlignCenter)
        v_layout.addWidget(label2,0,QtCore.Qt.AlignCenter)
        self.widget.setLayout(v_layout)

        self.setCentralWidget(self.widget)
        self.show()

    def label_updater(self):
        for prime in Prime.obtain_range(100):
            if prime is not None:
                self.home(prime)

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

    timer = QtCore.QTimer()
    timer.timeout.connect(self.label_updater)
    timer.start(50000)

run()






#Having issues with updating label2