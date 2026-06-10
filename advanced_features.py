"""
여행 추천 에이전트 - 고급 기능 (추천 필터링, 비교, 저장)
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from travel_data import TRAVEL_DESTINATIONS, PEOPLE_DISCOUNT_RATE


class TravelRecommendationEngine:
    """여행 추천 엔진"""
    
    def __init__(self):
        self.recommendations: List[Dict] = []
        self.saved_plans: List[Dict] = []
    
    def filter_by_budget(self, recommendations: List[Dict], max_budget: int, num_people: int) -> List[Dict]:
        """예산에 따라 추천 필터링"""
        filtered = []
        
        for rec in recommendations:
            # 비용 계산 (단순화)
            estimated_cost = rec.get("estimated_cost", 0)
            if estimated_cost <= max_budget:
                filtered.append(rec)
        
        return filtered
    
    def filter_by_duration(self, recommendations: List[Dict], duration: int) -> List[Dict]:
        """여행 기간에 맞는 추천 필터링"""
        filtered = []
        
        for rec in recommendations:
            rec_duration = int(rec.get("estimated_duration", "0").split("일")[0])
            if rec_duration <= duration:
                filtered.append(rec)
        
        return filtered
    
    def rank_by_popularity(self, recommendations: List[Dict]) -> List[Dict]:
        """인기순으로 정렬"""
        return sorted(recommendations, key=lambda x: x.get("rank", float('inf')))
    
    def rank_by_theme(self, recommendations: List[Dict], theme: str) -> List[Dict]:
        """테마별로 정렬"""
        # 이상적으로는 LLM이 매칭도를 반환해야 함
        return sorted(recommendations, key=lambda x: (x.get("rank", float('inf'))))
    
    def compare_recommendations(self, rec1: Dict, rec2: Dict) -> Dict:
        """두 추천안 비교"""
        return {
            "comparison": {
                "rec1": {
                    "name": rec1.get("name"),
                    "attractions_count": len(rec1.get("attractions", [])),
                    "duration": rec1.get("estimated_duration")
                },
                "rec2": {
                    "name": rec2.get("name"),
                    "attractions_count": len(rec2.get("attractions", [])),
                    "duration": rec2.get("estimated_duration")
                }
            }
        }
    
    def save_plan(self, plan: Dict, filename: str = None) -> str:
        """여행 계획 저장"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"travel_plan_{timestamp}.json"
        
        filepath = Path(filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        
        return str(filepath)
    
    def load_plan(self, filename: str) -> Dict:
        """저장된 여행 계획 로드"""
        filepath = Path(filename)
        
        if not filepath.exists():
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filename}")
        
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)


class CostOptimizer:
    """비용 최적화 엔진"""
    
    @staticmethod
    def calculate_detailed_cost(region: str, duration: int, num_people: int, 
                               base_cost: Dict) -> Dict:
        """상세 비용 계산"""
        
        # 교통비 (왕복)
        transport_cost = base_cost.get("transport", 0) * 2
        
        # 일별 비용
        daily_cost = base_cost.get("food", 20000) + base_cost.get("attraction", 15000)
        
        # 숙박비
        accommodation_cost = 60000 * (duration - 1) if duration > 1 else 0
        
        # 소계 (할인 전)
        subtotal = transport_cost + (daily_cost * duration) + accommodation_cost
        
        # 할인율 적용
        discount_rate = PEOPLE_DISCOUNT_RATE.get(num_people, 0.8)
        
        # 최종 비용
        total_per_person = subtotal * discount_rate
        total_all_people = total_per_person * num_people
        
        return {
            "breakdown": {
                "transport": transport_cost,
                "daily_cost": daily_cost,
                "daily_cost_total": daily_cost * duration,
                "accommodation": accommodation_cost,
                "subtotal_per_person": subtotal,
            },
            "discount": {
                "rate": discount_rate,
                "amount_per_person": subtotal - total_per_person,
                "amount_total": (subtotal - total_per_person) * num_people
            },
            "total": {
                "per_person": int(total_per_person),
                "total": int(total_all_people)
            },
            "details": {
                "num_people": num_people,
                "duration": duration,
                "discount_percentage": int((1 - discount_rate) * 100)
            }
        }
    
    @staticmethod
    def find_cheapest_option(recommendations: List[Dict]) -> Dict:
        """가장 저렴한 옵션 찾기"""
        if not recommendations:
            return {}
        
        return min(recommendations, key=lambda x: x.get("estimated_cost", float('inf')))
    
    @staticmethod
    def find_best_value(recommendations: List[Dict]) -> Dict:
        """최고의 가성비 옵션 찾기"""
        if not recommendations:
            return {}
        
        # 가성비 = 관광지 수 / 비용
        best = None
        best_ratio = 0
        
        for rec in recommendations:
            attractions_count = len(rec.get("attractions", []))
            cost = rec.get("estimated_cost", float('inf'))
            
            if cost > 0:
                ratio = attractions_count / cost
                if ratio > best_ratio:
                    best_ratio = ratio
                    best = rec
        
        return best or {}


