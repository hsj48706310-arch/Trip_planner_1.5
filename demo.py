"""
여행 추천 에이전트 - 사용 예시 및 테스트
"""

import json
from advanced_features import (
    TravelRecommendationEngine,
    CostOptimizer,
    UserPreferenceAnalyzer,
    RecommendationFormatter
)
from travel_data import TRAVEL_DESTINATIONS


def demo_basic_flow():
    """기본 흐름 데모"""
    print("\n" + "="*70)
    print("🌍 국내 여행 추천 에이전트 - 기본 사용 예시")
    print("="*70 + "\n")
    
    # 시나리오: 4명이 부산으로 3일 간 먹거리 투어
    print("📋 사용 시나리오: 4명이 부산으로 3일 간 먹거리 투어\n")
    
    region = "부산"
    duration = 3
    num_people = 4
    theme = "먹거리"
    
    # 1. 사용자 프로필 생성
    print("[1단계] 사용자 프로필 생성")
    analyzer = UserPreferenceAnalyzer()
    profile = analyzer.create_profile({
        "region": region,
        "duration": duration,
        "num_people": num_people,
        "theme_preference": theme,
        "pace": "보통",
        "crowded_places": "적당함"
    })
    print(f"✓ 프로필 생성 완료: {json.dumps(profile, ensure_ascii=False, indent=2)}\n")
    
    # 2. 지역의 available courses 조회
    print("[2단계] 추천 코스 조회")
    if region in TRAVEL_DESTINATIONS:
        courses = TRAVEL_DESTINATIONS[region].get("courses", {})
        print(f"'{region}'에서 이용 가능한 코스:")
        for i, (course_type, course_info) in enumerate(courses.items(), 1):
            print(f"  {i}. {course_info['name']}")
    print()
    
    # 3. 비용 계산
    print("[3단계] 비용 계산")
    
    # 부산 먹거리 투어 비용
    busan_food_tour_cost = {
        "transport": 30000,  # 서울-부산 왕복 기준
        "food": 45000,       # 일별 식사
        "attraction": 10000  # 일별 관광
    }
    
    # 상세 비용 계산
    optimizer = CostOptimizer()
    cost_detail = optimizer.calculate_detailed_cost(
        region=region,
        duration=duration,
        num_people=num_people,
        base_cost=busan_food_tour_cost
    )
    
    # 포맷된 리포트
    formatter = RecommendationFormatter()
    cost_report = formatter.format_cost_report({
        "num_people": num_people,
        "duration": duration,
        "transport": cost_detail["breakdown"]["transport"],
        "daily_food_attraction": cost_detail["breakdown"]["daily_cost"],
        "accommodation": cost_detail["breakdown"]["accommodation"],
        "total_per_person": cost_detail["total"]["per_person"],
        "total_all_people": cost_detail["total"]["total"]
    })
    print(cost_report)
    
    # 4. 추천 시뮬레이션
    print("[4단계] 추천 결과 (시뮬레이션)\n")
    
    sample_recommendations = [
        {
            "rank": 1,
            "name": "부산 해산물 투어",
            "description": "자갈치 시장의 신선한 해산물을 맛보고, 지역 맛집을 돌아다니는 미식 여행입니다.",
            "why_recommended": "당신의 먹거리 테마 선호도와 완벽히 일치합니다.",
            "attractions": ["자갈치 시장", "맛집 골목", "감천문화마을", "BIFF광장"],
            "estimated_duration": "2-3일",
            "estimated_cost": cost_detail["total"]["per_person"]
        },
        {
            "rank": 2,
            "name": "부산 해변 여행",
            "description": "해운대와 광안리의 아름다운 해변에서 휴양하며 자연을 즐기는 여행입니다.",
            "why_recommended": "부산의 명소를 골고루 경험할 수 있습니다.",
            "attractions": ["해운대 해수욕장", "광안리", "태종대", "해운대 야경"],
            "estimated_duration": "2-3일",
            "estimated_cost": int(cost_detail["total"]["per_person"] * 0.95)
        },
        {
            "rank": 3,
            "name": "부산 문화유산 투어",
            "description": "해인사와 범어사 등 불교 문화유산을 둘러보며 영적인 경험을 하는 여행입니다.",
            "why_recommended": "문화를 깊이 있게 체험할 수 있는 기회입니다.",
            "attractions": ["해인사", "범어사", "보수동 책방골목", "감천문화마을"],
            "estimated_duration": "3일",
            "estimated_cost": int(cost_detail["total"]["per_person"] * 1.05)
        }
    ]
    
    # 추천 결과 출력
    for rec in sample_recommendations:
        print(formatter.format_as_text(rec))


