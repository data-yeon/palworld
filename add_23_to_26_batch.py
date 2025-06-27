#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def parse_batch_23_to_26():
    pals_data = []
    
    # 23번 고스문
    killamari_data = {
        'id': 23,
        'name_kor': '고스문',
        'description_kor': '적에 머리에 달라붙어 내용물을 쪽쪽 빨아먹는다. 팰의 미라가 드물게 발견되는데 대개 고스문에게 희생된 팰이다.',
        'elements': '어둠, 물',
        'partnerSkill_name': '오징어튀김',
        'partnerSkill_describe': '보유하고 있는 동안 글라이더의 성능이 변화한다. 활공 중 느린 속도로 장시간 이동이 가능해진다.',
        'partnerSkill_needItem': '고스문의 장갑',
        'partnerSkill_needItemTechLevel': '9',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 60,
        'stats_food': 225,
        'stats_meleeAttack': 100,
        'stats_attack': 60,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1290,
        'stats_goldCoin': 1200,
        'stats_egg': '암흑의 알',
        'stats_code': 'NegativeOctopus',
        'movement_slowWalkSpeed': 60,
        'movement_walkSpeed': 120,
        'movement_runSpeed': 400,
        'movement_rideSprintSpeed': 550,
        'movement_transportSpeed': 260,
        'level60_health': '2775-3360',
        'level60_attack': '392-480',
        'level60_defense': '391-493',
        'activeSkills': 'Lv.1 워터 제트(물 속성, 30파워, 2초) | Lv.7 독 사격(어둠 속성, 30파워, 2초) | Lv.15 암흑구(어둠 속성, 40파워, 4초) | Lv.22 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.30 산성비(물 속성, 80파워, 18초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '독샘(2-4, 100%) | 고스문의 촉수(1, 50%)',
        'drops_count': 2,
        'workSuitabilities': '관개(LV.1) | 채집(LV.1) | 운반(LV.2)',
        'workSuitabilities_count': 3,
        'tribes': '어떤 감정도 없는 고스문 | 고스문',
        'tribes_count': 2,
        'spawners': '고스문(Lv. 5-10, 구릉 동굴, 외딴 섬의 동굴) | 어떤 감정도 없는 고스문(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 고스문(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 고스문(Lv. 5-10, 구릉 동굴) | 고스문(Lv. 11-18, 낚시터 Small 9.89%)',
        'spawners_count': 5
    }
    
    # 24번 냐옹테트
    mau_data = {
        'id': 24,
        'name_kor': '냐옹테트',
        'description_kor': '단단한 꼬리 조직은 잘라도 그대로이다. 그 꼬리가 재물을 불러온다는 미신이 성행해 대량의 냐옹테트가 목숨을 잃었다.',
        'elements': '어둠',
        'partnerSkill_name': '금화 수집',
        'partnerSkill_describe': '가축 목장에 배치하면 지면에서 금화를 파내기도 한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '0',
        'partnerSkill_level': '1',
        'stats_size': 'XS',
        'stats_rarity': 1,
        'stats_health': 70,
        'stats_food': 100,
        'stats_meleeAttack': 70,
        'stats_attack': 60,
        'stats_defense': 70,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1480,
        'stats_goldCoin': 1000,
        'stats_egg': '암흑의 알',
        'stats_code': 'Bastet',
        'movement_slowWalkSpeed': 52,
        'movement_walkSpeed': 105,
        'movement_runSpeed': 475,
        'movement_rideSprintSpeed': 550,
        'movement_transportSpeed': 317,
        'level60_health': '3100-3782',
        'level60_attack': '392-480',
        'level60_defense': '391-493',
        'activeSkills': 'Lv.1 모래 돌풍(땅 속성, 40파워, 4초) | Lv.7 암흑구(어둠 속성, 40파워, 4초) | Lv.15 그림자 폭발(어둠 속성, 55파워, 10초) | Lv.22 모래 폭풍(땅 속성, 80파워, 18초) | Lv.30 유령의 불꽃(어둠 속성, 75파워, 16초) | Lv.40 악몽의 구체(어둠 속성, 100파워, 30초) | Lv.50 어둠의 레이저(어둠 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '금화(100-200, 50%)',
        'drops_count': 1,
        'workSuitabilities': '목장(LV.1)',
        'workSuitabilities_count': 1,
        'tribes': '고귀한 광채의 냐옹테트 | 냐옹테트 | 칠테트',
        'tribes_count': 3,
        'spawners': '냐옹테트(Lv. 5-10, 구릉 동굴, 외딴 섬의 동굴) | 고귀한 광채의 냐옹테트(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 냐옹테트(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 냐옹테트(Lv. 12-15, 계곡의 동굴) | 냐옹테트(Lv. 5-10, 구릉 동굴) | 냐옹테트(암흑의 알, grass_grade_02) | 냐옹테트(Lv. 15-25, Captured Cage: Forest1)',
        'spawners_count': 7
    }
    
    # 25번 루미카이트
    celaray_data = {
        'id': 25,
        'name_kor': '루미카이트',
        'description_kor': '바람을 타고 자유로이 여행한다. 도착한 곳에서 파트너를 발견하면 이들의 여행도 끝이 난다.',
        'elements': '물',
        'partnerSkill_name': '실바람 글라이더',
        'partnerSkill_describe': '보유하고 있는 동안 글라이더의 성능이 변화한다. 활공 중 빠른 속도로 장시간 이동이 가능해진다.',
        'partnerSkill_needItem': '루미카이트의 장갑',
        'partnerSkill_needItemTechLevel': '7',
        'partnerSkill_level': '1',
        'stats_size': 'M',
        'stats_rarity': 3,
        'stats_health': 80,
        'stats_food': 225,
        'stats_meleeAttack': 100,
        'stats_attack': 70,
        'stats_defense': 80,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.1,
        'stats_maleProbability': 50,
        'stats_combiRank': 870,
        'stats_goldCoin': 2860,
        'stats_egg': '축축한 알',
        'stats_code': 'FlyingManta',
        'movement_slowWalkSpeed': 30,
        'movement_walkSpeed': 150,
        'movement_runSpeed': 550,
        'movement_rideSprintSpeed': 700,
        'movement_transportSpeed': 350,
        'level60_health': '3425-4205',
        'level60_attack': '441-543',
        'level60_defense': '440-557',
        'activeSkills': 'Lv.1 워터 제트(물 속성, 30파워, 2초) | Lv.7 아쿠아 샷(물 속성, 40파워, 4초) | Lv.15 파워 샷(무속성, 35파워, 4초) | Lv.22 버블 샷(물 속성, 65파워, 13초) | Lv.30 씨앗 기관총(풀 속성, 50파워, 9초) | Lv.40 물폭탄(물 속성, 100파워, 30초) | Lv.50 하이드로 스트림(물 속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '팰의 체액(1-2, 100%)',
        'drops_count': 1,
        'workSuitabilities': '관개(LV.1) | 운반(LV.1)',
        'workSuitabilities_count': 2,
        'tribes': '하늘을 헤엄치는 물고기 루미카이트 | 루미카이트',
        'tribes_count': 2,
        'spawners': '루미카이트(Lv. 2-4, 1_3_water) | 루미카이트(Lv. 9-12, 1_11_plain_Kelpee) | 하늘을 헤엄치는 물고기 루미카이트(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 루미카이트(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 루미카이트(축축한 알, grass_grade_02) | 루미카이트(축축한 알, grass_grade_01) | 루미카이트(Lv. 11-18, 낚시터 Small 9.89%)',
        'spawners_count': 7
    }
    
    # 26번 다크울프
    direhowl_data = {
        'id': 26,
        'name_kor': '다크울프',
        'description_kor': '인간과 접촉이 뜸해진 지 오래지만 다크울프 무리의 수렵 체계는 일찍이 인간과 함께했던 사냥이 그 뿌리다.',
        'elements': '무속성',
        'partnerSkill_name': '질주 본능',
        'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중의 이동 속도가 조금 빠른 것이 특징이다.',
        'partnerSkill_needItem': '다크울프의 마구',
        'partnerSkill_needItemTechLevel': '9',
        'partnerSkill_level': '1',
        'stats_size': 'S',
        'stats_rarity': 2,
        'stats_health': 80,
        'stats_food': 225,
        'stats_meleeAttack': 110,
        'stats_attack': 90,
        'stats_defense': 75,
        'stats_workSpeed': 100,
        'stats_support': 100,
        'stats_captureRateCorrect': 1.0,
        'stats_maleProbability': 50,
        'stats_combiRank': 1060,
        'stats_goldCoin': 1920,
        'stats_egg': '평범한 알',
        'stats_code': 'Garm',
        'movement_slowWalkSpeed': 90,
        'movement_walkSpeed': 180,
        'movement_runSpeed': 800,
        'movement_rideSprintSpeed': 1050,
        'movement_transportSpeed': 460,
        'level60_health': '3425-4205',
        'level60_attack': '538-670',
        'level60_defense': '415-525',
        'activeSkills': 'Lv.1 와일드 팽(무속성, 45파워, 2초) | Lv.7 모래 돌풍(땅 속성, 40파워, 4초) | Lv.15 공기 대포(무속성, 25파워, 2초) | Lv.22 파워 샷(무속성, 35파워, 4초) | Lv.30 파이어 샷(화염 속성, 30파워, 2초) | Lv.40 파워 폭탄(무속성, 70파워, 15초) | Lv.50 팰 폭발(무속성, 150파워, 55초)',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': '가죽(1-2, 100%) | 루비(1, 3%) | 금화(10-20, 3%)',
        'drops_count': 3,
        'workSuitabilities': '채집(LV.1)',
        'workSuitabilities_count': 1,
        'tribes': '초원의 사냥꾼 다크울프 | 다크울프 | 광폭화한 다크울프',
        'tribes_count': 3,
        'spawners': '다크울프(Lv. 5-10, 1_5_plain_pachiguri) | 다크울프(Lv. 10-15, 1_9_plain_SweetsSheep) | 다크울프(Lv. 12-14, 1_15_plain_mopking) | 다크울프(Lv. 4-7, PvP_21_1_1) | 다크울프(Lv. 4-7, PvP_21_2_1) | 초원의 사냥꾼 다크울프(Lv. 10-13, 구릉 동굴, 외딴 섬의 동굴) | 다크울프(Lv. 6-9, 구릉 동굴, 외딴 섬의 동굴) | 다크울프(평범한 알, grass_grade_01) | 다크울프(Lv. 3-3, 습격 6-9)',
        'spawners_count': 9
    }
    
    pals_data.extend([killamari_data, mau_data, celaray_data, direhowl_data])
    return pals_data

def add_batch_to_csv():
    # 기존 CSV 읽기
    existing_data = []
    with open('complete_1_to_22_pals.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새로운 팰 데이터
    new_pals = parse_batch_23_to_26()
    
    # 데이터 추가
    for pal_data in new_pals:
        existing_data.append(pal_data)
    
    # 새 CSV 파일로 저장
    output_filename = 'complete_1_to_26_pals.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ 23-26번 팰들이 성공적으로 추가되었습니다!")
    print(f"📄 파일명: {output_filename}")
    print(f"📊 총 팰 수: {len(existing_data)}개")
    
    # 추가된 팰 정보 출력
    for i, pal in enumerate(new_pals):
        print(f"🔸 {pal['id']}번 {pal['name_kor']} (희귀도: {pal['stats_rarity']}, 속성: {pal['elements']})")

if __name__ == "__main__":
    add_batch_to_csv() 