class UserPreferenceAnalyzer:
    """사용자 선호도 분석기"""
    
    def __init__(self):
        self.user_profile = {}
    
    def create_profile(self, responses: Dict) -> Dict:
        """사용자 프로필 생성"""
        profile = {
            "created_at": datetime.now().isoformat(),
            "region": responses.get("region"),
            "duration": responses.get("duration"),
            "num_people": responses.get("num_people"),
            "theme": responses.get("theme_preference"),
            "preferences": {
                "crowded_places": responses.get("crowded_places", "중간"),
                "budget_level": responses.get("budget_level", "보통"),
                "pace": responses.get("pace", "보통"),  # 빠름/보통/느림
                "transportation": responses.get("transportation", "대중교통"),  # 차량/대중교통
            }
        }
        
        self.user_profile = profile
        return profile
    
    def generate_recommendations_based_on_profile(self, recommendations: List[Dict]) -> List[Dict]:
        """프로필에 기반한 추천 순위 조정"""
        if not self.user_profile:
            return recommendations
        
        # 예시: 느린 속도를 선호하면 관광지 수가 적은 코스 상향
        pace = self.user_profile.get("preferences", {}).get("pace", "보통")
        crowded = self.user_profile.get("preferences", {}).get("crowded_places", "중간")
        
        scored = []
        for rec in recommendations:
            score = rec.get("rank", 0)
            
            # 페이스 조정
            attractions_count = len(rec.get("attractions", []))
            if pace == "느림" and attractions_count <= 3:
                score -= 1  # 높은 순위로 (낮은 숫자 = 높은 순위)
            elif pace == "빠름" and attractions_count >= 5:
                score -= 1
            
            scored.append({**rec, "adjusted_rank": score})
        
        return sorted(scored, key=lambda x: x.get("adjusted_rank", float('inf')))


class RecommendationFormatter:
    """추천 결과 포맷팅"""
    
    @staticmethod
    def format_as_text(recommendation: Dict) -> str:
        """텍스트 포맷"""
        text = f"""
{'='*60}
[{recommendation.get('rank', '?')}순위] {recommendation.get('name', 'N/A')}
{'='*60}

📝 설명:
{recommendation.get('description', 'N/A')}

✨ 추천 이유:
{recommendation.get('why_recommended', 'N/A')}

📍 포함 관광지:
{', '.join(recommendation.get('attractions', []))}

⏱️ 소요 기간: {recommendation.get('estimated_duration', 'N/A')}
{'='*60}
"""
        return text
    
    @staticmethod
    def format_as_html(recommendation: Dict) -> str:
        """HTML 포맷"""
        html = f"""
<div style="border: 1px solid #ddd; padding: 20px; margin: 10px 0; border-radius: 8px;">
    <h3>[{recommendation.get('rank', '?')}순위] {recommendation.get('name', 'N/A')}</h3>
    
    <h4>📝 설명</h4>
    <p>{recommendation.get('description', 'N/A')}</p>
    
    <h4>✨ 추천 이유</h4>
    <p>{recommendation.get('why_recommended', 'N/A')}</p>
    
    <h4>📍 포함 관광지</h4>
    <ul>
"""
        for attraction in recommendation.get('attractions', []):
            html += f"        <li>{attraction}</li>\n"
        
        html += f"""
    </ul>
    
    <h4>⏱️ 소요 기간</h4>
    <p>{recommendation.get('estimated_duration', 'N/A')}</p>
</div>
"""
        return html
    
    @staticmethod
    def format_cost_report(cost_estimate: Dict) -> str:
        """비용 리포트 포맷"""
        report = f"""
{'='*60}
💰 여행 비용 상세 보고서
{'='*60}

📊 개요:
  - 여행 인원: {cost_estimate.get('num_people', 'N/A')}명
  - 여행 기간: {cost_estimate.get('duration', 'N/A')}일
  - 단체 할인: {cost_estimate.get('discount_rate', 0)}%

💵 비용 세부사항 (1인 기준):
  - 교통비 (왕복): ₩{cost_estimate.get('transport', 0):,}
  - 식사 및 관광: ₩{cost_estimate.get('daily_food_attraction', 0) * cost_estimate.get('duration', 1):,}
  - 숙박비: ₩{cost_estimate.get('accommodation', 0):,}
  - 소계: ₩{cost_estimate.get('total_per_person', 0):,}

💳 최종 비용:
  - 1인당: ₩{cost_estimate.get('total_per_person', 0):,}
  - 전체 ({cost_estimate.get('num_people', 'N/A')}명): ₩{cost_estimate.get('total_all_people', 0):,}

{'='*60}
"""
        return report


# 사용 예시
if __name__ == "__main__":
    # 비용 계산 예시
    optimizer = CostOptimizer()
    cost = optimizer.calculate_detailed_cost(
        region="부산",
        duration=3,
        num_people=4,
        base_cost={"transport": 30000, "food": 25000, "attraction": 15000}
    )
    
    formatter = RecommendationFormatter()
    print(formatter.format_cost_report(cost["total"]))
    
    # 사용자 프로필 예시
    analyzer = UserPreferenceAnalyzer()
    profile = analyzer.create_profile({
        "region": "제주",
        "duration": 3,
        "num_people": 2,
        "theme_preference": "자연",
        "pace": "느림",
        "crowded_places": "조용한"
    })
    print(f"프로필 생성 완료: {profile}")