def demo_cost_comparison():
    """비용 비교 데모"""
    print("\n" + "="*70)
    print("💰 여행지별 비용 비교")
    print("="*70 + "\n")
    
    regions_data = {
        "서울": {"transport": 0, "duration": 2},
        "부산": {"transport": 30000, "duration": 2},
        "제주": {"transport": 50000, "duration": 3},
        "강릉": {"transport": 25000, "duration": 2},
    }
    
    print(f"조건: 4명, 숙박 포함\n")
    print(f"{'지역':<10} {'교통비(왕복)':<15} {'숙박비':<10} {'식사+관광':<15} {'합계(1인)':<15} {'합계(4명)':<15}")
    print("-" * 85)
    
    optimizer = CostOptimizer()
    
    for region, data in regions_data.items():
        cost = optimizer.calculate_detailed_cost(
            region=region,
            duration=data["duration"],
            num_people=4,
            base_cost={"transport": data["transport"], "food": 25000, "attraction": 15000}
        )
        
        transport = cost["breakdown"]["transport"]
        accommodation = cost["breakdown"]["accommodation"]
        daily = cost["breakdown"]["daily_cost"] * data["duration"]
        per_person = cost["total"]["per_person"]
        total = cost["total"]["total"]
        
        print(f"{region:<10} ₩{transport:<14,} ₩{accommodation:<9,} ₩{daily:<14,} ₩{per_person:<14,} ₩{total:<14,}")


def demo_preference_analysis():
    """사용자 선호도 분석 데모"""
    print("\n" + "="*70)
    print("👤 사용자 선호도 분석")
    print("="*70 + "\n")
    
    analyzer = UserPreferenceAnalyzer()
    
    # 다양한 사용자 프로필
    profiles = [
        {
            "name": "액티브한 여행자",
            "responses": {
                "region": "제주",
                "duration": 3,
                "num_people": 2,
                "theme_preference": "액티비티",
                "pace": "빠름",
                "crowded_places": "상관없음"
            }
        },
        {
            "name": "느린 여행을 선호하는 사람",
            "responses": {
                "region": "강릉",
                "duration": 3,
                "num_people": 3,
                "theme_preference": "휴양",
                "pace": "느림",
                "crowded_places": "조용한"
            }
        },
        {
            "name": "문화 관광을 좋아하는 사람",
            "responses": {
                "region": "경주",
                "duration": 2,
                "num_people": 4,
                "theme_preference": "문화",
                "pace": "보통",
                "crowded_places": "보통"
            }
        }
    ]
    
    for profile_data in profiles:
        print(f"\n📌 {profile_data['name']}")
        print("-" * 50)
        profile = analyzer.create_profile(profile_data["responses"])
        print(f"지역: {profile['region']}")
        print(f"기간: {profile['duration']}일")
        print(f"인원: {profile['num_people']}명")
        print(f"테마: {profile['theme']}")
        print(f"페이스: {profile['preferences']['pace']}")
        print(f"붐비는 정도: {profile['preferences']['crowded_places']}")


def demo_engine_features():
    """엔진 기능 데모"""
    print("\n" + "="*70)
    print("🎯 여행 추천 엔진 기능")
    print("="*70 + "\n")
    
    engine = TravelRecommendationEngine()
    
    # 샘플 추천
    sample_recs = [
        {
            "rank": 1,
            "name": "부산 해산물 투어",
            "attractions": ["자갈치", "맛집", "감천", "BIFF"],
            "estimated_duration": "2일",
            "estimated_cost": 250000
        },
        {
            "rank": 2,
            "name": "부산 해변 여행",
            "attractions": ["해운대", "광안리"],
            "estimated_duration": "2일",
            "estimated_cost": 200000
        },
        {
            "rank": 3,
            "name": "부산 문화 투어",
            "attractions": ["해인사", "범어사", "책방골목"],
            "estimated_duration": "3일",
            "estimated_cost": 280000
        }
    ]
    
    print("[기능 1] 추천 필터링 - 예산 기준")
    print("예산: 250,000원 이하")
    filtered = engine.filter_by_budget(sample_recs, 250000, 4)
    for rec in filtered:
        print(f"  ✓ {rec['name']} (₩{rec['estimated_cost']:,})")
    
    print("\n[기능 2] 가장 저렴한 옵션 찾기")
    cheapest = engine.find_cheapest_option(sample_recs)
    print(f"  {cheapest['name']}: ₩{cheapest['estimated_cost']:,}")
    
    print("\n[기능 3] 최고 가성비 옵션 찾기")
    best_value = engine.find_best_value(sample_recs)
    attractions = len(best_value.get('attractions', []))
    cost = best_value.get('estimated_cost', 1)
    ratio = attractions / cost if cost > 0 else 0
    print(f"  {best_value['name']}")
    print(f"  관광지: {attractions}개, 비용: ₩{cost:,}, 가성비: {ratio:.4f}")
    
    print("\n[기능 4] 계획 저장")
    plan = {
        "selected_course": sample_recs[0],
        "cost_estimate": {"total_all_people": 1000000},
        "user_profile": {"region": "부산", "duration": 2, "num_people": 4}
    }
    saved_path = engine.save_plan(plan, "sample_travel_plan.json")
    print(f"  ✓ 계획 저장 완료: {saved_path}")
    
    print("\n[기능 5] 저장된 계획 로드")
    loaded_plan = engine.load_plan("sample_travel_plan.json")
    print(f"  ✓ 계획 로드 완료")
    print(f"    코스: {loaded_plan['selected_course']['name']}")
    print(f"    비용: ₩{loaded_plan['cost_estimate']['total_all_people']:,}")


if __name__ == "__main__":
    # 모든 데모 실행
    demo_basic_flow()
    demo_cost_comparison()
    demo_preference_analysis()
    demo_engine_features()
    
    print("\n" + "="*70)
    print("✅ 모든 데모 실행 완료!")
    print("="*70 + "\n")
