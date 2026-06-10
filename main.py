"""
한국 국내 여행 추천 LLM 에이전트
"""

import json
from typing import Any, TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from travel_data import TRAVEL_DESTINATIONS, THEMES, TRANSPORT_COSTS

load_dotenv()


class TravelState(TypedDict):
    """여행 추천 에이전트의 상태"""
    region: str
    duration: int
    num_people: int
    theme_preference: str
    recommendations: list
    selected_course: dict
    cost_estimate: dict
    conversation_history: list


def input_collection_node(state: TravelState) -> dict:
    """사용자 입력 수집 노드"""
    print("\n=== 국내 여행 추천 에이전트에 오신 것을 환영합니다! ===\n")
    
    # 지역 선택
    print("이용 가능한 지역:")
    regions = list(TRAVEL_DESTINATIONS.keys())
    for i, region in enumerate(regions, 1):
        print(f"  {i}. {region}")
    
    while True:
        try:
            region_idx = int(input(f"\n지역을 선택하세요 (1-{len(regions)}): ")) - 1
            if 0 <= region_idx < len(regions):
                region = regions[region_idx]
                break
            else:
                print("유효한 선택을 해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    # 여행 기간 선택
    while True:
        try:
            duration = int(input("\n여행 기간(일수)을 입력하세요 (1-7): "))
            if 1 <= duration <= 7:
                break
            else:
                print("1-7일 사이로 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    # 인원수 선택
    while True:
        try:
            num_people = int(input("\n여행 인원수를 입력하세요 (1-10): "))
            if 1 <= num_people <= 10:
                break
            else:
                print("1-10명 사이로 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    # 테마 선택
    print("\n선호하는 여행 테마:")
    themes = list(THEMES.keys())
    for i, theme in enumerate(themes, 1):
        print(f"  {i}. {theme}: {THEMES[theme]}")
    
    while True:
        try:
            theme_idx = int(input(f"\n테마를 선택하세요 (1-{len(themes)}): ")) - 1
            if 0 <= theme_idx < len(themes):
                theme_preference = themes[theme_idx]
                break
            else:
                print("유효한 선택을 해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    return {
        **state,
        "region": region,
        "duration": duration,
        "num_people": num_people,
        "theme_preference": theme_preference
    }


def recommendation_generation_node(state: TravelState) -> dict:
    """추천 생성 노드 - LLM을 사용하여 맞춤형 추천 생성"""
    
    region = state["region"]
    duration = state["duration"]
    num_people = state["num_people"]
    theme = state["theme_preference"]
    
    # 해당 지역의 코스 중 사용자 테마와 일치하는 것 찾기
    available_courses = []
    if region in TRAVEL_DESTINATIONS:
        courses = TRAVEL_DESTINATIONS[region].get("courses", {})
        for course_type, course_info in courses.items():
            # 테마가 일치하거나 또는 모든 코스 포함
            available_courses.append({
                "type": course_type,
                "name": course_info["name"],
                "attractions": course_info["attractions"],
                "duration": course_info["duration_days"],
                "popular": course_info["popular"],
                "base_cost": course_info["base_cost"]
            })
    
    # LLM에게 추천 생성 요청
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    system_prompt = """당신은 한국 여행 전문가입니다. 사용자의 선호도에 맞는 여행 코스를 추천해주세요.
사용 가능한 코스 정보를 바탕으로, 가장 적합한 코스들을 추천하되:
1. 사용자의 테마 선호도를 반영하세요
2. 여행 기간에 맞춰 일정을 구성하세요
3. 각 코스의 매력을 설명해주세요
4. 최대 3개까지의 추천 코스를 제시하세요

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
    
    user_message = f"""지역: {region}
여행 기간: {duration}일
인원수: {num_people}명
선호 테마: {theme}

이용 가능한 코스들:
{json.dumps(available_courses, ensure_ascii=False, indent=2)}

위 정보를 바탕으로 3개의 추천 코스를 제시해주세요."""
    
    try:
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message)
        ])
        
        # JSON 파싱 시도
        response_text = response.content
        try:
            # "```json" 또는 "```" 제거
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0]
            
            recommendations = json.loads(response_text).get("recommendations", [])
        except (json.JSONDecodeError, IndexError):
            # JSON 파싱 실패시 폴백
            recommendations = [
                {
                    "rank": i+1,
                    "name": course["name"],
                    "description": f"{course['name']}을(를) 통해 {region}의 매력을 느껴보세요.",
                    "why_recommended": f"당신의 선호도에 맞는 {theme} 테마의 코스입니다.",
                    "attractions": course["attractions"],
                    "estimated_duration": f"{course['duration']}일"
                }
                for i, course in enumerate(available_courses[:3])
            ]
        
        state["recommendations"] = recommendations
        
    except Exception as e:
        print(f"LLM 호출 중 오류: {e}")
        # 폴백: 직접 추천
        state["recommendations"] = [
            {
                "rank": i+1,
                "name": course["name"],
                "description": f"{course['name']}을(를) 통해 {region}의 매력을 경험해보세요.",
                "why_recommended": f"당신의 선호도를 고려한 추천 코스입니다.",
                "attractions": course["attractions"],
                "estimated_duration": f"{course['duration']}일"
            }
            for i, course in enumerate(available_courses[:3])
        ]
    
    return state


def display_recommendations_node(state: TravelState) -> dict:
    """추천 사항 표시 노드"""
    print("\n=== 추천 코스 ===\n")
    
    for rec in state["recommendations"]:
        print(f"[{rec['rank']}순위] {rec['name']}")
        print(f"설명: {rec['description']}")
        print(f"추천 이유: {rec['why_recommended']}")
        print(f"관광지: {', '.join(rec['attractions'])}")
        print(f"소요 기간: {rec['estimated_duration']}")
        print("-" * 50)
    
    return state


def cost_calculation_node(state: TravelState) -> dict:
    """비용 계산 노드"""
    
    region = state["region"]
    duration = state["duration"]
    num_people = state["num_people"]
    
    # 기본 교통비 (왕복)
    transport_cost = TRANSPORT_COSTS.get(region, 0) * 2
    
    # 추천 코스 중 첫 번째 선택 (아직 선택 전)
    if state["recommendations"]:
        rec = state["recommendations"][0]
        
        # 코스 정보에서 비용 추출
        course_type = rec["name"].split()[0]
        
        # 지역에서 해당 코스 찾기
        course_info = None
        if region in TRAVEL_DESTINATIONS:
            courses = TRAVEL_DESTINATIONS[region].get("courses", {})
            for course in courses.values():
                if course["name"] == rec["name"]:
                    cost_data = course["base_cost"]
                    break
        else:
            cost_data = {"transport": 0, "food": 20000, "attraction": 15000}
        
        # 일별 비용 계산
        food_per_day = cost_data.get("food", 20000)
        attraction_per_day = cost_data.get("attraction", 15000)
        
        daily_cost = food_per_day + attraction_per_day
        accommodation_cost = 60000 * (duration - 1) if duration > 1 else 0  # 숙박비
        
        # 총 비용 계산
        total_cost_per_person = (
            transport_cost + 
            (daily_cost * duration) + 
            accommodation_cost
        )
        
        total_cost = total_cost_per_person * num_people
        
        cost_estimate = {
            "transport": transport_cost,
            "daily_food_attraction": daily_cost,
            "accommodation": accommodation_cost,
            "total_per_person": int(total_cost_per_person),
            "total_all_people": int(total_cost),
            "num_people": num_people,
            "duration": duration
        }
    else:
        cost_estimate = {
            "transport": transport_cost,
            "daily_food_attraction": 35000,
            "accommodation": 60000 * (duration - 1) if duration > 1 else 0,
            "total_per_person": 0,
            "total_all_people": 0,
            "num_people": num_people,
            "duration": duration
        }
    
    state["cost_estimate"] = cost_estimate
    return state


def display_cost_estimate_node(state: TravelState) -> dict:
    """비용 추정치 표시 노드"""
    cost = state["cost_estimate"]
    
    print("\n=== 여행 비용 추정 ===\n")
    print(f"여행 인원: {cost['num_people']}명")
    print(f"여행 기간: {cost['duration']}일")
    print()
    
    print("비용 세부사항 (1인 기준):")
    print(f"  - 교통비(왕복): ₩{cost['transport']:,}")
    print(f"  - 식사 및 관광 ({cost['duration']}일): ₩{cost['daily_food_attraction'] * cost['duration']:,}")
    print(f"  - 숙박비({cost['duration']-1}박): ₩{cost['accommodation']:,}")
    print(f"  - 소계: ₩{cost['total_per_person']:,}")
    print(f"\n전체 여행 비용: ₩{cost['total_all_people']:,}")
    
    return state


def course_selection_node(state: TravelState) -> dict:
    """코스 선택 노드"""
    print("\n=== 전국 여행 코스 선택 ===\n")
    
    recommendations = state["recommendations"]
    region = state["region"]
    
    print("위의 추천 코스 중에서 선택하시겠습니까?")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec['name']}")
    
    print(f"  {len(recommendations) + 1}. 다른 코스 보기")
    print(f"  {len(recommendations) + 2}. 종료")
    
    while True:
        try:
            choice = int(input(f"\n선택하세요 (1-{len(recommendations) + 2}): "))
            if 1 <= choice <= len(recommendations):
                selected = recommendations[choice - 1]
                state["selected_course"] = selected
                
                print(f"\n{selected['name']}을(를) 선택하셨습니다!")
                print(f"비용: ₩{state['cost_estimate']['total_per_person']:,} (1인)")
                print(f"전체: ₩{state['cost_estimate']['total_all_people']:,}")
                
                break
            elif choice == len(recommendations) + 1:
                # 다른 코스 보기
                if region in TRAVEL_DESTINATIONS:
                    other_courses = TRAVEL_DESTINATIONS[region].get("courses", {})
                    print("\n이용 가능한 다른 코스들:")
                    for i, (course_type, course_info) in enumerate(other_courses.items(), 1):
                        print(f"  {i}. {course_info['name']}")
                break
            elif choice == len(recommendations) + 2:
                print("여행 계획을 종료합니다.")
                break
            else:
                print("유효한 선택을 해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    return state


def final_report_node(state: TravelState) -> dict:
    """최종 보고서 생성 노드"""
    print("\n=== 여행 계획 최종 요약 ===\n")
    
    print(f"지역: {state['region']}")
    print(f"여행 기간: {state['duration']}일")
    print(f"여행 인원: {state['num_people']}명")
    print(f"선호 테마: {state['theme_preference']}\n")
    
    if state.get("selected_course"):
        course = state["selected_course"]
        print(f"선택한 코스: {course['name']}")
        print(f"포함 관광지: {', '.join(course['attractions'])}")
        
        cost = state["cost_estimate"]
        print(f"\n예상 총 비용: ₩{cost['total_all_people']:,}")
        print(f"  (1인당: ₩{cost['total_per_person']:,})")
        print()
        print("즐거운 여행되세요! 🌍")
    else:
        print("아직 코스를 선택하지 않으셨습니다.")
        print("다시 시도해주세요.")
    
    return state


def create_travel_agent():
    """여행 추천 에이전트 생성"""
    
    workflow = StateGraph(TravelState)
    
    # 노드 추가
    workflow.add_node("input_collection", input_collection_node)
    workflow.add_node("recommendation_generation", recommendation_generation_node)
    workflow.add_node("display_recommendations", display_recommendations_node)
    workflow.add_node("cost_calculation", cost_calculation_node)
    workflow.add_node("display_cost_estimate", display_cost_estimate_node)
    workflow.add_node("course_selection", course_selection_node)
    workflow.add_node("final_report", final_report_node)
    
    # 엣지 추가
    workflow.add_edge(START, "input_collection")
    workflow.add_edge("input_collection", "recommendation_generation")
    workflow.add_edge("recommendation_generation", "display_recommendations")
    workflow.add_edge("display_recommendations", "cost_calculation")
    workflow.add_edge("cost_calculation", "display_cost_estimate")
    workflow.add_edge("display_cost_estimate", "course_selection")
    workflow.add_edge("course_selection", "final_report")
    workflow.add_edge("final_report", END)
    
    return workflow.compile()


def main():
    """메인 함수"""
    print("국내 여행 추천 LLM 에이전트를 시작합니다...\n")
    
    # 초기 상태
    initial_state: TravelState = {
        "region": "",
        "duration": 0,
        "num_people": 0,
        "theme_preference": "",
        "recommendations": [],
        "selected_course": {},
        "cost_estimate": {},
        "conversation_history": []
    }
    
    # 에이전트 생성 및 실행
    agent = create_travel_agent()
    result = agent.invoke(initial_state)
    
    print("\n=== 에이전트 실행 완료 ===\n")


if __name__ == "__main__":
    main()
