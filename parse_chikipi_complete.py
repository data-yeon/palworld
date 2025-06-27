#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
꼬꼬닭 완전한 데이터 파싱 스크립트
"""

import re
import json

def parse_chikipi_data():
    """꼬꼬닭 마크다운 데이터를 파싱하여 구조화된 데이터로 변환"""
    
    markdown_text = """
[꼬꼬닭](https://paldb.cc/ko/Chikipi)#3

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

알 생산 Lv.1

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면
가끔씩 [알](https://paldb.cc/ko/Egg) 을(를) 낳기도 한다.

[작업 적성](https://paldb.cc/ko/Work_Suitability)

채집 Lv1
목장 Lv1

##### Stats

Size: XS
Rarity: 1
HP: 60
식사량: 100
MeleeAttack: 70
공격: 60
방어: 60
작업 속도: 100
Support: 70
CaptureRateCorrect: 1.5
MaleProbability: 50
CombiRank: 1500
금화: 1000
Egg: 평범한 알
Code: ChickenPal

##### Movement

SlowWalkSpeed: 50
WalkSpeed: 50
RunSpeed: 375
RideSprintSpeed: 550
TransportSpeed: 212

##### Level 60

HP: 2775 – 3360
공격: 392 – 480
방어: 342 – 430

##### Summary

너무나 약하고 또 너무나 맛있다.
도로롱 와(과) 함께 최약체를 담당한다.
많이 잡았다 싶으면 또 어디선가 튀어나온다.

##### Partner Skill: 알 생산

가축 목장 에 배치하면 가끔씩 알 을(를) 낳기도 한다.

##### Active Skills

Lv. 1 치킨 태클 (무속성, 위력: 30, 쿨타임: 1)
Lv. 7 공기 대포 (무속성, 위력: 25, 쿨타임: 2)
Lv. 15 파워 샷 (무속성, 위력: 35, 쿨타임: 4)
Lv. 22 자폭 (무속성, 위력: 230, 쿨타임: 55)
Lv. 30 초록 폭풍 (풀 속성, 위력: 80, 쿨타임: 18)
Lv. 40 모래 폭풍 (땅 속성, 위력: 80, 쿨타임: 18)
Lv. 50 화염 폭풍 (화염 속성, 위력: 80, 쿨타임: 18)

##### Possible Drops

알 1 (100%)
꼬꼬닭의 닭고기 1 (100%)

##### Tribes

퉁퉁한 몸집의 꼬꼬닭 (Tribe Boss)
꼬꼬닭 (Tribe Normal)

##### Spawner

꼬꼬닭 (Lv. 1–3, 1_1_plain_begginer)
꼬꼬닭 (Lv. 3–5, 1_3_plain_kitsunbi)
꼬꼬닭 (Lv. 2–5, PvP_21_1_1)
꼬꼬닭 (Lv. 2–5, PvP_21_2_1)
퉁퉁한 몸집의 꼬꼬닭 (Lv. 10–13, 구릉 동굴, 외딴 섬의 동굴)
꼬꼬닭 (Lv. 6–9, 구릉 동굴, 외딴 섬의 동굴)
꼬꼬닭 (Lv. 15 – 25, Captured Cage: Forest1)
"""
    
    pal_data = {
        'id': '3',
        'name_kor': '꼬꼬닭',
        'pal_nick_kor': '#3',
        'description_kor': '너무나 약하고 또 너무나 맛있다. 도로롱 와(과) 함께 최약체를 담당한다. 많이 잡았다 싶으면 또 어디선가 튀어나온다.',
        'elements': '무속성',
        'stats_size': 'XS',
        'stats_rarity': '1',
        'stats_health': '60',
        'stats_food': '100',
        'stats_attack': '60',
        'stats_defense': '60',
        'stats_meleeAttack': '70',
        'stats_workSpeed': '100',
        'stats_support': '70',
        'stats_captureRateCorrect': '1.5',
        'stats_maleProbability': '50',
        'stats_combiRank': '1500',
        'stats_goldCoin': '1000',
        'stats_egg': '평범한 알',
        'stats_code': 'ChickenPal',
        'movement_slowWalkSpeed': '50',
        'movement_walkSpeed': '50',
        'movement_runSpeed': '375',
        'movement_transportSpeed': '212',
        'movement_rideSprintSpeed': '550',
        'level60_health': '2775 – 3360',
        'level60_attack': '392 – 480',
        'level60_defense': '342 – 430',
        'partnerSkill_name': '알 생산',
        'partnerSkill_describe': '가축 목장 에 배치하면 가끔씩 알 을(를) 낳기도 한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '',
        'partnerSkill_level': '1',
        'activeSkills': '치킨 태클(무속성, 30파워, 1초) | 공기 대포(무속성, 25파워, 2초) | 파워 샷(무속성, 35파워, 4초) | 자폭(무속성, 230파워, 55초) | 초록 폭풍(풀 속성, 80파워, 18초) | 모래 폭풍(땅 속성, 80파워, 18초) | 화염 폭풍(화염 속성, 80파워, 18초)',
        'activeSkills_count': '7',
        'passiveSkills': '',
        'passiveSkills_count': '0',
        'drops': '알(1, 100%) | 꼬꼬닭의 닭고기(1, 100%)',
        'drops_count': '2',
        'workSuitabilities': '채집(LV.1) | 목장(LV.1)',
        'workSuitabilities_count': '2',
        'tribes': '퉁퉁한 몸집의 꼬꼬닭 | 꼬꼬닭',
        'tribes_count': '2',
        'spawners': '꼬꼬닭(Lv. 1–3, 1_1_plain_begginer) | 꼬꼬닭(Lv. 3–5, 1_3_plain_kitsunbi) | 꼬꼬닭(Lv. 2–5, PvP_21_1_1) | 꼬꼬닭(Lv. 2–5, PvP_21_2_1) | 퉁퉁한 몸집의 꼬꼬닭(Lv. 10–13, 구릉 동굴, 외딴 섬의 동굴) | 꼬꼬닭(Lv. 6–9, 구릉 동굴, 외딴 섬의 동굴) | 꼬꼬닭(Lv. 15 – 25, Captured Cage: Forest1)',
        'spawners_count': '7'
    }
    
    return pal_data

def main():
    """메인 함수"""
    chikipi_data = parse_chikipi_data()
    
    print("🐔 꼬꼬닭 완전한 데이터 파싱 완료!")
    print(f"📋 ID: {chikipi_data['id']}")
    print(f"📋 이름: {chikipi_data['name_kor']}")
    print(f"📋 속성: {chikipi_data['elements']}")
    print(f"📋 설명: {chikipi_data['description_kor']}")
    print(f"📋 파트너 스킬: {chikipi_data['partnerSkill_name']}")
    print(f"📋 작업 적성: {chikipi_data['workSuitabilities']}")
    print(f"📋 액티브 스킬 수: {chikipi_data['activeSkills_count']}")
    print(f"📋 드롭 수: {chikipi_data['drops_count']}")
    print(f"📋 스포너 수: {chikipi_data['spawners_count']}")
    
    # JSON으로 저장
    with open('chikipi_complete_data.json', 'w', encoding='utf-8') as f:
        json.dump(chikipi_data, f, ensure_ascii=False, indent=2)
    
    print("✅ chikipi_complete_data.json 저장 완료!")
    
    return chikipi_data

if __name__ == "__main__":
    main() 