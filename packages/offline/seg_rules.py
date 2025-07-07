
SEG_RULES = {
    "공구": {
        "keywords": ["공구", "공동구매", "할인", "세일"],
        "filter": "followers>=1000"  # Example filter
    },
    "공동구매": {
        "keywords": ["공동구매", "그룹구매", "공동구매", "할인"],
        "filter": "followers>=500"
    },
    "공구예정": {
        "keywords": ["공구예정", "미리보기", "알림"],
        "filter": "followers>=300"
    }
}
