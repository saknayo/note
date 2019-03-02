import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow, QTextEdit, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon


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

        # 状态栏
        # self.statusBar()
        # 菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        # 工具栏
        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(exitAct)

        self.setGeometry(600, 300, 500, 300)    # 设置窗口的坐标（以左上角为原点），及窗口的大小
        self.setWindowTitle('Test_01_GUI')      # 窗口标题
        self.setWindowIcon(QIcon('pic_01.png'))
        self.show()

    # 改变默认事件的处理——关闭窗口时弹出提示框
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Massage', "Are you sur to QUIT?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestGui()
    sys.exit(app.exec_())       # 安全退出主循环
