from PyQt4 import QtGui, QtCore
import sys
import Prime

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Prime number GUI")
        self.setStyleSheet("background: white")
        self.home()
        
    def home(self):

        widget = QtGui.QWidget()
        
        label = QtGui.QLabel("Prime Numbers", widget)
        label.setStyleSheet("font: 30pt Proxima Nova")

        label2 = QtGui.QLabel("",widget)
        label2.setStyleSheet("font: 20pt Proxima Nova")
        
        v_layout = QtGui.QVBoxLayout(widget)
        v_layout.addWidget(label,0,QtCore.Qt.AlignCenter)
        v_layout.addWidget(label2,0,QtCore.Qt.AlignCenter)
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)
        self.show()

    def label_updater(self):
        for prime in Prime.obtain_range(100):
            if prime is not None:
                label2.setText(str(prime))

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

    timer = QtCore.QTimer()
    timer.timeout.connect(self.label_updater)
    timer.start(20000)

run()

#Having issues with updating label2