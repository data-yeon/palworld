#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pal_nick_kor 컬럼 제거한 최종 CSV 생성 스크립트
"""

import csv

def create_final_csv_without_nick():
    """pal_nick_kor 컬럼을 제거한 최종 CSV 생성"""
    
    print("🔥 pal_nick_kor 컬럼 제거한 최종 CSV 생성 시작!")
    
    # 기존 완성된 CSV 읽기
    with open('ultimate_complete_1_to_10_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # pal_nick_kor 컬럼 제거
    for row in data:
        if 'pal_nick_kor' in row:
            del row['pal_nick_kor']
    
    # 새로운 CSV 생성
    filename = 'final_1_to_10_pals_without_nick.csv'
    
    if data:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    print(f"✅ pal_nick_kor 컬럼 제거 완료!")
    print(f"📋 총 {len(data)}개 팰 데이터")
    print(f"📄 파일명: {filename}")
    print(f"🗑️ 제거된 컬럼: pal_nick_kor")
    print(f"📊 남은 컬럼 수: {len(data[0].keys()) if data else 0}개")
    
    return data

if __name__ == "__main__":
    create_final_csv_without_nick() 