import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui_file import Ui_Form


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.pressed)
        self.go = False

    def paintEvent(self, event):
        if self.go:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.go = False

    def draw_flag(self, qp):
        for _ in range(randint(2, 5)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            radius = randint(10, 200)
            x, y = self.frameGeometry().width(), self.frameGeometry().height()
            qp.drawEllipse(randint(0, x - radius), randint(0, y - radius), radius, radius)

    def pressed(self):
        self.go = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())