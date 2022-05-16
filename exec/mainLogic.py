import threading
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from ui.main import Ui_MainWindow
from api import lcu_api, htmlUtil


class mainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.thread_1 = lcu_api.Thread_1()
        self.thread_1.start()
        self.setupUi(self)
        while lcu_api.g_summoner_name == '-':
            time.sleep(0.25)
        self.thread_2 = htmlUtil.Thread_2()
        self.thread_2.start()
        while htmlUtil.g_ranked_flex == '-':
            time.sleep(0.25)
        self.init_info()
        self.countTimer = QTimer(self)
        self.countTimer.start(500)
        self.countTimer.timeout.connect(self.refresh_ui)

    def refresh_ui(self):
        self.label_status.setText(lcu_api.g_client_status)
        self.label_status.repaint()

    def init_info(self):
        self.label_id.setText(lcu_api.g_summoner_name)
        self.label_id.repaint()
        self.label_uuid.setText(lcu_api.g_summoner_puuid)
        self.label_uuid.repaint()
        self.label_solo_rank.setText(htmlUtil.g_ranked_solo)
        self.label_solo_rank.repaint()
        self.label_solo_rank.setText(htmlUtil.g_ranked_solo)
        self.label_solo_rank.repaint()
        self.label_flex_rank.setText(htmlUtil.g_ranked_flex)
        self.label_flex_rank.repaint()




class myThread_status(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        mainUI.listen_status()
