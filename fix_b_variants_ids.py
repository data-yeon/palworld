#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
팰월드 B variants ID 수정 스크립트
마지막 8개 행의 빈 ID를 올바른 B variant ID로 수정합니다.
"""

import csv

def main():
    input_file = "enhanced_complete_pals_batch4_complete.csv"
    output_file = "enhanced_complete_pals_batch4_fixed.csv"
    
    # 새로운 B variants의 올바른 ID 목록
    b_variant_ids = ["23B", "24B", "25B", "35B", "37B", "39B", "40B", "45B"]
    
    print("🔄 CSV 파일 읽는 중...")
    
    # 기존 데이터 읽기
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []
        all_data = list(reader)
    
    print(f"📊 총 데이터: {len(all_data)}개 팰")
    
    # 마지막 8개 행의 ID를 수정
    for i, variant_id in enumerate(b_variant_ids):
        row_index = len(all_data) - 8 + i  # 마지막 8개 행
        if row_index >= 0 and row_index < len(all_data):
            all_data[row_index]['id'] = variant_id
            name_kor = all_data[row_index].get('name_kor', '')
            print(f"✅ 수정됨: 행 {row_index + 1} → {variant_id} {name_kor}")
    
    # 수정된 데이터를 새 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
    
    print(f"\n🎉 완료! {output_file}에 ID가 수정된 데이터가 저장되었습니다.")
    
    # 통계 확인
    b_variants_count = sum(1 for row in all_data if row.get('id', '').endswith('B'))
    print(f"📊 총 B variants: {b_variants_count}개")
    print(f"🎯 아종 완성도: {b_variants_count}/59 = {(b_variants_count/59)*100:.1f}%")

if __name__ == "__main__":
    main() 