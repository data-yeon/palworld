#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
배치로 추출한 팰 데이터를 CSV로 변환하는 스크립트
"""

import csv
import json
import os
from typing import List, Dict, Any

def format_active_skills(active_skills: List[Dict[str, Any]]) -> str:
    """액티브 스킬들을 읽기 쉬운 형태로 포맷팅"""
    if not active_skills:
        return ""
    
    skill_strings = []
    for skill in active_skills:
        skill_info = f"{skill.get('name', '')}({skill.get('element', '')}, 파워:{skill.get('power', '')}, 쿨타임:{skill.get('coolTime', '')}초)"
        skill_strings.append(skill_info)
    
    return " | ".join(skill_strings)

def format_drops(drops: List[Dict[str, Any]]) -> str:
    """드롭 아이템들을 읽기 쉬운 형태로 포맷팅"""
    if not drops:
        return ""
    
    drop_strings = []
    for drop in drops:
        drop_info = f"{drop.get('itemName', '')}({drop.get('quantity', '')}, 확률:{drop.get('probability', '')})"
        drop_strings.append(drop_info)
    
    return " | ".join(drop_strings)

def format_spawners(spawners: List[Dict[str, Any]]) -> str:
    """스포너들을 읽기 쉬운 형태로 포맷팅"""
    if not spawners:
        return ""
    
    spawner_strings = []
    for spawner in spawners:
        spawner_info = f"{spawner.get('name', '')}({spawner.get('level', '')}, 지역:{spawner.get('area', '')})"
        spawner_strings.append(spawner_info)
    
    return " | ".join(spawner_strings)

def format_work_suitabilities(work_suitabilities: List[Dict[str, Any]]) -> str:
    """작업 적성들을 읽기 쉬운 형태로 포맷팅"""
    if not work_suitabilities:
        return ""
    
    work_strings = []
    for work in work_suitabilities:
        work_info = f"{work.get('work', '')}(LV.{work.get('level', '')})"
        work_strings.append(work_info)
    
    return " | ".join(work_strings)

def flatten_pal_data(pal_data: Dict[str, Any]) -> Dict[str, str]:
    """중첩된 팰 데이터를 평면적인 CSV 형태로 변환"""
    flattened = {}
    
    # 기본 정보
    flattened['id'] = pal_data.get('id', '')
    flattened['name_kor'] = pal_data.get('name_kor', '')
    flattened['pal_nick_kor'] = pal_data.get('pal_nick_kor', '')
    flattened['description_kor'] = pal_data.get('description_kor', '')
    
    # 속성들을 문자열로 변환
    elements = pal_data.get('elements', [])
    flattened['elements'] = ', '.join(elements) if elements else ''
    
    # 스탯 정보
    stats = pal_data.get('stats', {})
    flattened['size'] = stats.get('size', '')
    flattened['rarity'] = str(stats.get('rarity', ''))
    flattened['health'] = str(stats.get('health', ''))
    flattened['food'] = str(stats.get('food', ''))
    flattened['attack'] = str(stats.get('attack', ''))
    flattened['defense'] = str(stats.get('defense', ''))
    flattened['melee_attack'] = str(stats.get('meleeAttack', ''))
    flattened['work_speed'] = str(stats.get('workSpeed', ''))
    flattened['support'] = str(stats.get('support', ''))
    flattened['capture_rate_correct'] = str(stats.get('captureRateCorrect', ''))
    flattened['male_probability'] = str(stats.get('maleProbability', ''))
    flattened['combi_rank'] = str(stats.get('combiRank', ''))
    flattened['gold_coin'] = str(stats.get('goldCoin', ''))
    flattened['egg'] = stats.get('egg', '')
    flattened['code'] = stats.get('code', '')
    
    # Movement 정보
    movement = pal_data.get('movement', {})
    flattened['slow_walk_speed'] = str(movement.get('slowWalkSpeed', ''))
    flattened['walk_speed'] = str(movement.get('walkSpeed', ''))
    flattened['run_speed'] = str(movement.get('runSpeed', ''))
    flattened['transport_speed'] = str(movement.get('transportSpeed', ''))
    flattened['ride_sprint_speed'] = str(movement.get('rideSprintSpeed', ''))
    
    # Level 60 스탯
    level60_stats = pal_data.get('level60Stats', {})
    flattened['level60_health'] = str(level60_stats.get('health', ''))
    flattened['level60_attack'] = str(level60_stats.get('attack', ''))
    flattened['level60_defense'] = str(level60_stats.get('defense', ''))
    
    # 파트너 스킬
    partner_skill = pal_data.get('partnerSkill', {})
    flattened['partner_skill_name'] = partner_skill.get('name', '')
    flattened['partner_skill_describe'] = partner_skill.get('describe', '')
    flattened['partner_skill_need_item'] = partner_skill.get('needItem', '')
    flattened['partner_skill_need_item_tech_level'] = str(partner_skill.get('needItemTechLevel', ''))
    flattened['partner_skill_level'] = str(partner_skill.get('level', ''))
    
    # 복수 데이터들을 포맷팅해서 저장
    flattened['active_skills'] = format_active_skills(pal_data.get('activeSkills', []))
    flattened['active_skills_count'] = str(len(pal_data.get('activeSkills', [])))
    
    flattened['passive_skills'] = ', '.join(pal_data.get('passiveSkills', []))
    flattened['passive_skills_count'] = str(len(pal_data.get('passiveSkills', [])))
    
    flattened['drops'] = format_drops(pal_data.get('drops', []))
    flattened['drops_count'] = str(len(pal_data.get('drops', [])))
    
    flattened['spawners'] = format_spawners(pal_data.get('spawners', []))
    flattened['spawners_count'] = str(len(pal_data.get('spawners', [])))
    
    flattened['work_suitabilities'] = format_work_suitabilities(pal_data.get('workSuitabilities', []))
    flattened['work_suitabilities_count'] = str(len(pal_data.get('workSuitabilities', [])))
    
    # Tribes 정보
    tribes = pal_data.get('tribes', [])
    tribe_names = [tribe.get('name', '') for tribe in tribes]
    flattened['tribes'] = ' | '.join(tribe_names)
    flattened['tribes_count'] = str(len(tribes))
    
    return flattened

def create_csv_from_batch_data(file_path: str, output_file: str):
    """배치 JSON 파일을 읽어서 CSV 파일로 변환"""
    
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        batch_data = json.load(f)
    
    pal_data = batch_data['pals']
    print(f"📊 총 {len(pal_data)}개의 팰 데이터를 처리합니다.")
    
    # 첫 번째 팰 데이터를 기준으로 CSV 필드명 생성
    if not pal_data:
        print("❌ 팰 데이터가 없습니다.")
        return
        
    flattened_data = [flatten_pal_data(pal) for pal in pal_data]
    fieldnames = list(flattened_data[0].keys())
    
    # CSV 파일 작성
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flattened_data)
    
    print(f"✅ CSV 파일이 생성되었습니다: {output_file}")
    print(f"📋 총 {len(fieldnames)}개의 컬럼, {len(flattened_data)}개의 행")
    
    # 컬럼 목록 출력
    print("\n📄 CSV 컬럼 목록:")
    for i, field in enumerate(fieldnames, 1):
        print(f"{i:2d}. {field}")

if __name__ == "__main__":
    # 배치 JSON 파일을 CSV로 변환
    input_file = 'pal_data_batch_1_20.json'
    output_file = 'pal_data_batch_1_20.csv'
    
    if os.path.exists(input_file):
        create_csv_from_batch_data(input_file, output_file)
    else:
        print(f"❌ 입력 파일을 찾을 수 없습니다: {input_file}") 