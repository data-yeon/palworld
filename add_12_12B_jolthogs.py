#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def parse_jolthog_data():
    """12번 찌릿도치 데이터 파싱"""
    
    return {
        'id': '12',
        'name_kor': '찌릿도치',
        'description_kor': '충격을 받으면 모았던 전기를 방출한다. 그 전압은 1,000만 볼트가 넘는다. 던지면 어설픈 중화기보다 더 위험하다.',
        'elements': '번개 속성',
        'partnerSkill_name': '찌르르 폭탄',
        'partnerSkill_describe': '발동하면 찌릿도치을 손에 장착하며 적에게 던져 착탄할 시 번개 폭발을 일으킨다.',
        'partnerSkill_needItem': '찌릿도치 장갑',
        'partnerSkill_needItemTechLevel': '8',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': '1',
        'stats_health': '70',
        'stats_food': '150',
        'stats_meleeAttack': '70',
        'stats_attack': '75',
        'stats_defense': '70',
        'stats_workSpeed': '100',
        'stats_support': '100',
        'stats_captureRateCorrect': '1.2',
        'stats_maleProbability': '50',
        'stats_combiRank': '1370',
        'stats_goldCoin': '1060',
        'stats_egg': '찌릿찌릿한 알',
        'stats_code': 'Hedgehog',
        'movement_slowWalkSpeed': '30',
        'movement_walkSpeed': '60',
        'movement_runSpeed': '400',
        'movement_rideSprintSpeed': '550',
        'movement_transportSpeed': '215',
        'level60_health': '3100-3782',
        'level60_attack': '465-575',
        'level60_defense': '391-493',
        'activeSkills': 'Lv.1 전기 파장(번개 속성, 40파워, 4초) | Lv.7 파워 샷(무속성, 35파워, 4초) | Lv.15 번개 구체(번개 속성, 50파워, 9초) | Lv.22 파워 폭탄(무속성, 70파워, 15초) | Lv.30 트라이 썬더(번개 속성, 90파워, 22초) | Lv.40 라인 썬더(번개 속성, 75파워, 16초) | Lv.50 전기 볼트(번개 속성, 150파워, 55초)',
        'activeSkills_count': '7',
        'passiveSkills': '',
        'passiveSkills_count': '0',
        'drops': '발전 기관(1, 100%)',
        'drops_count': '1',
        'workSuitabilities': '발전(LV.1)',
        'workSuitabilities_count': '1',
        'tribes': '부딪치면 위험! 찌릿도치(Tribe Boss) | 찌릿도치(Tribe Normal) | 코치도치(Variant)',
        'tribes_count': '3',
        'spawners': '찌릿도치(Lv.3-6, 1_5_plain_pachiguri) | 부딪치면 위험! 찌릿도치(Lv.10-13, 구릉 동굴, 외딴 섬의 동굴) | 찌릿도치(Lv.6-9, 구릉 동굴, 외딴 섬의 동굴)',
        'spawners_count': '3'
    }

