#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1-10번 팰 데이터 병합 스크립트
기존 4개 팰 + 새로운 6개 팰 = 완전한 10개 팰 CSV
"""

import json
import csv
import re
from typing import Dict, List, Any

def parse_pal_from_text(pal_id: str, name: str, raw_text: str) -> Dict[str, Any]:
    """raw_text에서 팰 데이터를 파싱"""
    
    pal = {
        'id': pal_id,
        'name_kor': name,
        'pal_nick_kor': '',
        'description_kor': '',
        'elements': '',
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
        'slow_walk_speed': '',
        'walk_speed': '',
        'run_speed': '',
        'ride_sprint_speed': '',
        'transport_speed': '',
        'health_60': '',
        'attack_60': '',
        'defense_60': '',
        'partner_skill_name': '',
        'partner_skill_need_item': '',
        'partner_skill_need_item_tech_level': '',
        'partner_skill_describe': '',
        'partner_skill_level': '',
        'partner_skill_items': '',
        'work_suitability_types': '',
        'work_suitability_levels': '',
        'work_suitability_count': '',
        'food_amount': '',
        'active_skills_required_level': '',
        'active_skills_name': '',
        'active_skills_element': '',
        'active_skills_power': '',
        'active_skills_count': '',
        'drops_item_name': '',
        'drops_item_quantity': '',
        'drops_item_probability': '',
        'drops_count': '',
        'tribes_name': '',
        'tribes_type': '',
        'tribes_count': '',
        'spawner_name': '',
        'spawner_level': '',
        'spawner_area': '',
        'spawner_count': ''
    }
    
    # 속성 추출
    if "무속성" in raw_text:
        pal['elements'] = "무속성"
    elif "풀 속성" in raw_text:
        pal['elements'] = "풀 속성"
    elif "화염 속성" in raw_text:
        pal['elements'] = "화염 속성"
    elif "물 속성" in raw_text and "얼음 속성" in raw_text:
        pal['elements'] = "물 속성|얼음 속성"
    elif "물 속성" in raw_text:
        pal['elements'] = "물 속성"
    elif "번개 속성" in raw_text:
        pal['elements'] = "번개 속성"
    
    # 파트너 스킬 추출
    partner_skill_match = re.search(r'파트너 스킬 ([^\s]+) Lv\.1', raw_text)
    if partner_skill_match:
        pal['partner_skill_name'] = partner_skill_match.group(1)
    
    # 파트너 스킬 설명 추출
    desc_matches = [
        "가축 목장 에 배치하면 가끔씩 알 을(를) 낳기도 한다",
        "발동하면 플레이어의 머리 위에 올라 공격에 맞춰 기관단총으로 추격한다",
        "발동하면 화염방사기로 변하여 플레이어에게 장착된다",
        "발동하면 청부리 이(가) 적을 향해 보디 서핑을 하며 달려든다",
        "보유하고 있는 동안 번개 속성 팰의 공격력이 증가한다",
        "발동하면 일정 시간 몽지 이(가) 근처 적에게 돌격 소총을 난사한다",
        "보유하고 있는 동안 화염 속성 팰의 공격력이 증가한다",
        "발동하면 로켓 발사기 을(를) 장착하여 펭키 을(를) 탄환 삼아 발사한다"
    ]
    
    for desc in desc_matches:
        if desc in raw_text:
            pal['partner_skill_describe'] = desc
            break
    
    # 기술 레벨 추출
    tech_match = re.search(r'기술(\d+)', raw_text)
    if tech_match:
        pal['partner_skill_need_item_tech_level'] = tech_match.group(1)
        pal['partner_skill_need_item'] = f"기술{tech_match.group(1)}"
    
    # 작업 적성 추출
    work_types = []
    work_levels = []
    
    work_patterns = [
        (r'채집 Lv(\d+)', '채집'),
        (r'목장 Lv(\d+)', '목장'),
        (r'파종 Lv(\d+)', '파종'),
        (r'수작업 Lv(\d+)', '수작업'),
        (r'벌목 Lv(\d+)', '벌목'),
        (r'제약 Lv(\d+)', '제약'),
        (r'불 피우기 Lv(\d+)', '불 피우기'),
        (r'관개 Lv(\d+)', '관개'),
        (r'운반 Lv(\d+)', '운반'),
        (r'발전 Lv(\d+)', '발전'),
        (r'냉각 Lv(\d+)', '냉각')
    ]
    
    for pattern, work_type in work_patterns:
        matches = re.findall(pattern, raw_text)
        for level in matches:
            work_types.append(work_type)
            work_levels.append(level)
    
    if work_types:
        pal['work_suitability_types'] = "|".join(work_types)
        pal['work_suitability_levels'] = "|".join(work_levels)
        pal['work_suitability_count'] = str(len(work_types))
    
    # 식사량 추출
    food_match = re.search(r'식사량 (\d+)', raw_text)
    if food_match:
        pal['food_amount'] = food_match.group(1)
    
    # Stats 추출
    stats_patterns = {
        'size': r'Size (\w+)',
        'rarity': r'Rarity (\d+)',
        'health': r'HP (\d+)',
        'food': r'식사량 (\d+)',
        'melee_attack': r'MeleeAttack (\d+)',
        'attack': r'공격 (\d+)',
        'defense': r'방어 (\d+)',
        'work_speed': r'작업 속도 (\d+)',
        'support': r'Support (\d+)',
        'capture_rate_correct': r'CaptureRateCorrect ([\d.]+)',
        'male_probability': r'MaleProbability (\d+)',
        'combi_rank': r'CombiRank (\d+)',
        'gold_coin': r'금화 (\d+)',
        'code': r'Code (\w+)'
    }
    
    for key, pattern in stats_patterns.items():
        match = re.search(pattern, raw_text)
        if match:
            pal[key] = match.group(1)
    
    # Egg 추출
    egg_patterns = [
        '평범한 알', '신록의 알', '열기 나는 알', '축축한 알', '찌릿찌릿한 알'
    ]
    for egg_type in egg_patterns:
        if egg_type in raw_text:
            pal['egg'] = egg_type
            break
    
    # Movement 추출
    movement_patterns = {
        'slow_walk_speed': r'SlowWalkSpeed (\d+)',
        'walk_speed': r'WalkSpeed (\d+)',
        'run_speed': r'RunSpeed (\d+)',
        'ride_sprint_speed': r'RideSprintSpeed (\d+)',
        'transport_speed': r'TransportSpeed ([\d\-]+)'
    }
    
    for key, pattern in movement_patterns.items():
        match = re.search(pattern, raw_text)
        if match:
            pal[key] = match.group(1)
    
    # Level 60 추출
    level60_health = re.search(r'Level 60 HP ([\d\s–\-]+)', raw_text)
    if level60_health:
        pal['health_60'] = level60_health.group(1).strip()
    
    level60_attack = re.search(r'Level 60.*?공격 ([\d\s–\-]+)', raw_text)
    if level60_attack:
        pal['attack_60'] = level60_attack.group(1).strip()
    
    level60_defense = re.search(r'Level 60.*?방어 ([\d\s–\-]+)', raw_text)
    if level60_defense:
        pal['defense_60'] = level60_defense.group(1).strip()
    
    # Summary 추출
    summary_match = re.search(r'Summary (.+)', raw_text)
    if summary_match:
        pal['description_kor'] = summary_match.group(1).strip()
    
    return pal

def main():
    """메인 함수: 1-10번 팰 데이터 병합"""
    
    # 기존 4개 팰 데이터 로드
    existing_pals = []
    try:
        with open('current_4_pals_complete.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_pals.append(row)
        print(f"✅ 기존 4개 팰 데이터 로드: {len(existing_pals)}개")
    except FileNotFoundError:
        print("❌ 기존 CSV 파일을 찾을 수 없습니다.")
        return
    
    # 새로운 팰 데이터 로드
    try:
        with open('pal_3_to_10_data.json', 'r', encoding='utf-8') as f:
            new_pal_data = json.load(f)
        print(f"✅ 새로운 팰 JSON 데이터 로드: {len(new_pal_data)}개")
    except FileNotFoundError:
        print("❌ 새로운 팰 JSON 파일을 찾을 수 없습니다.")
        return
    
    # 새로운 팰 데이터 파싱
    new_pals = []
    for pal_id, pal_info in new_pal_data.items():
        pal_data = parse_pal_from_text(pal_id, pal_info['name'], pal_info['raw_text'])
        new_pals.append(pal_data)
        print(f"📝 파싱 완료: {pal_id}번 {pal_info['name']}")
    
    # 기존 데이터에서 이미 있는 팰 제거 (1, 2번)
    filtered_existing = [pal for pal in existing_pals if pal['id'] in ['1', '2']]
    print(f"🔄 기존 데이터 필터링: {len(filtered_existing)}개 (1, 2번만 유지)")
    
    # 모든 팰 데이터 통합
    all_pals = filtered_existing + new_pals
    
    # ID 순으로 정렬
    all_pals.sort(key=lambda x: int(x['id']))
    
    # CSV 컬럼 정의 (기존 CSV와 동일한 구조)
    if existing_pals:
        columns = list(existing_pals[0].keys())
    else:
        columns = [
            'id', 'name_kor', 'pal_nick_kor', 'description_kor', 'elements',
            'size', 'rarity', 'health', 'food', 'melee_attack', 'attack', 'defense', 
            'work_speed', 'support', 'capture_rate_correct', 'male_probability', 
            'combi_rank', 'gold_coin', 'egg', 'code',
            'slow_walk_speed', 'walk_speed', 'run_speed', 'ride_sprint_speed', 'transport_speed',
            'health_60', 'attack_60', 'defense_60',
            'partner_skill_name', 'partner_skill_need_item', 'partner_skill_need_item_tech_level',
            'partner_skill_describe', 'partner_skill_level', 'partner_skill_items',
            'work_suitability_types', 'work_suitability_levels', 'work_suitability_count',
            'food_amount',
            'active_skills_required_level', 'active_skills_name', 'active_skills_element', 
            'active_skills_power', 'active_skills_count',
            'drops_item_name', 'drops_item_quantity', 'drops_item_probability', 'drops_count',
            'tribes_name', 'tribes_type', 'tribes_count',
            'spawner_name', 'spawner_level', 'spawner_area', 'spawner_count'
        ]
    
    # CSV 파일 저장
    output_file = 'pal_1_to_10_complete.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        
        for pal in all_pals:
            # 빈 컬럼들 채우기
            complete_pal = {}
            for col in columns:
                complete_pal[col] = pal.get(col, '')
            writer.writerow(complete_pal)
    
    print(f"\n🎉 완성된 CSV 파일 저장: {output_file}")
    print(f"📊 총 {len(all_pals)}개 팰 데이터 포함")
    
    # 팰 목록 출력
    print("\n📋 포함된 팰 목록:")
    for pal in all_pals:
        print(f"  {pal['id']}번: {pal['name_kor']} ({pal['elements']})")
    
    # 통계 출력
    print(f"\n📈 데이터 통계:")
    print(f"- 총 팰 수: {len(all_pals)}")
    print(f"- 컬럼 수: {len(columns)}")
    
    # 파일 크기 확인
    import os
    file_size = os.path.getsize(output_file)
    print(f"- 파일 크기: {file_size:,} bytes")

if __name__ == "__main__":
    main() 