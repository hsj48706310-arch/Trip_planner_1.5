#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'c:/miniproject1.5')

from travel_data import TRAVEL_DESTINATIONS

# 매칭 규칙 (app.py에서)
THEME_MATCHING_CATEGORIES = {
    "문화": ["문화", "문화2", "역사", "불교"],
    "식도락": ["식도락", "식도락2", "먹거리", "마실거리"],
    "자연": ["자연", "자연2", "바다", "해변", "산", "숲", "계곡"],
    "쇼핑": ["쇼핑", "쇼핑2", "기념품"],
    "휴양": ["휴양", "휴양2", "힐링", "리조트"],
    "액티비티": ["액티비티", "액티비티2", "체험", "스포츠"]
}

def course_type_matches_theme(course_type, theme_preference):
    course_type = course_type.strip()
    aliases = THEME_MATCHING_CATEGORIES.get(theme_preference, [theme_preference])
    
    if course_type == theme_preference:
        return True
    if course_type.startswith(theme_preference):
        return True
    if course_type in aliases:
        return True
    return any(alias in course_type for alias in aliases)

# 각 지역별 현황 분석
region_order = ["서울", "부산", "경주", "제주", "강릉", "대구", "전주", "인천", "대전", "광주", "수원", "창원", "청주", "포항", "울산"]

print("=" * 80)
print("각 지역별 테마별 코스 현황")
print("=" * 80)

gap_summary = []

for region in region_order:
    courses = TRAVEL_DESTINATIONS.get(region, {}).get("courses", {})
    all_course_types = list(courses.keys())
    
    print(f"\n[{region}]")
    print(f"전체 course_type: {all_course_types}")
    
    region_gap_count = 0
    for theme in ["문화", "식도락", "자연", "쇼핑", "휴양", "액티비티"]:
        matching = [ct for ct in all_course_types if course_type_matches_theme(ct, theme)]
        count = len(matching)
        status = "O" if count >= 2 else "X"
        
        if count < 2:
            region_gap_count += 1
            gap_summary.append((region, theme, count))
            print(f"  {status} {theme:6}: {count}개 -> {matching}")
        else:
            print(f"  {status} {theme:6}: {count}개 -> {matching[:2]}...")

print("\n" + "=" * 80)
print(f"총 {len(gap_summary)}개의 gap 발견")
print("=" * 80)
print("\nGAP 목록 (추가 필요):")
for region, theme, count in gap_summary:
    need = 2 - count
    print(f"  {region:5} - {theme:6}: {count}개 필요 (need {need}개 더)")

# 지역별 gap 수 정리
print("\n지역별 gap 수:")
for region in region_order:
    region_gaps = [(t, c) for r, t, c in gap_summary if r == region]
    if region_gaps:
        print(f"  {region:5}: {len(region_gaps)}개 - {[t for t, c in region_gaps]}")
