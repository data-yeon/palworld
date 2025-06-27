#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_hoocrates_data():
    # 15번 아테노울 기본 정보
    hoocrates_data = {
        'id': 15,
        'name_kor': '아테노울',
        'description_kor': '근심에 잠기는 경우가 많아 머릿속이 복잡해 잠을 잘 자지 못한다. \'나는 생각한다, 고로 존재한다\'',
        'elements': '어둠',
        
        # Partner Skill
        'partnerSkill_name': '어둠의 예지',
        'partnerSkill_describe': '보유하고 있는 동안 어둠 속성 팰의 공격력이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 225,
        'stats_meleeAttack': 70,
        'stats_attack': 70,
        'stats_defense': 80,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1390,
        'stats_goldCoin': 1050,
        'stats_egg': '암흑의 알',
        'stats_code': 'WizardOwl',
        
        # Movement
        'movement_slowWalkSpeed': 26,
        'movement_walkSpeed': 70,
        'movement_runSpeed': 380,
        'movement_rideSprintSpeed': 550,
        'movement_transportSpeed': 225,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '440-557',
        
        # Active Skills
        'activeSkills': 'Lv.1 공기 대포(무속성, 25파워, 2초) | Lv.7 암흑구(어둠 속성, 40파워, 4초) | Lv.15 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.22 모래 폭풍(땅 속성, 80파워, 18초) | Lv.30 유령의 불꽃(어둠 속성, 75파워, 16초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '섬유(5-10, 100%) | 고도의 기술서(1, 1%)',
        'drops_count': 2,
        
        # Work Suitabilities
        'workSuitabilities': '채집(LV.1)',
        'workSuitabilities_count': 1,
        
        # Tribes
        'tribes': '지혜의 전도사 아테노울 | 아테노울',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '아테노울(Lv. 4-7, 1_1_plain_begginer) | 아테노울(Lv. 3-6, 1_2_plain_grass) | 아테노울(Lv. 3-6, 1_3_plain_kitsunbi) | 아테노울(Lv. 3-6, 1_4_plain_fox) | 아테노울(Lv. 3-7, 1_5_plain_pachiguri) | 아테노울(Lv. 3-7, 1_3_water) | 아테노울(Lv. 11-12, 1_3_water) | 아테노울(Lv. 8-12, 1_6_plain_Kirin) | 아테노울(Lv. 13-14, 1_7_plain_Pekodon) | 아테노울(Lv. 3-7, PvP_21_1_1) | 지혜의 전도사 아테노울(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 아테노울(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴)',
        'spawners_count': 12
    }
    
    return [hoocrates_data]

def add_hoocrates_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_14_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_hoocrates_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_15_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 15번 아테노울이 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_hoocrates_to_csv() 