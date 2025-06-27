#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_depresso_data():
    # 17번 뚱코알라 기본 정보
    depresso_data = {
        'id': 17,
        'name_kor': '뚱코알라',
        'description_kor': '눈빛이 안 좋아 친구는 적지만 마음은 따뜻하다. 무리와 떨어진 미호에게 먹이를 나눠주는 모습이 목격되고 있다.',
        'elements': '어둠',
        
        # Partner Skill
        'partnerSkill_name': '카페인 수혈',
        'partnerSkill_describe': '발동하면 뚱코알라가 자양강장제를 대량 섭취하여 일정 시간 뚱코알라의 이동 속도가 크게 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 150,
        'stats_meleeAttack': 70,
        'stats_attack': 70,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1380,
        'stats_goldCoin': 1050,
        'stats_egg': '암흑의 알',
        'stats_code': 'NegativeKoala',
        
        # Movement
        'movement_slowWalkSpeed': 20,
        'movement_walkSpeed': 20,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 400,
        'movement_transportSpeed': 100,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '391-493',
        
        # Active Skills
        'activeSkills': 'Lv.1 독 사격(어둠 속성, 30파워, 2초) | Lv.7 모래 돌풍(땅 속성, 40파워, 4초) | Lv.15 암흑구(어둠 속성, 40파워, 4초) | Lv.22 얼음 미사일(얼음 속성, 30파워, 3초) | Lv.30 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '독샘(2-3, 100%)',
        'drops_count': 1,
        
        # Work Suitabilities
        'workSuitabilities': '수작업(LV.1) | 채굴(LV.1) | 운반(LV.1)',
        'workSuitabilities_count': 3,
        
        # Tribes
        'tribes': '3일 밤을 뜬 눈으로 지샌 뚱코알라 | 뚱코알라',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '뚱코알라(Lv. 3-6, 1_2_plain_grass) | 뚱코알라(Lv. 3-6, 1_3_plain_kitsunbi) | 뚱코알라(Lv. 3-6, 1_4_plain_fox) | 뚱코알라(Lv. 3-7, 1_5_plain_pachiguri) | 뚱코알라(Lv. 3-7, 1_3_water) | 뚱코알라(Lv. 8-12, 1_6_plain_Kirin) | 뚱코알라(Lv. 13-14, 1_7_plain_Pekodon) | 뚱코알라(Lv. 3-7, PvP_21_1_1) | 뚱코알라(Lv. 4-6, PvP_21_2_1) | 3일 밤을 뜬 눈으로 지샌 뚱코알라(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 뚱코알라(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 뚱코알라(Lv. 40-45, sakurajima_6_4_Grave) | 뚱코알라(암흑의 알, Sakurajima_grade_01) | 뚱코알라(Lv. 30-35, Captured Cage: Sakurajima1) | 뚱코알라(Lv. 50-50, 습격 25-99)',
        'spawners_count': 15
    }
    
    return [depresso_data]

def add_depresso_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_16_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_depresso_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_17_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 17번 뚱코알라가 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_depresso_to_csv() 