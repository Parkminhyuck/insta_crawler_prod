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