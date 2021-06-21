import sys

from PyQt5.QtWidgets import QApplication

from src.Windows import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()  # 显示窗口
    sys.exit(app.exec_())
