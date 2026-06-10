# 🚀 국내 여행 추천 LLM 에이전트 - 사용 가이드

## 📦 프로젝트 구조

```
miniproject1.5/
├── main.py                 # 메인 에이전트 (LangGraph 기반)
├── travel_data.py          # 여행지 데이터 및 가격 정보
├── advanced_features.py    # 고급 기능 (필터링, 비용 계산, 포맷팅)
├── demo.py                 # 데모 및 테스트 코드
├── 1_prolog.ipynb          # Jupyter 노트북 (설계 및 학습 자료)
├── pyproject.toml          # 프로젝트 설정
├── README.md               # 프로젝트 개요
├── USAGE.md                # 이 파일
└── .env                    # 환경 변수 (사용자가 작성)
```

---

## 🔧 사전 준비

### 1. OpenAI API 키 설정

```bash
# .env 파일 생성
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

또는 텍스트 에디터로 `.env` 파일 생성 후:

```
OPENAI_API_KEY=your_openai_api_key
```

### 2. 패키지 설치

```bash
# uv를 사용하는 경우 (권장)
uv sync

# 또는 pip를 사용하는 경우
pip install -r requirements.txt
```

---

## ▶️ 실행 방법

### 옵션 1: 메인 에이전트 실행 (대화형)

```bash
python main.py
```

**흐름:**
1. 지역 선택 (7개 중)
2. 여행 기간 입력 (1-7일)
3. 인원수 입력 (1-10명)
4. 테마 선택 (10개 중)
5. LLM 기반 추천 결과 조회
6. 비용 계산 확인
7. 최종 코스 선택

**예시 입력:**
```
지역을 선택하세요 (1-7): 2
여행 기간(일수)을 입력하세요 (1-7): 3
여행 인원수를 입력하세요 (1-10): 4
테마를 선택하세요 (1-10): 2
```

### 옵션 2: 데모 코드 실행

```bash
python demo.py
```

**포함 내용:**
- 기본 사용 예시 (부산 4명 3일)
- 여행지별 비용 비교
- 사용자 선호도 분석
- 엔진 기능 시연

### 옵션 3: Jupyter 노트북

```bash
jupyter notebook 1_prolog.ipynb
```

에이전트 설계와 구현 과정을 학습할 수 있습니다.

---

## 📊 기능별 상세 설명

### 1. 입력 수집 시스템

```python
# main.py의 input_collection_node
- 지역 선택: TRAVEL_DESTINATIONS의 모든 키
- 기간 설정: 1-7일
- 인원수: 1-10명
- 테마: THEMES의 10가지 이상 테마
```

### 2. LLM 추천 생성

```python
# GPT-4o-mini 사용
- 입력: 지역, 기간, 인원, 테마 + 이용 가능한 코스 정보
- 출력: JSON 형식 추천 (최대 3개)
- 특징: 자연스러운 설명 + 추천 이유 포함
```

**응답 형식:**
```json
{
  "recommendations": [
    {
      "rank": 1,
      "name": "코스명",
      "description": "상세 설명",
      "why_recommended": "추천 이유",
      "attractions": ["관광지1", "관광지2"],
      "estimated_duration": "2일"
    }
  ]
}
```

### 3. 정확한 비용 계산

**계산 공식:**
```
기본 비용 = 교통비(왕복) + (일일비용 × 기간) + 숙박비
할인 적용 = 기본 비용 × PEOPLE_DISCOUNT_RATE[인원수]
총 비용 = 할인 적용 비용 × 인원수
```

**할인 규정:**
| 인원 | 할인율 |
|-----|--------|
| 1명 | 0% |
| 2명 | 5% |
| 3명 | 10% |
| 4명 | 15% |
| 5명+ | 20% |

**비용 구성:**
- **교통비**: 지역별 기차/버스 왕복요금
- **식사비**: 일일 평균 25,000-45,000원
- **관광료**: 일일 평균 5,000-60,000원
- **숙박비**: 1박에 60,000원 (기본값)

### 4. 고급 기능 (advanced_features.py)

#### TravelRecommendationEngine
```python
engine = TravelRecommendationEngine()

# 예산에 따라 필터링
filtered = engine.filter_by_budget(recommendations, max_budget=300000, num_people=4)

# 기간에 따라 필터링
filtered = engine.filter_by_duration(recommendations, duration=2)

# 계획 저장
engine.save_plan(plan, "my_travel_plan.json")

# 저장된 계획 로드
loaded = engine.load_plan("my_travel_plan.json")
```

#### CostOptimizer
```python
optimizer = CostOptimizer()

# 상세 비용 계산
cost = optimizer.calculate_detailed_cost(
    region="부산",
    duration=3,
    num_people=4,
    base_cost={"transport": 30000, "food": 25000, "attraction": 15000}
)

