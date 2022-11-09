from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys
from wall2d import *
from ray import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Raytracer"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event): # Displays onto the screen (GUI)
        painter = QPainter()
        painter.begin(self)
        x = Wall2d(Qt.red)
        x.drawWalls2d(painter)
        r = Ray()
        r.drawRay(painter)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())