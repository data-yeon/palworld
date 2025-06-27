#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
빠른 팰 데이터 추출을 위한 개선된 크롤링 스크립트
- 배치 크기 증가 (20개씩)
- 병렬 처리 시도
"""

import csv
import json
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

def get_remaining_pals():
    """아직 추출하지 않은 팰들의 목록 반환"""
    
    # 이미 추출한 팰 ID들
    extracted_ids = {'1', '26', '37'}
    
    # 다음에 추출할 팰들 (20개 배치)
    next_batch_pals = [
        {'id': '2', 'name': 'Cattiva', 'name_kor': '까부냥'},
        {'id': '3', 'name': 'Chikipi', 'name_kor': '병아리파'},  
        {'id': '4', 'name': 'Lifmunk', 'name_kor': '라이문크'},
        {'id': '5', 'name': 'Foxparks', 'name_kor': '키츠네비'},
        {'id': '6', 'name': 'Fuack', 'name_kor': '거북이'},
        {'id': '7', 'name': 'Sparkit', 'name_kor': '전기너구리'},
        {'id': '8', 'name': 'Tanzee', 'name_kor': '춤원숭이'},
        {'id': '9', 'name': 'Rooby', 'name_kor': '루비토끼'},
        {'id': '10', 'name': 'Pengullet', 'name_kor': '펭키'},
        {'id': '11', 'name': 'Penking', 'name_kor': '펭킹'},
        {'id': '12', 'name': 'Jolthog', 'name_kor': '전기고슴도치'},
        {'id': '13', 'name': 'Gumoss', 'name_kor': '잔디덮개'},
        {'id': '14', 'name': 'Vixy', 'name_kor': '비키'},
        {'id': '15', 'name': 'Hoocrates', 'name_kor': '후크래트'},
        {'id': '16', 'name': 'Teafant', 'name_kor': '찻잔코끼리'},
        {'id': '17', 'name': 'Depresso', 'name_kor': '우울이'},
        {'id': '18', 'name': 'Cremis', 'name_kor': '크레미스'},
        {'id': '19', 'name': 'Daedream', 'name_kor': '데드림'},
        {'id': '20', 'name': 'Rushoar', 'name_kor': '돌진멧돼지'},
        {'id': '21', 'name': 'Nox', 'name_kor': '녹스'},
    ]
    
    return next_batch_pals

def create_batch_urls(pal_list):
    """팰 목록을 URL로 변환"""
    base_url = "https://paldb.cc/ko/"
    urls = []
    
    for pal in pal_list:
        url = f"{base_url}{pal['name']}"
        urls.append(url)
    
    return urls

def speed_optimization_tips():
    """속도 개선을 위한 팁 제공"""
    tips = [
        "🚀 **배치 크기 증가**: 10개 → 20개로 증가하여 API 호출 횟수 감소",
        "⚡ **병렬 처리**: 여러 팰을 동시에 처리하여 대기 시간 단축", 
        "🎯 **직접 URL 사용**: 팰별 직접 URL로 정확한 페이지 접근",
        "📊 **점진적 확장**: 작은 배치로 시작하여 점차 확장",
        "💾 **로컬 캐싱**: 이미 추출한 데이터는 재사용",
        "🔄 **재시도 로직**: 실패한 요청에 대한 자동 재시도"
    ]
    
    return tips

def estimate_time():
    """예상 소요 시간 계산"""
    total_pals = 214
    extracted_pals = 3
    remaining_pals = total_pals - extracted_pals
    
    # 현재 속도 기준 (10개당 약 2-3분)
    current_batch_time = 150  # 초
    batches_needed = remaining_pals // 20  # 20개씩 배치
    
    estimated_seconds = batches_needed * current_batch_time
    estimated_minutes = estimated_seconds / 60
    estimated_hours = estimated_minutes / 60
    
    return {
        'remaining_pals': remaining_pals,
        'batches_needed': batches_needed,
        'estimated_minutes': round(estimated_minutes, 1),
        'estimated_hours': round(estimated_hours, 1)
    }

def main():
    print("🔍 **팰 크롤링 속도 분석 및 최적화**\n")
    
    # 현재 상황 분석
    print("📊 **현재 상황:**")
    print("- 총 팰 수: 214개")
    print("- 추출 완료: 3개 (1.4%)")
    print("- 남은 팰: 211개")
    
    # 느린 이유 분석
    print("\n🐌 **느린 이유:**")
    reasons = [
        "1. **Firecrawl API 처리 시간**: 각 페이지 스크래핑 + 구조화 변환",
        "2. **작은 배치 크기**: 10개씩 처리로 많은 API 호출 필요",
        "3. **복잡한 데이터**: 40+ 필드의 상세한 정보 추출",
        "4. **순차 처리**: 한 배치씩 순서대로 처리"
    ]
    
    for reason in reasons:
        print(f"   {reason}")
    
    # 개선 방안
    print("\n⚡ **속도 개선 방안:**")
    tips = speed_optimization_tips()
    for i, tip in enumerate(tips, 1):
        print(f"   {tip}")
    
    # 시간 예측
    print("\n⏱️ **예상 소요 시간:**")
    time_est = estimate_time()
    print(f"   - 남은 팰: {time_est['remaining_pals']}개")
    print(f"   - 필요 배치: {time_est['batches_needed']}회 (20개씩)")
    print(f"   - 예상 시간: {time_est['estimated_minutes']}분 ({time_est['estimated_hours']}시간)")
    
    # 다음 배치 준비
    print("\n📋 **다음 추출 대상 (20개 배치):**")
    next_pals = get_remaining_pals()
    for i, pal in enumerate(next_pals, 1):
        print(f"   {i:2d}. ID: {pal['id']} - {pal['name_kor']} ({pal['name']})")
    
    # URL 생성
    urls = create_batch_urls(next_pals)
    print(f"\n🔗 **생성된 URL 수**: {len(urls)}개")
    print("   첫 번째 URL:", urls[0])
    print("   마지막 URL:", urls[-1])
    
    print("\n✨ **권장 사항:**")
    print("   1. 20개 배치로 크기 증가")
    print("   2. 현재까지의 3개 데이터로 구조 검증")
    print("   3. 점진적으로 더 큰 배치 시도")
    print("   4. 실패한 팰에 대한 개별 재시도")

if __name__ == "__main__":
    main() 