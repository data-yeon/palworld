#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import re

def parse_penking_data():
    """11번 펭킹 데이터 파싱"""
    
    penking_markdown = """
사실 [펭키](https://paldb.cc/ko/Pengullet) 와(과) 아무 연관도 없는 종.
멋대로 상전 대접을 받은 터라
일단 열심히 뻗대고 보고 있다.

##### Partner Skill: 용감한 바다의 전사

함께 싸우는 동안 화염 속성 팰을 쓰러뜨렸을 때
드롭 아이템 획득량이 증가한다.

##### Stats
Size: L
Rarity: 6
HP: 95
식사량: 525
MeleeAttack: 70
공격: 95
방어: 95
작업 속도: 100

##### Movement
SlowWalkSpeed: 50
WalkSpeed: 110
RunSpeed: 450
RideSprintSpeed: 600
TransportSpeed: 280

##### Level 60
HP: 3912 – 4838
공격: 563 – 702
방어: 513 – 652

##### Active Skills
Lv. 1 아쿠아 샷 (물 속성, 위력: 40, 쿨타임: 4초)
Lv. 7 빙산 (얼음 속성, 위력: 70, 쿨타임: 15초)
Lv. 15 캡틴 슬라이딩 (얼음 속성, 위력: 70, 쿨타임: 10초)
Lv. 22 서리 낀 입김 (얼음 속성, 위력: 90, 쿨타임: 22초)
Lv. 30 물폭탄 (물 속성, 위력: 100, 쿨타임: 30초)
Lv. 40 눈보라 스파이크 (얼음 속성, 위력: 130, 쿨타임: 45초)
Lv. 50 하이드로 스트림 (물 속성, 위력: 150, 쿨타임: 55초)

##### Possible Drops
빙결 기관 1–3 (100%)
펭킹 날개 장식 1 (50%)

##### Work Suitabilities
관개 Lv2
수작업 Lv2
채굴 Lv2
냉각 Lv2
운반 Lv2
"""

    return {
        'id': '11',
        'name_kor': '펭킹',
        'description_kor': '사실 펭키와 아무 연관도 없는 종. 멋대로 상전 대접을 받은 터라 일단 열심히 뻗대고 보고 있다.',
        'elements': '물 속성|얼음 속성',
        'partnerSkill_name': '용감한 바다의 전사',
        'partnerSkill_describe': '함께 싸우는 동안 화염 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        'stats_size': 'L',
        'stats_rarity': '6',
        'stats_health': '95',
        'stats_food': '525',
        'stats_meleeAttack': '70',
        'stats_attack': '95',
        'stats_defense': '95',
        'stats_workSpeed': '100',
        'stats_support': '100',
        'stats_captureRateCorrect': '1',
        'stats_maleProbability': '50',
        'stats_combiRank': '520',
        'stats_goldCoin': '5410',
        'stats_egg': '축축한 대형 알',
        'stats_code': 'CaptainPenguin',
        'movement_slowWalkSpeed': '50',
        'movement_walkSpeed': '110',
        'movement_runSpeed': '450',
        'movement_rideSprintSpeed': '600',
        'movement_transportSpeed': '280',
        'level60_health': '3912-4838',
        'level60_attack': '563-702',
        'level60_defense': '513-652',
        'activeSkills': 'Lv.1 아쿠아 샷(물 속성, 40파워, 4초) | Lv.7 빙산(얼음 속성, 70파워, 15초) | Lv.15 캡틴 슬라이딩(얼음 속성, 70파워, 10초) | Lv.22 서리 낀 입김(얼음 속성, 90파워, 22초) | Lv.30 물폭탄(물 속성, 100파워, 30초) | Lv.40 눈보라 스파이크(얼음 속성, 130파워, 45초) | Lv.50 하이드로 스트림(물 속성, 150파워, 55초)',
        'activeSkills_count': '7',
        'passiveSkills': '',
        'passiveSkills_count': '0',
        'drops': '빙결 기관(1-3, 100%) | 펭킹 날개 장식(1, 50%)',
        'drops_count': '2',
        'workSuitabilities': '관개(LV.2) | 수작업(LV.2) | 채굴(LV.2) | 냉각(LV.2) | 운반(LV.2)',
        'workSuitabilities_count': '5',
        'tribes': '얼어붙은 바다의 개척자 펭킹(Tribe Boss) | 펭킹(Tribe Normal)',
        'tribes_count': '2',
        'spawners': '얼어붙은 바다의 개척자 펭킹(Lv.15-15, World Map 311,-13) | 펭킹(Lv.18-22, 제1 사냥 금지 구역) | 펭킹(Lv.11-18, 낚시터 Small 4.95%)',
        'spawners_count': '3'
    }

def main():
    print("🔧 11번 펭킹 데이터 추가 작업 시작!")
    
    # 기존 완전한 1-10B 데이터 로드
    try:
        base_df = pd.read_csv('verified_complete_1_to_10B_final.csv', encoding='utf-8')
        print(f"✅ 기존 데이터 로드: {len(base_df)}개 팰")
    except FileNotFoundError:
        print("❌ 기존 파일을 찾을 수 없습니다")
        return
    
    # 펭킹 데이터 파싱
    penking_data = parse_penking_data()
    
    # 기존 컬럼 구조에 맞춰 조정
    penking_df = pd.DataFrame([penking_data])
    penking_df = penking_df.reindex(columns=base_df.columns, fill_value='')
    
    # 데이터 합치기
    combined_df = pd.concat([base_df, penking_df], ignore_index=True)
    
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
    output_file = 'complete_1_to_11_pals.csv'
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"🎉 완성! 총 {len(combined_df)}개 팰 (1-11번)")
    print(f"📁 파일: {output_file}")
    print(f"✅ 11번 펭킹 완전한 데이터 추가됨!")
    
    # 새로 추가된 팰 확인
    print(f"\n📋 새로 추가된 팰:")
    new_pal = combined_df[combined_df['id'] == '11'].iloc[0]
    print(f"  11: {new_pal['name_kor']} ({new_pal['elements']})")
    print(f"     파트너 스킬: {new_pal['partnerSkill_name']}")
    print(f"     희귀도: {new_pal['stats_rarity']}, 사이즈: {new_pal['stats_size']}")
    print(f"     액티브 스킬: {new_pal['activeSkills_count']}개")
    print(f"     작업 적성: {new_pal['workSuitabilities_count']}개")

if __name__ == "__main__":
    main() 