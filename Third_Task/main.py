import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

from Third_Task.ui import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.should_draw = False
        self.circles = []
        self.pushButton.clicked.connect(self.generate_circle)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)

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
