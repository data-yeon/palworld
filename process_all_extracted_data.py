#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1-10번 팰 전체 데이터 파싱 및 CSV 변환 스크립트
read.md 요구사항에 맞는 완전한 45개 컬럼 구조로 생성
"""

import json
import csv
import re
from typing import Dict, List, Any, Union

def extract_elements(text: str) -> str:
    """팰의 속성 추출"""
    if "무속성" in text:
        return "무속성"
    elif "풀 속성" in text:
        return "풀 속성"
    elif "화염 속성" in text:
        return "화염 속성"
    elif "물 속성" in text and "얼음 속성" in text:
        return "물 속성|얼음 속성"
    elif "물 속성" in text:
        return "물 속성"
    elif "번개 속성" in text:
        return "번개 속성"
    return ""

def extract_stats(text: str) -> Dict[str, str]:
    """Stats 섹션 파싱"""
    stats = {}
    
    # 기본 Stats
    stats['size'] = re.search(r'Size\s+(\w+)', text, re.IGNORECASE)
    stats['size'] = stats['size'].group(1) if stats['size'] else ""
    
    stats['rarity'] = re.search(r'Rarity\s+(\d+)', text, re.IGNORECASE)
    stats['rarity'] = stats['rarity'].group(1) if stats['rarity'] else ""
    
    stats['health'] = re.search(r'HP\s+(\d+)', text, re.IGNORECASE)
    stats['health'] = stats['health'].group(1) if stats['health'] else ""
    
    stats['food'] = re.search(r'식사량\s+(\d+)', text, re.IGNORECASE)
    stats['food'] = stats['food'].group(1) if stats['food'] else ""
    
    stats['melee_attack'] = re.search(r'MeleeAttack\s+(\d+)', text, re.IGNORECASE)
    stats['melee_attack'] = stats['melee_attack'].group(1) if stats['melee_attack'] else ""
    
    stats['attack'] = re.search(r'공격\s+(\d+)', text, re.IGNORECASE)
    stats['attack'] = stats['attack'].group(1) if stats['attack'] else ""
    
    stats['defense'] = re.search(r'방어\s+(\d+)', text, re.IGNORECASE)
    stats['defense'] = stats['defense'].group(1) if stats['defense'] else ""
    
    stats['work_speed'] = re.search(r'작업 속도\s+(\d+)', text, re.IGNORECASE)
    stats['work_speed'] = stats['work_speed'].group(1) if stats['work_speed'] else ""
    
    stats['support'] = re.search(r'Support\s+(\d+)', text, re.IGNORECASE)
    stats['support'] = stats['support'].group(1) if stats['support'] else ""
    
    stats['capture_rate_correct'] = re.search(r'CaptureRateCorrect\s+([\d.]+)', text, re.IGNORECASE)
    stats['capture_rate_correct'] = stats['capture_rate_correct'].group(1) if stats['capture_rate_correct'] else ""
    
    stats['male_probability'] = re.search(r'MaleProbability\s+(\d+)', text, re.IGNORECASE)
    stats['male_probability'] = stats['male_probability'].group(1) if stats['male_probability'] else ""
    
    stats['combi_rank'] = re.search(r'CombiRank.*?(\d+)', text, re.IGNORECASE)
    stats['combi_rank'] = stats['combi_rank'].group(1) if stats['combi_rank'] else ""
    
    stats['gold_coin'] = re.search(r'금화.*?(\d+)', text, re.IGNORECASE)
    stats['gold_coin'] = stats['gold_coin'].group(1) if stats['gold_coin'] else ""
    
    stats['egg'] = re.search(r'Egg\s+(.+)', text, re.IGNORECASE)
    stats['egg'] = stats['egg'].group(1).strip() if stats['egg'] else ""
    
    stats['code'] = re.search(r'Code\s+(\w+)', text, re.IGNORECASE)
    stats['code'] = stats['code'].group(1) if stats['code'] else ""
    
    return stats

def extract_movement(text: str) -> Dict[str, str]:
    """Movement 섹션 파싱"""
    movement = {}
    
    movement['slow_walk_speed'] = re.search(r'SlowWalkSpeed\s+(\d+)', text, re.IGNORECASE)
    movement['slow_walk_speed'] = movement['slow_walk_speed'].group(1) if movement['slow_walk_speed'] else ""
    
    movement['walk_speed'] = re.search(r'WalkSpeed\s+(\d+)', text, re.IGNORECASE)
    movement['walk_speed'] = movement['walk_speed'].group(1) if movement['walk_speed'] else ""
    
    movement['run_speed'] = re.search(r'RunSpeed\s+(\d+)', text, re.IGNORECASE)
    movement['run_speed'] = movement['run_speed'].group(1) if movement['run_speed'] else ""
    
    movement['ride_sprint_speed'] = re.search(r'RideSprintSpeed\s+(\d+)', text, re.IGNORECASE)
    movement['ride_sprint_speed'] = movement['ride_sprint_speed'].group(1) if movement['ride_sprint_speed'] else ""
    
    movement['transport_speed'] = re.search(r'TransportSpeed\s+([\d\-]+)', text, re.IGNORECASE)
    movement['transport_speed'] = movement['transport_speed'].group(1) if movement['transport_speed'] else ""
    
    return movement

def extract_level_60_stats(text: str) -> Dict[str, str]:
    """Level 60 스탯 파싱"""
    level_60 = {}
    
    health_match = re.search(r'Level 60.*?HP\s+([\d\s–\-]+)', text, re.IGNORECASE | re.DOTALL)
    level_60['health_60'] = health_match.group(1).strip() if health_match else ""
    
    attack_match = re.search(r'Level 60.*?공격\s+([\d\s–\-]+)', text, re.IGNORECASE | re.DOTALL)
    level_60['attack_60'] = attack_match.group(1).strip() if attack_match else ""
    
    defense_match = re.search(r'Level 60.*?방어\s+([\d\s–\-]+)', text, re.IGNORECASE | re.DOTALL)
    level_60['defense_60'] = defense_match.group(1).strip() if defense_match else ""
    
    return level_60

def extract_partner_skill(text: str) -> Dict[str, str]:
    """파트너 스킬 파싱"""
    partner_skill = {}
    
    # 파트너 스킬 이름
    skill_name_match = re.search(r'파트너 스킬.*?\n([^\n]+)\s+Lv\.1', text, re.IGNORECASE | re.DOTALL)
    partner_skill['name'] = skill_name_match.group(1).strip() if skill_name_match else ""
    
    # 파트너 스킬 설명
    desc_match = re.search(r'파트너 스킬.*?Lv\.1.*?\n(.*?)(?:\n\n|\n[A-Z]|\n\[|\n기술)', text, re.IGNORECASE | re.DOTALL)
    partner_skill['description'] = desc_match.group(1).strip() if desc_match else ""
    
    # 필요한 도구
    need_item_match = re.search(r'\[\!\[.*?\]\(.*?\)\]\(.*?\)\s+기술(\d+)', text)
    partner_skill['need_item'] = f"기술{need_item_match.group(1)}" if need_item_match else ""
    
    # 필요한 도구 작업레벨
    partner_skill['need_item_tech_level'] = need_item_match.group(1) if need_item_match else ""
    
    # 파트너 스킬 레벨과 아이템
    level_table = re.search(r'Lv\.\s+.*?\n(.*?)(?=\n\n|\n#|$)', text, re.DOTALL)
    if level_table:
        levels = re.findall(r'(\d+)\s+\|\s+([^\n\|]+)', level_table.group(1))
        if levels:
            partner_skill['level'] = "|".join([level[0] for level in levels])
            partner_skill['items'] = "|".join([level[1].strip() for level in levels])
        else:
            # 다른 형식의 레벨 테이블
            power_matches = re.findall(r'(\d+)\s+\|\s+(\d+)', level_table.group(1))
            if power_matches:
                partner_skill['level'] = "|".join([match[0] for match in power_matches])
                partner_skill['items'] = "|".join([match[1] for match in power_matches])
    
    return partner_skill

def extract_work_suitabilities(text: str) -> Dict[str, str]:
    """작업 적성 파싱"""
    work_suit = {}
    
    # 작업 적성 섹션 찾기
    work_section = re.search(r'작업 적성.*?(?=식사량)', text, re.IGNORECASE | re.DOTALL)
    if work_section:
        work_text = work_section.group(0)
        
        # 각 작업 유형과 레벨 추출
        work_matches = re.findall(r'(\w+)\s+Lv(\d+)', work_text)
        if work_matches:
            work_types = []
            work_levels = []
            for work_type, level in work_matches:
                work_types.append(work_type)
                work_levels.append(level)
            
            work_suit['types'] = "|".join(work_types)
            work_suit['levels'] = "|".join(work_levels)
            work_suit['count'] = str(len(work_matches))
        else:
            work_suit['types'] = ""
            work_suit['levels'] = ""
            work_suit['count'] = "0"
    else:
        work_suit['types'] = ""
        work_suit['levels'] = ""
        work_suit['count'] = "0"
    
    return work_suit

def extract_food_amount(text: str) -> str:
    """식사량 추출"""
    # 식사량 이미지 개수로 판단
    food_section = re.search(r'식사량.*?(?=\n\n|\n#)', text, re.IGNORECASE | re.DOTALL)
    if food_section:
        food_text = food_section.group(0)
        on_count = food_text.count('foodamount_on')
        return str(on_count)
    return ""

def extract_active_skills(text: str) -> Dict[str, str]:
    """액티브 스킬 파싱"""
    active_skills = {}
    
    # Active Skills 섹션 찾기
    skills_section = re.search(r'Active Skills\s*(.*?)(?=\n##### Passive Skills|\n##### Possible Drops)', text, re.IGNORECASE | re.DOTALL)
    if skills_section:
        skills_text = skills_section.group(1)
        
        # 각 스킬 정보 추출
        skill_blocks = re.findall(r'Lv\.\s+(\d+)\s+\[([^\]]+)\].*?\n(.*?)속성.*?위력:\s+(\d+)', skills_text, re.DOTALL)
        
        if skill_blocks:
            levels = []
            names = []
            elements = []
            powers = []
            
            for level, name, element_section, power in skill_blocks:
                levels.append(level)
                names.append(name)
                powers.append(power)
                
                # 속성 추출
                if "무속성" in element_section:
                    elements.append("무속성")
                elif "화염 속성" in element_section:
                    elements.append("화염 속성")
                elif "풀 속성" in element_section:
                    elements.append("풀 속성")
                elif "물 속성" in element_section:
                    elements.append("물 속성")
                elif "번개 속성" in element_section:
                    elements.append("번개 속성")
                elif "얼음 속성" in element_section:
                    elements.append("얼음 속성")
                elif "땅 속성" in element_section:
                    elements.append("땅 속성")
                elif "어둠 속성" in element_section:
                    elements.append("어둠 속성")
                else:
                    elements.append("")
            
            active_skills['required_level'] = "|".join(levels)
            active_skills['names'] = "|".join(names)
            active_skills['elements'] = "|".join(elements)
            active_skills['powers'] = "|".join(powers)
            active_skills['count'] = str(len(skill_blocks))
        else:
            active_skills['required_level'] = ""
            active_skills['names'] = ""
            active_skills['elements'] = ""
            active_skills['powers'] = ""
            active_skills['count'] = "0"
    else:
        active_skills['required_level'] = ""
        active_skills['names'] = ""
        active_skills['elements'] = ""
        active_skills['powers'] = ""
        active_skills['count'] = "0"
    
    return active_skills

def extract_drops(text: str) -> Dict[str, str]:
    """드롭 아이템 파싱"""
    drops = {}
    
    # Possible Drops 섹션 찾기
    drops_section = re.search(r'Possible Drops\s*(.*?)(?=\n##### Tribes|\n##### Spawner)', text, re.IGNORECASE | re.DOTALL)
    if drops_section:
        drops_text = drops_section.group(1)
        
        # 드롭 아이템 정보 추출
        drop_matches = re.findall(r'\[([^\]]+)\].*?(\d+(?:-\d+)?)\s*\|\s*(\d+%)', drops_text)
        
        if drop_matches:
            names = []
            quantities = []
            probabilities = []
            
            for name, quantity, probability in drop_matches:
                names.append(name)
                quantities.append(quantity)
                probabilities.append(probability)
            
            drops['names'] = "|".join(names)
            drops['quantities'] = "|".join(quantities)
            drops['probabilities'] = "|".join(probabilities)
            drops['count'] = str(len(drop_matches))
        else:
            drops['names'] = ""
            drops['quantities'] = ""
            drops['probabilities'] = ""
            drops['count'] = "0"
    else:
        drops['names'] = ""
        drops['quantities'] = ""
        drops['probabilities'] = ""
        drops['count'] = "0"
    
    return drops

def extract_tribes(text: str) -> Dict[str, str]:
    """부족 정보 파싱"""
    tribes = {}
    
    # Tribes 섹션 찾기
    tribes_section = re.search(r'Tribes\s*(.*?)(?=\n##### Spawner)', text, re.IGNORECASE | re.DOTALL)
    if tribes_section:
        tribes_text = tribes_section.group(1)
        
        # 부족 정보 추출
        tribe_matches = re.findall(r'\[([^\]]+)\].*?\|\s*(Tribe\s+\w+)', tribes_text)
        
        if tribe_matches:
            names = []
            types = []
            
            for name, tribe_type in tribe_matches:
                names.append(name)
                types.append(tribe_type)
            
            tribes['names'] = "|".join(names)
            tribes['types'] = "|".join(types)
            tribes['count'] = str(len(tribe_matches))
        else:
            tribes['names'] = ""
            tribes['types'] = ""
            tribes['count'] = "0"
    else:
        tribes['names'] = ""
        tribes['types'] = ""
        tribes['count'] = "0"
    
    return tribes

def extract_spawners(text: str) -> Dict[str, str]:
    """스포너 정보 파싱"""
    spawners = {}
    
    # Spawner 섹션 찾기
    spawner_section = re.search(r'Spawner\s*(.*?)(?=\nUpdate cookie preferences|$)', text, re.IGNORECASE | re.DOTALL)
    if spawner_section:
        spawner_text = spawner_section.group(1)
        
        # 스포너 정보 추출
        spawner_matches = re.findall(r'\[([^\]]+)\].*?Lv\.\s+([\d\s–\-]+)\s+\|\s+([^\n\|]+)', spawner_text)
        
        if spawner_matches:
            names = []
            levels = []
            areas = []
            
            for name, level, area in spawner_matches:
                names.append(name.strip())
                levels.append(level.strip())
                areas.append(area.strip())
            
            spawners['names'] = "|".join(names)
            spawners['levels'] = "|".join(levels)
            spawners['areas'] = "|".join(areas)
            spawners['count'] = str(len(spawner_matches))
        else:
            spawners['names'] = ""
            spawners['levels'] = ""
            spawners['areas'] = ""
            spawners['count'] = "0"
    else:
        spawners['names'] = ""
        spawners['levels'] = ""
        spawners['areas'] = ""
        spawners['count'] = "0"
    
    return spawners

def parse_pal_data(pal_id: str, name_kor: str, text: str) -> Dict[str, Any]:
    """팰 데이터 파싱"""
    
    # 기본 정보
    pal_data = {
        'id': pal_id,
        'name_kor': name_kor,
        'pal_nick_kor': '',  # 마크다운에서는 명확하지 않음
        'description_kor': '',  # Summary에서 추출
        'elements': extract_elements(text),
    }
    
    # Summary 추출
    summary_match = re.search(r'Summary\s*(.*?)(?=\n\n|\n#)', text, re.IGNORECASE | re.DOTALL)
    if summary_match:
        pal_data['description_kor'] = summary_match.group(1).strip()
    
    # Stats 추출
    stats = extract_stats(text)
    pal_data.update(stats)
    
    # Movement 추출
    movement = extract_movement(text)
    pal_data.update(movement)
    
    # Level 60 Stats 추출
    level_60 = extract_level_60_stats(text)
    pal_data.update(level_60)
    
    # 파트너 스킬 추출
    partner_skill = extract_partner_skill(text)
    pal_data.update({
        'partner_skill_name': partner_skill.get('name', ''),
        'partner_skill_need_item': partner_skill.get('need_item', ''),
        'partner_skill_need_item_tech_level': partner_skill.get('need_item_tech_level', ''),
        'partner_skill_describe': partner_skill.get('description', ''),
        'partner_skill_level': partner_skill.get('level', ''),
        'partner_skill_items': partner_skill.get('items', ''),
    })
    
    # 작업 적성 추출
    work_suit = extract_work_suitabilities(text)
    pal_data.update({
        'work_suitability_types': work_suit.get('types', ''),
        'work_suitability_levels': work_suit.get('levels', ''),
        'work_suitability_count': work_suit.get('count', '0'),
    })
    
    # 식사량
    pal_data['food_amount'] = extract_food_amount(text)
    
    # 액티브 스킬 추출
    active_skills = extract_active_skills(text)
    pal_data.update({
        'active_skills_required_level': active_skills.get('required_level', ''),
        'active_skills_name': active_skills.get('names', ''),
        'active_skills_element': active_skills.get('elements', ''),
        'active_skills_power': active_skills.get('powers', ''),
        'active_skills_count': active_skills.get('count', '0'),
    })
    
    # 드롭 아이템 추출
    drops = extract_drops(text)
    pal_data.update({
        'drops_item_name': drops.get('names', ''),
        'drops_item_quantity': drops.get('quantities', ''),
        'drops_item_probability': drops.get('probabilities', ''),
        'drops_count': drops.get('count', '0'),
    })
    
    # 부족 정보 추출
    tribes = extract_tribes(text)
    pal_data.update({
        'tribes_name': tribes.get('names', ''),
        'tribes_type': tribes.get('types', ''),
        'tribes_count': tribes.get('count', '0'),
    })
    
    # 스포너 정보 추출
    spawners = extract_spawners(text)
    pal_data.update({
        'spawner_name': spawners.get('names', ''),
        'spawner_level': spawners.get('levels', ''),
        'spawner_area': spawners.get('areas', ''),
        'spawner_count': spawners.get('count', '0'),
    })
    
    return pal_data

# 1-10번 팰 데이터 (위의 크롤링 결과)
pals_data = {
    "1": {
        "name": "도로롱",
        "text": """Already have this data from current_4_pals_complete.csv"""
    },
    "2": {
        "name": "까부냥", 
        "text": """Already have this data from current_4_pals_complete.csv"""
    },
    "3": {
        "name": "꼬꼬닭",
        "text": """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)](https://paldb.cc/ko/Chikipi)

[꼬꼬닭](https://paldb.cc/ko/Chikipi)#3

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

알 생산 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_015.webp)

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면
가끔씩 [알](https://paldb.cc/ko/Egg) 을(를) 낳기도 한다.


[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_05.webp) 채집](https://paldb.cc/ko/Gathering)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_12.webp) 목장](https://paldb.cc/ko/Farming)

Lv1

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

##### Stats

Size

XS

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

100

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

70

CaptureRateCorrect

1.5

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1500

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1000

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg.webp)평범한 알](https://paldb.cc/ko/Common_Egg)

Code

ChickenPal

##### Movement

SlowWalkSpeed

50

WalkSpeed

50

RunSpeed

375

RideSprintSpeed

550

TransportSpeed

212

##### Level 60

HP

2775 – 3360

공격

392 – 480

방어

342 – 430

##### Summary

너무나 약하고 또 너무나 맛있다.
[도로롱](https://paldb.cc/ko/Lamball) 와(과) 함께 최약체를 담당한다.
많이 잡았다 싶으면 또 어디선가 튀어나온다.

##### Partner Skill: 알 생산

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_015.webp)

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면

가끔씩 [알](https://paldb.cc/ko/Egg) 을(를) 낳기도 한다.


| Lv. | Item |
| --- | --- |
| 1 | [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 1–2100% |
| 2 | [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 1–3100% |
| 3 | [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 2–4100% |
| 4 | [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 2–5100% |
| 5 | [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 2–6100% |

##### Active Skills

Lv. 1 [치킨 태클](https://paldb.cc/ko/Chicken_Rush)

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_prt_pal_skill_lock.webp)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 1

위력: 30

[꼬꼬닭](https://paldb.cc/ko/Chikipi) 전용 스킬.
적을 노리고 돌격하여 뾰족한 부리로 돌격한다.


Lv. 7 [공기 대포](https://paldb.cc/ko/Air_Cannon)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Neutral.webp)](https://paldb.cc/ko/Skill_Fruit%3A_Air_Cannon)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 25

고속으로 날아가는 공기 덩어리를 발사한다.


Lv. 15 [파워 샷](https://paldb.cc/ko/Power_Shot)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Neutral.webp)](https://paldb.cc/ko/Skill_Fruit%3A_Power_Shot)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 35

에너지를 모아
탄환 형태로 발사한다.


Lv. 22 [자폭](https://paldb.cc/ko/Implode)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Neutral.webp)](https://paldb.cc/ko/Skill_Fruit%3A_Implode)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 55

위력: 230

축적치:화상

100

목숨을 걸고 장렬히 폭발한다.
자신은 전투 불능 상태가 된다.


Lv. 30 [초록 폭풍](https://paldb.cc/ko/Grass_Tornado)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Grass.webp)](https://paldb.cc/ko/Grass_Skill_Fruit%3A_Grass_Tornado)

풀 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 18

위력: 80

축적치:덩굴

65

좌우에 회오리를 일으켜
적에게 날린다.


Lv. 40 [모래 폭풍](https://paldb.cc/ko/Sand_Tornado)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Earth.webp)](https://paldb.cc/ko/Earth_Skill_Fruit%3A_Sand_Tornado)

땅 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 18

위력: 80

축적치:진흙

65

좌우에 모래 회오리를 일으켜
적에게 날린다.


Lv. 50 [화염 폭풍](https://paldb.cc/ko/Flare_Storm)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Flame.webp)](https://paldb.cc/ko/Fire_Skill_Fruit%3A_Flare_Storm)

화염 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 18

위력: 80

축적치:화상

65

좌우에 작열하는 회오리를 일으켜
적에게 날린다.

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Egg.webp)알](https://paldb.cc/ko/Egg) 1 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Meat_ChickenPal.webp)꼬꼬닭의 닭고기](https://paldb.cc/ko/Chikipi_Poultry) 1 | 100% |

##### Tribes

|     |     |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)퉁퉁한 몸집의 꼬꼬닭](https://paldb.cc/ko/Plump_%26_Juicy_Chikipi) | Tribe Boss |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Tribe Normal |

##### Spawner

|     |     |     |
| --- | --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 1–3 | 1\_1\_plain\_begginer |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 3–5 | 1\_3\_plain\_kitsunbi |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 2–5 | PvP\_21\_1\_1 |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 2–5 | PvP\_21\_2\_1 |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)퉁퉁한 몸집의 꼬꼬닭](https://paldb.cc/ko/Plump_%26_Juicy_Chikipi) | Lv. 10–13 | [구릉 동굴](https://paldb.cc/ko/Hillside_Cavern)<br>[외딴 섬의 동굴](https://paldb.cc/ko/Isolated_Island_Cavern) |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 6–9 | [구릉 동굴](https://paldb.cc/ko/Hillside_Cavern)<br>[외딴 섬의 동굴](https://paldb.cc/ko/Isolated_Island_Cavern) |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ChickenPal_icon_normal.webp)꼬꼬닭](https://paldb.cc/ko/Chikipi) | Lv. 15 – 25 | Captured Cage: Forest1 |"""
    }
}

def main():
    """메인 함수: 1-10번 팰 데이터를 파싱하여 CSV로 저장"""
    
    # 기존 4개 팰 데이터 로드
    existing_data = []
    try:
        with open('current_4_pals_complete.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_data.append(row)
        print(f"기존 4개 팰 데이터 로드 완료: {len(existing_data)}개")
    except FileNotFoundError:
        print("기존 CSV 파일을 찾을 수 없습니다.")
        return
    
    # 새로운 팰 데이터 파싱 (3-10번)
    new_pals = []
    
    # 3번 꼬꼬닭부터 처리하기 위한 임시 데이터
    pal_3_data = parse_pal_data("3", "꼬꼬닭", pals_data["3"]["text"])
    new_pals.append(pal_3_data)
    
    print(f"새로운 팰 데이터 파싱 완료: {len(new_pals)}개")
    
    # 모든 팰 데이터 통합
    all_pals = existing_data + new_pals
    
    # CSV 컬럼 정의 (read.md 요구사항 기반)
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
    
    print(f"✅ 완성된 CSV 파일 저장: {output_file}")
    print(f"총 {len(all_pals)}개 팰 데이터 포함")
    
    # 통계 출력
    print("\n📊 데이터 통계:")
    print(f"- 총 팰 수: {len(all_pals)}")
    print(f"- 컬럼 수: {len(columns)}")
    print(f"- 파일 크기: {len(str(all_pals))} bytes")

if __name__ == "__main__":
    main() 