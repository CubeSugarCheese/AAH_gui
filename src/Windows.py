import json
import sys

from PyQt5.QtWidgets import QMainWindow  # 导入PyQt相关模块

from src.Threading import Thread
from windows.Not_implemented import *  # 导入未实现窗口模块
from windows.about import *  # 导入关于窗口模块
from windows.main_gui import *  # 导入主窗口模块
from windows.settings import *  # 导入设置窗口模块


# 为了实现UI设计和操作逻辑分离，创建从窗口py文件中继承的类
class MainWindow(Ui_guiMainWindow, QMainWindow):
    already_load: bool = False

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.settingsWindow = SettingsWindow()
        self.aboutWindow = AboutWindow()
        self.notWindow = NotWindow()

        self.setFixedSize(self.width(), self.height())  # 禁止调整窗口大小和窗口最大化
        self.settings.triggered.connect(self.settingsWindow.show)  # 绑定打开settings窗口
        self.about.triggered.connect(self.aboutWindow.show)  # 绑定打开About窗口
        self.taskPlanning.triggered.connect(self.notWindow.show)  # 绑定打开[未实现]窗口
        self.clearButton.clicked.connect(self.textBrowser.clear)  # 绑定清空记录
        self.initializationButton.clicked.connect(self.reload)
        self.startBattleButton.clicked.connect(self.start_battle)
        self.quickStartBattleButton.clicked.connect(self.start_battle_slim)
        self.stopButton.clicked.connect(self.stop_thread)
        self.openGameButton.clicked.connect(self.open_game)
        self.closeGameButton.clicked.connect(self.close_game)

    def printf(self, string):
        self.textBrowser.append(str(string))  # 文本框逐条添加数据
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def closeEvent(self, event):  # 覆盖原方法以实现关闭警告
        reply = QtWidgets.QMessageBox.question(self, 'aah', '确认退出助手?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击关闭按钮

    def start_battle(self):
        if self.already_load:
            stage = self.stage.text()
            battle_time = int(self.battleTime.text())
            if stage is None and battle_time is None:
                self.printf("输入不合法，请重新输入")
            else:
                self.thread.ak_helper.module_battle(stage, battle_time)
        else:
            self.printf("未初始化助手，请点击初始化按钮")

    def start_battle_slim(self):
        if self.already_load:
            battle_time = int(self.battleTime.text())
            if battle_time is None:
                self.printf("输入不合法，请重新输入")
            else:
                self.thread.ak_helper.module_battle_slim(set_count=battle_time)
        else:
            self.printf("未初始化助手，请点击初始化按钮")

    def open_game(self):
        if self.already_load:
            self.thread.ak_helper.check_game_active()
            self.printf("游戏已开启")
        else:
            self.printf("线程未运行")

    def close_game(self):
        if self.already_load:
            self.thread.ak_helper.close_game()
            self.printf("成功关闭游戏")
        else:
            self.printf("线程未运行")

    def stop_thread(self):
        if self.already_load:
            self.thread.exit()
            self.already_load = False
            self.printf("线程已经中止")
        else:
            self.printf("线程未运行")

    def load(self):
        self.printf("初始化开始")
        self.thread = Thread()
        self.already_load: bool = True
        self.printf("初始化完毕")

    def reload(self):
        self.load()

    def closeEvent(self, event):
        # 重写该方法主要是解决打开子窗口时，如果关闭了主窗口但子窗口仍显示的问题，使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭
        sys.exit(0)


class SettingsWindow(QMainWindow, Ui_setthingsWindow):

    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_setting()

        self.saveButton.clicked.connect(lambda: self.save_setting())

    def load_setting(self):
        with open("src/config.json", "r") as f:
            setting = json.load(f)
        self.refillApWithitemCheckBox.setChecked(setting["refill_ap_with_item"])
        self.refillApWithOriginCheckBox.setChecked(setting["refill_ap_with_origin"])
        self.adbServer.setText(setting["adb_server"])

    def save_setting(self):
        refill_ap_with_item = self.refillApWithitemCheckBox.isChecked()
        refill_ap_with_origin = self.refillApWithOriginCheckBox.isChecked()
        adb_server = self.adbServer.text()
        setting = {"refill_ap_with_item": refill_ap_with_item, "refill_ap_with_origin": refill_ap_with_origin,
                   "adb_server": adb_server}
        with open("src/config.json", "w") as f:
            json.dump(setting, f)


class AboutWindow(QMainWindow, Ui_aboutWindow):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)


class NotWindow(QMainWindow, Ui_NotImplementedWindow):
    def __init__(self, parent=None):
        super(NotWindow, self).__init__(parent)
        self.setupUi(self)
