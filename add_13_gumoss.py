#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_gumoss_data():
    # 13번 초롱이 기본 정보
    gumoss_data = {
        'id': 13,
        'name_kor': '초롱이',
        'description_kor': '수액 같은 몸을 가진 신기한 팰. 뒤집어쓸 게 없으면 서서히 말라가다가 결국 썩어서 없어진다.',
        'elements': '풀,땅',
        
        # Partner Skill
        'partnerSkill_name': '나무꾼의 지원',
        'partnerSkill_describe': '보유하고 있는 동안 플레이어가 벌목할 때 피해량이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 100,
        'stats_meleeAttack': 100,
        'stats_attack': 70,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.3,
        'stats_maleProbability': 50,
        'stats_combiRank': 1240,
        'stats_goldCoin': 1310,
        'stats_egg': '신록의 알',
        'stats_code': 'PlantSlime',
        
        # Movement
        'movement_slowWalkSpeed': 50,
        'movement_walkSpeed': 50,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 400,
        'movement_transportSpeed': 175,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '391-493',
        
        # Active Skills
        'activeSkills': 'Lv.1 모래 돌풍(땅 속성, 40파워, 4초) | Lv.7 바람의 칼날(풀 속성, 30파워, 2초) | Lv.15 바위 폭발(땅 속성, 55파워, 10초) | Lv.22 씨앗 기관총(풀 속성, 50파워, 9초) | Lv.30 씨앗 지뢰(풀 속성, 65파워, 13초) | Lv.40 모래 폭풍(땅 속성, 80파워, 18초) | Lv.50 태양 폭발(풀 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops
        'drops': '열매 씨(1, 100%) | 초롱이 잎사귀(1, 50%)',
        'drops_count': 2,
        
        # Work Suitabilities
        'workSuitabilities': '파종(LV.1)',
        'workSuitabilities_count': 1,
        
        # Tribes
        'tribes': '갑자기 변이한 초롱이 | 초롱이',
        'tribes_count': 2,
        
        # Spawners
        'spawners': '초롱이(Lv. 3-5, 1_3_plain_kitsunbi) | 초롱이(Lv. 12-14, 1_15_plain_mopking) | 초롱이(Lv. 2-5, PvP_21_1_1) | 갑자기 변이한 초롱이(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 초롱이(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴)',
        'spawners_count': 5
    }
    
    # 13B 변종 정보
    gumoss_b_data = {
        'id': '13B',
        'name_kor': '초롱이',
        'description_kor': '수액 같은 몸을 가진 신기한 팰. 뒤집어쓸 게 없으면 서서히 말라가다가 결국 썩어서 없어진다.',
        'elements': '풀,땅',
        
        # Partner Skill
        'partnerSkill_name': '나무꾼의 지원',
        'partnerSkill_describe': '보유하고 있는 동안 플레이어가 벌목할 때 피해량이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        
        # Stats
        'stats_size': 'XS',
        'stats_rarity': 10,
        'stats_health': 70,
        'stats_food': 100,
        'stats_meleeAttack': 100,
        'stats_attack': 70,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.3,
        'stats_maleProbability': 50,
        'stats_combiRank': 1240,
        'stats_goldCoin': 1310,
        'stats_egg': '신록의 거대한 알',
        'stats_code': 'PlantSlime_Flower',
        
        # Movement
        'movement_slowWalkSpeed': 50,
        'movement_walkSpeed': 50,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 400,
        'movement_transportSpeed': 175,
        
        # Level 60 stats
        'level60_health': '3100-3782',
        'level60_attack': '441-543',
        'level60_defense': '391-493',
        
        # Active Skills
        'activeSkills': 'Lv.1 모래 돌풍(땅 속성, 40파워, 4초) | Lv.7 바람의 칼날(풀 속성, 30파워, 2초) | Lv.15 바위 폭발(땅 속성, 55파워, 10초) | Lv.22 씨앗 기관총(풀 속성, 50파워, 9초) | Lv.30 씨앗 지뢰(풀 속성, 65파워, 13초) | Lv.40 모래 폭풍(땅 속성, 80파워, 18초) | Lv.50 태양 폭발(풀 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        
        # Passive Skills
        'passiveSkills': '',
        'passiveSkills_count': 0,
        
        # Drops (B 변종은 예쁜 꽃 추가)
        'drops': '열매 씨(1, 100%) | 예쁜 꽃(3, 100%) | 초롱이 잎사귀(1, 50%)',
        'drops_count': 3,
        
        # Work Suitabilities
        'workSuitabilities': '파종(LV.1)',
        'workSuitabilities_count': 1,
        
        # Tribes
        'tribes': '갑자기 변이한 초롱이 | 초롱이',
        'tribes_count': 2,
        
        # Spawners (B 변종은 제한적)
        'spawners': '초롱이(Lv. 3-5, 1_3_plain_kitsunbi) | 초롱이(Lv. 12-14, 1_15_plain_mopking) | 초롱이(Lv. 2-5, PvP_21_1_1)',
        'spawners_count': 3
    }
    
    return [gumoss_data, gumoss_b_data]

def add_gumoss_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_12B_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_gumoss_data()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_13B_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 13번 초롱이와 13B 변종이 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_gumoss_to_csv() 