import streamlit as st
import json
import pydeck as pdk
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from travel_data import TRAVEL_DESTINATIONS, THEMES, TRANSPORT_COSTS
from tavily_search import search_travel_info, deduplicate_results, format_tavily_context

load_dotenv()

st.set_page_config(page_title="국내 여행 추천 에이전트", page_icon="🚂")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 메인 배경색: 연한 노란색 */
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFE0;
    }
    /* 사이드바 배경색: 연한 녹색 */
    [data-testid="stSidebar"] {
        background-color: #E8F5E8;
    }
    /* 타이틀 글씨 크기 조정 */
    h1 {
        font-size: 33px !important;        text-align: left !important;    }
</style>
""", unsafe_allow_html=True)

st.title("🚞 국내 여행 코스, 내 취향대로 추천해드려요 🌈")
st.sidebar.header("여행 정보 입력")

THEME_MATCHING_CATEGORIES = {
    "문화": ["문화", "문화2", "역사", "불교"],
    "식도락": ["식도락", "식도락2", "먹거리", "마실거리"],
    "자연": ["자연", "자연2", "바다", "해변", "산", "숲", "계곡"],
    "쇼핑": ["쇼핑", "쇼핑2", "기념품"],
    "휴양": ["휴양", "휴양2", "힐링", "리조트"],
    "액티비티": ["액티비티", "액티비티2", "체험", "스포츠"]
}


def course_type_matches_theme(course_type: str, theme_preference: str) -> bool:
    course_type = course_type.strip()
    theme_preference = theme_preference.strip()
    aliases = THEME_MATCHING_CATEGORIES.get(theme_preference, [theme_preference])

    if course_type == theme_preference:
        return True
    if course_type.startswith(theme_preference):
        return True
    if course_type in aliases:
        return True
    return any(alias in course_type for alias in aliases)

# 입력 필드
regions = list(TRAVEL_DESTINATIONS.keys())
departure_region = st.sidebar.selectbox("출발 지역", regions)
region = st.sidebar.selectbox("여행 지역", regions)

duration = st.sidebar.slider("여행 기간 (일)", 1, 7, 3)

num_people = st.sidebar.slider("여행 인원수", 1, 10, 4)

themes = list(THEMES.keys())
theme_descriptions = [f"{theme}: {THEMES[theme]}" for theme in themes]
theme_preference = st.sidebar.selectbox("선호 테마", themes, format_func=lambda x: f"{x}: {THEMES[x]}")

# Attraction coordinates for route map display
ATTRACTION_COORDINATES = {
    # 서울
    "경복궁": (37.579617, 126.977041),
    "덕수궁": (37.565384, 126.970476),
    "경희궁": (37.572222, 126.962778),
    "창덕궁": (37.574633, 127.010274),
    "북촌 한옥마을": (37.582600, 126.984900),
    "북촌한옥마을": (37.582600, 126.984900),
    "청계천": (37.569702, 126.982000),
    "명동": (37.560950, 126.985620),
    "강남역": (37.498110, 127.027610),
    "압구정": (37.527755, 127.027244),
    "청담동": (37.530208, 127.031429),
    "신사동": (37.520831, 127.021514),
    "가로수길": (37.527755, 127.027244),
    "동대문": (37.567597, 127.009664),
    "한강공원": (37.521907, 126.907622),
    "여의도공원": (37.523892, 126.928133),
    "난지도": (37.544056, 126.862814),
    "뚝섬": (37.533289, 127.088133),
    "서울숲": (37.544244, 127.086392),
    "봉산": (37.551170, 126.988226),
    "남산타워": (37.551170, 126.988226),
    "서울 스카이": (37.513248, 127.098263),
    "삼청동": (37.595555, 126.990833),
    "인사동": (37.574277, 126.989532),
    "광장시장": (37.565833, 126.997778),
    "남대문시장": (37.564167, 127.010556),
    "종로": (37.566297, 126.992622),
    "강남 한우거리": (37.498533, 127.025636),
    
    # 부산
    "해운대 해수욕장": (35.158698, 129.160408),
    "광안리": (35.153918, 129.118341),
    "광안대교": (35.158889, 129.114722),
    "태종대": (35.086312, 129.081814),
    "송정 해수욕장": (35.177778, 129.183889),
    "자갈치 시장": (35.097710, 129.035453),
    "감천문화마을": (35.097478, 129.010354),
    "BIFF광장": (35.097323, 129.035887),
    "오륙도": (35.082222, 129.084167),
    "절영해안산책로": (35.117222, 129.099167),
    "동백섬": (35.082500, 129.084167),
    "해녀촌": (35.147222, 129.117222),
    "청사포 해변": (35.193889, 129.203056),
    "이기대": (35.091944, 129.082222),
    "정도어촌": (35.113056, 129.086944),
    "부산국제시장": (35.097710, 129.035453),
    "보수동 책방골목": (35.103333, 129.040000),
    "용두산공원": (35.101667, 129.028333),
    "초량 7080추억거리": (35.095833, 129.041667),
    "국립해양박물관": (35.098889, 129.042222),
    "이중섭거리": (35.098056, 129.051389),
    "롯데백화점": (35.164167, 129.163889),
    "신세계백화점": (35.098056, 129.029167),
    
    # 경주
    "불국사": (35.790784, 129.334601),
    "석굴암": (35.724182, 129.331916),
    "대릉원": (35.836389, 129.223056),
    "안압지": (35.836389, 129.219722),
    "원성왕릉": (35.840556, 129.228333),
    "에밀레종": (35.790833, 129.335000),
    "성덕대왕신공원": (35.781944, 129.342500),
    "남산": (35.840556, 129.213889),
    "토함산": (35.720278, 129.329722),
    "문무대왕릉": (35.847222, 129.225000),
    "대명리계곡": (35.810000, 129.456667),
    "보문호": (35.830556, 129.356944),
    "황리단길": (35.830556, 129.229167),
    
    # 제주
    "한라산": (33.362500, 126.533333),
    "만장굴": (33.385833, 126.915833),
    "협재 해수욕장": (33.251451, 126.242408),
    "성산일출봉": (33.459868, 126.940747),
    "중문 관광단지": (33.248968, 126.417726),
    "정방폭포": (33.251439, 126.417500),
    "천지연폭포": (33.254444, 126.560833),
    "용머리해안": (33.291389, 126.264722),
    
    # 강릉
    "경포대 해수욕장": (37.778889, 128.906389),
    "정동진": (37.776656, 129.124104),
    "오죽헌": (37.776727, 128.893621),
    "아바이마을": (37.777500, 128.912500),
    "선교장": (37.770000, 128.895833),
    "초당두부마을": (37.790556, 128.879167),
    "경포호": (37.781667, 128.906389),
    
    # 대구
    "대구 약령시": (35.873859, 128.590600),
    "삼덕동 카페골목": (35.872500, 128.595556),
    "팔공산": (35.945109, 128.648732),
    "동화사": (35.945278, 128.664167),
    "중앙로": (35.871389, 128.597222),
    "달성공원": (35.874167, 128.593056),
    "국채보상운동기념공원": (35.871944, 128.597500),
    "33인 광장": (35.872500, 128.600000),
    
    # 전주
    "한옥마을": (35.818644, 127.149696),
    "경기전": (35.815512, 127.143009),
    "전주 박물관": (35.821042, 127.142635),
    "오목대": (35.823611, 127.141389),
    "황리단길": (35.815556, 127.155833),
    "전주영화박물관": (35.817222, 127.146667),
    "전주미술관": (35.815278, 127.154444),
    "전주예술센터": (35.819167, 127.147500),
    
    # 인천
    "차이나타운": (37.471085, 126.619115),
    "인천항": (37.461389, 126.614722),
    "개항장": (37.471667, 126.615833),
    "자유공원": (37.471111, 126.614444),
    "문학경기장": (37.439167, 126.617778),
    "인천대교": (37.451667, 126.563056),
    "소래포구": (37.295000, 126.692222),
    "영흥대교": (37.216667, 126.575833),
    "강화도": (37.742500, 126.392500),
    "펄문석산": (37.680556, 126.460833),
    "교동도": (37.661111, 126.268333),
    
    # 대전
    "국립중앙과학관": (36.360399, 127.367694),
    "한밭수목원": (36.327121, 127.360910),
    "대전시립미술관": (36.359722, 127.368333),
    "유성온천": (36.352778, 127.368889),
    "계룡산": (36.304722, 127.203333),
    "동학사": (36.304444, 127.195556),
    "대전역사문화관": (36.327500, 127.424167),
    
    # 광주
    "국립광주박물관": (35.162709, 126.911996),
    "무등산": (35.143889, 126.885833),
    "광주비엔날레": (35.162222, 126.915833),
    "5.18기념공원": (35.168056, 126.903889),
    "문화전당": (35.161389, 126.914444),
    "담양죽녹원": (35.301667, 127.007222),
    
    # 수원
    "수원화성": (37.286408, 127.007500),
    "화성행궁": (37.283889, 127.001944),
    "팔달문": (37.280000, 127.008889),
    "행궁동": (37.285278, 127.003333),
    "광교생태공원": (37.286667, 127.068333),
    "선큰정원": (37.282222, 127.047222),
    
    # 창원
    "창원산업단지": (35.217896, 128.680322),
    "진해군항제": (35.133889, 128.661111),
    "마산항": (35.228889, 128.561111),
    "창원시립마산박물관": (35.230000, 128.563889),
    "진해해변": (35.150000, 128.648889),
    "창원대교": (35.239444, 128.606667),
    "진해대교": (35.180833, 128.683333),
    "마산해양신도시": (35.200833, 128.609167),
    "홍곡저수지": (35.350000, 128.750000),
    
    # 청주
    "청주고인쇄박물관": (36.648889, 127.110000),
    "청남대": (36.733333, 127.213889),
    "문의문화재단지": (36.730556, 127.300833),
    "대청호": (36.496667, 127.460000),
    "무심천": (36.636151, 127.471273),
    "우암산": (36.647222, 127.156667),
    
    # 포항
    "호미곶": (35.991026, 129.628239),
    "영일대해수욕장": (36.027512, 129.406422),
    "포항운하": (36.021389, 129.370833),
    "구룡포": (36.063889, 129.538056),
    "포스코": (36.140000, 129.350000),
    "영일만항": (36.028333, 129.393333),
    "죽도": (35.924722, 129.534444),
    "이사부동상": (35.998333, 129.618056),
    
    # 울산
    "울산대교": (35.506599, 129.427094),
    "태화강": (35.554423, 129.263350),
    "간절곶": (35.537778, 129.639444),
    "대왕암": (35.553056, 129.400833),
    "영남알프스": (35.700000, 129.300000),
    "현대자동차": (35.519722, 129.280556),
    "울산박물관": (35.560000, 129.320000),
    "신불산": (35.732222, 129.306389),
    "가지산": (35.733611, 129.308611),
    "천황산": (35.700000, 129.250000),
}

REGION_RECOMMENDED_PLACES = {
    "서울": {
        "restaurants": [{"name": "광화문 미진", "avg_cost": 18000}, {"name": "삼청동 수연산방", "avg_cost": 22000}],
        "cafes": [{"name": "앤트러사이트", "avg_cost": 9000}, {"name": "폴바셋", "avg_cost": 8500}]
    },
    "부산": {
        "restaurants": [{"name": "부산 돼지국밥", "avg_cost": 12000}, {"name": "광안리 회센터", "avg_cost": 25000}],
        "cafes": [{"name": "해운대 카페거리", "avg_cost": 9500}, {"name": "더베이101 카페", "avg_cost": 10000}]
    },
    "제주": {
        "restaurants": [{"name": "흑돼지 거리 맛집", "avg_cost": 18000}, {"name": "제주 해물탕", "avg_cost": 22000}],
        "cafes": [{"name": "카페 델문도", "avg_cost": 11000}, {"name": "아날로그 감귤", "avg_cost": 9000}]
    },
    "경주": {
        "restaurants": [{"name": "경주 황남빵", "avg_cost": 9000}, {"name": "교리김밥", "avg_cost": 7000}],
        "cafes": [{"name": "경주 카페거리", "avg_cost": 8500}, {"name": "황리단길 카페", "avg_cost": 9000}]
    },
    "울산": {
        "restaurants": [{"name": "간절곶 해물탕", "avg_cost": 20000}, {"name": "울산 막창 골목", "avg_cost": 18000}],
        "cafes": [{"name": "태화강 카페", "avg_cost": 9500}, {"name": "울산 대공원 카페", "avg_cost": 9000}]
    }
}

DEFAULT_PLACE_SET = {
    "restaurants": [{"name": "현지 추천 맛집", "avg_cost": 18000}],
    "cafes": [{"name": "감성 카페", "avg_cost": 9000}],
    "extra_spots": [{"name": "현지 명소", "avg_cost": 0}]
}

COURSE_RECOMMENDED_PLACES = {
    "서울": {
        "문화": {
            "restaurants": [{"name": "광화문 미진", "avg_cost": 18000}, {"name": "오죽헌 한옥식당", "avg_cost": 22000}],
            "cafes": [{"name": "삼청동 카페", "avg_cost": 9500}, {"name": "안국동 티룸", "avg_cost": 12000}],
            "extra_spots": [{"name": "덕수궁 돌담길", "avg_cost": 0}, {"name": "인사동 공예 거리", "avg_cost": 0}]
        },
        "문화2": {
            "restaurants": [{"name": "경희궁 한정식", "avg_cost": 20000}, {"name": "창덕궁 근처 카페", "avg_cost": 8000}],
            "cafes": [{"name": "종로 전통 찻집", "avg_cost": 10000}, {"name": "광교 북카페", "avg_cost": 11000}],
            "extra_spots": [{"name": "경희궁 산책로", "avg_cost": 0}, {"name": "창덕궁 후원", "avg_cost": 15000}]
        },
        "쇼핑": {
            "restaurants": [{"name": "명동 칼국수", "avg_cost": 12000}, {"name": "강남 한우구이", "avg_cost": 28000}],
            "cafes": [{"name": "스타필드 코엑스 카페", "avg_cost": 10000}, {"name": "가로수길 브런치 카페", "avg_cost": 13000}],
            "extra_spots": [{"name": "동대문 패션타운", "avg_cost": 0}, {"name": "명품 거리 청담동", "avg_cost": 0}]
        },
        "쇼핑2": {
            "restaurants": [{"name": "강남역 맛집", "avg_cost": 22000}, {"name": "압구정 로데오", "avg_cost": 25000}],
            "cafes": [{"name": "강남 럭셔리 카페", "avg_cost": 14000}, {"name": "신사동 가로수길 카페", "avg_cost": 12000}],
            "extra_spots": [{"name": "신세계백화점", "avg_cost": 0}, {"name": "미술관 쇼핑", "avg_cost": 0}]
        },
        "식도락": {
            "restaurants": [{"name": "강남 한우거리", "avg_cost": 35000}, {"name": "명동 먹거리", "avg_cost": 15000}],
            "cafes": [{"name": "종로 다방", "avg_cost": 7000}, {"name": "명동 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "광장시장", "avg_cost": 0}, {"name": "남대문시장", "avg_cost": 0}]
        },
        "식도락2": {
            "restaurants": [{"name": "삼계탕 골목", "avg_cost": 12000}, {"name": "전통 찌개", "avg_cost": 13000}],
            "cafes": [{"name": "서촌 카페", "avg_cost": 10000}, {"name": "북촌 전통 찻집", "avg_cost": 9000}],
            "extra_spots": [{"name": "경동시장", "avg_cost": 0}, {"name": "중앙시장", "avg_cost": 0}]
        },
        "자연": {
            "restaurants": [{"name": "한강 한정식", "avg_cost": 18000}, {"name": "여의도 브런치", "avg_cost": 16000}],
            "cafes": [{"name": "한강공원 카페", "avg_cost": 8000}, {"name": "뚝섬 카페트럭", "avg_cost": 7000}],
            "extra_spots": [{"name": "한강 자전거길", "avg_cost": 0}, {"name": "봄 벚꽃", "avg_cost": 0}]
        },
        "자연2": {
            "restaurants": [{"name": "서울숲 카페식당", "avg_cost": 14000}, {"name": "남산 전망 식당", "avg_cost": 20000}],
            "cafes": [{"name": "서울숲 카페", "avg_cost": 9000}, {"name": "봉산 트래킹 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "봉산 트래킹", "avg_cost": 0}, {"name": "남산 산책로", "avg_cost": 0}]
        },
        "휴양": {
            "restaurants": [{"name": "강남 프렌치 레스토랑", "avg_cost": 35000}, {"name": "여의도 일식", "avg_cost": 28000}],
            "cafes": [{"name": "강남 룸카페", "avg_cost": 12000}, {"name": "한강 뷰 카페", "avg_cost": 13000}],
            "extra_spots": [{"name": "강남 스파", "avg_cost": 0}, {"name": "한강 야경", "avg_cost": 0}]
        },
        "휴양2": {
            "restaurants": [{"name": "명동 스시", "avg_cost": 30000}, {"name": "청담동 카페레스토랑", "avg_cost": 25000}],
            "cafes": [{"name": "한강 라운지", "avg_cost": 13000}, {"name": "종로 찜질방 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "한계사 찜질방", "avg_cost": 8000}, {"name": "명동 나이트 투어", "avg_cost": 0}]
        },
        "액티비티": {
            "restaurants": [{"name": "올림픽공원 카페", "avg_cost": 12000}, {"name": "한강레일바이크 카페", "avg_cost": 10000}],
            "cafes": [{"name": "잠수교 자전거 카페", "avg_cost": 9000}, {"name": "올림픽공원 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "한강 자전거", "avg_cost": 0}, {"name": "롤러스케이트", "avg_cost": 0}]
        },
        "액티비티2": {
            "restaurants": [{"name": "강남 스포츠 센터 카페", "avg_cost": 11000}, {"name": "여의도 보트 카페", "avg_cost": 12000}],
            "cafes": [{"name": "클라이밍장 카페", "avg_cost": 8000}, {"name": "볼링장 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "실내 스노우보드", "avg_cost": 0}, {"name": "짚라인", "avg_cost": 0}]
        }
    },
    "부산": {
        "해변": {
            "restaurants": [{"name": "해운대 회센터", "avg_cost": 25000}, {"name": "광안리 카페식당", "avg_cost": 18000}],
            "cafes": [{"name": "해운대 파라다이스 카페", "avg_cost": 9500}, {"name": "광안리 바다뷰 카페", "avg_cost": 10000}],
            "extra_spots": [{"name": "송정 해변 산책", "avg_cost": 0}, {"name": "다대포 일몰 명소", "avg_cost": 0}]
        },
        "해변2": {
            "restaurants": [{"name": "오륙도 횟집", "avg_cost": 28000}, {"name": "해녀촌 식당", "avg_cost": 20000}],
            "cafes": [{"name": "광안대교 야경 카페", "avg_cost": 10000}, {"name": "절영해안 산책 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "오륙도 일몰", "avg_cost": 0}, {"name": "태종대 트래킹", "avg_cost": 0}]
        },
        "식도락": {
            "restaurants": [{"name": "자갈치 시장 골목", "avg_cost": 15000}, {"name": "부산 밀면 전문점", "avg_cost": 12000}],
            "cafes": [{"name": "부산 감천 카페", "avg_cost": 9500}, {"name": "해운대 디저트 카페", "avg_cost": 11000}],
            "extra_spots": [{"name": "부산 국제시장", "avg_cost": 0}, {"name": "부산 책방골목", "avg_cost": 0}]
        },
        "식도락2": {
            "restaurants": [{"name": "부산 국밥 골목", "avg_cost": 10000}, {"name": "부산 떡국", "avg_cost": 8000}],
            "cafes": [{"name": "중앙로 카페", "avg_cost": 8000}, {"name": "보수동 전통 찻집", "avg_cost": 7000}],
            "extra_spots": [{"name": "중앙시장", "avg_cost": 0}, {"name": "국제시장 야식", "avg_cost": 0}]
        },
        "문화": {
            "restaurants": [{"name": "부산 전통 한식당", "avg_cost": 20000}, {"name": "해운대 양식 레스토랑", "avg_cost": 28000}],
            "cafes": [{"name": "감천문화마을 카페", "avg_cost": 9000}, {"name": "부산 미술관 카페", "avg_cost": 12000}],
            "extra_spots": [{"name": "해인사 가는 산책길", "avg_cost": 0}, {"name": "보수동 책방골목", "avg_cost": 0}]
        },
        "문화2": {
            "restaurants": [{"name": "용두산 전망식당", "avg_cost": 22000}, {"name": "이중섭 거리 카페", "avg_cost": 12000}],
            "cafes": [{"name": "초량 추억거리 카페", "avg_cost": 8000}, {"name": "국립해양박물관 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "용두산 야경", "avg_cost": 0}, {"name": "해운대 박물관", "avg_cost": 0}]
        },
        "쇼핑": {
            "restaurants": [{"name": "롯데백화점 레스토랑", "avg_cost": 30000}, {"name": "신세계 식당", "avg_cost": 28000}],
            "cafes": [{"name": "롯데월드 카페", "avg_cost": 10000}, {"name": "신세계 카페", "avg_cost": 11000}],
            "extra_spots": [{"name": "서면 상권", "avg_cost": 0}, {"name": "롯데 아울렛", "avg_cost": 0}]
        },
        "자연": {
            "restaurants": [{"name": "태종대 한정식", "avg_cost": 25000}, {"name": "절영해안 카페식당", "avg_cost": 15000}],
            "cafes": [{"name": "태종대 카페", "avg_cost": 9000}, {"name": "해변 산책 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "절영해안산책로", "avg_cost": 0}, {"name": "동백섬 산책", "avg_cost": 0}]
        },
        "휴양": {
            "restaurants": [{"name": "해운대 브런치", "avg_cost": 18000}, {"name": "카페식당", "avg_cost": 16000}],
            "cafes": [{"name": "해변 휴식 카페", "avg_cost": 10000}, {"name": "룸카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "해변 산책", "avg_cost": 0}, {"name": "야경 데이트 코스", "avg_cost": 0}]
        },
        "액티비티": {
            "restaurants": [{"name": "다이빙센터 카페", "avg_cost": 12000}, {"name": "수상스포츠 카페", "avg_cost": 11000}],
            "cafes": [{"name": "스쿠버 카페", "avg_cost": 8000}, {"name": "스포츠센터 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "스쿠버다이빙", "avg_cost": 0}, {"name": "제트스키", "avg_cost": 0}]
        }
    },
    "경주": {
        "문화": {
            "restaurants": [{"name": "불국사 식당", "avg_cost": 15000}, {"name": "안압지 한정식", "avg_cost": 18000}],
            "cafes": [{"name": "불국사 카페", "avg_cost": 8000}, {"name": "안압지 전통 찻집", "avg_cost": 9000}],
            "extra_spots": [{"name": "대릉원 산책", "avg_cost": 0}, {"name": "신라 유산", "avg_cost": 0}]
        },
        "문화2": {
            "restaurants": [{"name": "성덕대왕신공원 카페", "avg_cost": 12000}, {"name": "원성왕릉 한정식", "avg_cost": 16000}],
            "cafes": [{"name": "황리단길 카페", "avg_cost": 9000}, {"name": "문화재 주변 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "에밀레종", "avg_cost": 0}, {"name": "유적지 투어", "avg_cost": 0}]
        },
        "식도락": {
            "restaurants": [{"name": "황남빵", "avg_cost": 5000}, {"name": "교리김밥", "avg_cost": 8000}],
            "cafes": [{"name": "경주 전통 찻집", "avg_cost": 7000}, {"name": "황리단길 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "로컬 음식 투어", "avg_cost": 0}, {"name": "명소별 간식", "avg_cost": 0}]
        },
        "자연": {
            "restaurants": [{"name": "남산 트래킹 카페", "avg_cost": 11000}, {"name": "계곡 식당", "avg_cost": 13000}],
            "cafes": [{"name": "산책길 카페", "avg_cost": 8000}, {"name": "자연 휴식 카페", "avg_cost": 7000}],
            "extra_spots": [{"name": "남산트래킹", "avg_cost": 0}, {"name": "계곡 산책", "avg_cost": 0}]
        },
        "휴양": {
            "restaurants": [{"name": "보문호 레스토랑", "avg_cost": 20000}, {"name": "온천 한정식", "avg_cost": 18000}],
            "cafes": [{"name": "보문호 카페", "avg_cost": 10000}, {"name": "온천 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "호수 산책", "avg_cost": 0}, {"name": "온천 스파", "avg_cost": 15000}]
        },
        "액티비티": {
            "restaurants": [{"name": "자전거길 카페", "avg_cost": 10000}, {"name": "스포츠센터 식당", "avg_cost": 12000}],
            "cafes": [{"name": "트래킹 카페", "avg_cost": 8000}, {"name": "레저센터 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "자전거 투어", "avg_cost": 0}, {"name": "액티비티", "avg_cost": 0}]
        },
        "쇼핑": {
            "restaurants": [{"name": "황리단길 식당", "avg_cost": 14000}, {"name": "전통공예 카페", "avg_cost": 9000}],
            "cafes": [{"name": "황리단길 카페", "avg_cost": 9000}, {"name": "전통공예관 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "전통공예 쇼핑", "avg_cost": 0}, {"name": "기념품 거리", "avg_cost": 0}]
        }
    },
    "제주": {
        "문화": {
            "restaurants": [{"name": "제주 향토 식당", "avg_cost": 16000}, {"name": "민속촌 카페", "avg_cost": 10000}],
            "cafes": [{"name": "제주 전통 다방", "avg_cost": 8000}, {"name": "유물관 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "제주민속촌", "avg_cost": 8000}, {"name": "방주교회", "avg_cost": 0}]
        },
        "자연": {
            "restaurants": [{"name": "제주 향토 음식점", "avg_cost": 20000}, {"name": "제주 뷔페", "avg_cost": 25000}],
            "cafes": [{"name": "제주 카멜리아 힐 카페", "avg_cost": 11000}, {"name": "협재 해변 카페", "avg_cost": 10000}],
            "extra_spots": [{"name": "오설록 티뮤지엄", "avg_cost": 0}, {"name": "용머리해안 산책", "avg_cost": 0}]
        },
        "자연2": {
            "restaurants": [{"name": "폭포 정식", "avg_cost": 18000}, {"name": "해변 현지 식당", "avg_cost": 15000}],
            "cafes": [{"name": "경관 카페", "avg_cost": 10000}, {"name": "자연휴식 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "정방폭포 근처", "avg_cost": 0}, {"name": "해안경관", "avg_cost": 0}]
        },
        "식도락": {
            "restaurants": [{"name": "흑돼지 거리", "avg_cost": 22000}, {"name": "회센터", "avg_cost": 28000}],
            "cafes": [{"name": "올레시장 카페", "avg_cost": 7000}, {"name": "먹거리 센터 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "올레시장", "avg_cost": 0}, {"name": "해산물 직판장", "avg_cost": 0}]
        },
        "휴양": {
            "restaurants": [{"name": "중문 리조트 뷔페", "avg_cost": 28000}, {"name": "제주 해산물 전문점", "avg_cost": 22000}],
            "cafes": [{"name": "카페 드림타워", "avg_cost": 12000}, {"name": "해변가 브런치 카페", "avg_cost": 13000}],
            "extra_spots": [{"name": "중문 골프장 산책", "avg_cost": 0}, {"name": "카페 골목 투어", "avg_cost": 0}]
        },
        "휴양2": {
            "restaurants": [{"name": "스파 레스토랑", "avg_cost": 26000}, {"name": "휴양지 브런치", "avg_cost": 20000}],
            "cafes": [{"name": "명상 카페", "avg_cost": 11000}, {"name": "뷰 포인트 카페", "avg_cost": 12000}],
            "extra_spots": [{"name": "스파 & 웰니스", "avg_cost": 20000}, {"name": "명상 명소", "avg_cost": 0}]
        },
        "액티비티": {
            "restaurants": [{"name": "제주 액티비티 마켓", "avg_cost": 18000}, {"name": "해녀촌 식당", "avg_cost": 22000}],
            "cafes": [{"name": "서귀포 바다 카페", "avg_cost": 11000}, {"name": "산방산 카페", "avg_cost": 10000}],
            "extra_spots": [{"name": "스쿠버 다이빙 포인트", "avg_cost": 0}, {"name": "올레길 트레킹", "avg_cost": 0}]
        },
        "액티비티2": {
            "restaurants": [{"name": "레저센터 카페", "avg_cost": 13000}, {"name": "스포츠 식당", "avg_cost": 14000}],
            "cafes": [{"name": "활동 베이스 카페", "avg_cost": 9000}, {"name": "휴식 카페", "avg_cost": 10000}],
            "extra_spots": [{"name": "서핑 포인트", "avg_cost": 0}, {"name": "트레킹 코스", "avg_cost": 0}]
        },
        "쇼핑": {
            "restaurants": [{"name": "롯데 레스토랑", "avg_cost": 28000}, {"name": "신라호텔 식당", "avg_cost": 30000}],
            "cafes": [{"name": "고급 쇼핑 카페", "avg_cost": 12000}, {"name": "명품 카페", "avg_cost": 13000}],
            "extra_spots": [{"name": "롯데 아울렛", "avg_cost": 0}, {"name": "제주 면세점", "avg_cost": 0}]
        }
    },
    "강릉": {
        "문화": {
            "restaurants": [{"name": "오죽헌 정식", "avg_cost": 16000}, {"name": "선교장 카페", "avg_cost": 10000}],
            "cafes": [{"name": "강릉 전통 다방", "avg_cost": 8000}, {"name": "선재 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "오죽헌 투어", "avg_cost": 5000}, {"name": "선교장 관람", "avg_cost": 8000}]
        },
        "해변": {
            "restaurants": [{"name": "경포대 횟집", "avg_cost": 20000}, {"name": "해변 카페식당", "avg_cost": 14000}],
            "cafes": [{"name": "경포대 카페", "avg_cost": 9000}, {"name": "해변 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "경포대 산책", "avg_cost": 0}, {"name": "해변 휴식", "avg_cost": 0}]
        },
        "해변2": {
            "restaurants": [{"name": "정동진 카페식당", "avg_cost": 16000}, {"name": "해안 음식점", "avg_cost": 12000}],
            "cafes": [{"name": "정동진 카페", "avg_cost": 10000}, {"name": "동해 뷰 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "정동진 일출", "avg_cost": 0}, {"name": "해안드라이브", "avg_cost": 0}]
        },
        "식도락": {
            "restaurants": [{"name": "초당두부마을", "avg_cost": 12000}, {"name": "강릉 해산물", "avg_cost": 18000}],
            "cafes": [{"name": "두부 카페", "avg_cost": 7000}, {"name": "로컬 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "두부 직판장", "avg_cost": 0}, {"name": "음식 투어", "avg_cost": 0}]
        },
        "자연": {
            "restaurants": [{"name": "호수 전망식당", "avg_cost": 15000}, {"name": "산책길 카페", "avg_cost": 10000}],
            "cafes": [{"name": "경포호 카페", "avg_cost": 8000}, {"name": "자연 휴식 카페", "avg_cost": 9000}],
            "extra_spots": [{"name": "경포호 산책", "avg_cost": 0}, {"name": "숲길 트래킹", "avg_cost": 0}]
        },
        "휴양": {
            "restaurants": [{"name": "온천 정식", "avg_cost": 18000}, {"name": "휴양 식당", "avg_cost": 16000}],
            "cafes": [{"name": "온천 카페", "avg_cost": 10000}, {"name": "휴양 라운지", "avg_cost": 11000}],
            "extra_spots": [{"name": "강릉온천", "avg_cost": 0}, {"name": "스파", "avg_cost": 15000}]
        },
        "액티비티": {
            "restaurants": [{"name": "레포츠 센터 카페", "avg_cost": 12000}, {"name": "스포츠 식당", "avg_cost": 13000}],
            "cafes": [{"name": "활동 베이스 카페", "avg_cost": 9000}, {"name": "레저 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "서핑", "avg_cost": 0}, {"name": "래프팅", "avg_cost": 0}]
        },
        "쇼핑": {
            "restaurants": [{"name": "경포 쇼핑몰 레스토랑", "avg_cost": 16000}, {"name": "역 근처 식당", "avg_cost": 12000}],
            "cafes": [{"name": "쇼핑몰 카페", "avg_cost": 9000}, {"name": "상업지 카페", "avg_cost": 8000}],
            "extra_spots": [{"name": "경포 쇼핑몰", "avg_cost": 0}, {"name": "강릉역 상권", "avg_cost": 0}]
        }
    }
}


def get_attraction_points(attractions):
    points = []
    for attraction in attractions:
        coords = ATTRACTION_COORDINATES.get(attraction)
        if coords:
            points.append({"lat": coords[0], "lon": coords[1], "name": attraction})
    return points


def get_recommended_places(region, course_type):
    region_data = COURSE_RECOMMENDED_PLACES.get(region, {})
    if course_type and course_type in region_data:
        return region_data[course_type]
    return REGION_RECOMMENDED_PLACES.get(region, DEFAULT_PLACE_SET)


def get_route_view_state(points):
    if not points:
        return None
    avg_lat = sum(p["lat"] for p in points) / len(points)
    avg_lon = sum(p["lon"] for p in points) / len(points)
    return pdk.ViewState(latitude=avg_lat, longitude=avg_lon, zoom=11)


# 지역별 일일 현지 대중교통 평균 비용 (버스/지하철 하루 4~6회 이용 기준)
LOCAL_DAILY_TRANSPORT = {
    "서울":  7500,   # 지하철/버스 교통카드 1,500원 × 5회
    "부산":  6000,   # 도시철도/버스 1,500원 × 4회
    "제주":  5500,   # 버스 1,200원 × 4~5회 (시외버스 포함)
    "경주":  6000,   # 버스 1,400원 × 4~5회
    "강릉":  5000,   # 버스 1,250원 × 4회
    "대구":  5500,   # 도시철도/버스 1,350원 × 4회
    "전주":  5200,   # 버스 1,300원 × 4회
    "인천":  5500,   # 버스/지하철 1,350원 × 4회
    "대전":  5500,   # 버스 1,350원 × 4회
    "광주":  5200,   # 버스 1,300원 × 4회
    "수원":  5600,   # 버스/전철 1,400원 × 4회
    "창원":  5000,   # 버스 1,250원 × 4회
    "청주":  5200,   # 버스 1,300원 × 4회
    "포항":  5800,   # 버스 1,450원 × 4회
    "울산":  5600,   # 버스/도시철도 1,400원 × 4회
}

# 서울 기준 지역별 편도 도로 거리 (km) - 고속도로 경로 기준
INTERCITY_KM_FROM_SEOUL = {
    "서울":  0,
    "인천":  40,
    "수원":  45,
    "대전": 160,
    "청주": 130,
    "전주": 200,
    "광주": 330,
    "대구": 290,
    "부산": 420,
    "경주": 380,
    "울산": 385,
    "포항": 380,
    "창원": 440,
    "강릉": 185,
    "제주":   0,   # 선박·항공 이동 -> 현지에서만 렌터카
}
# 렌터카 비용 상수 (2025년 기준)
RENTAL_DAILY_RATE   = 80_000   # 중형차(아반떼·K3급) 1일 대여료, 보험 포함 (롯데·SK 평균)
FUEL_TOLL_PER_KM    = 187      # 유류비(142원/km) + 고속도로 통행료(45원/km)
LOCAL_KM_PER_DAY    = 80       # 현지 관광지 이동 평균 (km/일)
LOCAL_KM_JEJU       = 120      # 제주 현지 이동 (섬 전체 이동 고려)


def _estimate_intercity_km(region: str, departure_region: str) -> int:
    """두 지역 간 편도 도로 거리(km)를 추정한다."""
    if region == "제주":
        return 0   # 비행기·배로 이동, 렌터카는 현지 용도만
    dist_region    = INTERCITY_KM_FROM_SEOUL.get(region, 200)
    dist_departure = INTERCITY_KM_FROM_SEOUL.get(departure_region, 0)
    raw = abs(dist_region - dist_departure)
    # 동서 사선 이동(예: 부산↔광주) 보정 계수 1.15
    return int(raw * 1.15) if raw > 0 else 0


def build_course_details(course_name, region, course_type, transport_cost, duration=1, departure_region="서울"):
    places = get_recommended_places(region, course_type)

    # ── 대중교통 비용 ──────────────────────────────────────────
    local_daily = LOCAL_DAILY_TRANSPORT.get(region, 5500)
    local_total = local_daily * duration

    # ── 렌터카 비용 (실제 시세 기반) ───────────────────────────
    intercity_km   = _estimate_intercity_km(region, departure_region)
    local_km_day   = LOCAL_KM_JEJU if region == "제주" else LOCAL_KM_PER_DAY
    intercity_cost = intercity_km * 2 * FUEL_TOLL_PER_KM          # 왕복 유류비+통행료
    local_fuel     = local_km_day * FUEL_TOLL_PER_KM * duration    # 현지 이동 유류비
    rental_fee     = RENTAL_DAILY_RATE * duration                   # 대여료

    return {
        "route_points": None,
        "restaurants": places.get("restaurants", []),
        "cafes": places.get("cafes", []),
        "extra_spots": places.get("extra_spots", []),
        "transport_public": int(transport_cost + local_total),
        "transport_public_detail": {
            "intercity": int(transport_cost),
            "local_daily": local_daily,
            "local_total": int(local_total),
        },
        "transport_rentacar": int(intercity_cost + local_fuel + rental_fee),
        "transport_rentacar_detail": {
            "rental_fee": int(rental_fee),
            "intercity_cost": int(intercity_cost),
            "local_fuel": int(local_fuel),
            "intercity_km": intercity_km,
            "local_km_day": local_km_day,
        },
    }

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

if st.sidebar.button("추천 받기"):
    with st.spinner("AI가 여행 코스를 추천하고 있습니다. 잠시만 기다려주세요..."):
        # 추천 생성: 선택한 테마에 정확히 맞는 코스만 우선 제공
        available_courses = []
        if region in TRAVEL_DESTINATIONS:
            courses = TRAVEL_DESTINATIONS[region].get("courses", {})
            for course_type, course_info in courses.items():
                if course_type_matches_theme(course_type, theme_preference):
                    available_courses.append({
                        "type": course_type,
                        "name": course_info["name"],
                        "attractions": course_info["attractions"],
                        "duration": course_info["duration_days"],
                        "popular": course_info["popular"],
                        "base_cost": course_info["base_cost"]
                    })

        # 선택한 테마에 맞는 코스가 부족할 때만 안내 메시지를 표시
        if not available_courses:
            st.error(f"❌ 선택하신 '{region}' 지역에 '{theme_preference}' 테마에 맞는 코스가 없습니다. 다른 테마나 지역을 선택해주세요.")
            st.stop()

        if len(available_courses) < 2:
            st.warning(f"⚠️ 선택하신 '{theme_preference}' 테마에 일치하는 코스가 2개 미만입니다. 현재 가능한 코스만 표시됩니다.")

        # 선택한 테마에 맞는 코스가 부족하면 안내 메시지를 표시
        if not available_courses:
            st.error(f"❌ 선택하신 '{region}' 지역에 '{theme_preference}' 테마의 코스가 없습니다. 다른 테마나 지역을 선택해주세요.")
            st.stop()

        if len(available_courses) < 2:
            st.warning(f"⚠️ 현재 '{region}' 지역에서 '{theme_preference}' 테마에 딱 맞는 코스가 2개 미만입니다. 관련 추천 코스까지 함께 보여드립니다.")

        # ── Tavily 실시간 검색 보강 (실패 시 빈 컨텍스트로 폴백) ──────────
        existing_names  = [c["name"] for c in available_courses]
        tavily_raw      = search_travel_info(region, theme_preference, duration)
        tavily_clean    = deduplicate_results(tavily_raw, existing_names)
        tavily_context  = format_tavily_context(tavily_clean)

        # ── LLM 호출 ──────────────────────────────────────────────────────
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

        system_prompt = """당신은 한국 여행 전문가입니다. 사용자의 선호 테마에 가장 잘 맞는 여행 코스를 추천해주세요.

