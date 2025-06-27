#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기존 CSV에 B 변종들을 추가하는 스크립트
5B 아이호, 6B 적부리, 10B 뎅키 추가
"""

import csv
import re

def parse_pal_data_simple(markdown_content, pal_id, pal_name_kor):
    """마크다운 데이터를 간단히 파싱하여 팰 정보 추출"""
    
    data = {
        'id': pal_id,
        'name_kor': pal_name_kor,
        'description_kor': '',
        'elements': '',
        'partner_skill_name': '',
        'partner_skill_describe': '', 
        'partner_skill_need_item': '',
        'partner_skill_need_item_tech_level': '',
        'work_suitabilities': '',
        'work_suitabilities_count': 0,
        'food_amount': '',
        
        # Stats
        'size': '',
        'rarity': '',
        'health': '',
        'food': '',
        'melee_attack': '',
        'attack': '',
        'defense': '',
        'work_speed': '',
        'support': '',
        'capture_rate_correct': '',
        'male_probability': '',
        'combi_rank': '',
        'gold_coin': '',
        'egg': '',
        'code': '',
        
        # Movement
        'slow_walk_speed': '',
        'walk_speed': '',
        'run_speed': '',
        'ride_sprint_speed': '',
        'transport_speed': '',
        
        # Level 60
        'level_60_health': '',
        'level_60_attack': '',
        'level_60_defense': '',
        
        # Active Skills
        'active_skills': '',
        'active_skills_count': 0,
        
        # Passive Skills
        'passive_skills': '',
        'passive_skills_count': 0,
        
        # Drops
        'drops': '',
        'drops_count': 0,
        
        # Tribes
        'tribes': '',
        'tribes_count': 0,
        
        # Spawners
        'spawners': '',
        'spawners_count': 0
    }
    
    # Elements 추출
    elements = re.findall(r'(무속성|화염 속성|물 속성|번개 속성|풀 속성|어둠 속성|용 속성|땅 속성|얼음 속성)', markdown_content)
    data['elements'] = '|'.join(elements) if elements else ''
    
    # Description 추출 (Summary 섹션)
    summary_match = re.search(r'##### Summary\s*\n\n(.+?)(?=\n\n|$)', markdown_content, re.DOTALL)
    if summary_match:
        data['description_kor'] = summary_match.group(1).strip()
    
    # Partner Skill 추출
    partner_skill_match = re.search(r'##### Partner Skill: (.+?)\n', markdown_content)
    if partner_skill_match:
        data['partner_skill_name'] = partner_skill_match.group(1).strip()
    
    # Partner Skill 설명 추출
    partner_desc_match = re.search(r'발동하면.*?(?=\n\n|\n#+|$)', markdown_content, re.DOTALL)
    if partner_desc_match:
        data['partner_skill_describe'] = partner_desc_match.group(0).strip()
    
    # 필요 아이템 추출 (기술XX 패턴)
    tech_match = re.search(r'기술(\d+)', markdown_content)
    if tech_match:
        data['partner_skill_need_item_tech_level'] = tech_match.group(1)
        data['partner_skill_need_item'] = f"기술{tech_match.group(1)}"
    
    # Work Suitabilities 추출
    work_matches = re.findall(r'(불 피우기|관개|파종|발전|수작업|채집|벌목|채굴|제약|냉각|운반|목장)\s*Lv(\d+)', markdown_content)
    if work_matches:
        work_list = [f"{name} Lv{level}" for name, level in work_matches]
        data['work_suitabilities'] = '|'.join(work_list)
        data['work_suitabilities_count'] = len(work_list)
    
    # Stats 추출
    stats_patterns = {
        'size': r'Size\s*([XS|S|M|L|XL]+)',
        'rarity': r'Rarity\s*(\d+)',
        'health': r'HP\s*(\d+)',
        'food': r'식사량\s*(\d+)',
        'melee_attack': r'MeleeAttack\s*(\d+)',
        'attack': r'공격\s*(\d+)',
        'defense': r'방어\s*(\d+)',
        'work_speed': r'작업 속도\s*(\d+)',
        'support': r'Support\s*(\d+)',
        'capture_rate_correct': r'CaptureRateCorrect\s*([\d.]+)',
        'male_probability': r'MaleProbability\s*(\d+)',
        'combi_rank': r'CombiRank\s*(\d+)',
        'gold_coin': r'금화\s*(\d+)',
        'code': r'Code\s*([A-Za-z_]+)'
    }
    
    for key, pattern in stats_patterns.items():
        match = re.search(pattern, markdown_content)
        if match:
            data[key] = match.group(1)
    
    # Egg 추출
    egg_match = re.search(r'Egg\s*([^\n]+)', markdown_content)
    if egg_match:
        data['egg'] = egg_match.group(1).strip()
    
    # Movement 추출
    movement_patterns = {
        'slow_walk_speed': r'SlowWalkSpeed\s*(\d+)',
        'walk_speed': r'WalkSpeed\s*(\d+)',
        'run_speed': r'RunSpeed\s*(\d+)',
        'ride_sprint_speed': r'RideSprintSpeed\s*(\d+)',
        'transport_speed': r'TransportSpeed\s*(\d+)'
    }
    
    for key, pattern in movement_patterns.items():
        match = re.search(pattern, markdown_content)
        if match:
            data[key] = match.group(1)
    
    # Level 60 Stats 추출
    level60_match = re.search(r'##### Level 60\s*HP\s*([\d–\s]+)\s*공격\s*([\d–\s]+)\s*방어\s*([\d–\s]+)', markdown_content, re.DOTALL)
    if level60_match:
        data['level_60_health'] = level60_match.group(1).strip()
        data['level_60_attack'] = level60_match.group(2).strip()
        data['level_60_defense'] = level60_match.group(3).strip()
    
    # Active Skills 추출
    active_skills_matches = re.findall(r'Lv\. (\d+) \[([^\]]+)\].*?위력: (\d+)', markdown_content, re.DOTALL)
    if active_skills_matches:
        skills_list = [f"Lv{level} {name} (위력:{power})" for level, name, power in active_skills_matches]
        data['active_skills'] = '|'.join(skills_list)
        data['active_skills_count'] = len(skills_list)
    
    # Drops 추출
    drops_matches = re.findall(r'\[([^\]]+)\][^\d]*(\d+[–-]?\d*)\s*\|\s*(\d+%)', markdown_content)
    if drops_matches:
        drops_list = [f"{item} x{quantity} ({prob})" for item, quantity, prob in drops_matches]
        data['drops'] = '|'.join(drops_list)
        data['drops_count'] = len(drops_list)
    
    # Tribes 추출
    tribes_matches = re.findall(r'([^|]+)\s*\|\s*(Tribe [A-Za-z]+)', markdown_content)
    if tribes_matches:
        tribes_list = [f"{name.strip()} ({tribe_type})" for name, tribe_type in tribes_matches]
        data['tribes'] = '|'.join(tribes_list)
        data['tribes_count'] = len(tribes_list)
    
    # Spawners 추출
    spawner_matches = re.findall(r'Lv\. ([\d–\s]+)\s*\|\s*([^|]+)', markdown_content)
    if spawner_matches:
        spawner_list = [f"Lv{level.strip()} {area.strip()}" for level, area in spawner_matches]
        data['spawners'] = '|'.join(spawner_list)
        data['spawners_count'] = len(spawner_list)
    
    return data

def add_b_variants():
    """기존 CSV에 B 변종들을 추가"""
    
    print("🔥 기존 CSV에 B 변종들 추가 시작!")
    
    # 기존 CSV 읽기
    existing_data = []
    try:
        with open('final_1_to_10_pals_without_nick.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)
        print(f"📄 기존 데이터 {len(existing_data)}개 읽기 완료")
    except FileNotFoundError:
        print("❌ 기존 CSV 파일을 찾을 수 없습니다.")
        return
    
    # B 변종 데이터 생성
    b_variants = [
        ('5B', '아이호', """
