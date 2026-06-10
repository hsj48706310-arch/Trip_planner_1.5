#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
각 지역별 부족한 코스를 추가하는 스크립트
"""

import json

# 추가할 코스 정보 (지역별로)
new_courses_data = {
    "경주": {
        "식도락2": {
            "name": "경주 시장 먹거리 투어",
            "attractions": ["보문시장", "불국사 주변", "인왕동 맛집골목"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 25000, "food": 30000, "attraction": 0}
        },
        "자연2": {
            "name": "경주 계곡 트래킹",
            "attractions": ["토함산", "대명천", "남산 계곡"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 18000, "attraction": 12000}
        },
        "쇼핑2": {
            "name": "경주 공예품 쇼핑",
            "attractions": ["보문관광단지 쇼핑", "경주 기념품점"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 15000, "attraction": 0}
        },
        "휴양2": {
            "name": "경주 보문호 힐링",
            "attractions": ["보문호 카페", "호수 산책로", "관광호텔"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 25000, "food": 28000, "attraction": 15000}
        },
        "액티비티2": {
            "name": "경주 문화체험",
            "attractions": ["불국사", "석굴암 트레킹", "유적지"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 22000, "attraction": 20000}
        }
    },
    "제주": {
        "문화2": {
            "name": "제주 독립운동 역사관",
            "attractions": ["제3독립관", "역사박물관", "탐라박물관"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 50000, "food": 28000, "attraction": 15000}
        },
        "식도락2": {
            "name": "제주 해산물 회타운",
            "attractions": ["서문시장", "신제주 횟집", "해산물 맛집"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 50000, "food": 50000, "attraction": 5000}
        },
        "쇼핑2": {
            "name": "제주 면세점 쇼핑",
            "attractions": ["제주 면세점", "신라면세점", "롯데 아울렛"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 50000, "food": 32000, "attraction": 0}
        }
    },
    "강릉": {
        "문화2": {
            "name": "강릉 강원도청 문화투어",
            "attractions": ["강원도청", "강릉선비문화축제", "박물관"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 20000, "attraction": 10000}
        },
        "식도락2": {
            "name": "강릉 메밀국수 투어",
            "attractions": ["강릉 메밀국수", "중앙시장", "로컬 맛집"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 25000, "food": 25000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "강릉 상설시장 쇼핑",
            "attractions": ["강릉시장", "유명 기념품점"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "강릉 해변 휴양",
            "attractions": ["정동진 해변", "카페거리", "휴식"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 25000, "food": 25000, "attraction": 10000}
        },
        "액티비티2": {
            "name": "강릉 카약 스포츠",
            "attractions": ["경포호 카약", "해변 액티비티"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 20000, "attraction": 40000}
        }
    },
    "대구": {
        "자연2": {
            "name": "대구 앞산 숲길",
            "attractions": ["앞산공원", "숲길 산책", "자연"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 18000, "attraction": 8000}
        },
        "쇼핑2": {
            "name": "대구 대백화점 쇼핑",
            "attractions": ["동성로", "백화점", "쇼핑몰"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 0}
        },
        "휴양2": {
            "name": "대구 카페 힐링",
            "attractions": ["신타운 카페", "앞산 전망"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 22000, "attraction": 8000}
        },
        "액티비티2": {
            "name": "대구 클라이밍",
            "attractions": ["클라이밍짐", "스포츠센터"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 25000}
        }
    },
    "전주": {
        "자연2": {
            "name": "전주 내장산 트래킹",
            "attractions": ["내장산", "트래킹", "계곡"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 12000}
        },
        "쇼핑2": {
            "name": "전주 시장 쇼핑",
            "attractions": ["전주시장", "공예품점", "기념품"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "전주 한옥마을 카페",
            "attractions": ["한옥마을 카페", "휴식공간"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 20000, "food": 24000, "attraction": 10000}
        },
        "액티비티2": {
            "name": "전주 한지 만들기",
            "attractions": ["한지 공방", "도예 체험"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 22000, "attraction": 25000}
        }
    },
    "인천": {
        "문화2": {
            "name": "인천 인천역 역사",
            "attractions": ["인천역", "개항장", "차이나타운"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 18000, "attraction": 12000}
        },
        "식도락2": {
            "name": "인천 중화음식 투어",
            "attractions": ["차이나타운 음식", "중화집"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 15000, "food": 30000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "인천 외항 쇼핑",
            "attractions": ["아울렛", "백화점", "상업지구"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 16000, "attraction": 0}
        },
        "휴양2": {
            "name": "인천 섬 카페",
            "attractions": ["연평도", "카페", "해변"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 20000, "attraction": 12000}
        },
        "액티비티2": {
            "name": "인천 섬 트래킹",
            "attractions": ["강화도", "트래킹", "자연"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 18000, "attraction": 15000}
        }
    },
    "대전": {
        "문화2": {
            "name": "대전 박물관 투어",
            "attractions": ["대전박물관", "미술관", "갤러리"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 15000}
        },
        "식도락2": {
            "name": "대전 로컬음식",
            "attractions": ["중앙시장", "음식점", "닭강정"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 28000, "attraction": 0}
        },
        "자연2": {
            "name": "대전 동학사 트래킹",
            "attractions": ["동학사", "계룡산", "숲"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 12000}
        },
        "쇼핑2": {
            "name": "대전 백화점 쇼핑",
            "attractions": ["신세계", "갤러리아", "롯데"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 0}
        },
        "휴양2": {
            "name": "대전 유성온천",
            "attractions": ["온천", "스파", "호텔"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 20000, "food": 26000, "attraction": 12000}
        },
        "액티비티2": {
            "name": "대전 래프팅",
            "attractions": ["공주 래프팅", "스포츠"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 18000, "attraction": 30000}
        }
    },
    "광주": {
        "자연2": {
            "name": "광주 무등산 트래킹",
            "attractions": ["무등산", "계곡", "폭포"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 25000, "food": 18000, "attraction": 10000}
        },
        "쇼핑2": {
            "name": "광주 시장 쇼핑",
            "attractions": ["충장로", "시장", "상점"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "광주 문화전당 힐링",
            "attractions": ["문화전당", "광장", "카페"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 22000, "attraction": 10000}
        },
        "액티비티2": {
            "name": "광주 자전거",
            "attractions": ["자전거", "트래킹"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 25000, "food": 18000, "attraction": 15000}
        }
    },
    "수원": {
        "식도락2": {
            "name": "수원 닭발 투어",
            "attractions": ["닭발거리", "시장"], 
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 10000, "food": 28000, "attraction": 0}
        },
        "자연2": {
            "name": "수원 광교 생태공원",
            "attractions": ["광교생태공원", "산책로"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 16000, "attraction": 5000}
        },
        "쇼핑2": {
            "name": "수원 쇼핑몰",
            "attractions": ["쇼핑몰", "백화점"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "수원 호수 카페",
            "attractions": ["광교호수", "카페"],
            "duration_days": 2,
            "popular": True,
            "base_cost": {"transport": 10000, "food": 20000, "attraction": 8000}
        },
        "액티비티2": {
            "name": "수원 자전거",
            "attractions": ["화성 자전거", "스포츠"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 18000, "attraction": 20000}
        }
    },
    "창원": {
        "문화2": {
            "name": "창원 박물관",
            "attractions": ["마산박물관", "문화관"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 20000, "attraction": 10000}
        },
        "식도락2": {
            "name": "창원 음식 투어",
            "attractions": ["마산국밥", "시장", "맛집"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 10000, "food": 25000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "창원 백화점",
            "attractions": ["백화점", "쇼핑"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "창원 해변 카페",
            "attractions": ["해변 카페", "휴식"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 18000, "attraction": 8000}
        },
        "액티비티2": {
            "name": "창원 스포츠",
            "attractions": ["해양스포츠", "액티비티"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 10000, "food": 16000, "attraction": 25000}
        }
    },
    "청주": {
        "식도락2": {
            "name": "청주 수제비",
            "attractions": ["청주음식", "시장"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 24000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "청주 쇼핑",
            "attractions": ["백화점", "아울렛"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 18000, "attraction": 0}
        },
        "휴양2": {
            "name": "청주 호수 카페",
            "attractions": ["대청호 카페", "휴식"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 20000, "attraction": 8000}
        },
        "액티비티2": {
            "name": "청주 수상스포츠",
            "attractions": ["수상액티비티", "보트"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 20000, "food": 16000, "attraction": 25000}
        }
    },
    "포항": {
        "문화2": {
            "name": "포항 호미곶 역사",
            "attractions": ["호미곶", "등대", "박물관"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 18000, "attraction": 10000}
        },
        "식도락2": {
            "name": "포항 회센터",
            "attractions": ["회센터", "맛집"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 15000, "food": 35000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "포항 쇼핑",
            "attractions": ["백화점", "시장"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 16000, "attraction": 0}
        },
        "휴양2": {
            "name": "포항 해변 호텔",
            "attractions": ["해변 호텔", "휴식"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 20000, "attraction": 10000}
        },
        "액티비티2": {
            "name": "포항 다이빙",
            "attractions": ["스쿠버다이빙", "수상스포츠"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 15000, "food": 18000, "attraction": 40000}
        }
    },
    "울산": {
        "문화2": {
            "name": "울산 박물관",
            "attractions": ["울산박물관", "미술관"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 0, "food": 20000, "attraction": 10000}
        },
        "식도락2": {
            "name": "울산 회센터",
            "attractions": ["울산 회", "맛집"],
            "duration_days": 1,
            "popular": True,
            "base_cost": {"transport": 0, "food": 30000, "attraction": 0}
        },
        "쇼핑2": {
            "name": "울산 쇼핑",
            "attractions": ["백화점", "상점"],
            "duration_days": 1,
            "popular": False,
            "base_cost": {"transport": 0, "food": 16000, "attraction": 0}
        },
        "휴양2": {
            "name": "울산 해변 휴양",
            "attractions": ["해변 카페", "휴식"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 0, "food": 18000, "attraction": 8000}
        },
        "액티비티2": {
            "name": "울산 해양스포츠",
            "attractions": ["수상스포츠", "낚시"],
            "duration_days": 2,
            "popular": False,
            "base_cost": {"transport": 0, "food": 16000, "attraction": 25000}
        }
    }
}

# 이제 이 데이터를 travel_data.py에 추가해야 합니다
print("부족한 코스 데이터 생성 완료:")
for region, courses in new_courses_data.items():
    print(f"{region}: {len(courses)}개 코스")

print(f"\n총 {sum(len(c) for c in new_courses_data.values())}개의 새 코스 생성됨")
print("\n이제 travel_data.py에 추가할 준비 완료")
