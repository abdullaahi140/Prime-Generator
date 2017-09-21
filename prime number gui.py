from PyQt4 import QtGui, QtCore
import sys
import Prime

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        self.setStyleSheet("background: white")
        self.show_primes()

    def show_primes(self):

        widget2 = QtGui.QWidget()
        
        label = QtGui.QLabel("Prime Numbers", widget2)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QtGui.QLabel("2",widget2)
        label2.setStyleSheet("font: 20pt Proxima Nova")
        QtCore.QTimer.singleShot(1000, lambda: self.label_updater(label2))

        v_layout = QtGui.QVBoxLayout(widget2)
        v_layout.addWidget(label,0,QtCore.Qt.AlignLeft)
        v_layout.addWidget(label2,0,QtCore.Qt.AlignCenter)
        widget2.setLayout(v_layout)

        self.setCentralWidget(widget2)
        self.show()

    def label_updater(self,label2):
        testnum = int(label2.text()) + 1
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

run()