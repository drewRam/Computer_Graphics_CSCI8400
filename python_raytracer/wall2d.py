from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
import sys

"""
Our 2d wall is to ur boundaries we will soon project to 3d.
"""
class Wall2d(QWidget):
    def __init__(self, color=Qt.red, x1=400, y1=0, x2=400, y2=400):
        super().__init__()
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def drawWalls2d(self, qp):
        qp.setRenderHint(qp.Antialiasing)
        qp.setPen(self.color)
        qp.setBrush(Qt.white)
        qp.drawLine(self.x1, self.y1, self.x2, self.y2)