얼음 속성

##### Summary

태어난 직후엔 냉기를 잘 못 다뤄서
걸핏하면 냉기를 뿜다가 숨이 탁 막힌다.
감기에 걸리면 콧물이 어는 바람에 숨이 가빠진다.

##### Partner Skill: 포옹 프로스트

발동하면 플레이어에게 장착되어
냉기를 방출해 공격할 수 있다.

기술24

냉각 Lv1

Size XS
Rarity 1
HP 65
식사량 150
MeleeAttack 70
공격 80
방어 70
작업 속도 100
Support 100
CaptureRateCorrect 1.1
MaleProbability 50
CombiRank 1305
금화 1410
Egg 얼어붙은 알
Code Kitsunebi_Ice

SlowWalkSpeed 40
WalkSpeed 80
RunSpeed 400
RideSprintSpeed 550
TransportSpeed 240

##### Level 60
HP 2937 – 3571
공격 490 – 607
방어 391 – 493

Lv. 1 [얼음 미사일] 위력: 30
Lv. 15 [얼음 칼날] 위력: 55

가죽 1–2 | 100%
빙결 기관 1–3 | 100%

여로를 수놓는 얼음꽃 아이호 | Tribe Boss
아이호 | Tribe Normal

Lv. 52–55 | yamijima_7_2_DarkArea
"""),
        ('6B', '적부리', """
