from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QAction, QPushButton, QVBoxLayout, QSizeGrip
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mouseclick = False

        self.globaly = 300
        self.globalx = 600
        self.ui()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseclick = True
            self.m_x = event.x()
            self.m_y = event.y()
            print(self.m_x,self.m_y)

    def mouseMoveEvent(self, event):
        if self.mouseclick:
            self.g_x = event.x()
            self.g_y = event.y()
            v_x = self.g_x-self.m_x
            v_y = self.g_y-self.m_y
            self.globalx = self.globalx+v_x
            self.globaly = self.globaly+v_y
            # print(self.globalx, self.globaly)
            self.update()

    def mouseReleaseEvent(self, event):
        self.mouseclick = False

    def paintEvent(self, *args, **kwargs):
        self.setGeometry(self.globalx, self.globaly, 600, 400)

    # def resizeEvent(self, event):
    #     event.x
    #     self.setGeometry(self.globalx, self.globaly, 600, 400)
    #     pass

    def ui(self, *args, **kwargs):
        exitAct = QAction(QIcon('pic_01.png'), 'Exit', self)
        # exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        minimizeAct = QAction(QIcon('pic_min.png'), 'Minimize', self)
        minimizeAct.triggered.connect(self.showMinimized)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.toolbar.addAction(minimizeAct)

        self.setGeometry(self.globalx, self.globaly, 600, 400)  # 设置窗口的坐标（以左上角为原点），及窗口的大小
        self.setWindowTitle('Test_02')  # 窗口标题
        self.setWindowIcon(QIcon('pic_01.png'))
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # window.setWindowFlags(flags)
        self.setWindowFlags(flags)


class ResizeButton(QPushButton):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

    def mouseReleaseEvent(self, event):
        self.mouseclick = False

    def paintEvent(self, *args, **kwargs):
        self.setGeometry(self.globalx, self.globaly, 500, 300)

    def resizeEvent(self, event):
        self.mainWindow.resize(event.x(), event.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())





