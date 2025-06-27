#!/usr/bin/env python3
import csv

def analyze_paldb_gap():
    """우리 데이터와 paldb.cc의 214마리 차이 분석"""
    
    print("🔍 paldb.cc 기준 팰 데이터 분석...")
    print(f"📊 paldb.cc 총 팰 수: 214마리")
    
    # 현재 우리 데이터 분석
    with open('final_complete_pal_database.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        
        our_regular = []
        our_b_variants = []
        
        for row in reader:
            if row and len(row) > 0:
                pal_id = row[0].strip()
                if pal_id.endswith('B'):
                    try:
                        num = int(pal_id[:-1])
                        our_b_variants.append(num)
                    except:
                        continue
                else:
                    try:
                        num = int(pal_id)
                        our_regular.append(num)
                    except:
                        continue
    
    print(f"📊 우리 현재 데이터:")
    print(f"   일반 팰: {len(our_regular)}마리")
    print(f"   B variants: {len(our_b_variants)}마리")
    print(f"   총합: {len(our_regular) + len(our_b_variants)}마리")
    
    print(f"\n💔 부족한 팰 수:")
    print(f"   전체 부족: {214 - (len(our_regular) + len(our_b_variants))}마리")
    
    # paldb.cc에서 확인된 최신 범위 분석
    print(f"\n🆕 paldb.cc에서 확인된 새로운 팰들:")
    print(f"   #116-155: 40마리의 새로운 팰들!")
    print(f"   + 추가 B variants들")
    print(f"   + 특수 팰들 (슬라임, 배트 등)")
    
    # 우리가 놓친 주요 구간들
    missing_ranges = [
        (116, 155, "최신 업데이트 팰들"),
        (156, 214, "미발견 팰들?")
    ]
    
    print(f"\n🎯 우선순위 크롤링 대상:")
    for start, end, desc in missing_ranges:
        count = end - start + 1
        print(f"   {start}-{end}번: {desc} ({count}마리)")
    
    # 특별한 팰들 (슬라임, 배트 등)
    special_pals = [
        "Green Slime", "Blue Slime", "Red Slime", "Purple Slime",
        "Illuminant Slime", "Rainbow Slime", "Enchanted Sword",
        "Cave Bat", "Illuminant Bat", "Eye of Cthulhu", "Demon Eye"
    ]
    
    print(f"\n🎮 특수 팰들:")
    for pal in special_pals:
        print(f"   {pal}")
    
    print(f"\n🚀 다음 액션 플랜:")
    print(f"   1. 116-155번 팰들 대량 크롤링")
    print(f"   2. 추가 B variants 발견")
    print(f"   3. 특수 팰들 데이터 수집")
    print(f"   4. 최종 214마리 완성!")
    
    return len(our_regular) + len(our_b_variants)

if __name__ == "__main__":
    current_count = analyze_paldb_gap()
    print(f"\n🎯 목표: {214 - current_count}마리 추가 필요!") 