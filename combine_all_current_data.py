#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def main():
    # 기존 1-10B 데이터 로드
    try:
        df1 = pd.read_csv('complete_1_to_10_with_b_variants.csv', encoding='utf-8')
        print(f"✅ 기존 1-10B 데이터 로드: {len(df1)}개 팰")
    except FileNotFoundError:
        print("❌ complete_1_to_10_with_b_variants.csv 파일을 찾을 수 없습니다")
        return
    
    # 새로운 11-12B 데이터 로드
    try:
        df2 = pd.read_csv('pals_11_to_12B_complete.csv', encoding='utf-8')
        print(f"✅ 새로운 11-12B 데이터 로드: {len(df2)}개 팰")
    except FileNotFoundError:
        print("❌ pals_11_to_12B_complete.csv 파일을 찾을 수 없습니다")
        return
    
    # 컬럼 순서 맞추기 (df1 기준)
    df2_reordered = df2.reindex(columns=df1.columns, fill_value='')
    
    # 데이터 합치기
    combined_df = pd.concat([df1, df2_reordered], ignore_index=True)
    
    # ID별로 정렬 (숫자 순서대로)
    def sort_key(id_str):
        if 'B' in str(id_str):
            base_id = int(str(id_str).replace('B', ''))
            return (base_id, 1)  # B 변종은 같은 번호 다음에 오도록
        else:
            return (int(str(id_str)), 0)
    
    combined_df['sort_key'] = combined_df['id'].apply(sort_key)
    combined_df = combined_df.sort_values('sort_key').drop('sort_key', axis=1)
    
    # 최종 파일 저장
    output_filename = 'complete_1_to_12B_all_pals.csv'
    combined_df.to_csv(output_filename, index=False, encoding='utf-8')
    
    print(f"\n🎉 데이터 합치기 완료!")
    print(f"📁 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(combined_df)}개")
    print(f"📋 컬럼 수: {len(combined_df.columns)}개")
    
    # 팰 ID 목록 출력
    print(f"\n📝 포함된 팰 ID들:")
    ids = combined_df['id'].tolist()
    for i, pal_id in enumerate(ids):
        if i > 0 and i % 10 == 0:
            print()
        print(f"{pal_id}", end=", " if i < len(ids)-1 else "\n")
    
    # 한국어 이름들도 출력
    print(f"\n🏷️ 팰 이름들:")
    names = combined_df['name_kor'].tolist()
    for i, name in enumerate(names):
        if i > 0 and i % 5 == 0:
            print()
        print(f"{combined_df.iloc[i]['id']}:{name}", end=", " if i < len(names)-1 else "\n")

if __name__ == "__main__":
    main() 