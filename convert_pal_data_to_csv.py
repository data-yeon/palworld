#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
팰 정보를 CSV 파일로 변환하는 스크립트 (개선된 버전)
복수 데이터를 더 명확하게 처리
"""

import csv
import json
import os
from typing import List, Dict, Any

def format_active_skills(active_skills: List[Dict[str, Any]]) -> str:
    """
    액티브 스킬들을 읽기 쉬운 형태로 포맷팅
    """
    if not active_skills:
        return ""
    
    skill_strings = []
    for skill in active_skills:
        skill_info = f"{skill.get('name', '')}({skill.get('element', '')}, 파워:{skill.get('power', '')}, 쿨타임:{skill.get('coolTime', '')}초)"
        skill_strings.append(skill_info)
    
    return " | ".join(skill_strings)

def format_drops(drops: List[Dict[str, Any]]) -> str:
    """
    드롭 아이템들을 읽기 쉬운 형태로 포맷팅
    """
    if not drops:
        return ""
    
    drop_strings = []
    for drop in drops:
        drop_info = f"{drop.get('itemName', '')}({drop.get('quantity', '')}, 확률:{drop.get('probability', '')})"
        drop_strings.append(drop_info)
    
    return " | ".join(drop_strings)

def format_work_suitabilities(work_suitabilities: List[Dict[str, Any]]) -> str:
    """
    작업 적성들을 읽기 쉬운 형태로 포맷팅
    """
    if not work_suitabilities:
        return ""
    
    work_strings = []
    for work in work_suitabilities:
        work_info = f"{work.get('work', '')}(LV.{work.get('level', '')})"
        work_strings.append(work_info)
    
    return " | ".join(work_strings)

def format_spawners(spawners: List[Dict[str, Any]]) -> str:
    """
    스포너들을 읽기 쉬운 형태로 포맷팅
    """
    if not spawners:
        return ""
    
    spawner_strings = []
    for spawner in spawners:
        spawner_info = f"{spawner.get('name', '')}({spawner.get('level', '')}, 지역:{spawner.get('area', '')})"
        spawner_strings.append(spawner_info)
    
    return " | ".join(spawner_strings)

def flatten_pal_data(pal_data: Dict[str, Any]) -> Dict[str, str]:
    """
    중첩된 팰 데이터를 평면적인 CSV 형태로 변환 (개선된 버전)
    """
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
    flattened['melee_attack'] = str(stats.get('meleeAttack', ''))
    flattened['attack'] = str(stats.get('attack', ''))
    flattened['defense'] = str(stats.get('defense', ''))
    flattened['work_speed'] = str(stats.get('workSpeed', ''))
    flattened['support'] = str(stats.get('support', ''))
    flattened['capture_rate_correct'] = str(stats.get('captureRateCorrect', ''))
    flattened['male_probability'] = str(stats.get('maleProbability', ''))
    flattened['combi_rank'] = str(stats.get('combiRank', ''))
    flattened['gold_coin'] = str(stats.get('goldCoin', ''))
    flattened['egg'] = stats.get('egg', '')
    flattened['code'] = stats.get('code', '')
    
    # 이동 정보
    movement = pal_data.get('movement', {})
    flattened['slow_walk_speed'] = str(movement.get('slowWalkSpeed', ''))
    flattened['walk_speed'] = str(movement.get('walkSpeed', ''))
    flattened['run_speed'] = str(movement.get('runSpeed', ''))
    flattened['ride_sprint_speed'] = str(movement.get('rideSprintSpeed', ''))
    flattened['transport_speed'] = str(movement.get('transportSpeed', ''))
    
    # 레벨 60 스탯
    level60_stats = pal_data.get('level60Stats', {})
    flattened['level60_health'] = str(level60_stats.get('health', ''))
    flattened['level60_attack'] = str(level60_stats.get('attack', ''))
    flattened['level60_defense'] = str(level60_stats.get('defense', ''))
    
    # 파트너 스킬
    partner_skill = pal_data.get('partnerSkill', {})
    flattened['partner_skill_name'] = partner_skill.get('name', '')
    flattened['partner_skill_describe'] = partner_skill.get('describe', '')
    flattened['partner_skill_need_item'] = partner_skill.get('needItem', '')
    flattened['partner_skill_level'] = str(partner_skill.get('level', ''))
    
    # 파트너 스킬 아이템들 - 더 읽기 쉬운 형태로
    partner_items = partner_skill.get('items', [])
    partner_quantities = partner_skill.get('itemQuantity', [])
    partner_probabilities = partner_skill.get('itemProbability', [])
    
    partner_item_details = []
    for i, item in enumerate(partner_items):
        quantity = partner_quantities[i] if i < len(partner_quantities) else ""
        probability = partner_probabilities[i] if i < len(partner_probabilities) else ""
        detail = f"{item}(수량:{quantity}, 확률:{probability}%)"
        partner_item_details.append(detail)
    
    flattened['partner_skill_items_detail'] = " | ".join(partner_item_details)
    
    # 액티브 스킬들 - 개선된 포맷으로
    active_skills = pal_data.get('activeSkills', [])
    flattened['active_skills_formatted'] = format_active_skills(active_skills)
    flattened['active_skills_count'] = str(len(active_skills))
    
    # 액티브 스킬 상세 정보들을 각각 컬럼으로
    flattened['active_skills_names'] = " | ".join([skill.get('name', '') for skill in active_skills])
    flattened['active_skills_elements'] = " | ".join([skill.get('element', '') for skill in active_skills])
    flattened['active_skills_powers'] = " | ".join([str(skill.get('power', '')) for skill in active_skills])
    flattened['active_skills_cooldowns'] = " | ".join([str(skill.get('coolTime', '')) for skill in active_skills])
    
    # 패시브 스킬들
    passive_skills = pal_data.get('passiveSkills', [])
    flattened['passive_skills'] = ' | '.join(passive_skills) if passive_skills else ''
    flattened['passive_skills_count'] = str(len(passive_skills))
    
    # 드롭 아이템들 - 개선된 포맷으로
    drops = pal_data.get('drops', [])
    flattened['drops_formatted'] = format_drops(drops)
    flattened['drops_count'] = str(len(drops))
    
    # 드롭 아이템 상세 정보들을 각각 컬럼으로
    flattened['drops_item_names'] = " | ".join([drop.get('itemName', '') for drop in drops])
    flattened['drops_quantities'] = " | ".join([drop.get('quantity', '') for drop in drops])
    flattened['drops_probabilities'] = " | ".join([drop.get('probability', '') for drop in drops])
    
    # 작업 적성 - 개선된 포맷으로
    work_suitabilities = pal_data.get('workSuitabilities', [])
    flattened['work_suitabilities_formatted'] = format_work_suitabilities(work_suitabilities)
    flattened['work_suitabilities_count'] = str(len(work_suitabilities))
    
    # 부족들
    tribes = pal_data.get('tribes', [])
    flattened['tribes'] = ' | '.join(tribes) if tribes else ''
    flattened['tribes_count'] = str(len(tribes))
    
    # 스포너들 - 개선된 포맷으로
    spawners = pal_data.get('spawners', [])
    flattened['spawners_formatted'] = format_spawners(spawners)
    flattened['spawners_count'] = str(len(spawners))
    
    # 스포너 상세 정보들을 각각 컬럼으로
    flattened['spawners_names'] = " | ".join([spawner.get('name', '') for spawner in spawners])
    flattened['spawners_levels'] = " | ".join([spawner.get('level', '') for spawner in spawners])
    flattened['spawners_areas'] = " | ".join([spawner.get('area', '') for spawner in spawners])
    
    # 원본 JSON 데이터도 보존 (필요시 참조용)
    flattened['active_skills_json'] = json.dumps(active_skills, ensure_ascii=False)
    flattened['drops_json'] = json.dumps(drops, ensure_ascii=False)
    flattened['work_suitabilities_json'] = json.dumps(work_suitabilities, ensure_ascii=False)
    flattened['spawners_json'] = json.dumps(spawners, ensure_ascii=False)
    
    return flattened

def create_csv_from_pal_data(pal_data_list: List[Dict[str, Any]], output_file: str):
    """
    팰 데이터 리스트를 CSV 파일로 저장
    """
    if not pal_data_list:
        print("팰 데이터가 비어있습니다.")
        return
    
    # 첫 번째 항목으로부터 필드명 추출
    fieldnames = list(flatten_pal_data(pal_data_list[0]).keys())
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 헤더 작성
        writer.writeheader()
        
        # 각 팰 데이터를 평면화하여 작성
        for pal_data in pal_data_list:
            flattened_data = flatten_pal_data(pal_data)
            writer.writerow(flattened_data)
    
    print(f"CSV 파일이 생성되었습니다: {output_file}")
    print(f"총 {len(pal_data_list)}개의 팰 정보가 저장되었습니다.")

def sample_pal_data_extended():
    """
    확장된 샘플 팰 데이터 - 복수 데이터가 포함된 예시
    """
    sample_data = [
        {
            "id": "1",
            "name_kor": "도로롱",
            "pal_nick_kor": "#1",
            "description_kor": "언덕길을 걷다 저 혼자 데굴데굴 구른다. 결국 눈이 핑핑 돌아 몸을 못 가눌 때 간단히 처치할 수 있는 먹이 사슬의 최하층이다.",
            "elements": ["Normal"],
            "stats": {
                "size": "XS",
                "rarity": 1,
                "health": 70,
                "food": 150,
                "meleeAttack": 70,
                "attack": 70,
                "defense": 70,
                "workSpeed": 100,
                "support": 100,
                "captureRateCorrect": 1.5,
                "maleProbability": 50,
                "combiRank": 1470,
                "goldCoin": 1000,
                "egg": "평범한 알",
                "code": "SheepBall"
            },
            "movement": {
                "slowWalkSpeed": 23,
                "walkSpeed": 40,
                "runSpeed": 400,
                "rideSprintSpeed": 550,
                "transportSpeed": 160
            },
            "level60Stats": {
                "health": 3100,
                "attack": 441,
                "defense": 391
            },
            "partnerSkill": {
                "name": "복슬복슬 방패",
                "describe": "발동하면 방패로 변하여 플레이어에게 장착된다. [가축 목장]에 배치하면 [양털]을(를) 떨어뜨리기도 한다.",
                "needItem": "",
                "level": 1,
                "items": ["양털"],
                "itemQuantity": [1100],
                "itemProbability": [100]
            },
            "activeSkills": [
                {
                    "name": "데굴데굴 솜사탕",
                    "element": "Normal",
                    "power": 35,
                    "coolTime": 1,
                    "shootAttack": False,
                    "meleeAttack": True,
                    "accumulatedElement": "",
                    "accumulatedValue": 0,
                    "describe": "[도로롱] 전용 스킬. 데굴데굴 구르면서 적을 쫓아간다. 공격 후엔 눈이 핑핑 돌아 움직일 수 없게 된다."
                },
                {
                    "name": "공기 대포",
                    "element": "Normal",
                    "power": 25,
                    "coolTime": 2,
                    "shootAttack": True,
                    "meleeAttack": False,
                    "accumulatedElement": "",
                    "accumulatedValue": 0,
                    "describe": "압축된 공기를 빠르게 발사한다."
                }
            ],
            "passiveSkills": ["겁쟁이", "빠른 발"],
            "drops": [
                {
                    "itemName": "양털",
                    "quantity": "1–3",
                    "probability": "100%"
                },
                {
                    "itemName": "가죽",
                    "quantity": "1–2",
                    "probability": "80%"
                }
            ],
            "workSuitabilities": [
                {
                    "work": "수작업",
                    "level": 1
                },
                {
                    "work": "운반", 
                    "level": 1
                },
                {
                    "work": "목장",
                    "level": 1
                }
            ],
            "tribes": ["SheepBall", "CommonPals"],
            "spawners": [
                {
                    "name": "도로롱",
                    "level": "Lv. 1–3",
                    "area": "1_1_plain_beginner"
                },
                {
                    "name": "도로롱 무리",
                    "level": "Lv. 2–4",
                    "area": "1_2_forest_area"
                }
            ]
        }
    ]
    return sample_data

if __name__ == "__main__":
    # 확장된 샘플 데이터로 테스트
    pal_data = sample_pal_data_extended()
    create_csv_from_pal_data(pal_data, "pal_complete_data_improved.csv")
    
    print("\n🎯 개선된 CSV 파일이 생성되었습니다!")
    print("📊 주요 개선사항:")
    print("  • 액티브 스킬: 포맷팅된 형태 + 개별 컬럼 분리")
    print("  • 드롭 아이템: 읽기 쉬운 형태 + 상세 정보 분리")
    print("  • 작업 적성: 레벨까지 포함한 명확한 표시")
    print("  • 스포너: 지역 정보까지 포함한 상세 표시")
    print("  • 각 항목별 개수 정보 추가")
    
    print("\n생성된 CSV 파일의 컬럼들:")
    fieldnames = list(flatten_pal_data(pal_data[0]).keys())
    for i, field in enumerate(fieldnames, 1):
        print(f"{i:2d}. {field}")

    # 새로 추출된 JSON 데이터를 읽어서 CSV로 변환하는 부분을 추가

    # 새로 추출된 배치 데이터 로드
    with open('pal_data_batch_1_20.json', 'r', encoding='utf-8') as f:
        batch_data = json.load(f)
        new_pal_data = batch_data['pals']

        print(f"새로 추출된 팰 데이터 수: {len(new_pal_data)}")
        
        # 새 데이터를 기존 샘플 데이터에 추가
        pal_data.extend(new_pal_data)
        print(f"총 팰 데이터 수: {len(pal_data)}")

    # CSV 파일 생성
    output_file = 'pal_complete_data_batch1_20.csv'
    create_csv_from_pal_data(pal_data, output_file) 