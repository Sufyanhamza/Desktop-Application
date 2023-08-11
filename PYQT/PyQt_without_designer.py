import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Hello World', self)
        self.label.move(100, 50)

        self.button = QPushButton('Click me!', self)
        self.button.move(100, 100)
        
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
