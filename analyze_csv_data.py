#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json
from collections import Counter

def analyze_pal_database():
    """팰 데이터베이스를 분석하고 보기 좋게 정리"""
    
    # CSV 파일 읽기
    df = pd.read_csv('perfect_complete_pal_database_214.csv')
    
    print("=" * 80)
    print("🎯 팰월드 완벽 데이터베이스 분석 보고서")
    print("=" * 80)
    
    # 1. 기본 통계
    print("\n📊 **기본 통계 정보**")
    print(f"총 팰 수: {len(df)}개")
    print(f"컬럼 수: {len(df.columns)}개")
    
    # 2. ID 범위 분석
    regular_pals = df[~df['id'].astype(str).str.contains('B|S', na=False)]
    b_variants = df[df['id'].astype(str).str.contains('B', na=False)]
    s_series = df[df['id'].astype(str).str.contains('S', na=False)]
    
    print(f"\n🔢 **ID 분포**")
    print(f"일반 팰: {len(regular_pals)}개")
    print(f"B 변형: {len(b_variants)}개")
    print(f"S 시리즈: {len(s_series)}개")
    
    # 3. 타입 분석
    print(f"\n🌟 **타입별 분포**")
    type1_counts = Counter(df['type1'].dropna())
    type2_counts = Counter(df['type2'].dropna())
    
    print("주 속성:")
    for type_name, count in type1_counts.most_common():
        print(f"  {type_name}: {count}개")
    
    print("\n부 속성:")
    for type_name, count in type2_counts.most_common():
        print(f"  {type_name}: {count}개")
    
    # 4. 희귀도 분석
    print(f"\n⭐ **희귀도별 분포**")
    rarity_counts = Counter(df['rarity'].dropna())
    for rarity, count in sorted(rarity_counts.items()):
        print(f"희귀도 {rarity}: {count}개")
    
    # 5. 크기별 분포
    print(f"\n📏 **크기별 분포**")
    size_counts = Counter(df['size'].dropna())
    for size, count in size_counts.most_common():
        print(f"  {size}: {count}개")
    
    # 6. 샘플 데이터 (처음 10개)
    print(f"\n📋 **샘플 데이터 (처음 10개 팰)**")
    print("-" * 80)
    for idx, row in df.head(10).iterrows():
        print(f"ID: {row['id']} | {row['name']} ({row['englishName']})")
        print(f"   타입: {row['type1']}" + (f"/{row['type2']}" if pd.notna(row['type2']) else ""))
        print(f"   스탯: HP{row['hp']} ATK{row['attack']} DEF{row['defense']}")
        print(f"   설명: {row['description'][:50]}..." if len(str(row['description'])) > 50 else f"   설명: {row['description']}")
        print()
    
    # 7. B 변형 팰들
    if len(b_variants) > 0:
        print(f"\n🌈 **B 변형 팰들 ({len(b_variants)}개)**")
        print("-" * 50)
        for idx, row in b_variants.iterrows():
            print(f"ID: {row['id']} | {row['name']} ({row['englishName']})")
    
    # 8. S 시리즈 팰들
    if len(s_series) > 0:
        print(f"\n👻 **S 시리즈 팰들 ({len(s_series)}개)**")
        print("-" * 50)
        for idx, row in s_series.iterrows():
            print(f"ID: {row['id']} | {row['name']} ({row['englishName']})")
    
    # 9. 최신 크롤링된 팰들 (116번 이후)
    latest_pals = df[df['id'].astype(str).str.match(r'^(11[6-9]|1[2-5][0-9])$', na=False)]
    if len(latest_pals) > 0:
        print(f"\n🆕 **최신 크롤링된 팰들 (116번 이후, {len(latest_pals)}개)**")
        print("-" * 60)
        for idx, row in latest_pals.iterrows():
            print(f"ID: {row['id']} | {row['name']} ({row['englishName']}) - {row['type1']}" + 
                  (f"/{row['type2']}" if pd.notna(row['type2']) else ""))
    
    # 10. 파일 정보
    print(f"\n💾 **파일 정보**")
    print(f"파일명: perfect_complete_pal_database_214.csv")
    print(f"컬럼: {', '.join(df.columns.tolist())}")
    
    # 11. 데이터 품질 체크
    print(f"\n🔍 **데이터 품질 체크**")
    print(f"빈 이름: {df['name'].isnull().sum()}개")
    print(f"빈 영어명: {df['englishName'].isnull().sum()}개")
    print(f"빈 설명: {df['description'].isnull().sum()}개")
    print(f"빈 타입1: {df['type1'].isnull().sum()}개")
    
    # 12. CSV 미리보기 저장
    preview_data = []
    for idx, row in df.head(20).iterrows():
        preview_data.append({
            'ID': row['id'],
            '이름': row['name'],
            '영어명': row['englishName'],
            '타입': f"{row['type1']}" + (f"/{row['type2']}" if pd.notna(row['type2']) else ""),
            'HP': row['hp'],
            '공격': row['attack'],
            '방어': row['defense'],
            '희귀도': row['rarity'],
            '크기': row['size']
        })
    
    # JSON으로 미리보기 저장
    with open('csv_preview_analysis.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total_count': len(df),
            'regular_pals': len(regular_pals),
            'b_variants': len(b_variants),
            's_series': len(s_series),
            'type1_distribution': dict(type1_counts),
            'type2_distribution': dict(type2_counts),
            'rarity_distribution': dict(rarity_counts),
            'size_distribution': dict(size_counts),
            'preview_data': preview_data,
            'columns': df.columns.tolist()
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 분석 완료! 미리보기 데이터가 'csv_preview_analysis.json'에 저장되었습니다.")
    print("=" * 80)

if __name__ == "__main__":
    analyze_pal_database() 