
# tiering.py - Example rules for filtering based on follower count and hashtags

tiering_rules = {
    "공구": {
        "keywords": ["공구", "공동구매", "할인", "세일"],
        "min_followers": 1000
    },
    "공동구매": {
        "keywords": ["공동구매", "그룹구매", "할인"],
        "min_followers": 500
    },
    "공구예정": {
        "keywords": ["공구예정", "알림", "미리보기"],
        "min_followers": 300
    }
}
