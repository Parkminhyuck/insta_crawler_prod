# db.py ─ SQLite 간단 CRUD
import sqlite3, pathlib

DB_PATH = pathlib.Path("insta.db")

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS accounts(
  username TEXT PRIMARY KEY,
  followers INT,
  posts INT,
  gender CHAR(1),
  age INT,
  bio TEXT,
  segment TEXT,
  tier CHAR(1),
  last_seen DATETIME,
  last_dm DATETIME
);
CREATE TABLE IF NOT EXISTS queue(
  username TEXT PRIMARY KEY,
  segment TEXT,
  tier CHAR(1),
  dm_sent INT DEFAULT 0
);
CREATE TABLE IF NOT EXISTS errors(
  ts DATETIME DEFAULT CURRENT_TIMESTAMP,
  stage TEXT,
  info TEXT
);
"""

def _conn():
    init = not DB_PATH.exists()
    conn = sqlite3.connect(DB_PATH)
    if init:
        conn.executescript(SCHEMA)
    return conn

# 계정 정보 upsert
def upsert_account(row: dict):
    with _conn() as c:
        c.execute("""
        INSERT INTO accounts(username,followers,posts,gender,age,bio,segment,tier,last_seen)
        VALUES (:username,:followers,:posts,:gender,:age,:bio,:segment,:tier,:last_seen)
        ON CONFLICT(username) DO UPDATE SET
          followers=:followers, posts=:posts, gender=:gender, age=:age,
          bio=:bio, segment=:segment, tier=:tier, last_seen=:last_seen;
        """, row)

# DM 대상 큐
def enqueue(username, segment, tier):
    with _conn() as c:
        c.execute("INSERT OR IGNORE INTO queue(username,segment,tier) VALUES (?,?,?)",
                  (username, segment, tier))

def next_queue(batch=20):
    with _conn() as c:
        return c.execute(
            "SELECT username,segment,tier FROM queue WHERE dm_sent=0 LIMIT ?",
            (batch,)
        ).fetchall()

def mark_sent(username):
    with _conn() as c:
        c.execute("UPDATE queue SET dm_sent=1 WHERE username=?", (username,))
        c.execute("UPDATE accounts SET last_dm=CURRENT_TIMESTAMP WHERE username=?", (username,))

def log_error(stage, info):
    with _conn() as c:
        c.execute("INSERT INTO errors(stage,info) VALUES (?,?)", (stage, info))
