import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui',self)

        self.dial1.valueChanged.connect(self.perform_op)
        self.dial2.valueChanged.connect(self.perform_op)
        self.op.currentTextChanged.connect(self.perform_op)
        

    def perform_op(self):
        x = self.dial1.value()
        y = self.dial2.value()
        self.line1.setText(str(x))
        self.line2.setText(str(y))
        if self.op.currentText() =='Add':
            self.lcd.display(x+y)
        if self.op.currentText() =='Difference':
            self.lcd.display(abs(x-y))
        if self.op.currentText() =='Multiply':
            self.lcd.display(x*y)
        if self.op.currentText() =='Divide':
            self.lcd.display(x/y)      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