물 속성
화염 속성

##### Summary

배의 마찰력이 아주 강한 탓에
보디 서핑을 하면 불이 붙을 정도다.
너무 신나게 미끄러지다 간혹 불덩이가 되기도 한다.

##### Partner Skill: 파이어 태클

발동하면 적부리 이(가) 적을 향해
파이어 서핑을 하며 달려든다.

불 피우기 Lv1
관개 Lv1
수작업 Lv1
운반 Lv1

Size XS
Rarity 2
HP 60
식사량 150
MeleeAttack 100
공격 85
방어 60
작업 속도 100
Support 100
CaptureRateCorrect 1.1
MaleProbability 50
CombiRank 1290
금화 1340
Egg 축축한 알
Code BluePlatypus_Fire

SlowWalkSpeed 70
WalkSpeed 105
RunSpeed 300
RideSprintSpeed 400
TransportSpeed 202

##### Level 60
HP 2775 – 3360
공격 514 – 638
방어 342 – 430

Lv. 1 [파이어 샷] 위력: 30
Lv. 15 [버블 샷] 위력: 65

가죽 1 | 100%
팰의 체액 1 | 100%
발화 기관 1–2 | 50%

폭주 중인 파도 타는 꼬맹이 적부리 | Tribe Boss
적부리 | Tribe Normal

Lv. 16–27 | 커다란 낚시터 Medium 8.72%
"""),
        ('10B', '뎅키', """
물 속성
번개 속성

##### Summary

날개가 완전히 퇴화해 날 수 없다.
하늘을 향한 미련은 어느덧 질투로 변화하여
하늘을 나는 모든 것을 격추할 전기의 힘을 얻게 되었다!

##### Partner Skill: 뎅키 발사기

발동하면 로켓 발사기 을(를) 장착하여
뎅키 을(를) 탄환 삼아 발사한다.
착탄하여 폭발하면 뎅키 이(가) 빈사 상태가 된다.

기술39

관개 Lv1
발전 Lv2
수작업 Lv1
운반 Lv1

Size XS
Rarity 2
HP 70
식사량 150
MeleeAttack 100
공격 80
방어 70
작업 속도 100
Support 100
CaptureRateCorrect 0.9
MaleProbability 50
CombiRank 1310
금화 1290
Egg 축축한 알
Code Penguin_Electric

SlowWalkSpeed 30
WalkSpeed 60
RunSpeed 500
RideSprintSpeed 650
TransportSpeed 265

##### Level 60
HP 3100 – 3782
공격 490 – 607
방어 391 – 493

Lv. 1 [번개 창] 위력: 30
Lv. 15 [버블 샷] 위력: 65

발전 기관 1–2 | 100%
팰의 체액 1 | 100%

과음한 뎅키 | Tribe Boss
뎅키 | Tribe Normal

Lv. 16–27 | 커다란 낚시터 Medium 9.96%
"""),
    ]
    
    # B 변종 데이터 파싱
    new_data = []
    for pal_id, pal_name, markdown_content in b_variants:
        print(f"📊 처리 중: {pal_id} {pal_name}")
        parsed_data = parse_pal_data_simple(markdown_content, pal_id, pal_name)
        new_data.append(parsed_data)
    
    # 모든 데이터 합치기 (기존 + 새로운 B 변종들)
    all_data = existing_data + new_data
    
    # ID별로 정렬 (1, 2, 3, 4, 5, 5B, 6, 6B, 7, 8, 9, 10, 10B)
    def sort_key(item):
        pal_id = item['id']
        if 'B' in pal_id:
            base_num = int(pal_id.replace('B', ''))
            return (base_num, 1)  # B 변종은 기본 팰 다음에
        else:
            return (int(pal_id), 0)  # 기본 팰이 먼저
    
    all_data.sort(key=sort_key)
    
    # 새로운 CSV 생성
    filename = 'complete_1_to_10_with_b_variants.csv'
    
    if all_data:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
            writer.writeheader()
            writer.writerows(all_data)
        
        print(f"\n🎉 완성! {filename} 파일 생성 완료!")
        print(f"📋 총 {len(all_data)}개 팰 데이터 (1-10 + B변종들)")
        print(f"📊 컬럼 수: {len(all_data[0].keys())}개")
        
        # 파일 내용 미리보기
        print(f"\n📄 팰 순서:")
        for i, row in enumerate(all_data):
            print(f"  {i+1}. {row['id']} - {row['name_kor']} ({row['elements']})")
    
    else:
        print("❌ 생성할 데이터가 없습니다.")

if __name__ == "__main__":
    add_b_variants() 