[중요] 반드시 지켜야 할 규칙:
1. 사용자의 선호 테마와 일치하는 코스를 우선 추천하세요
2. 정확히 일치하는 코스가 부족하면 관련된 다른 코스도 함께 고려하세요
3. 여행 기간에 맞춰 일정을 구성하세요
4. 최소 2개 이상의 추천 코스를 제시하세요

JSON 형식으로 다음과 같이 응답하세요:
{
  "recommendations": [
    {
      "rank": 1,
      "name": "코스명",
      "description": "3-4줄의 설명",
      "why_recommended": "왜 추천하는지 간단한 설명",
      "attractions": ["관광지1", "관광지2"],
      "estimated_duration": "예상 여행 일수"
    }
  ]
}"""

        tavily_section = ("\n" + tavily_context + "\n") if tavily_context else ""
        user_message = (
            f"지역: {region}\n"
            f"여행 기간: {duration}일\n"
            f"인원수: {num_people}명\n"
            f"선호 테마: {theme_preference}\n"
            "\n이용 가능한 코스들:\n"
            + json.dumps(available_courses, ensure_ascii=False, indent=2)
            + tavily_section
            + f"\n위 코스 중에서 '{theme_preference}' 테마에 정확히 맞는 코스들만 골라서 최대 5개까지 추천해주세요."
        )

        try:
            response = llm.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_message)
            ])

            response_text = response.content
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0]

            recommendations = json.loads(response_text).get("recommendations", [])
            for rec in recommendations:
                if "type" not in rec:
                    for course in available_courses:
                        if course["name"] == rec.get("name"):
                            rec["type"] = course["type"]
                            break
        except:
            # 폴백
            recommendations = [
                {
                    "rank": i+1,
                    "type": course["type"],
                    "name": course["name"],
                    "description": f"{course['name']}을(를) 통해 {region}의 매력을 느껴보세요.",
                    "why_recommended": f"당신의 선호도에 맞는 {theme_preference} 테마의 코스입니다.",
                    "attractions": course["attractions"],
                    "estimated_duration": f"{course['duration']}일"
                }
                for i, course in enumerate(available_courses[:3])
            ]

        # 비용 계산 (각 코스별)
        for rec in recommendations:
            # 교통비 계산: 출발 지역 기준
            transport_cost = abs(TRANSPORT_COSTS.get(region, 0) - TRANSPORT_COSTS.get(departure_region, 0)) * 2
            
            # 코스별 비용 데이터 찾기
            cost_data = {"transport": 0, "food": 20000, "attraction": 15000}  # 기본값
            if region in TRAVEL_DESTINATIONS:
                courses = TRAVEL_DESTINATIONS[region].get("courses", {})
                for course in courses.values():
                    if course["name"] == rec["name"]:
                        cost_data = course["base_cost"]
                        break
            
            food_per_day = cost_data.get("food", 20000)
            attraction_per_day = cost_data.get("attraction", 15000)
            daily_cost = food_per_day + attraction_per_day
            accommodation_cost = 60000 * (duration - 1) if duration > 1 else 0
            
            total_cost_per_person = transport_cost + (daily_cost * duration) + accommodation_cost
            total_cost = total_cost_per_person * num_people
            
            rec["cost_estimate"] = {
                "transport": transport_cost,
                "daily_food_attraction": daily_cost,
                "accommodation": accommodation_cost,
                "total_per_person": int(total_cost_per_person),
                "total_all_people": int(total_cost),
                "num_people": num_people,
                "duration": duration
            }

            course_type = rec.get("type")
            course_details = build_course_details(rec["name"], region, course_type, transport_cost, duration, departure_region)
            course_details["route_points"] = get_attraction_points(rec["attractions"])
            rec["course_details"] = course_details

        st.session_state.recommendations = recommendations

# 결과 표시
if st.session_state.recommendations:
    recommendations = st.session_state.recommendations

    st.header("🎯 추천 코스")

    for rec in recommendations:
        with st.container():
            st.subheader(f"🏆 {rec['rank']}순위: {rec['name']}")
            st.write(f"**설명:** {rec['description']}")
            st.write(f"**추천 이유:** {rec['why_recommended']}")
            st.write(f"**관광지:** {', '.join(rec['attractions'])}")
            st.write(f"**소요 기간:** {rec['estimated_duration']}")
            
            # 코스별 비용 표시
            cost = rec["cost_estimate"]
            st.write("**💰 예상 비용:**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("1인당 비용", f"₩{cost['total_per_person']:,}")
                st.metric("전체 비용", f"₩{cost['total_all_people']:,}")
            with col2:
                st.metric("교통비(왕복)", f"₩{cost['transport']:,}")
                st.metric("숙박비", f"₩{cost['accommodation']:,}")
            with st.expander(f"{rec['name']} 비용 세부사항"):
                st.write(f"식사 및 관광 ({cost['duration']}일): ₩{cost['daily_food_attraction'] * cost['duration']:,}")
            
            st.divider()

    # 코스 선택
    st.header("✅ 코스 선택")
    selected_course = st.selectbox("추천 코스 중 선택", [rec['name'] for rec in recommendations])

    if selected_course:
        selected_rec = next(rec for rec in recommendations if rec['name'] == selected_course)
        st.success(f"🎉 {selected_course}을(를) 선택하셨습니다!")

        course_details = selected_rec.get("course_details", {})
        route_points = course_details.get("route_points", [])

        st.subheader("🗺️ 선택 코스 경로")
        if route_points:
            st.write("코스에 포함된 주요 지점을 지도로 확인하세요.")
            path = [{"path": [[point["lon"], point["lat"]] for point in route_points]}]
            route_layer = pdk.Layer(
                "PathLayer",
                data=path,
                get_path="path",
                get_width=6,
                get_color=[252, 136, 3],
                width_min_pixels=4
            )
            view_state = get_route_view_state(route_points)
            st.pydeck_chart(
                pdk.Deck(
                    layers=[route_layer],
                    initial_view_state=view_state,
                    map_style=None,
                )
            )
            st.write("**루트 방문 순서:**")
            for i, point in enumerate(route_points, 1):
                st.write(f"{i}. {point['name']}")
        else:
            st.write("지도 경로 정보를 불러올 수 없습니다. 상세 정보를 확인해주세요.")

        st.subheader("🚗 교통비 비교")
        trip_days = selected_rec['cost_estimate']['duration']

        # 대중교통 세부
        pub_detail = course_details.get("transport_public_detail", {})
        intercity_pub = pub_detail.get("intercity", 0)
        local_daily   = pub_detail.get("local_daily", 0)
        local_total   = pub_detail.get("local_total", 0)
        st.write(f"- **대중교통 예상 합계: ₩{course_details.get('transport_public', 0):,}**")
        st.write(f"  - 시외 이동비(왕복): ₩{intercity_pub:,}")
        st.write(f"  - 현지 대중교통({trip_days}일 × ₩{local_daily:,}/일): ₩{local_total:,}")

        # 렌터카 세부
        rc_detail      = course_details.get("transport_rentacar_detail", {})
        rental_fee     = rc_detail.get("rental_fee", 0)
        intercity_cost = rc_detail.get("intercity_cost", 0)
        local_fuel     = rc_detail.get("local_fuel", 0)
        intercity_km   = rc_detail.get("intercity_km", 0)
        local_km_day   = rc_detail.get("local_km_day", 80)
        st.write(f"- **렌터카 예상 합계: ₩{course_details.get('transport_rentacar', 0):,}** (중형차 1대 기준)")
        st.write(f"  - 대여료(₩80,000/일 × {trip_days}일): ₩{rental_fee:,}")
        if intercity_km > 0:
            st.write(f"  - 시외 이동 유류비+통행료({intercity_km}km 왕복): ₩{intercity_cost:,}")
        st.write(f"  - 현지 이동 유류비({local_km_day}km/일 × {trip_days}일): ₩{local_fuel:,}")

        st.subheader("🍽️ 추천 식당")
        for restaurant in course_details.get("restaurants", []):
            st.write(f"- {restaurant['name']} (평균 ₩{restaurant['avg_cost']:,})")

        st.subheader("☕ 추천 카페")
        for cafe in course_details.get("cafes", []):
            st.write(f"- {cafe['name']} (평균 ₩{cafe['avg_cost']:,})")

        st.subheader("� 추천 추가 장소")
        for spot in course_details.get("extra_spots", []):
            st.write(f"- {spot['name']}")

        st.subheader("�📌 선택 코스 비용 요약")
        st.write(f"- 1인당 총 예상 비용: ₩{selected_rec['cost_estimate']['total_per_person']:,}")
        st.write(f"- 전체 예상 비용: ₩{selected_rec['cost_estimate']['total_all_people']:,}")

st.sidebar.markdown("---")
st.sidebar.markdown("**교통비 기준:** 선택한 출발 지역")
st.sidebar.markdown("**모델:** GPT-4o-mini")