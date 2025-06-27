#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_teafant_data():
    # 16번 차코리 기본 정보
    teafant_data = {
        'id': 16,
        'name_kor': '차코리',
        'description_kor': '코로 추정되는 기관에서 대량의 물이 나오는데 그냥 콧물이라는 지적도 있다. 연구자들 사이에 열띤 토론이 한창이다.',
        'elements': '물',
        
        # Partner Skill
        'partnerSkill_name': '치유의 샤워',
        'partnerSkill_describe': '발동하면 상처에 잘 듣는 신비한 물을 뿜어 플레이어의 HP를 회복한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'M',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 150,
        'stats_meleeAttack': 70,
        'stats_attack': 60,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.3,
        'stats_maleProbability': 50,
        'stats_combiRank': 1490,
        'stats_goldCoin': 1000,
        'stats_egg': '축축한 알',
        'stats_code': 'Ganesha',
        
        # Movement
        'movement_slowWalkSpeed': 30,
        'movement_walkSpeed': 60,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 400,
        'movement_transportSpeed': 180,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '392-480',
        'level60_defense': '391-493',
        
        # Active Skills
        'activeSkills': 'Lv.1 아쿠아 샷(물 속성, 40파워, 4초) | Lv.7 워터 제트(물 속성, 30파워, 2초) | Lv.15 모래 돌풍(땅 속성, 40파워, 4초) | Lv.22 버블 샷(물 속성, 65파워, 13초) | Lv.30 산성비(물 속성, 80파워, 18초) | Lv.40 물폭탄(물 속성, 100파워, 30초) | Lv.50 하이드로 스트림(물 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '팰의 체액(1, 100%)',
        'drops_count': 1,
        
        # Work Suitabilities
        'workSuitabilities': '관개(LV.1)',
        'workSuitabilities_count': 1,
        
        # Tribes
        'tribes': '편리한 물뿌리개 차코리 | 차코리',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '차코리(Lv. 1-4, 1_2_plain_grass) | 차코리(Lv. 2-4, 1_3_water) | 차코리(Lv. 2-5, PvP_21_2_1) | 편리한 물뿌리개 차코리(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 차코리(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 차코리(Lv. 15-25, Captured Cage: Forest1)',
        'spawners_count': 6
    }
    
    return [teafant_data]

def add_teafant_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_15_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_teafant_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_16_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 16번 차코리가 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_teafant_to_csv() 