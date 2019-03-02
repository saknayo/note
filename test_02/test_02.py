import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt


class TestGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 创建窗口
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('pic_01.png'), 'Exit', self)
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        # self.change_color_button = QtWidgets.QToolButton()
        # self.change_color_button.setIcon(QtGui.QIcon('color.png'))
        # self.change_color_button.setIconSize(QtCore.QSize(2, 2))
        # self.change_color_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #
        # self.change_font_button = QtWidgets.QToolButton()
        # self.change_font_button.setIcon(QtGui.QIcon('font.png'))
        # self.change_font_button.setIconSize(QtCore.QSize(2, 2))
        # self.change_font_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(self.change_color_button)
        # hbox.addWidget(self.change_font_button)
        #
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        #
        # self.setLayout(vbox)

        # 状态栏
        # self.statusBar()
        # 菜单栏
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&Exit')
        # fileMenu.addAction(exitAct)
        # 工具栏
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(600, 300, 500, 300)    # 设置窗口的坐标（以左上角为原点），及窗口的大小
        self.setWindowTitle('Test_02')      # 窗口标题
        self.setWindowIcon(QIcon('pic_01.png'))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.show()

    # 改变默认事件的处理——关闭窗口时弹出提示框
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Massage', "Are you sur to QUIT?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestGui()
    sys.exit(app.exec_())       # 安全退出主循环