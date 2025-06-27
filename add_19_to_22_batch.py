#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_batch_19_to_22():
    pals_data = []
    
    # 19번 몽마둥이
    daedream_data = {
        'id': 19,
        'name_kor': '몽마둥이',
        'description_kor': '마음에 드는 상대를 깊은 잠에 빠뜨려 행복한 꿈을 꾸게 해준다. 죽을 때까지 잠에서 깰 일은 절대 없다.',
        'elements': '어둠',
        'partnerSkill_name': '꿈빛 체이서',
        'partnerSkill_describe': '보유하고 있는 동안 플레이어 가까이에 출현한다. 플레이어의 공격에 맞춰 마탄으로 추격한다.',
        'partnerSkill_needItem': '몽마둥이의 목걸이',
        'partnerSkill_needItemTechLevel': '8',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 225,
        'stats_meleeAttack': 100,
        'stats_attack': 75,
        'stats_defense': 60,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1230,
        'stats_goldCoin': 1330,
        'stats_egg': '암흑의 알',
        'stats_code': 'DreamDemon',
        'movement_slowWalkSpeed': 70,
        'movement_walkSpeed': 140,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 550,
        'movement_transportSpeed': 220,
        'level60_health': '3100-3782',
        'level60_attack': '465-575',
        'level60_defense': '342-430',
        'activeSkills': 'Lv.1 암흑구(어둠 속성, 40파워, 4초) | Lv.7 독 사격(어둠 속성, 30파워, 2초) | Lv.15 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.22 서리 낀 입김(얼음 속성, 90파워, 22초) | Lv.30 유령의 불꽃(어둠 속성, 75파워, 16초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '독샘(1, 100%) | 작은 팰 영혼(1, 1%)',
        'drops_count': 2,
        'workSuitabilities': '수작업(LV.1) | 채집(LV.1) | 운반(LV.1)',
        'workSuitabilities_count': 3,
        'tribes': '꿈 포식자 몽마둥이 | 몽마둥이',
        'tribes_count': 2,
        'spawners': '몽마둥이(Lv. 4-7, 1_1_plain_begginer) | 몽마둥이(Lv. 3-6, 1_3_plain_kitsunbi) | 몽마둥이(Lv. 3-6, 1_4_plain_fox) | 몽마둥이(Lv. 3-7, 1_5_plain_pachiguri) | 몽마둥이(Lv. 4-6, PvP_21_2_1) | 몽마둥이(Lv. 5-10, 구릉 동굴, 외딴 섬의 동굴) | 꿈 포식자 몽마둥이(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 몽마둥이(Lv. 12-15, 계곡의 동굴) | 몽마둥이(Lv. 5-10, 구릉 동굴) | 몽마둥이(암흑의 알, grass_grade_01)',
        'spawners_count': 10
    }
    
    # 20번 돌진돼지
    rushoar_data = {
        'id': 20,
        'name_kor': '돌진돼지',
        'description_kor': '굉장히 호전적으로 힘 차이를 계산한 뒤 상대에게 달려든다. 몸집이 작은 팰이지만, 무시무시한 돌진력은 큰 바위도 날릴 기세다.',
        'elements': '땅',
        'partnerSkill_name': '돌대가리',
        'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 바위 파괴 효율이 향상된다.',
        'partnerSkill_needItem': '돌진돼지의 안장',
        'partnerSkill_needItemTechLevel': '6',
        'partnerSkill_level': '1',
        'stats_size': 'S',
        'stats_rarity': 1,
        'stats_health': 80,
        'stats_food': 225,
        'stats_meleeAttack': 100,
        'stats_attack': 70,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1130,
        'stats_goldCoin': 1680,
        'stats_egg': '거친 느낌의 알',
        'stats_code': 'Boar',
        'movement_slowWalkSpeed': 70,
        'movement_walkSpeed': 150,
        'movement_runSpeed': 500,
        'movement_rideSprintSpeed': 800,
        'movement_transportSpeed': 300,
        'level60_health': '3425-4205',
        'level60_attack': '441-543',
        'level60_defense': '391-493',
        'activeSkills': 'Lv.1 멧돼지 돌진(무속성, 55파워, 2초) | Lv.7 모래 돌풍(땅 속성, 40파워, 4초) | Lv.15 파워 샷(무속성, 35파워, 4초) | Lv.22 바위 폭발(땅 속성, 55파워, 10초) | Lv.30 파워 폭탄(무속성, 70파워, 15초) | Lv.40 바위 창(땅 속성, 150파워, 55초) | Lv.50 팰 폭발(무속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '돌진돼지의 살코기(1-2, 100%) | 가죽(1, 100%) | 뼈(1, 100%)',
        'drops_count': 3,
        'workSuitabilities': '채굴(LV.1)',
        'workSuitabilities_count': 1,
        'tribes': '숲의 무법자 돌진돼지 | 돌진돼지',
        'tribes_count': 2,
        'spawners': '돌진돼지(Lv. 3-6, 1_4_plain_fox) | 돌진돼지(Lv. 2-5, PvP_21_1_1) | 돌진돼지(Lv. 2-5, PvP_21_2_1) | 숲의 무법자 돌진돼지(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 돌진돼지(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 돌진돼지(Lv. 15-25, Captured Cage: Forest1)',
        'spawners_count': 6
    }
    
    # 21번 루나티
    nox_data = {
        'id': 21,
        'name_kor': '루나티',
        'description_kor': '밤길에 루나티의 털을 발견했다면 줍지 말고 그대로 두는 게 좋다. 그 털은 밝지 않는 밤으로 향하는 편도 티켓이다.',
        'elements': '어둠',
        'partnerSkill_name': '쿨한 새침데기',
        'partnerSkill_describe': '함께 싸우는 동안 플레이어의 공격이 어둠 속성으로 변화한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': 6,
        'stats_health': 75,
        'stats_food': 150,
        'stats_meleeAttack': 70,
        'stats_attack': 85,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 140,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1180,
        'stats_goldCoin': 1480,
        'stats_egg': '암흑의 대형 알',
        'stats_code': 'NightFox',
        'movement_slowWalkSpeed': 30,
        'movement_walkSpeed': 60,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 500,
        'movement_transportSpeed': 164,
        'level60_health': '3262-3993',
        'level60_attack': '514-638',
        'level60_defense': '391-493',
        'activeSkills': 'Lv.1 공기 대포(무속성, 25파워, 2초) | Lv.7 암흑구(어둠 속성, 40파워, 4초) | Lv.15 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.22 파워 폭탄(무속성, 70파워, 15초) | Lv.30 유령의 불꽃(어둠 속성, 75파워, 16초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '가죽(1, 100%) | 작은 팰 영혼(1, 40%)',
        'drops_count': 2,
        'workSuitabilities': '채집(LV.1)',
        'workSuitabilities_count': 1,
        'tribes': '밤의 귀공자 루나티 | 루나티',
        'tribes_count': 2,
        'spawners': '루나티(Lv. 5-7, 1_1_plain_begginer) | 루나티(Lv. 5-7, 1_2_plain_grass) | 루나티(Lv. 5-6, 1_3_plain_kitsunbi) | 루나티(Lv. 5-6, 1_4_plain_fox) | 루나티(Lv. 11-12, 1_5_plain_pachiguri) | 루나티(Lv. 3-7, PvP_21_1_1) | 루나티(Lv. 3-7, PvP_21_2_1) | 루나티(Lv. 12-15, 계곡의 동굴) | 밤의 귀공자 루나티(Lv. 17-19, 계곡의 동굴) | 루나티(암흑의 대형 알, grass_grade_01) | 루나티(Lv. 1-10, Captured Cage: Grass) | 루나티(Lv. 10-20, Captured Cage: Grass2) | 루나티(Lv. 15-25, Captured Cage: Forest1)',
        'spawners_count': 13
    }
    
    # 22번 두더비
    fuddler_data = {
        'id': 22,
        'name_kor': '두더비',
        'description_kor': '커다란 발톱은 다이아몬드처럼 단단하지만 발톱 손질에 힘을 너무 쏟은 나머지 그대로 지쳐 하루를 마감하기도 한다.',
        'elements': '땅',
        'partnerSkill_name': '광석 탐지',
        'partnerSkill_describe': '발동하면 미세한 진동을 발신해 가까이 있는 광석의 위치를 탐지할 수 있다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 65,
        'stats_food': 150,
        'stats_meleeAttack': 100,
        'stats_attack': 80,
        'stats_defense': 50,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1220,
        'stats_goldCoin': 1360,
        'stats_egg': '거친 느낌의 알',
        'stats_code': 'CuteMole',
        'movement_slowWalkSpeed': 30,
        'movement_walkSpeed': 60,
        'movement_runSpeed': 300,
        'movement_rideSprintSpeed': 550,
        'movement_transportSpeed': 240,
        'level60_health': '2937-3571',
        'level60_attack': '490-607',
        'level60_defense': '293-366',
        'activeSkills': 'Lv.1 모래 돌풍(땅 속성, 40파워, 4초) | Lv.7 파워 샷(무속성, 35파워, 4초) | Lv.15 바위 폭발(땅 속성, 55파워, 10초) | Lv.22 바위 대포(땅 속성, 70파워, 15초) | Lv.30 파워 폭탄(무속성, 70파워, 15초) | Lv.40 모래 폭풍(땅 속성, 80파워, 18초) | Lv.50 바위 창(땅 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '가죽(1-2, 100%)',
        'drops_count': 1,
        'workSuitabilities': '수작업(LV.1) | 채굴(LV.1) | 운반(LV.1)',
        'workSuitabilities_count': 3,
        'tribes': '땅속의 탐구자 두더비 | 두더비',
        'tribes_count': 2,
        'spawners': '두더비(Lv. 14-17, 1_8_plain_dessert) | 두더비(Lv. 24-30, 4_2_dessert_1) | 두더비(Lv. 5-10, 구릉 동굴, 외딴 섬의 동굴) | 땅속의 탐구자 두더비(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 두더비(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 두더비(Lv. 12-15, 계곡의 동굴) | 두더비(Lv. 30-34, 화산 동굴) | 땅속의 탐구자 두더비(Lv. 37-40, 모래 언덕 동굴, 화산 동굴) | 두더비(Lv. 33-36, 모래 언덕 동굴, 화산 동굴) | 두더비(Lv. 5-10, 구릉 동굴) | 두더비(거친 느낌의 알, grass_grade_01) | 두더비(거친 느낌의 알, desert_grade_01) | 두더비(Lv. 1-10, Captured Cage: Grass) | 두더비(Lv. 20-30, Captured Cage: Desert1)',
        'spawners_count': 14
    }
    
    pals_data.extend([daedream_data, rushoar_data, nox_data, fuddler_data])
    return pals_data

def add_batch_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_18_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_batch_19_to_22()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_22_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 19-22번 팰들이 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_batch_to_csv() 