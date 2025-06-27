#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def parse_penking_lux_data():
    """11B 펭키드 데이터 파싱"""
    
    return {
        'id': '11B',
        'name_kor': '펭키드',
        'description_kor': '수중 사냥에 도움이 되도록 전기의 힘을 얻어 색이 변화했으며 그 결과 펭키의 충성을 잃고 말았다. 그러나 어째서인지는 몰라도 이번에는 뎅키의 충성을 얻게 되었다.',
        'elements': '물 속성|번개 속성',
        'partnerSkill_name': '불굴의 전격 수장',
        'partnerSkill_describe': '함께 싸우는 동안 물 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        'stats_size': 'L',
        'stats_rarity': '7',
        'stats_health': '100',
        'stats_food': '525',
        'stats_meleeAttack': '100',
        'stats_attack': '100',
        'stats_defense': '100',
        'stats_workSpeed': '100',
        'stats_support': '100',
        'stats_captureRateCorrect': '1',
        'stats_maleProbability': '50',
        'stats_combiRank': '490',
        'stats_goldCoin': '6490',
        'stats_egg': '축축한 대형 알',
        'stats_code': 'CaptainPenguin_Black',
        'movement_slowWalkSpeed': '50',
        'movement_walkSpeed': '110',
        'movement_runSpeed': '450',
        'movement_rideSprintSpeed': '600',
        'movement_transportSpeed': '280',
        'level60_health': '4075-5050',
        'level60_attack': '587-733',
        'level60_defense': '537-683',
        'activeSkills': 'Lv.1 번개 창(번개 속성, 30파워, 2초) | Lv.7 플라즈마 토네이도(번개 속성, 65파워, 13초) | Lv.15 버블 샷(물 속성, 65파워, 13초) | Lv.22 트라이 스파크(번개 속성, 110파워, 35초) | Lv.30 썬더 슬라이딩(번개 속성, 145파워, 35초) | Lv.40 아쿠아 서지(물 속성, 160파워, 56초) | Lv.50 번개 폭풍(번개 속성, 160파워, 60초)',
        'activeSkills_count': '7',
        'passiveSkills': '',
        'passiveSkills_count': '0',
        'drops': '발전 기관(1-3, 100%) | 펭킹 날개 장식(1, 50%)',
        'drops_count': '2',
        'workSuitabilities': '관개(LV.2) | 발전(LV.2) | 수작업(LV.2) | 채굴(LV.2) | 운반(LV.2)',
        'workSuitabilities_count': '5',
        'tribes': '까마득한 어둠의 개척자 펭키드(Tribe Boss) | 펭키드(Tribe Normal)',
        'tribes_count': '2',
        'spawners': '펭키드(Lv.21-34, 커다란 낚시터 Big 8.57%)',
        'spawners_count': '1'
    }

def main():
    print("🔧 11B 펭키드 데이터 추가 작업 시작!")
    
    # 기존 1-11 데이터 로드
    try:
        base_df = pd.read_csv('complete_1_to_11_pals.csv', encoding='utf-8')
        print(f"✅ 기존 데이터 로드: {len(base_df)}개 팰")
    except FileNotFoundError:
        print("❌ 기존 파일을 찾을 수 없습니다")
        return
    
    # 펭키드 데이터 파싱
    penking_lux_data = parse_penking_lux_data()
    
    # 기존 컬럼 구조에 맞춰 조정
    penking_lux_df = pd.DataFrame([penking_lux_data])
    penking_lux_df = penking_lux_df.reindex(columns=base_df.columns, fill_value='')
    
    # 데이터 합치기
    combined_df = pd.concat([base_df, penking_lux_df], ignore_index=True)
    
    # ID 순서로 정렬
    def sort_key(id_str):
        if 'B' in str(id_str):
            base_id = int(str(id_str).replace('B', ''))
            return (base_id, 1)
        else:
            return (int(str(id_str)), 0)
    
    combined_df['sort_key'] = combined_df['id'].apply(sort_key)
    combined_df = combined_df.sort_values('sort_key').drop('sort_key', axis=1)
    
    # 저장
    output_file = 'complete_1_to_11B_pals.csv'
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"🎉 완성! 총 {len(combined_df)}개 팰 (1-11B)")
    print(f"📁 파일: {output_file}")
    print(f"✅ 11B 펭키드 완전한 데이터 추가됨!")
    
    # 새로 추가된 팰 확인
    print(f"\n📋 새로 추가된 팰:")
    new_pal = combined_df[combined_df['id'] == '11B'].iloc[0]
    print(f"  11B: {new_pal['name_kor']} ({new_pal['elements']})")
    print(f"      파트너 스킬: {new_pal['partnerSkill_name']}")
    print(f"      희귀도: {new_pal['stats_rarity']}, 사이즈: {new_pal['stats_size']}")
    print(f"      액티브 스킬: {new_pal['activeSkills_count']}개")
    print(f"      작업 적성: {new_pal['workSuitabilities_count']}개")
    
    print(f"\n📊 현재 완성된 팰 목록:")
    for _, row in combined_df.iterrows():
        print(f"  {row['id']:>3}: {row['name_kor']} ({row['elements']})")

if __name__ == "__main__":
    main() 