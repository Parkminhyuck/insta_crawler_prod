"""utils_delay.py – 세분화 딜레이 컨트롤

settings_offline.ini
[DELAY]
post_delay = 2.0      # 게시글 간
action_delay = 3.0    # 좋아요/팔로우/DM 후
"""
import time, random, pathlib
from configparser import ConfigParser

CFG = ConfigParser()
CFG.read(pathlib.Path(__file__).resolve().parent / "settings_offline.ini", encoding="utf-8")

POST_DELAY   = CFG.getfloat("DELAY", "post_delay",   fallback=1.0)
ACTION_DELAY = CFG.getfloat("DELAY", "action_delay", fallback=1.5)

def sleep_post():
    time.sleep(random.uniform(POST_DELAY*0.8, POST_DELAY*1.2))

def sleep_action():
    time.sleep(random.uniform(ACTION_DELAY*0.8, ACTION_DELAY*1.2))
    # utils_delay.py

import datetime

def is_within_dm_window() -> bool:
    """
    현재 시간이 00:00~03:00 사이인지 검사합니다.
    True면 DM 발송 가능 시간, False면 불가 시간입니다.
    """
    now = datetime.datetime.now().time()
    start = datetime.time(0, 0)
    end   = datetime.time(3, 0)
    return start <= now <= end
import datetime

def is_within_dm_window() -> bool:
    """
    현재 시간이 00:00~03:00 사이인지 검사합니다.
    True면 DM 발송 허용, False면 그 외 시간대입니다.
    """
    now = datetime.datetime.now().time()
    start = datetime.time(0, 0)
    end   = datetime.time(3, 0)
    return start <= now <= end

