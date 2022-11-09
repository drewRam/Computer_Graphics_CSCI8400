from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
import sys

class Ray():                                        # dir is my end points
    def __init__(self, color=Qt.red, x1=100, y1=100, x2=300, y2=100): #x3, y3, x4, y4
        super().__init__()
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def drawRay(self, qp):
        qp.setRenderHint(qp.Antialiasing)
        qp.setPen(self.color)
        qp.setBrush(Qt.white)
        qp.drawLine(self.x1, self.y1, self.x2, self.y2)
        print("Displaying ray...")

    def cast(wall): # I don't know if I want to change these var names to match Ctrain
        intX1 = wall.x1
        intY1 = wall.y1
        intX2 = wall.x2
        intY2 = wall.y2