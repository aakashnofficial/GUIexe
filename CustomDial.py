from PyQt5.QtWidgets import QDial
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint, QPointF
import math

class CustomDial(QDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(360)
        self.setFixedSize(550, 550)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        center = rect.center()
        radius = min(rect.width(), rect.height()) / 2 - 10
        painter.translate(center)

        # Draw background
        painter.setBrush(QColor("#6a8b99"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(0, 0), radius, radius)

        # Calculate handle position
        angle = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * 360
        radian = math.radians(angle + 90)  # -90 to start from the top
        handle_length = radius - 50  # Adjust handle length
        handle_x = handle_length * math.cos(radian)
        handle_y = handle_length * math.sin(radian)

        # Draw handle
        painter.setBrush(QColor("#1d3c4e"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(handle_x, handle_y), 40, 40)  # Handle size

        painter.end()
