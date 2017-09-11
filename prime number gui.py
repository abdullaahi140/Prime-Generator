from PyQt4 import QtGui, QtCore
import sys
import Prime

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        #self.setStyleSheet("background: white")
        self.home()
        
    def home(self):

        widget = QtGui.QWidget()
        
        label = QtGui.QLabel("Prime Numbers", widget)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QtGui.QLabel("2",widget)
        label2.setStyleSheet("font: 20pt Proxima Nova")
        QtCore.QTimer.singleShot(1000, lambda: self.label_updater(label2))

        v_layout = QtGui.QVBoxLayout(widget)
        v_layout.addWidget(label,0,QtCore.Qt.AlignCenter)
        v_layout.addWidget(label2,0,QtCore.Qt.AlignCenter)
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)
        self.show()

    def label_updater(self,label2):
        testnum = int(label2.text())+1
        prime = Prime.obtain_prime(testnum)
        while prime is None:
            testnum += 1
            prime = Prime.obtain_prime(testnum)
        label2.setText(str(prime))
        QtCore.QTimer.singleShot(1000, lambda: self.label_updater(label2))

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

    # timer = QtCore.QTimer()
    # timer.timeout.connect(self.label_updater)
    # timer.start(10000)

run()

#Having issues with updating label2