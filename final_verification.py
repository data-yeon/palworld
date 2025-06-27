#!/usr/bin/env python3
import csv

def final_verification():
    """최종 검증: 모든 번호가 완전한지 확인"""
    
    print("🔍 최종 완성도 검증 시작...")
    
    # CSV 읽기
    with open('final_complete_pal_database.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    # 번호별 분류
    regular_pals = []
    b_variants = []
    
    for row in rows:
        if row and len(row) > 0:
            pal_id = row[0].strip()
            if pal_id.endswith('B'):
                try:
                    num = int(pal_id[:-1])
                    b_variants.append((num, row[1], row[2]))
                except:
                    continue
            else:
                try:
                    num = int(pal_id)
                    regular_pals.append((num, row[1], row[2]))
                except:
                    continue
    
    # 정렬
    regular_pals.sort()
    b_variants.sort()
    
    print(f"📊 데이터베이스 완성도 검증 결과:")
    print(f"=" * 50)
    
    # 일반 팰 연속성 확인
    regular_numbers = [num for num, _, _ in regular_pals]
    expected_numbers = list(range(1, 116))  # 1~115
    missing_numbers = [num for num in expected_numbers if num not in regular_numbers]
    
    print(f"🔢 일반 팰 (1~115번):")
    print(f"   ✅ 보유: {len(regular_numbers)}/115개")
    print(f"   📈 완성도: {len(regular_numbers)/115*100:.1f}%")
    
    if missing_numbers:
        print(f"   ❌ 누락: {missing_numbers}")
    else:
        print(f"   🎉 완전! 모든 번호 보유!")
    
    # 추가 팰 (116번 이상)
    extra_pals = [num for num in regular_numbers if num > 115]
    if extra_pals:
        print(f"   🆕 추가 팰 (116번 이상): {len(extra_pals)}개")
        for num in extra_pals:
            pal_name = next(name for n, name, _ in regular_pals if n == num)
            print(f"      {num}번 {pal_name}")
    
    # B variants 분석
    print(f"\n🔀 B variants:")
    print(f"   ✅ 보유: {len(b_variants)}개")
    print(f"   📈 예상 완성도: {len(b_variants)/59*100:.1f}%")
    
    # B variants 목록 (5개씩 그룹)
    print(f"   📋 보유 목록:")
    b_numbers = [num for num, _, _ in b_variants]
    for i in range(0, len(b_numbers), 5):
        group = b_numbers[i:i+5]
        group_str = ', '.join([f"{num}B" for num in group])
        print(f"      {group_str}")
    
    # 범위별 통계
    print(f"\n📊 범위별 완성도:")
    ranges = [
        (1, 20, "초급 팰"),
        (21, 40, "중급 팰"),
        (41, 60, "고급 팰"),
        (61, 80, "전설 팰"),
        (81, 100, "마스터 팰"),
        (101, 115, "최고급 팰")
    ]
    
    for start, end, category in ranges:
        count = sum(1 for num in regular_numbers if start <= num <= end)
        total = end - start + 1
        print(f"   {category} ({start}~{end}번): {count}/{total}개 ({count/total*100:.1f}%)")
    
    # 최종 요약
    total_pals = len(regular_pals) + len(b_variants)
    
    print(f"\n🎯 최종 요약:")
    print(f"=" * 50)
    print(f"📁 파일: final_complete_pal_database.csv")
    print(f"📊 총 팰: {total_pals}개")
    print(f"🔢 일반 팰: {len(regular_pals)}개")
    print(f"🔀 B variants: {len(b_variants)}개")
    print(f"✨ 상태: {'완전한 데이터베이스!' if not missing_numbers else '일부 누락 있음'}")
    
    if not missing_numbers:
        print(f"\n🏆 축하합니다! 팰월드 데이터베이스가 완전히 완성되었습니다!")
        print(f"🎮 1번부터 115번까지 모든 팰이 포함되어 있습니다.")
        print(f"🌟 추가로 {len(b_variants)}개의 B variants도 포함되어 있습니다.")
    
    return len(missing_numbers) == 0

if __name__ == "__main__":
    final_verification() 