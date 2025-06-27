#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_vixy_data():
    # 14번 미호 기본 정보
    vixy_data = {
        'id': 14,
        'name_kor': '미호',
        'description_kor': '팰파고스섬의 아이돌. 미호를 괴롭히면 전 세계가 적으로 돌변한다.',
        'elements': '무속성',
        
        # Partner Skill
        'partnerSkill_name': '여기를 파자',
        'partnerSkill_describe': '가축 목장에 배치하면 지면에서 아이템을 파내기도 한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 2,
        'stats_health': 70,
        'stats_food': 100,
        'stats_meleeAttack': 70,
        'stats_attack': 70,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 140,
        'stats_captureRateCorrect': 1.3,
        'stats_maleProbability': 50,
        'stats_combiRank': 1450,
        'stats_goldCoin': 1000,
        'stats_egg': '평범한 알',
        'stats_code': 'CuteFox',
        
        # Movement
        'movement_slowWalkSpeed': 30,
        'movement_walkSpeed': 60,
        'movement_runSpeed': 350,
        'movement_rideSprintSpeed': 450,
        'movement_transportSpeed': 190,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '391-493',
        
        # Active Skills
        'activeSkills': 'Lv.1 공기 대포(무속성, 25파워, 2초) | Lv.7 모래 돌풍(땅 속성, 40파워, 4초) | Lv.15 파워 샷(무속성, 35파워, 4초) | Lv.22 바람의 칼날(풀 속성, 30파워, 2초) | Lv.30 씨앗 기관총(풀 속성, 50파워, 9초) | Lv.40 파워 폭탄(무속성, 70파워, 15초) | Lv.50 팰 폭발(무속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '가죽(1, 100%) | 뼈(1, 100%)',
        'drops_count': 2,
        
        # Work Suitabilities
        'workSuitabilities': '채집(LV.1) | 목장(LV.1)',
        'workSuitabilities_count': 2,
        
        # Tribes
        'tribes': '초원의 아이돌 미호 | 미호',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '미호(Lv. 3-6, 1_4_plain_fox) | 초원의 아이돌 미호(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 미호(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 미호(Lv. 1-10, Captured Cage: Grass) | 미호(Lv. 15-25, Captured Cage: Forest1)',
        'spawners_count': 5
    }
    
    return [vixy_data]

def add_vixy_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_13B_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_vixy_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_14_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 14번 미호가 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_vixy_to_csv() 