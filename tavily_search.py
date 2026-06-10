"""
Tavily 검색 기반 여행 정보 보강 모듈

역할:
1. search_travel_info  - 지역+테마 기반 최신 여행 정보 검색
2. deduplicate_results - 기존 코스명과 중복 제거 및 품질 필터링
3. format_tavily_context - LLM 프롬프트용 컨텍스트 텍스트 변환
"""

from typing import List, Dict


def search_travel_info(region: str, theme: str, duration: int) -> List[Dict]:
    """Tavily로 지역+테마 기반 최신 여행 정보 검색.

    Args:
        region: 여행 지역 (예: '부산')
        theme: 여행 테마 (예: '식도락')
        duration: 여행 기간(일)

    Returns:
        검색 결과 리스트. 실패 시 빈 리스트 반환 (폴백 보장).
    """
    try:
        from langchain_tavily import TavilySearch
        tool = TavilySearch(max_results=5)
        query = f"{region} {theme} 여행 추천 코스 {duration}일"
        results = tool.invoke({"query": query})
        return results if isinstance(results, list) else []
    except Exception:
        return []


def deduplicate_results(
    tavily_results: List[Dict],
    existing_names: List[str],
) -> List[Dict]:
    """Tavily 결과에서 기존 코스와 중복/저품질 항목을 제거.

    Args:
        tavily_results: search_travel_info() 반환값
        existing_names: 이미 내부 데이터에 있는 코스 이름 목록

    Returns:
        정제된 결과 리스트 (최대 3개).
    """
    seen = set(name.strip() for name in existing_names)
    filtered = []

    for item in tavily_results:
        title = item.get("title", "").strip()
        content = item.get("content", "").strip()

        # 내용이 너무 짧으면 제외
        if len(content) < 50:
            continue
        # 이미 내부 DB에 있는 코스명과 동일하면 제외
        if title in seen:
            continue

        seen.add(title)
        filtered.append({
            "title": title,
            "content": content[:300],   # LLM 토큰 절감용 요약
            "url": item.get("url", ""),
        })

    return filtered[:3]


def format_tavily_context(tavily_results: List[Dict]) -> str:
    """정제된 Tavily 결과를 LLM 프롬프트 삽입용 텍스트로 변환.

    Args:
        tavily_results: deduplicate_results() 반환값

    Returns:
        프롬프트에 삽입할 문자열. 결과가 없으면 빈 문자열.
    """
    if not tavily_results:
        return ""

    lines = ["[실시간 여행 참고 정보 (Tavily)]"]
    for i, r in enumerate(tavily_results, 1):
        lines.append(f"{i}. {r['title']}: {r['content']}")
    return "\n".join(lines)