def parse_jolthog_cryst_data():
    """12B 코치도치 데이터 파싱"""
    
    return {
        'id': '12B',
        'name_kor': '코치도치',
        'description_kor': '충격을 받으면 모았던 냉기를 방출한다. 방사상에 퍼진 냉기는 대기를 꽁꽁 얼려 습격해온 상대의 몸을 꿰뚫는다.',
        'elements': '얼음 속성',
        'partnerSkill_name': '딱딱 폭탄',
        'partnerSkill_describe': '발동하면 코치도치을 손에 장착하며 적에게 던져 착탄할 시 얼음 폭발을 일으킨다.',
        'partnerSkill_needItem': '코치도치 장갑',
        'partnerSkill_needItemTechLevel': '11',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': '2',
        'stats_health': '70',
        'stats_food': '150',
        'stats_meleeAttack': '70',
        'stats_attack': '75',
        'stats_defense': '80',
        'stats_workSpeed': '100',
        'stats_support': '100',
        'stats_captureRateCorrect': '1',
        'stats_maleProbability': '50',
        'stats_combiRank': '1360',
        'stats_goldCoin': '1070',
        'stats_egg': '얼어붙은 알',
        'stats_code': 'Hedgehog_Ice',
        'movement_slowWalkSpeed': '30',
        'movement_walkSpeed': '60',
        'movement_runSpeed': '400',
        'movement_rideSprintSpeed': '550',
        'movement_transportSpeed': '215',
        'level60_health': '3100-3782',
        'level60_attack': '465-575',
        'level60_defense': '440-557',
        'activeSkills': 'Lv.1 얼음 미사일(얼음 속성, 30파워, 3초) | Lv.7 파워 샷(무속성, 35파워, 4초) | Lv.15 빙산(얼음 속성, 70파워, 15초) | Lv.22 파워 폭탄(무속성, 70파워, 15초) | Lv.30 얼음 칼날(얼음 속성, 55파워, 10초) | Lv.40 서리 낀 입김(얼음 속성, 90파워, 22초) | Lv.50 눈보라 스파이크(얼음 속성, 130파워, 45초)',
        'activeSkills_count': '7',
        'passiveSkills': '',
        'passiveSkills_count': '0',
        'drops': '빙결 기관(1, 100%)',
        'drops_count': '1',
        'workSuitabilities': '냉각(LV.1)',
        'workSuitabilities_count': '1',
        'tribes': '밟으면 위험! 코치도치(Tribe Boss) | 코치도치(Tribe Normal) | 찌릿도치(Variant)',
        'tribes_count': '3',
        'spawners': '코치도치(Lv.1-10, Captured Cage: Grass) | 코치도치(Lv.10-20, Captured Cage: Grass2)',
        'spawners_count': '2'
    }

def main():
    print("🔧 12번, 12B 도치들 데이터 추가 작업 시작!")
    
    # 기존 1-11B 데이터 로드
    try:
        base_df = pd.read_csv('complete_1_to_11B_pals.csv', encoding='utf-8')
        print(f"✅ 기존 데이터 로드: {len(base_df)}개 팰")
    except FileNotFoundError:
        print("❌ 기존 파일을 찾을 수 없습니다")
        return
    
    # 새로운 팰 데이터 파싱
    jolthog_data = parse_jolthog_data()
    jolthog_cryst_data = parse_jolthog_cryst_data()
    
    # 기존 컬럼 구조에 맞춰 조정
    jolthog_df = pd.DataFrame([jolthog_data])
    jolthog_cryst_df = pd.DataFrame([jolthog_cryst_data])
    
    jolthog_df = jolthog_df.reindex(columns=base_df.columns, fill_value='')
    jolthog_cryst_df = jolthog_cryst_df.reindex(columns=base_df.columns, fill_value='')
    
    # 데이터 합치기
    combined_df = pd.concat([base_df, jolthog_df, jolthog_cryst_df], ignore_index=True)
    
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
    output_file = 'complete_1_to_12B_pals.csv'
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"🎉 완성! 총 {len(combined_df)}개 팰 (1-12B)")
    print(f"📁 파일: {output_file}")
    print(f"✅ 12번 찌릿도치, 12B 코치도치 완전한 데이터 추가됨!")
    
    # 새로 추가된 팰들 확인
    print(f"\n📋 새로 추가된 팰들:")
    new_pals = combined_df[combined_df['id'].isin(['12', '12B'])]
    for _, row in new_pals.iterrows():
        print(f"  {row['id']:>3}: {row['name_kor']} ({row['elements']})")
        print(f"      파트너 스킬: {row['partnerSkill_name']} (기술{row['partnerSkill_needItemTechLevel']})")
        print(f"      희귀도: {row['stats_rarity']}, 사이즈: {row['stats_size']}")
        print(f"      액티브 스킬: {row['activeSkills_count']}개")
        print(f"      작업 적성: {row['workSuitabilities_count']}개")
        print()
    
    print(f"📊 현재 완성된 팰 총 개수: {len(combined_df)}개")

if __name__ == "__main__":
    main() 