import logging
from .batch_runner import run_crawler

class Collector:
    def __init__(self, segment: str, limit: int, dm_enabled: bool = True):
        self.segment = segment
        self.limit = limit
        self.dm_enabled = dm_enabled

    def run(self):
        try:
            run_crawler(self.segment, self.limit, self.dm_enabled)
        except Exception as e:
            logging.warning(f"❗ Collector 예외 발생: {e}")
