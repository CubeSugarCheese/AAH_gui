from PyQt5.QtCore import QThread

from src.Windows import MainWindow


class BattleThread(QThread, helper.ArknightsHelper):
    def __init__(self, stage, battle_time):
        super(BattleThread, self).__init__()
        self.stage = stage
        self.battle_time = battle_time

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self) -> None:
        MainWindow.printf(string="开始作战")
        self.module_battle(c_id=self.stage, set_count=self.battle_time)
        MainWindow.printf(string="作战结束")
