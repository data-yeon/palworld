#!/usr/bin/env python3
import csv
import re

def analyze_missing_numbers():
    """CSV에서 누락된 번호와 중복된 번호 분석"""
    
    print("🔍 팰 번호 분석 시작...")
    
    # CSV 읽기
    with open('complete_clean_pal_database.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        
        regular_numbers = []
        b_variants = []
        
        for row in reader:
            if row and len(row) > 0:
                pal_id = row[0].strip()
                
                if pal_id.endswith('B'):
                    # B variant
                    try:
                        num = int(pal_id[:-1])
                        b_variants.append(num)
                    except:
                        continue
                else:
                    # 일반 팰
                    try:
                        num = int(pal_id)
                        regular_numbers.append(num)
                    except:
                        continue
    
    # 정렬
    regular_numbers.sort()
    b_variants.sort()
    
    print(f"📊 발견된 일반 팰: {len(regular_numbers)}개")
    print(f"📊 발견된 B variants: {len(b_variants)}개")
    
    # 중복 확인
    regular_duplicates = []
    for i in range(len(regular_numbers)-1):
        if regular_numbers[i] == regular_numbers[i+1]:
            if regular_numbers[i] not in regular_duplicates:
                regular_duplicates.append(regular_numbers[i])
    
    b_duplicates = []
    for i in range(len(b_variants)-1):
        if b_variants[i] == b_variants[i+1]:
            if b_variants[i] not in b_duplicates:
                b_duplicates.append(b_variants[i])
    
    if regular_duplicates:
        print(f"⚠️ 중복된 일반 팰: {regular_duplicates}")
    
    if b_duplicates:
        print(f"⚠️ 중복된 B variants: {b_duplicates}")
    
    # 누락된 번호 찾기 (1~115 범위)
    expected_range = set(range(1, 116))
    found_regular = set(regular_numbers)
    missing_regular = sorted(expected_range - found_regular)
    
    print(f"\n🔍 일반 팰 분석 (1~115):")
    print(f"✅ 있는 번호: {len(found_regular)}개")
    print(f"❌ 누락된 번호: {len(missing_regular)}개")
    
    if missing_regular:
        print(f"누락된 번호들: {missing_regular}")
        
        # 누락된 번호들이 연속적인지 확인
        gaps = []
        start = None
        for i, num in enumerate(missing_regular):
            if start is None:
                start = num
            elif missing_regular[i-1] + 1 != num:
                if start == missing_regular[i-1]:
                    gaps.append(str(start))
                else:
                    gaps.append(f"{start}-{missing_regular[i-1]}")
                start = num
        
        # 마지막 그룹 추가
        if start is not None:
            if start == missing_regular[-1]:
                gaps.append(str(start))
            else:
                gaps.append(f"{start}-{missing_regular[-1]}")
        
        print(f"누락 구간: {', '.join(gaps)}")
    
    # B variants 분석
    print(f"\n🔍 B variants 분석:")
    print(f"✅ 있는 B variants: {sorted(set(b_variants))}")
    
    # 일반 팰 중에서 B variant가 있어야 할 후보들 확인
    potential_b_variants = []
    for num in found_regular:
        if num not in b_variants and num <= 111:  # 111 이후는 최신 팰들
            potential_b_variants.append(num)
    
    print(f"🤔 B variant가 없는 일반 팰들 (처음 20개): {potential_b_variants[:20]}")
    
    # 전체 통계
    print(f"\n📈 전체 통계:")
    print(f"일반 팰: {len(found_regular)}/115 = {len(found_regular)/115*100:.1f}%")
    print(f"B variants: {len(set(b_variants))}/59 = {len(set(b_variants))/59*100:.1f}%")
    
    return missing_regular, regular_duplicates, b_duplicates

if __name__ == "__main__":
    analyze_missing_numbers() 