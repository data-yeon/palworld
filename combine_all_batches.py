#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모든 배치의 팰 데이터를 통합하고 CSV로 변환하는 스크립트
"""

import csv
import json
import os
from typing import List, Dict, Any

# 첫 번째와 두 번째 배치 데이터 (이미 저장된 JSON 파일)
batch_1_2_data = [
    {
        "id": "1",
        "name_kor": "도로롱",
        "pal_nick_kor": "#1",
        "description_kor": "언덕길을 걷다 저 혼자 데굴데굴 구른다. 결국 눈이 핑핑 돌아 몸을 못 가눌 때 간단히 처치할 수 있는 먹이 사슬의 최하층이다.",
        "elements": ["무속성"],
        "stats": {
            "egg": "평범한 알",
            "code": "SheepBall",
            "food": 150,
            "size": "XS",
            "attack": 70,
            "health": 70,
            "rarity": 1,
            "defense": 70,
            "support": 100,
            "goldCoin": 1000,
            "combiRank": 1470,
            "workSpeed": 100,
            "meleeAttack": 70,
            "maleProbability": 50,
            "captureRateCorrect": 1.5
        },
        "movement": {
            "runSpeed": 400,
            "walkSpeed": 40,
            "slowWalkSpeed": 23,
            "transportSpeed": 160,
            "rideSprintSpeed": 550
        },
        "level60Stats": {
            "attack": 441,
            "health": 3100,
            "defense": 391
        },
        "partnerSkill": {
            "name": "복슬복슬 방패",
            "level": 1,
            "describe": "발동하면 방패로 변하여 플레이어에게 장착된다. [가축 목장]에 배치하면 [양털]을(를) 떨어뜨리기도 한다.",
            "needItem": "",
            "needItemTechLevel": 0,
            "items": [
                {
                    "name": "양털",
                    "quantity": "1–3",
                    "probability": "100%"
                }
            ]
        },
        "activeSkills": [
            {
                "name": "데굴데굴 솜사탕",
                "power": 35,
                "element": "무속성",
                "coolTime": 1,
                "describe": "[도로롱] 전용 스킬. 데굴데굴 구르면서 적을 쫓아간다. 공격 후엔 눈이 핑핑 돌아 움직일 수 없게 된다.",
                "meleeAttack": True,
                "shootAttack": False,
                "accumulatedValue": 0,
                "accumulatedElement": ""
            },
            {
                "name": "공기 대포",
                "power": 25,
                "element": "무속성",
                "coolTime": 2,
                "describe": "고속으로 날아가는 공기 덩어리를 발사한다.",
                "meleeAttack": False,
                "shootAttack": False,
                "accumulatedValue": 0,
                "accumulatedElement": ""
            }
        ],
        "passiveSkills": [],
        "drops": [
            {
                "itemName": "양털",
                "quantity": "1–3",
                "probability": "100%"
            },
            {
                "itemName": "도로롱의 양고기",
                "quantity": "1",
                "probability": "100%"
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
        "tribes": [
            {
                "name": "커다란 털 뭉치 도로롱",
                "type": "Tribe Boss"
            },
            {
                "name": "도로롱",
                "type": "Tribe Normal"
            }
        ],
        "spawners": [
            {
                "area": "1_1_plain_begginer",
                "name": "도로롱",
                "level": "Lv. 1–3"
            },
            {
                "area": "1_2_plain_grass",
                "name": "도로롱",
                "level": "Lv. 1–4"
            }
        ]
    },
    {
        "id": "2",
        "name_kor": "까부냥",
        "pal_nick_kor": "#2",
        "description_kor": "얼핏 보기엔 당당하지만 실은 대단한 겁쟁이다. 까부냥이 핥아준다는 건 어떤 의미에선 최고의 굴욕이다.",
        "elements": ["무속성"],
        "stats": {
            "egg": "평범한 알",
            "code": "PinkCat",
            "food": 150,
            "size": "XS",
            "attack": 70,
            "health": 70,
            "rarity": 1,
            "defense": 70,
            "support": 100,
            "goldCoin": 1000,
            "combiRank": 1460,
            "workSpeed": 100,
            "meleeAttack": 70,
            "maleProbability": 50,
            "captureRateCorrect": 1.5
        },
        "movement": {
            "runSpeed": 400,
            "walkSpeed": 60,
            "slowWalkSpeed": 30,
            "transportSpeed": 160,
            "rideSprintSpeed": 550
        },
        "level60Stats": {
            "attack": 441,
            "health": 3100,
            "defense": 391
        },
        "partnerSkill": {
            "name": "고양이 손 빌리기",
            "level": 1,
            "describe": "보유하고 있는 동안 까부냥이 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.",
            "needItem": "",
            "needItemTechLevel": 0,
            "items": [
                {
                    "name": "소지 중량 +50 (ToTrainer)",
                    "quantity": "1",
                    "probability": "100%"
                }
            ]
        },
        "activeSkills": [
            {
                "name": "냥냥 펀치",
                "power": 40,
                "element": "무속성",
                "coolTime": 1,
                "describe": "적을 쫓아가며 양팔을 휘둘러 연속으로 펀치를 퍼붓는다.",
                "meleeAttack": True,
                "shootAttack": False,
                "accumulatedValue": 0,
                "accumulatedElement": ""
            }
        ],
        "passiveSkills": ["겁쟁이"],
        "drops": [
            {
                "itemName": "빨간 열매",
                "quantity": "1",
                "probability": "100%"
            }
        ],
        "workSuitabilities": [
            {
                "work": "수작업",
                "level": 1
            },
            {
                "work": "채집",
                "level": 1
            },
            {
                "work": "채굴",
                "level": 1
            },
            {
                "work": "운반",
                "level": 1
            }
        ],
        "tribes": [
            {
                "name": "잘난 척 대마왕 까부냥",
                "type": "Tribe Boss"
            },
            {
                "name": "까부냥",
                "type": "Tribe Normal"
            }
        ],
        "spawners": [
            {
                "area": "1_1_plain_begginer",
                "name": "까부냥",
                "level": "Lv. 1–3"
            }
        ]
    }
]

# 세 번째 배치 데이터 (차코리부터 칠테트까지)
batch_3_data = [
    {
        "id": "16",
        "name_kor": "차코리",
        "pal_nick_kor": "",
        "description_kor": "코로 추정되는 기관에서 대량의 물이 나오는데 그냥 콧물이라는 지적도 있다. 연구자들 사이에 열띤 토론이 한창이다.",
        "elements": ["물 속성"],
        "stats": {
            "egg": "축축한 알",
            "code": "Ganesha",
            "food": 150,
            "size": "M",
            "attack": 60,
            "health": 70,
            "rarity": 1,
            "defense": 70,
            "support": 100,
            "goldCoin": 1000,
            "combiRank": 1490,
            "workSpeed": 100,
            "meleeAttack": 70,
            "maleProbability": 50,
            "captureRateCorrect": 1.3
        },
        "movement": {
            "runSpeed": 300,
            "walkSpeed": 60,
            "slowWalkSpeed": 30,
            "transportSpeed": 180,
            "rideSprintSpeed": 400
        },
        "level60Stats": {
            "attack": 392,
            "health": 3100,
            "defense": 391
        },
        "partnerSkill": {
            "name": "치유의 샤워",
            "level": 1,
            "describe": "발동하면 상처에 잘 듣는 신비한 물을 뿜어 플레이어의 HP를 회복한다.",
            "needItem": "",
            "needItemTechLevel": 0,
            "items": [
                {
                    "name": "치유",
                    "quantity": "200",
                    "probability": ""
                }
            ]
        },
        "activeSkills": [
            {
                "name": "아쿠아 샷",
                "power": 40,
                "element": "물 속성",
                "coolTime": 4,
                "describe": "대상을 향해 일직선으로 날아가는 물 탄환을 발사한다.",
                "meleeAttack": False,
                "shootAttack": True,
                "accumulatedValue": 50,
                "accumulatedElement": "젖음"
            }
        ],
        "passiveSkills": [],
        "drops": [
            {
                "itemName": "팰의 체액",
                "quantity": "1",
                "probability": "100%"
            }
        ],
        "workSuitabilities": [
            {
                "work": "관개",
                "level": 1
            }
        ],
        "tribes": [
            {
                "name": "편리한 물뿌리개 차코리",
                "type": "Tribe Boss"
            },
            {
                "name": "차코리",
                "type": "Tribe Normal"
            }
        ],
        "spawners": [
            {
                "area": "1_2_plain_grass",
                "name": "차코리",
                "level": "Lv. 1–4"
            }
        ]
    }
]

# 네 번째 배치 데이터 (다크울프부터 초판다까지) - 최신 추출 데이터

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

def create_combined_csv():
    """모든 배치 데이터를 결합하여 CSV 파일로 생성"""
    
    # 추출된 모든 데이터를 통합
    all_pal_data = []
    
    # 기본 데이터 추가
    all_pal_data.extend(batch_1_2_data)
    all_pal_data.extend(batch_3_data)
    
    print(f"📊 총 {len(all_pal_data)}개의 팰 데이터를 처리합니다.")
    
    if not all_pal_data:
        print("❌ 팰 데이터가 없습니다.")
        return
        
    flattened_data = [flatten_pal_data(pal) for pal in all_pal_data]
    fieldnames = list(flattened_data[0].keys())
    
    # CSV 파일 작성
    output_file = 'pal_complete_all_batches.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flattened_data)
    
    print(f"✅ CSV 파일이 생성되었습니다: {output_file}")
    print(f"📋 총 {len(fieldnames)}개의 컬럼, {len(flattened_data)}개의 행")
    
    # 팰 ID 목록 출력
    print("\n📄 추출된 팰 목록:")
    for i, pal in enumerate(all_pal_data, 1):
        print(f"{i:2d}. ID: {pal.get('id', '')} - {pal.get('name_kor', '')}")

if __name__ == "__main__":
    create_combined_csv() 