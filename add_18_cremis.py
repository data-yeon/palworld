#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_cremis_data():
    # 18번 밀피 기본 정보
    cremis_data = {
        'id': 18,
        'name_kor': '밀피',
        'description_kor': '도로롱보다 털의 품질이 좋고 도로롱보다 가축으로 삼기 좋은 성격이다. 하지만 역사적으로는 항상 애완용 팰로 사육되어 왔다. 역시 귀여운 게 최고다.',
        'elements': '무속성',
        
        # Partner Skill
        'partnerSkill_name': '푹신푹신 양털',
        'partnerSkill_describe': '보유하고 있는 동안 무속성 팰의 공격력이 증가한다. 가축 목장에 배치하면 양털을 떨어뜨리기도 한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 150,
        'stats_meleeAttack': 100,
        'stats_attack': 70,
        'stats_defense': 75,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.3,
        'stats_maleProbability': 50,
        'stats_combiRank': 1455,
        'stats_goldCoin': 1420,
        'stats_egg': '평범한 알',
        'stats_code': 'WoolFox',
        
        # Movement
        'movement_slowWalkSpeed': 20,
        'movement_walkSpeed': 40,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 450,
        'movement_transportSpeed': 170,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '415-525',
        
        # Active Skills
        'activeSkills': 'Lv.1 공기 대포(무속성, 25파워, 2초) | Lv.7 모래 돌풍(땅 속성, 40파워, 4초) | Lv.15 스파크 샷(번개 속성, 30파워, 2초) | Lv.22 파워 샷(무속성, 35파워, 4초) | Lv.30 전기 파장(번개 속성, 40파워, 4초) | Lv.40 파워 폭탄(무속성, 70파워, 15초) | Lv.50 전기 볼트(번개 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '양털(1-2, 100%)',
        'drops_count': 1,
        
        # Work Suitabilities
        'workSuitabilities': '채집(LV.1) | 목장(LV.1)',
        'workSuitabilities_count': 2,
        
        # Tribes
        'tribes': '너무나 사랑스러운 털 뭉치 밀피 | 밀피',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '밀피(Lv. 2-4, 1_3_plain_kitsunbi) | 밀피(Lv. 2-4, 1_4_plain_fox) | 밀피(Lv. 12-14, 1_15_plain_mopking) | 밀피(Lv. 2-5, PvP_21_1_1) | 너무나 사랑스러운 털 뭉치 밀피(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 밀피(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴)',
        'spawners_count': 6
    }
    
    return [cremis_data]

def add_cremis_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_17_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_cremis_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_18_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 18번 밀피가 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_cremis_to_csv() 