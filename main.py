

from src.Windows import *

# class LoadThread(QThread):
#    def __init__(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()  # 显示窗口
    sys.exit(app.exec_())
