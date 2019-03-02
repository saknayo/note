import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit


class TitleBar(QWidget):
    pass


class FramelessWindow(QWidget):
    margins = 5

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(self.margins, self.margins, self.margins, self.margins)
        self.titleBar = TitleBar(self)
        layout.addWidget(self.titleBar)

    def setWidget(self, widget):
        self.widget = widget
        self.widget.setAutoFillBackground(True)
        palette = self.widget.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240, 240))
        self.widget.setPalette(palette)
        self.widget.installEventFilter(self)
        self.layout().addWidget(self.widget)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)


class TGui(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)
        self.resize(QSize(500,800))
        self.move(500,0)
        self.setWidget(MainWindow(self))
        # self.setGeometry(600, 300, 500, 300)  # 设置窗口的坐标（以左上角为原点），及窗口的大小
        # self.setWindowTitle('Test_01_GUI')  # 窗口标题
        self.setWindowIcon(QIcon('pic_01.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TGui()
    sys.exit(app.exec_())

