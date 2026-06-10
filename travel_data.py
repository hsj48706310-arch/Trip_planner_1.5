# 국내 여행 코스 데이터 및 비용 정보

TRAVEL_DESTINATIONS = {
    "서울": {
        "courses": {
            "문화": {
                "name": "서울 전통문화 투어",
                "attractions": ["경복궁", "북촌 한옥마을", "청계천", "명동"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 30000, "attraction": 25000}
            },
            "문화2": {
                "name": "서울 궁궐과 역사 탐방",
                "attractions": ["덕수궁", "경희궁", "창덕궁", "인사동"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "서울 쇼핑 천국",
                "attractions": ["명동", "강남", "동대문", "가로수길"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 35000, "attraction": 0}
            },
            "쇼핑2": {
                "name": "강남 럭셔리 쇼핑 여행",
                "attractions": ["강남역", "압구정", "청담동", "신사동"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 40000, "attraction": 0}
            },
            "식도락": {
                "name": "서울 미식 투어",
                "attractions": ["강남 한우거리", "명동 먹거리", "진계미로시장", "경동시장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 45000, "attraction": 10000}
            },
            "식도락2": {
                "name": "서울 전통음식 체험",
                "attractions": ["광장시장", "남대문시장", "종로", "삼계탕 골목"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 35000, "attraction": 8000}
            },
            "자연": {
                "name": "한강 생태 휴양",
                "attractions": ["한강공원", "여의도공원", "난지도", "뚝섬"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 10000}
            },
            "자연2": {
                "name": "서울 숲 치유 여행",
                "attractions": ["서울숲", "봉산", "아차산", "용산 공원"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 8000}
            },
            "휴양": {
                "name": "강남 휴양 여행",
                "attractions": ["강남 호텔", "한강공원", "강남 카페거리", "코엑스"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 40000, "attraction": 15000}
            },
            "휴양2": {
                "name": "서울 웰니스 리트릿",
                "attractions": ["종로 찜질방", "강남 스파", "청담동 카페", "한강"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 35000, "attraction": 20000}
            },
            "액티비티": {
                "name": "서울 스포츠 활동",
                "attractions": ["잠수교", "한강 자전거", "보라매공원", "올림픽공원"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 15000}
            },
            "액티비티2": {
                "name": "서울 어드벤처 투어",
                "attractions": ["롤러스케이트장", "볼링장", "실내스키", "짚라인"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 30000, "attraction": 40000}
            }
        }
    },
    "부산": {
        "courses": {
            "문화": {
                "name": "부산 문화유산 투어",
                "attractions": ["해인사", "범어사", "보수동 책방골목", "감천문화마을"],
                "duration_days": 3,
                "popular": False,
                "base_cost": {"transport": 35000, "food": 30000, "attraction": 20000}
            },
            "문화2": {
                "name": "부산 근현대 역사 투어",
                "attractions": ["용두산공원", "초량 7080추억거리", "국립해양박물관", "이중섭거리"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 25000, "attraction": 15000}
            },
            "해변": {
                "name": "부산 해변 여행",
                "attractions": ["해운대 해수욕장", "광안리", "태종대", "송정 해수욕장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 25000, "attraction": 15000}
            },
            "해변2": {
                "name": "부산 동해 일출 여행",
                "attractions": ["광안리 해변", "광안대교", "오륙도", "바다향로공원"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 28000, "attraction": 12000}
            },
            "식도락": {
                "name": "부산 해산물 투어",
                "attractions": ["자갈치 시장", "맛집 골목", "감천문화마을", "BIFF광장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 45000, "attraction": 10000}
            },
            "식도락2": {
                "name": "부산 국밥과 회 투어",
                "attractions": ["부산국제시장", "부산 돼지국밥 골목", "자갈치", "용두산"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 40000, "attraction": 8000}
            },
            "자연": {
                "name": "부산 섬 탐험",
                "attractions": ["오륙도", "절영해안산책로", "태종대", "동백섬"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 35000, "food": 25000, "attraction": 20000}
            },
            "자연2": {
                "name": "부산 산책 여행",
                "attractions": ["해운대 해녀촌", "청사포 해변", "이기대", "정도어촌"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 22000, "attraction": 10000}
            },
            "쇼핑": {
                "name": "부산 쇼핑 투어",
                "attractions": ["부산 국제시장", "부산 보수동", "서면 상권", "호텔신라"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 30000, "attraction": 5000}
            },
            "쇼핑2": {
                "name": "부산 백화점 쇼핑",
                "attractions": ["롯데백화점", "신세계백화점", "갤러리아", "서면"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 30000, "food": 35000, "attraction": 0}
            },
            "휴양": {
                "name": "부산 해변 휴양",
                "attractions": ["해운대", "카페거리", "비치클럽", "해변 산책"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 35000, "attraction": 20000}
            },
            "휴양2": {
                "name": "부산 온천 리조트",
                "attractions": ["해운대 온천", "스파랜드", "호텔 라운지", "해변 휴식"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 40000, "attraction": 25000}
            },
            "액티비티": {
                "name": "부산 수상액티비티",
                "attractions": ["해수욕장", "스쿠버다이빙", "제트스키", "보트투어"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 30000, "food": 30000, "attraction": 35000}
            },
            "액티비티2": {
                "name": "부산 트래킹 투어",
                "attractions": ["태종대", "절영해안산책로", "동백섬", "오륙도"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 30000, "food": 25000, "attraction": 15000}
            }
        }
    },
    "경주": {
        "courses": {
            "문화": {
                "name": "경주 신라문화 투어",
                "attractions": ["불국사", "석굴암", "대릉원", "안압지"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 25000}
            },
            "문화2": {
                "name": "경주 유적지 탐방",
                "attractions": ["대릉원", "원성왕릉", "에밀레종", "성덕대왕신공원"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 20000}
            },
            "불교": {
                "name": "경주 불교유산 투어",
                "attractions": ["불국사", "석굴암", "감은사지", "낭산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 20000}
            },
            "식도락": {
                "name": "경주 로컬 푸드",
                "attractions": ["황남빵", "교리김밥", "안강포 떡국", "교촌마을"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 5000}
            },
            "자연": {
                "name": "경주 자연 트래킹",
                "attractions": ["남산", "토함산", "문무대왕릉", "대명리계곡"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 15000}
            },
            "휴양": {
                "name": "경주 온천 휴양",
                "attractions": ["경주 보문호", "온천단지", "관광호텔", "카페거리"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 30000, "attraction": 20000}
            },
            "액티비티": {
                "name": "경주 자전거 투어",
                "attractions": ["보문호 자전거길", "불국사", "대릉원", "황리단길"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 10000}
            },
            "쇼핑": {
                "name": "경주 전통공예 쇼핑",
                "attractions": ["황리단길", "보문관광단지", "전통공예관", "기념품거리"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 5000}
            },
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
        }
    },
    "제주": {
        "courses": {
            "문화": {
                "name": "제주 전통문화 투어",
                "attractions": ["용머리해안", "성이시돌목장", "제주민속촌", "방주교회"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 30000, "attraction": 20000}
            },
            "자연": {
                "name": "제주 자연경관 투어",
                "attractions": ["한라산", "만장굴", "협재 해수욕장", "성산일출봉"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 35000, "attraction": 30000}
            },
            "자연2": {
                "name": "제주 해안 경관",
                "attractions": ["정방폭포", "천지연폭포", "중문색달해변", "용머리"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 32000, "attraction": 25000}
            },
            "식도락": {
                "name": "제주 흑돼지 투어",
                "attractions": ["흑돼지 거리", "회센터", "해산물 맛집", "올레시장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 45000, "attraction": 10000}
            },
            "휴양": {
                "name": "제주 휴양지 여행",
                "attractions": ["중문 관광단지", "신화월드", "해수욕장", "카페 투어"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 40000, "attraction": 25000}
            },
            "휴양2": {
                "name": "제주 스파 리조트",
                "attractions": ["해양박물관", "치유의숲", "카페거리", "해변"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 45000, "attraction": 30000}
            },
            "액티비티": {
                "name": "제주 액티비티 투어",
                "attractions": ["해녀체험", "스쿠버다이빙", "서핑", "트래킹"],
                "duration_days": 3,
                "popular": False,
                "base_cost": {"transport": 50000, "food": 35000, "attraction": 60000}
            },
            "액티비티2": {
                "name": "제주 올레길 트래킹",
                "attractions": ["올레길 1-7코스", "해변산책", "용머리", "성산일출봉"],
                "duration_days": 3,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 30000, "attraction": 15000}
            },
            "쇼핑": {
                "name": "제주 롯데월드 쇼핑",
                "attractions": ["롯데 아울렛", "해비치호텔", "신라호텔", "쇼핑몰"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 50000, "food": 35000, "attraction": 10000}
            },
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
        }
    },

    "강릉": {
        "courses": {
            "문화": {
                "name": "강릉 한옥 문화",
                "attractions": ["오죽헌", "선교장", "정동진역", "강릉선비문화축제"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 15000}
            },
            "해변": {
                "name": "강릉 해변 여행",
                "attractions": ["경포대 해수욕장", "정동진", "아바이마을", "어촌"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 10000}
            },
            "해변2": {
                "name": "강릉 동해 해안 드라이브",
                "attractions": ["정동진", "동해 해변", "추암", "죽도"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 22000, "attraction": 12000}
            },
            "식도락": {
                "name": "강릉 로컬 푸드",
                "attractions": ["초당두부마을", "강릉 해산물", "경포닭강정", "순두부"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 28000, "attraction": 5000}
            },
            "자연": {
                "name": "강릉 자연산책",
                "attractions": ["경포 수련지", "오죽헌 숲", "강릉 해변", "석병산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 18000, "attraction": 10000}
            },
            "휴양": {
                "name": "강릉 온천 휴양",
                "attractions": ["강릉 온천", "경포호텔", "해변 카페", "선제 가옥"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 30000, "attraction": 20000}
            },
            "액티비티": {
                "name": "강릉 레포츠 투어",
                "attractions": ["서핑", "카약", "스키장", "래프팅"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 35000}
            },
            "쇼핑": {
                "name": "강릉 쇼핑",
                "attractions": ["경포 쇼핑몰", "강릉역", "중앙시장", "아울렛"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 0}
            },
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
        }
    },
    "대구": {
        "courses": {
            "문화": {
                "name": "대구 문화유산 투어",
                "attractions": ["대구 약령시", "삼덕동 카페골목", "팔공산", "보문"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 10000}
            },
            "문화2": {
                "name": "대구 근대 건축물 투어",
                "attractions": ["중앙로", "달성공원", "국채보상운동기념공원", "33인 광장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 8000}
            },
            "식도락": {
                "name": "대구 맛의 도시 투어",
                "attractions": ["약령시", "푸드 코트", "팔공산 자락", "카페존"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 35000, "attraction": 5000}
            },
            "식도락2": {
                "name": "대구 국밥과 닭요리",
                "attractions": ["중앙로 닭거리", "염매시장", "국밥 골목", "수성구"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 30000, "attraction": 0}
            },
            "자연": {
                "name": "대구 팔공산 트래킹",
                "attractions": ["팔공산", "북문", "금강공원", "동화사"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 10000}
            },
            "휴양": {
                "name": "대구 도심 휴양",
                "attractions": ["신타운", "카페거리", "앞산공원", "팔공산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 10000}
            },
            "액티비티": {
                "name": "대구 액티비티",
                "attractions": ["팔공산 등산", "자전거", "래프팅", "클라이밍"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 22000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "대구 쇼핑",
                "attractions": ["중앙로", "아울렛", "백화점", "중앙시장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 0}
            },
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
        }
    },
    "전주": {
        "courses": {
            "문화": {
                "name": "전주 한옥마을 투어",
                "attractions": ["한옥마을", "경기전", "오목대", "전주 박물관"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 10000}
            },
            "문화2": {
                "name": "전주 예술 투어",
                "attractions": ["전주영화박물관", "전주미술관", "황리단길", "예술센터"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 22000, "attraction": 12000}
            },
            "식도락": {
                "name": "전주 음식문화 투어",
                "attractions": ["전주 비빔밥", "한옥마을 맛집", "경기전", "야시장"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 35000, "attraction": 5000}
            },
            "식도락2": {
                "name": "전주 로컬 음식",
                "attractions": ["콩나물국밥", "우육", "육회", "생선까스"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 30000, "attraction": 0}
            },
            "자연": {
                "name": "전주 자연",
                "attractions": ["덕진공원", "용진강", "내장산", "모악산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 10000}
            },
            "휴양": {
                "name": "전주 한옥 휴양",
                "attractions": ["한옥마을 숙박", "전주 카페", "경기전", "산책로"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 28000, "attraction": 15000}
            },
            "액티비티": {
                "name": "전주 문화체험",
                "attractions": ["한지 만들기", "도자기", "비빔밥 체험", "부채"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "전주 쇼핑",
                "attractions": ["한옥마을", "공예품", "기념품", "백화점"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 5000}
            },
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
        }
    },
    "인천": {
        "courses": {
            "문화": {
                "name": "인천 역사 투어",
                "attractions": ["차이나타운", "인천항", "개항장", "자유공원"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 15000}
            },
            "해변": {
                "name": "인천 해변 여행",
                "attractions": ["문학경기장", "인천대교", "소래포구", "영흥대교"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 10000}
            },
            "해변2": {
                "name": "인천 섬 투어",
                "attractions": ["강화도", "펄문석산", "교동도", "석모도"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 22000, "attraction": 12000}
            },
            "식도락": {
                "name": "인천 해산물",
                "attractions": ["소래포구", "해산물", "중국음식", "차이나타운"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 30000, "attraction": 5000}
            },
            "자연": {
                "name": "인천 자연",
                "attractions": ["강화도 트래킹", "갯벌 트래킹", "해수욕장", "숲길"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 18000, "attraction": 8000}
            },
            "휴양": {
                "name": "인천 휴양",
                "attractions": ["비로도", "호텔", "카페", "해변"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 15000}
            },
            "액티비티": {
                "name": "인천 액티비티",
                "attractions": ["스카이라크", "래프팅", "자전거", "낚시"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 25000}
            },
            "쇼핑": {
                "name": "인천 쇼핑",
                "attractions": ["차이나타운", "아울렛", "판타지아", "백화점"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 18000, "attraction": 0}
            },
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
        }
    },
    "대전": {
        "courses": {
            "문화": {
                "name": "대전 문화 투어",
                "attractions": ["대전역사문화관", "유성온천", "대전문화예술단지", "계룡산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 10000}
            },
            "과학": {
                "name": "대전 과학 투어",
                "attractions": ["국립중앙과학관", "대전시립미술관", "한밭수목원", "엑스포과학공원"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 20000}
            },
            "과학2": {
                "name": "대전 전시회 투어",
                "attractions": ["대전컨벤션센터", "미술관", "박물관", "갤러리"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 22000, "attraction": 15000}
            },
            "식도락": {
                "name": "대전 음식",
                "attractions": ["중앙로 맛집", "유성 미식", "닭강정", "청국장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 0}
            },
            "자연": {
                "name": "대전 계룡산 트래킹",
                "attractions": ["계룡산", "동학사", "자동차", "숲길"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 10000}
            },
            "휴양": {
                "name": "대전 온천 휴양",
                "attractions": ["유성온천", "스파", "호텔", "카페"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 28000, "attraction": 15000}
            },
            "액티비티": {
                "name": "대전 액티비티",
                "attractions": ["스카이로드", "과학관 체험", "클라이밍", "래프팅"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 25000}
            },
            "쇼핑": {
                "name": "대전 쇼핑",
                "attractions": ["중앙로", "아울렛", "백화점", "동문시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 0}
            },
            "문화2": {
                "name": "대전 박물관",
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
        }
    },
    "광주": {
        "courses": {
            "문화": {
                "name": "광주 문화 투어",
                "attractions": ["국립광주박물관", "무등산", "광주비엔날레", "문화전당"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 22000, "attraction": 15000}
            },
            "역사": {
                "name": "광주 역사 투어",
                "attractions": ["국립광주박물관", "무등산", "광주비엔날레", "5.18기념공원"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 15000}
            },
            "식도락": {
                "name": "광주 음식 투어",
                "attractions": ["광주 맛집", "1913송정역시장", "양림동", "충장로"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 30000, "attraction": 5000}
            },
            "식도락2": {
                "name": "광주 전통 음식",
                "attractions": ["광주 떡갈비", "중앙시장", "국밥", "된장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 28000, "attraction": 0}
            },
            "자연": {
                "name": "광주 자연",
                "attractions": ["무등산", "담양죽녹원", "정자", "계곡"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 10000}
            },
            "휴양": {
                "name": "광주 휴양",
                "attractions": ["무등산 카페", "문화전당", "호텔", "산책"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 25000, "attraction": 12000}
            },
            "액티비티": {
                "name": "광주 액티비티",
                "attractions": ["무등산 등산", "자전거", "래프팅", "클라이밍"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "광주 쇼핑",
                "attractions": ["충장로", "아울렛", "백화점", "시장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 25000, "food": 20000, "attraction": 0}
            },
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
        }
    },
    "수원": {
        "courses": {
            "문화": {
                "name": "수원 역사 투어",
                "attractions": ["수원화성", "화성행궁", "팔달문", "행궁동"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 25000, "attraction": 15000}
            },
            "문화2": {
                "name": "수원 화성 투어",
                "attractions": ["수원화성", "화성행궁", "성곽 산책", "연무대"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 22000, "attraction": 12000}
            },
            "쇼핑": {
                "name": "수원 쇼핑 투어",
                "attractions": ["갤러리아백화점", "AK플라자", "롯데몰", "수원역"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 20000, "attraction": 5000}
            },
            "식도락": {
                "name": "수원 로컬 음식",
                "attractions": ["화성행궁", "전통음식", "닭발거리", "중앙시장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 25000, "attraction": 0}
            },
            "자연": {
                "name": "수원 자연",
                "attractions": ["광교생태공원", "선큰정원", "흰지봉", "이목공원"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 18000, "attraction": 8000}
            },
            "휴양": {
                "name": "수원 도심 휴양",
                "attractions": ["광교호수", "카페거리", "공원", "산책"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 22000, "attraction": 10000}
            },
            "액티비티": {
                "name": "수원 액티비티",
                "attractions": ["화성 슬라프라인", "자전거", "클라이밍", "래프팅"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 20000, "attraction": 25000}
            },
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
        }
    },
    "창원": {
        "courses": {
            "문화": {
                "name": "창원 문화 투어",
                "attractions": ["창원시립마산박물관", "진해 벚꽃", "해양공원", "포토존"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 22000, "attraction": 12000}
            },
            "산업": {
                "name": "창원 산업 투어",
                "attractions": ["창원산업단지", "진해군항제", "마산항", "창원시립마산박물관"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 25000, "attraction": 10000}
            },
            "자연": {
                "name": "창원 자연 투어",
                "attractions": ["창원대교", "진해대교", "마산해양신도시", "홍곡 저수지"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 20000, "attraction": 15000}
            },
            "해변": {
                "name": "창원 해변",
                "attractions": ["마산해변", "진해해변", "돝섬", "용원"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 20000, "attraction": 10000}
            },
            "식도락": {
                "name": "창원 음식",
                "attractions": ["마산국밥", "창원 닭", "우동", "회"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 10000, "food": 22000, "attraction": 0}
            },
            "휴양": {
                "name": "창원 휴양",
                "attractions": ["진해만, 호텔", "카페", "공원", "산책"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 20000, "attraction": 10000}
            },
            "액티비티": {
                "name": "창원 액티비티",
                "attractions": ["해양스포츠", "자전거", "등산", "낚시"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 18000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "창원 쇼핑",
                "attractions": ["마산 상권", "백화점", "아울렛", "시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 10000, "food": 18000, "attraction": 0}
            },
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
        }
    },
    "청주": {
        "courses": {
            "문화": {
                "name": "청주 문화 투어",
                "attractions": ["청주고인쇄박물관", "청남대", "문의문화재단지", "청주랜드"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 15000}
            },
            "문화2": {
                "name": "청주 역사",
                "attractions": ["대청호", "박물관", "문화재", "유적지"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 12000}
            },
            "자연": {
                "name": "청주 자연 투어",
                "attractions": ["국립청주박물관", "무심천", "우암산", "대청호"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 25000, "attraction": 10000}
            },
            "자연2": {
                "name": "청주 호수 자연",
                "attractions": ["대청호", "트래킹", "보트", "카페"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 20000, "food": 20000, "attraction": 12000}
            },
            "식도락": {
                "name": "청주 음식",
                "attractions": ["청주약산", "수제비", "중앙동", "시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 22000, "attraction": 0}
            },
            "휴양": {
                "name": "청주 휴양",
                "attractions": ["대청호 호텔", "카페", "공원", "산책"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 22000, "attraction": 10000}
            },
            "액티비티": {
                "name": "청주 액티비티",
                "attractions": ["수상스포츠", "트래킹", "자전거", "클라이밍"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "청주 쇼핑",
                "attractions": ["구도심", "아울렛", "백화점", "시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 20000, "food": 18000, "attraction": 0}
            },
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
        }
    },
    "포항": {
        "courses": {
            "문화": {
                "name": "포항 문화",
                "attractions": ["호미곶", "등대", "해안", "박물관"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 12000}
            },
            "해변": {
                "name": "포항 해변 투어",
                "attractions": ["호미곶", "영일대해수욕장", "포항운하", "구룡포"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 25000, "attraction": 15000}
            },
            "해변2": {
                "name": "포항 동해 해안",
                "attractions": ["영일대", "호미곶등대", "죽도", "이사부"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 22000, "attraction": 12000}
            },
            "산업": {
                "name": "포항 산업 투어",
                "attractions": ["포스코", "포항산업과학연구원", "영일만항", "철강단지"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 10000}
            },
            "식도락": {
                "name": "포항 해산물",
                "attractions": ["영일대 회", "포항국밥", "구룡포", "중앙시장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 15000, "food": 28000, "attraction": 0}
            },
            "자연": {
                "name": "포항 자연",
                "attractions": ["죽도", "호미곶", "이사부 동상", "해안산책"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 10000}
            },
            "휴양": {
                "name": "포항 해변 휴양",
                "attractions": ["호텔", "카페", "해변", "산책"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 22000, "attraction": 12000}
            },
            "액티비티": {
                "name": "포항 액티비티",
                "attractions": ["서핑", "다이빙", "낚시", "트래킹"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 20000, "attraction": 25000}
            },
            "쇼핑": {
                "name": "포항 쇼핑",
                "attractions": ["포항역", "백화점", "아울렛", "시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 15000, "food": 18000, "attraction": 0}
            },
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
        }
    },
    "울산": {
        "courses": {
            "문화": {
                "name": "울산 문화",
                "attractions": ["울산박물관", "대왕암", "황금색마", "영남알프스"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 22000, "attraction": 12000}
            },
            "산업": {
                "name": "울산 산업 투어",
                "attractions": ["현대자동차", "울산대교", "산업단지", "태화강"],
                "duration_days": 2,
                "popular": True,
                "base_cost": {"transport": 0, "food": 25000, "attraction": 10000}
            },
            "산업2": {
                "name": "울산 해양 산업",
                "attractions": ["현대중공업", "울산항", "선박", "공업지구"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 20000, "attraction": 8000}
            },
            "자연": {
                "name": "울산 자연경관 투어",
                "attractions": ["간절곶", "대왕암", "영남알프스", "태화강"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 20000, "attraction": 15000}
            },
            "자연2": {
                "name": "울산 산 트래킹",
                "attractions": ["영남알프스", "신불산", "가지산", "천황산"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 18000, "attraction": 10000}
            },
            "식도락": {
                "name": "울산 음식",
                "attractions": ["간절곶 회", "울산 막창", "일산", "시장"],
                "duration_days": 1,
                "popular": True,
                "base_cost": {"transport": 0, "food": 25000, "attraction": 0}
            },
            "휴양": {
                "name": "울산 휴양",
                "attractions": ["태화강", "카페", "공원", "호텔"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 20000, "attraction": 10000}
            },
            "액티비티": {
                "name": "울산 액티비티",
                "attractions": ["등산", "자전거", "낚시", "수상스포츠"],
                "duration_days": 2,
                "popular": False,
                "base_cost": {"transport": 0, "food": 18000, "attraction": 20000}
            },
            "쇼핑": {
                "name": "울산 쇼핑",
                "attractions": ["울산역", "백화점", "아울렛", "시장"],
                "duration_days": 1,
                "popular": False,
                "base_cost": {"transport": 0, "food": 18000, "attraction": 0}
            },
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
}

# 여행 테마별 설명
THEMES = {
    "문화": "역사적 유산과 전통문화를 체험하는 여행",
    "식도락": "지역의 특색있는 음식을 맛보는 여행",
    "자연": "산, 바다, 숲, 계곡 등 자연경관을 감상하는 여행",
    "쇼핑": "쇼핑과 도시문화를 즐기는 여행",
    "휴양": "조용한 휴양지에서 쉬는 여행",
    "액티비티": "체험과 레저 활동을 하는 여행"
}

# 지역별 교통 비용 (울산 기준)
TRANSPORT_COSTS = {
    "울산": 0,
    "서울": 40000,
    "부산": 10000,
    "경주": 15000,
    "제주": 55000,
    "강릉": 35000,
    "대구": 20000,
    "전주": 30000,
    "인천": 30000,
    "대전": 25000,
    "광주": 35000,
    "수원": 35000,
    "창원": 15000,
    "청주": 30000,
    "포항": 20000
}

