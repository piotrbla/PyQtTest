from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

IMG_PAWN = QImage("./Chess_plt45.png")


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.text = "Piotr Błaszyński\n Zażółć gęślą jaźń \n Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(900, 300, 880, 370)
        self.setWindowTitle('Drawing text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_decorative_text(event, qp)
        qp.end()

    def draw_decorative_text(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 14))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
