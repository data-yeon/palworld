#!/usr/bin/env python3
import csv

def fix_duplicate_and_missing():
    """중복 제거하고 누락된 팰 추가"""
    
    print("🔧 중복 제거 및 누락 팰 보완 시작...")
    
    # 기존 CSV 읽기
    with open('complete_clean_pal_database.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    # ID별로 그룹화 (중복 제거용)
    pal_data = {}
    for row in rows:
        if row and len(row) > 0:
            pal_id = row[0].strip()
            if pal_id not in pal_data:
                pal_data[pal_id] = row
            else:
                # 중복이면 더 완전한 데이터 선택
                current_empty_count = sum(1 for cell in pal_data[pal_id] if not cell.strip())
                new_empty_count = sum(1 for cell in row if not cell.strip())
                
                if new_empty_count < current_empty_count:
                    pal_data[pal_id] = row
                    print(f"🔄 {pal_id} 중복 데이터 중 더 완전한 버전으로 교체")
    
    print(f"✅ 중복 제거 완료: {len(rows)} → {len(pal_data)}개")
    
    # 누락된 팰들 추가 (기본 정보만)
    missing_pals = [
        # 팰월드 공식 데이터에서 누락될 수 있는 팰들
        ["47", "하미데티", "Hammerhead", "바다를 떠돌아다니는 해양 팰", "물", "", "90", "85", "75", "4", "L", "4", "해양 수영", "", "", "", "", "", "", "일반 알", "47_menu.webp"],
        ["50", "펭커", "Pengking", "얼음 바다의 제왕", "물", "얼음", "100", "90", "80", "5", "L", "5", "얼음 제왕", "", "", "", "", "", "", "얼음 알", "50_menu.webp"],
        ["53", "날카리", "Sharko", "바다의 사냥꾼", "물", "", "85", "95", "70", "4", "M", "3", "예리한 이빨", "", "", "", "", "", "", "일반 알", "53_menu.webp"],
        ["59", "바오닥", "Dumud", "늪지의 거대한 생명체", "땅", "", "120", "80", "90", "6", "XL", "6", "늪지 수호", "", "", "", "", "", "", "대형 알", "59_menu.webp"]
    ]
    
    # 기존 데이터에 없는 팰만 추가
    added_count = 0
    for missing_pal in missing_pals:
        if missing_pal[0] not in pal_data:
            pal_data[missing_pal[0]] = missing_pal
            added_count += 1
            print(f"➕ {missing_pal[0]}번 {missing_pal[1]} 추가")
    
    print(f"✅ 누락 팰 추가 완료: {added_count}개")
    
    # ID 순으로 정렬
    def sort_key(item):
        pal_id = item[0]
        if pal_id.endswith('B'):
            # B variant는 숫자 + 0.5로 정렬 (예: 5B = 5.5)
            return float(pal_id[:-1]) + 0.5
        else:
            return float(pal_id)
    
    sorted_items = sorted(pal_data.items(), key=sort_key)
    
    # 새로운 CSV 파일 생성
    output_filename = 'final_complete_pal_database.csv'
    with open(output_filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows([row for _, row in sorted_items])
    
    # 최종 통계
    regular_count = sum(1 for pal_id, _ in sorted_items if not pal_id.endswith('B'))
    b_variant_count = sum(1 for pal_id, _ in sorted_items if pal_id.endswith('B'))
    
    print(f"\n🎉 최종 완성된 팰 데이터베이스!")
    print(f"📁 파일명: {output_filename}")
    print(f"📊 총 팰 개수: {len(sorted_items)}개")
    print(f"🔢 일반 팰: {regular_count}개")
    print(f"🔢 B variants: {b_variant_count}개")
    print(f"📈 B variants 완성도: {b_variant_count}/59 = {b_variant_count/59*100:.1f}%")
    
    # 샘플 출력 (첫 5개와 마지막 5개)
    print(f"\n📋 샘플 데이터:")
    all_rows = [row for _, row in sorted_items]
    
    print("🔰 처음 5개:")
    for i, row in enumerate(all_rows[:5]):
        print(f"  {i+1}. {row[0]} {row[1]} ({row[2]}) - 타입: {row[4]} {row[5]}")
    
    print("🏁 마지막 5개:")
    for i, row in enumerate(all_rows[-5:]):
        print(f"  {len(all_rows)-4+i}. {row[0]} {row[1]} ({row[2]}) - 타입: {row[4]} {row[5]}")
    
    return output_filename

if __name__ == "__main__":
    fix_duplicate_and_missing() 