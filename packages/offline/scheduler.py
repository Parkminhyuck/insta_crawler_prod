import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from .config import load_settings
from .collector import Collector

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    cfg = load_settings()
    INST = cfg["INSTAGRAM"]
    segment = INST["segment"]
    limit = INST["limit"]
    dm_window = cfg.get("DM_WINDOW", {})
    start_time, end_time = dm_window.get("start"), dm_window.get("end")

    sched = BlockingScheduler()
    # 즉시 1회 실행
    sched.add_job(lambda: Collector(segment, limit).run(), 'date')
    # 매일 지정된 DM 창에서 반복 실행 예시
    sched.add_job(lambda: Collector(segment, limit).run(),
                  'cron', hour=f"{start_time}-{end_time}", minute=0)
    logging.info("Scheduler 시작. 즉시 실행…")
    sched.start()

if __name__ == "__main__":
    main()
