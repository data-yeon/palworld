#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1-10번 팰을 순서대로 추출하는 스크립트
"""

def get_pals_1_to_10_list():
    """1-10번 팰 목록과 URL 반환"""
    
    pals_1_to_10 = [
        {"id": "1", "name": "Lamball", "name_kor": "도로롱", "url": "https://paldb.cc/ko/Lamball"},
        {"id": "2", "name": "Cattiva", "name_kor": "까부냥", "url": "https://paldb.cc/ko/Cattiva"},
        {"id": "3", "name": "Chikipi", "name_kor": "병아리파", "url": "https://paldb.cc/ko/Chikipi"},
        {"id": "4", "name": "Lifmunk", "name_kor": "라이문크", "url": "https://paldb.cc/ko/Lifmunk"},
        {"id": "5", "name": "Foxparks", "name_kor": "키츠네비", "url": "https://paldb.cc/ko/Foxparks"},
        {"id": "6", "name": "Fuack", "name_kor": "푸악", "url": "https://paldb.cc/ko/Fuack"},
        {"id": "7", "name": "Sparkit", "name_kor": "스파키", "url": "https://paldb.cc/ko/Sparkit"},
        {"id": "8", "name": "Tanzee", "name_kor": "탄지", "url": "https://paldb.cc/ko/Tanzee"},
        {"id": "9", "name": "Rooby", "name_kor": "루비", "url": "https://paldb.cc/ko/Rooby"},
        {"id": "10", "name": "Pengullet", "name_kor": "펭귈릿", "url": "https://paldb.cc/ko/Pengullet"}
    ]
    
    return pals_1_to_10

def check_current_status():
    """현재 추출 상태 확인"""
    
    # 현재 있는 팰들
    current_pals = {
        "1": "도로롱",
        "2": "까부냥", 
        "26": "다크울프",
        "37": "신령사슴"
    }
    
    # 1-10번 중 필요한 팰들
    pals_1_to_10 = get_pals_1_to_10_list()
    needed_pals = []
    
    for pal in pals_1_to_10:
        if pal["id"] not in current_pals:
            needed_pals.append(pal)
    
    return {
        "current_pals": current_pals,
        "total_1_to_10": len(pals_1_to_10),
        "have_count": len([p for p in pals_1_to_10 if p["id"] in current_pals]),
        "needed_pals": needed_pals,
        "needed_count": len(needed_pals)
    }

def main():
    print("🎯 1-10번 팰 추출 계획\n")
    
    # 현재 상태 확인
    status = check_current_status()
    
    print("📊 현재 상황:")
    print(f"  - 1-10번 팰 총 개수: {status['total_1_to_10']}개")
    print(f"  - 이미 있는 팰: {status['have_count']}개")
    print(f"  - 필요한 팰: {status['needed_count']}개")
    
    print(f"\n✅ 이미 추출된 팰들:")
    for pal_id, pal_name in status['current_pals'].items():
        if int(pal_id) <= 10:
            print(f"  - ID {pal_id}: {pal_name}")
    
    print(f"\n❌ 아직 필요한 1-10번 팰들:")
    for pal in status['needed_pals']:
        print(f"  - ID {pal['id']}: {pal['name_kor']} ({pal['name']})")
    
    print(f"\n🔗 추출할 URL 목록:")
    for pal in status['needed_pals']:
        print(f"  {pal['url']}")
    
    print(f"\n🚀 다음 단계:")
    print(f"  1. 나머지 {status['needed_count']}개 팰 스크래핑")
    print(f"  2. JSON 파싱 및 변환") 
    print(f"  3. 기존 데이터와 통합")
    print(f"  4. 완전한 1-10번 팰 CSV 생성")
    
    print(f"\n💡 예상 시간: {status['needed_count'] * 10}초 - {status['needed_count'] * 20}초")

if __name__ == "__main__":
    main() 