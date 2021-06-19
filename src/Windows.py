import json
import logging
import sys

from PyQt5.QtWidgets import QMainWindow  # 导入PyQt相关模块
from PyQt5.QtWidgets import QTextBrowser

from src.Threading import Thread
from windows.Not_implemented import *  # 导入未实现窗口模块
from windows.about import *  # 导入关于窗口模块
from windows.main_gui import *  # 导入主窗口模块
from windows.settings import *  # 导入设置窗口模块


def printf(string):
    MainWindow.textBrowser.append(str(string))  # 文本框逐条添加数据
    MainWindow.textBrowser.moveCursor(MainWindow.textBrowser.textCursor().End)  # 文本框显示到底部


# 为了实现UI设计和操作逻辑分离，创建从窗口py文件中继承的类
class MainWindow(QMainWindow, Ui_guiMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.width(), self.height())  # 禁止调整窗口大小和窗口最大化
        self.settings.triggered.connect(lambda: self.show())  # 绑定打开settings窗口
        self.about.triggered.connect(lambda: self.show())  # 绑定打开About窗口
        self.taskPlanning.triggered.connect(lambda: self.show())  # 绑定打开[未实现]窗口
        self.clearButton.clicked.connect(lambda: self.textBrowser.clear())  # 绑定清空记录
        self.initializationButton.clicked.connect(lambda: self.reload())
        self.startBattleButton.clicked.connect(lambda: self.start_battle())

        self.thread = Thread()

    def printf(self, string):
        self.textBrowser.append(str(string))  # 文本框逐条添加数据
        self.textBrowser.moveCursor(MainWindow.textBrowser.textCursor().End)  # 文本框显示到底部

    def closeEvent(self, event):  # 覆盖原方法以实现关闭警告
        reply = QtWidgets.QMessageBox.question(self, 'aah', '确认退出助手?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击关闭按钮

    def start_battle(self):
        stage = self.stage.text()
        battle_time = int(self.battleTime.text())
        self.thread.ak_helper.module_battle(stage, battle_time)

    def load(self):
        self.__init__()

    def reload(self):
        self.load()

    def closeEvent(self, event):
        # 重写该方法主要是解决打开子窗口时，如果关闭了主窗口但子窗口仍显示的问题，使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭
        sys.exit(0)


class SettingsWindow(Ui_setthingsWindow):

    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)

    def load_setting(self):
        with open("gui_config/config.json", "r") as f:
            setting = json.load(f)
        self.refillApWithitemCheckBox.setChecked(setting["refill_ap_with_item"])
        self.refillApWithOriginCheckBox.setChecked(setting["refill_ap_with_origin"])
        self.penguinReportCheckBox.setChecked(setting["penguin_report"])
        self.reporterID.setText(str(setting["reporter_id"]))
        self.adbServer.setText(setting["adb_server"])
        self.account.setText(setting["account"])
        self.password.setText(setting["password"])

    def save_setting(self):
        refill_ap_with_item = self.refillApWithitemCheckBox.isChecked()
        refill_ap_with_origin = self.refillApWithOriginCheckBox.isChecked()
        penguin_report = self.penguinReportCheckBox.isChecked()
        reporter_id = int(self.reporterID.text())
        adb_server = self.adbServer.text()
        account = self.account.text()
        password = self.password.text()
        setting = {"refill_ap_with_item": refill_ap_with_item, "refill_ap_with_origin": refill_ap_with_origin,
                   "penguin_report": penguin_report, "reporter_id": reporter_id,
                   "adb_server": adb_server,
                   "account": account, "password": password}
        with open("gui_config/config.json", "w") as f:
            json.dump(setting, f)


class AboutWindow(Ui_aboutWindow):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)


class NotWindow(Ui_NotImplementedWindow):
    def __init__(self, parent=None):
        super(NotWindow, self).__init__(parent)
        self.setupUi(self)


class QTextBrowserLogger(logging.Handler):
    def __init__(self, parent: QTextBrowser):
        super().__init__()
        self.widget = parent
        self.widget.setReadOnly(True)
        self.widget.setEnabled(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.append(msg)
