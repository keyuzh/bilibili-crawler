from bilibili_api import user
import pickle
from pathlib import Path

class Crawl:
    def __init__(self):
        self.info = dict()
        self.datapath = Path("./data")

    def start_crawling(self, start: int, end: int, show_trace=False):
        current = start
        for _ in range((end - start) // 10000 + 1):
            for _ in range(10000):
                if current > end:
                    break
                self.get_level_data(current, show_trace)
                current += 1
            self.save_data()

    def get_level_data(self, uid: int, log=False):
        try:
            info = user.get_user_info(uid)
            level = info['level']
        except user.exceptions.BilibiliException:
            level = None
        self.info[uid] = level
        print(f"Fetched uid: {uid}; level: {level}")

    def save_data(self):
        min_id = min(self.info.keys())
        max_id = max(self.info.keys())
        target_file = self.datapath / f"data_{min_id}_{max_id}.pickle"
        pickle.dump(self.info, open(target_file, "wb"))
