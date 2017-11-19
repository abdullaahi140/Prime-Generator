from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import Prime

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        self.setStyleSheet("background: white")
        self.show_primes()

    def show_primes(self):

        widget2 = QWidget()
        
        label = QLabel("Prime Numbers", widget2)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QLabel("2",widget2)
        label2.setStyleSheet("font: 20pt Proxima Nova")
        QTimer.singleShot(1000, lambda: self.label_updater(label2))

        v_layout = QVBoxLayout(widget2)
        v_layout.addWidget(label,0,Qt.AlignLeft)
        v_layout.addWidget(label2,0,Qt.AlignCenter)
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
        QTimer.singleShot(1000, lambda: self.label_updater(label2))

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
