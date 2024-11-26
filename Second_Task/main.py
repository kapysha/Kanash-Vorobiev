import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.should_draw = False
        self.circles = []
        self.pushButton.clicked.connect(self.generate_circle)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(255, 255, 0)

        self.circles.append((x, y, diameter, color))

        self.should_draw = True
        self.update()

    def paintEvent(self, event):
        if not self.should_draw:  # Без флага экран постоянно перерисовывается
            return

        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing)  # Включает сглаживание, чтобы окружности выглядели гладкими.

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.GlobalColor.transparent)  # Убирает обводку
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