# 가장 저렴한 옵션
cheapest = optimizer.find_cheapest_option(recommendations)

# 최고 가성비 옵션
best_value = optimizer.find_best_value(recommendations)
```

#### UserPreferenceAnalyzer
```python
analyzer = UserPreferenceAnalyzer()

# 사용자 프로필 생성
profile = analyzer.create_profile({
    "region": "제주",
    "duration": 3,
    "num_people": 2,
    "theme_preference": "자연",
    "pace": "느림",
    "crowded_places": "조용한"
})

# 프로필 기반 추천 조정
adjusted = analyzer.generate_recommendations_based_on_profile(recommendations)
```

#### RecommendationFormatter
```python
formatter = RecommendationFormatter()

# 텍스트 포맷
text = formatter.format_as_text(recommendation)

# HTML 포맷
html = formatter.format_as_html(recommendation)

# 비용 리포트
report = formatter.format_cost_report(cost_estimate)
```

---

## 🌍 지역별 코스 예시

### 서울
- **문화**: 경복궁, 북촌 한옥마을, 청계천
- **쇼핑**: 명동, 강남, 동대문
- **야경**: 남산타워, 한강공원, 서울 스카이

### 부산
- **해변**: 해운대, 광안리, 태종대
- **먹거리**: 자갈치 시장, 맛집 골목, 감천문화마을
- **문화**: 해인사, 범어사, 보수동 책방골목

### 제주
- **자연**: 한라산, 만장굴, 성산일출봉
- **휴양**: 중문 관광단지, 신화월드, 해변 카페
- **액티비티**: 해녀체험, 스쿠버다이빙, 트래킹

---

## 💡 활용 팁

### 팁 1: 비용 절감
```
더 많은 인원이 참여할수록 할인율이 높아집니다!
1인 vs 5인+: 최대 20%의 차이
```

### 팁 2: 여러 옵션 비교
```bash
# 같은 조건으로 여러 번 실행하여 비교
python main.py  # 1회
python main.py  # 2회
```

### 팁 3: 데이터 커스터마이징
`travel_data.py`의 `TRAVEL_DESTINATIONS`를 수정하여 새로운 지역/코스 추가 가능

### 팁 4: API 요금 절감
- 테스트: `gpt-4o-mini` 사용 (저비용)
- 프로덕션: 필요시 `gpt-4` 변경

---

## 🐛 트러블슈팅

### 1. "OPENAI_API_KEY가 없습니다" 에러

```bash
# .env 파일 재확인
cat .env

# 올바른 형식인지 확인
# OPENAI_API_KEY=sk-... (공백 없음)
```

### 2. "모듈을 찾을 수 없습니다" 에러

```bash
# 필요한 패키지 재설치
uv sync

# 또는
pip install langchain langchain-openai langgraph python-dotenv
```

### 3. LLM 응답이 JSON이 아닌 경우

```
자동으로 폴백 메커니즘이 작동하여 기본 추천을 제공합니다.
이를 해결하려면 프롬프트를 조정하거나 다시 시도하세요.
```

### 4. 비용 계산이 정확하지 않은 경우

```python
# travel_data.py에서 가격 조정
TRANSPORT_COSTS = {
    "부산": 30000,  # 원하는 값으로 수정
}
```

---

## 📈 성능 최적화

### 1. API 호출 최소화
```python
# 같은 검색 결과를 캐시
recommendations_cache = {}
```

### 2. 응답 시간 개선
```python
# temperature 조정 (0 = 일관성, 1 = 다양성)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
```

### 3. 비용 절감
```
기본 모델: gpt-4o-mini (저비용)
프롬프트 크기: 최소화 (JSON 구조로)
```

---

## 🔄 워크플로우 커스터마이징

### 단계 추가
```python
def my_custom_node(state: TravelState) -> dict:
    # 커스텀 로직
    state["custom_field"] = "value"
    return state

# main.py에 추가
workflow.add_node("my_custom_node", my_custom_node)
workflow.add_edge("some_node", "my_custom_node")
```

### 조건부 라우팅
```python
def router(state: TravelState) -> str:
    if state["duration"] <= 1:
        return "fast_travel"
    else:
        return "relaxed_travel"

workflow.add_conditional_edges(
    "recommendation_generation",
    router,
    {
        "fast_travel": "display_recommendations",
        "relaxed_travel": "display_recommendations"
    }
)
```

---

## 📚 참고 자료

- [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
- [OpenAI API 문서](https://platform.openai.com/docs/)
- [Python 타입 힌팅](https://docs.python.org/3/library/typing.html)

---

## 📞 지원

문제가 발생하거나 개선 사항이 있으면 이슈를 등록해주세요!

---

**마지막 업데이트**: 2026년 4월 10일
**버전**: 1.0.0
