#!/usr/bin/env python3

import csv
from pathlib import Path

def create_pal_data():
    """57-60번 팰 데이터 생성 - 실제 CSV 필드명에 맞춤"""
    
    # 57번 빙호 (Foxcicle)
    foxcicle = {
        'id': 57,
        'name_kor': '빙호',
        'description_kor': '오로라가 보이는 밤이면 하늘을 올려다보며 아름다운 목소리로 노래를 시작한다. 다만 그 탓에 적에게 자주 공격당한다.',
        'elements': 'Ice',
        'partnerSkill_name': '오로라의 인도',
        'partnerSkill_describe': '보유하고 있는 동안 얼음 속성 팰의 공격력이 증가한다.',
        'partnerSkill_needItem': '',
        'partnerSkill_needItemTechLevel': '',
        'partnerSkill_level': '',
        'stats_size': 'S',
        'stats_rarity': 5,
        'stats_health': 90,
        'stats_food': 3,
        'stats_meleeAttack': 95,
        'stats_attack': 95,
        'stats_defense': 105,
        'stats_workSpeed': 100,
        'stats_support': '',
        'stats_captureRateCorrect': '',
        'stats_maleProbability': '',
        'stats_combiRank': 760,
        'stats_goldCoin': '',
        'stats_egg': '',
        'stats_code': 'Foxcicle',
        'movement_slowWalkSpeed': '',
        'movement_walkSpeed': 130,
        'movement_runSpeed': 600,
        'movement_rideSprintSpeed': 0,
        'movement_transportSpeed': '',
        'level60_health': '3750-4627',
        'level60_attack': '563-702',
        'level60_defense': '561-715',
        'activeSkills': '공기 대포, 얼음 미사일, 얼음 칼날, 유령의 불꽃, 빙산, 서리 낀 입김, 눈보라 스파이크',
        'activeSkills_count': 7,
        'passiveSkills': '',
        'passiveSkills_count': 0,
        'drops': 'Leather x1, Ice Organ x2-3',
        'drops_count': 2,
        'workSuitabilities': 'Cooling Lv2',
        'workSuitabilities_count': 1,
        'tribes': '',
        'tribes_count': 0,
        'spawners': 'Northern ice regions, Frozen areas',
        'spawners_count': 2
    }
    
    # 58번 파이린 (Pyrin)
    pyrin = {
        'id': 58,
        'name_kor': '파이린',
        'description_kor': '전신이 고효율의 방열 기관이 되어 경이적인 지구력을 발휘한다. 누가 올라타면 화상을 입지 않도록 배려해준다.',
        'elements': 'Fire',
        'partnerSkill_name': '적토마',
 