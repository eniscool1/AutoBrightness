import sys

# from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import screen_brightness_control as sbc



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # button = QPushButton("Press Me!")

        
        layout = QVBoxLayout()


        self.text = QLabel("Word")
        self.text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text)
        # text.setText()


        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.valuechange)
        self.slider.value()

        # layout.addWidget(text)
        layout.addWidget(self.slider)


        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        # self.setLayout(layout)


    def valuechange(self):
    #   size = self.slider.value()
    #   self.text.setText(size)
      sbc.set_brightness(self.slider.value())
    
    
      
      



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
