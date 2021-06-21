from PyQt5.QtCore import QThread
import json

from src.aah.Arknights.helper import ArknightsHelper


class Thread(QThread):
    refill_ap_with_item: bool
    refill_ap_with_origin: bool
    reporter_id: int
    adb_host: str
    account: str
    password: str

    def __init__(self):
        super().__init__()
        self.load_config()
        self.ak_helper = ArknightsHelper(adb_host=self.adb_host)

    def load_config(self):
        with open("./src/config.json", "r") as r:
            config: dict = json.load(r)
            self.refill_ap_with_item: bool = config["refill_ap_with_item"]
            self.refill_ap_with_origin: bool = config["refill_ap_with_origin"]
            self.adb_host: str = config["adb_server"]



    def run(self):
        pass
