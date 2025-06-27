#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import csv

# 크롤링된 팰 데이터 저장
pals_data = {
    "11": {
        "name_kor": "펭킹",
        "elements": "물|얼음",
        "markdown": """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_CaptainPenguin_icon_normal.webp)](https://paldb.cc/ko/Penking)

[펭킹](https://paldb.cc/ko/Penking)#11

물 속성

얼음 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

용감한 바다의 전사 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_014.webp)

함께 싸우는 동안 화염 속성 팰을 쓰러뜨렸을 때
드롭 아이템 획득량이 증가한다.

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_01.webp) 관개](https://paldb.cc/ko/Watering)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_04.webp) 수작업](https://paldb.cc/ko/Handiwork)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_07.webp) 채굴](https://paldb.cc/ko/Mining)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_10.webp) 냉각](https://paldb.cc/ko/Cooling)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_11.webp) 운반](https://paldb.cc/ko/Transporting)

Lv2

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

##### Stats

Size

L

Rarity

6

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

95

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

525

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

95

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

95

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

520

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

5410

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Water_01.webp)축축한 대형 알](https://paldb.cc/ko/Large_Damp_Egg)

Code

CaptainPenguin

##### Movement

SlowWalkSpeed

50

WalkSpeed

110

RunSpeed

450

RideSprintSpeed

600

TransportSpeed

280

##### Level 60

HP

3912 – 4838

공격

563 – 702

방어

513 – 652

##### Active Skills

Lv. 1 [아쿠아 샷](https://paldb.cc/ko/Aqua_Gun)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Water.webp)](https://paldb.cc/ko/Water_Skill_Fruit%3A_Aqua_Gun)

물 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 40

축적치:젖음

50

대상을 향해 일직선으로 날아가는
물 탄환을 발사한다.

Lv. 7 [빙산](https://paldb.cc/ko/Iceberg)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Frost.webp)](https://paldb.cc/ko/Ice_Skill_Fruit%3A_Iceberg)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 15

위력: 70

축적치:빙결

100

적의 발 밑에
날카로운 얼음칼을 불러낸다.

Lv. 15 [캡틴 슬라이딩](https://paldb.cc/ko/Emperor_Slide)

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_prt_pal_skill_lock.webp)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 10

위력: 70

축적치:빙결

50

[펭킹](https://paldb.cc/ko/Penking) 전용 스킬.
땅에 배를 붙이고 온몸으로 냉기를 발산하여
적을 향해 미끄러지며 부딪친다.

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_IceOrgan.webp)빙결 기관](https://paldb.cc/ko/Ice_Organ) 1–3 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalItem_CaptainPenguin.webp)펭킹 날개 장식](https://paldb.cc/ko/Penking_Plume) 1 | 50% |

##### Summary

사실 [펭키](https://paldb.cc/ko/Pengullet) 와(과) 아무 연관도 없는 종.
멋대로 상전 대접을 받은 터라
일단 열심히 뻗대고 보고 있다.
"""
    },
    "11B": {
        "name_kor": "펭키드",
        "elements": "물|번개",
        "markdown": """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_CaptainPenguin_Black_icon_normal.webp)](https://paldb.cc/ko/Penking_Lux)

[펭키드](https://paldb.cc/ko/Penking_Lux)#11B

물 속성

번개 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

불굴의 전격 수장 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_014.webp)

함께 싸우는 동안 물 속성 팰을 쓰러뜨렸을 때
드롭 아이템 획득량이 증가한다.

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_01.webp) 관개](https://paldb.cc/ko/Watering)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_03.webp) 발전](https://paldb.cc/ko/Generating_Electricity)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_04.webp) 수작업](https://paldb.cc/ko/Handiwork)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_07.webp) 채굴](https://paldb.cc/ko/Mining)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_11.webp) 운반](https://paldb.cc/ko/Transporting)

Lv2

##### Stats

Size

L

Rarity

7

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

525

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

100

##### Summary

수중 사냥에 도움이 되도록 전기의 힘을 얻어 색이 변화했으며
그 결과 [펭키](https://paldb.cc/ko/Pengullet) 의 충성을 잃고 말았다.
그러나 어째서인지는 몰라도
이번에는 [뎅키](https://paldb.cc/ko/Pengullet_Lux) 의 충성을 얻게 되었다.
"""
    },
    "12": {
        "name_kor": "찌릿도치",
        "elements": "번개",
        "markdown": """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Hedgehog_icon_normal.webp)](https://paldb.cc/ko/Jolthog)

[찌릿도치](https://paldb.cc/ko/Jolthog)#12

번개 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

찌르르 폭탄 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 [찌릿도치](https://paldb.cc/ko/Jolthog) 을(를) 손에 장착하며
적에게 던져 착탄할 시 번개 폭발을 일으킨다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Gloves.webp)](https://paldb.cc/ko/Jolthogs_Gloves) 기술8

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_03.webp) 발전](https://paldb.cc/ko/Generating_Electricity)

Lv1

##### Stats

Size

XS

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

##### Summary

충격을 받으면 모았던 전기를 방출한다.
그 전압은 1,000만 볼트가 넘는다.
던지면 어설픈 중화기보다 더 위험하다.
"""
    },
    "12B": {
        "name_kor": "코치도치",
        "elements": "얼음",
        "markdown": """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Hedgehog_Ice_icon_normal.webp)](https://paldb.cc/ko/Jolthog_Cryst)

[코치도치](https://paldb.cc/ko/Jolthog_Cryst)#12B

얼음 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

딱딱 폭탄 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 [코치도치](https://paldb.cc/ko/Jolthog_Cryst) 을(를) 손에 장착하며
적에게 던져 착탄할 시 얼음 폭발을 일으킨다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Gloves.webp)](https://paldb.cc/ko/Jolthog_Crysts_Gloves) 기술11

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_10.webp) 냉각](https://paldb.cc/ko/Cooling)

Lv1

##### Stats

Size

XS

Rarity

2

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

##### Summary

충격을 받으면 모았던 냉기를 방출한다.
방사상에 퍼진 냉기는 대기를 꽁꽁 얼려
습격해온 상대의 몸을 꿰뚫는다.
"""
    }
}

def parse_pal_stats_from_markdown(markdown_content):
    """마크다운에서 팰 스탯 정보를 추출"""
    
    def get_value_after_label(label, text):
        pattern = rf'{re.escape(label)}\s*\n\s*([^\n]+)'
        match = re.search(pattern, text)
        return match.group(1).strip() if match else ""
    
    def count_food_icons(text):
        on_count = text.count('T_Icon_foodamount_on.webp')
        return str(on_count)
    
    def extract_work_suitabilities(text):
        # 작업 적성 섹션 찾기
        work_section_match = re.search(r'\[작업 적성\].*?(?=\n#|$)', text, re.DOTALL)
        if not work_section_match:
            return {}
        
        work_section = work_section_match.group(0)
        suitabilities = {}
        
        # 각 작업 유형과 레벨 추출
        work_patterns = {
            '불 피우기': r'불 피우기.*?Lv(\d+)',
            '관개': r'관개.*?Lv(\d+)',
            '파종': r'파종.*?Lv(\d+)',
            '발전': r'발전.*?Lv(\d+)',
            '수작업': r'수작업.*?Lv(\d+)',
            '채집': r'채집.*?Lv(\d+)',
            '벌목': r'벌목.*?Lv(\d+)',
            '채굴': r'채굴.*?Lv(\d+)',
            '제약': r'제약.*?Lv(\d+)',
            '냉각': r'냉각.*?Lv(\d+)',
            '운반': r'운반.*?Lv(\d+)',
            '목장': r'목장.*?Lv(\d+)'
        }
        
        for work_name, pattern in work_patterns.items():
            match = re.search(pattern, work_section)
            if match:
                suitabilities[work_name] = match.group(1)
            else:
                suitabilities[work_name] = ""
        
        return suitabilities
    
    def extract_partner_skill(text):
        # 파트너 스킬 정보 추출
        partner_match = re.search(r'\[파트너 스킬\].*?\n\n([^\n]+).*?\n\n([^#]+?)(?=\n#|\[작업 적성\])', text, re.DOTALL)
        if partner_match:
            skill_name = partner_match.group(1).strip()
            # 기술 레벨 정보가 있는지 확인
            tech_match = re.search(r'기술(\d+)', partner_match.group(2))
            tech_level = tech_match.group(1) if tech_match else ""
            skill_desc = re.sub(r'기술\d+', '', partner_match.group(2)).strip()
            return skill_name, skill_desc, "", tech_level
        return "", "", "", ""
    
    def extract_active_skills(text):
        # 액티브 스킬 섹션 찾기
        skills_match = re.search(r'##### Active Skills.*?(?=##### |$)', text, re.DOTALL)
        
        # 기본값으로 빈 리스트 초기화
        required_levels = [""] * 7
        skill_names = [""] * 7
        elements = [""] * 7
        cool_times = [""] * 7
        powers = [""] * 7
        descriptions = [""] * 7
        
        if not skills_match:
            return (required_levels, skill_names, elements, cool_times, 
                    powers, descriptions, [""] * 7, [""] * 7)
        
        skills_section = skills_match.group(0)
        
        # 개별 스킬 정보 추출
        skill_patterns = re.finditer(r'Lv\. (\d+) \[([^\]]+)\]', skills_section)
        
        skill_index = 0
        for match in skill_patterns:
            if skill_index >= 7:  # 최대 7개까지
                break
                
            required_levels[skill_index] = match.group(1)
            skill_names[skill_index] = match.group(2)
            
            # 더 세부적인 정보는 스킬 블록에서 추출
            skill_block_start = match.start()
            skill_block_end = skills_section.find('Lv.', skill_block_start + 1)
            if skill_block_end == -1:
                skill_block_end = len(skills_section)
            
            skill_block = skills_section[skill_block_start:skill_block_end]
            
            # 속성 추출
            element_match = re.search(r'(무속성|화염 속성|물 속성|번개 속성|풀 속성|어둠 속성|용 속성|땅 속성|얼음 속성)', skill_block)
            elements[skill_index] = element_match.group(1).replace(' 속성', '') if element_match else ""
            
            # 쿨타임 추출
            cool_match = re.search(r'웝: (\d+)', skill_block)
            cool_times[skill_index] = cool_match.group(1) if cool_match else ""
            
            # 위력 추출
            power_match = re.search(r'위력: (\d+)', skill_block)
            powers[skill_index] = power_match.group(1) if power_match else ""
            
            # 설명 추출 (더 간단하게)
            desc_match = re.search(r'위력: \d+.*?\n\n([^#]+?)(?=\n\n|Lv\.|$)', skill_block, re.DOTALL)
            if desc_match:
                descriptions[skill_index] = desc_match.group(1).strip()
            else:
                descriptions[skill_index] = ""
            
            skill_index += 1
        
        return (required_levels, skill_names, elements, cool_times, 
                powers, descriptions, [""] * 7, [""] * 7)  # 마지막 두 리스트는 빈 값
    
    def extract_drops(text):
        # 드롭 정보 추출
        drops_match = re.search(r'##### Possible Drops.*?(?=##### |$)', text, re.DOTALL)
        if not drops_match:
            return [], []
        
        drops_section = drops_match.group(0)
        
        items = []
        probabilities = []
        
        # 드롭 아이템 패턴 찾기
        drop_patterns = re.finditer(r'\[\!\[.*?\]\(.*?\)\]\([^)]+\)\s*([^|]+?)\s*\|\s*([^|]+)', drops_section)
        
        for match in drop_patterns:
            item_name = re.sub(r'\s*\d+[-–]\d+', '', match.group(1)).strip()
            probability = match.group(2).strip()
            
            items.append(item_name)
            probabilities.append(probability)
        
        return items, probabilities
    
    # 기본 정보 추출
    name_match = re.search(r'\[([^\]]+)\].*?#(\d+[A-Z]*)', markdown_content)
    pal_id = name_match.group(2) if name_match else ""
    name_kor = name_match.group(1) if name_match else ""
    
    # 속성 추출
    elements = []
    element_patterns = [
        '무속성', '화염 속성', '물 속성', '번개 속성', 
        '풀 속성', '어둠 속성', '용 속성', '땅 속성', '얼음 속성'
    ]
    for element in element_patterns:
        if element in markdown_content:
            elements.append(element.replace(' 속성', ''))
    
    # 설명 추출
    summary_match = re.search(r'##### Summary\n\n([^#]+?)(?=\n#|$)', markdown_content, re.DOTALL)
    description_kor = summary_match.group(1).strip() if summary_match else ""
    
    # 스탯 추출
    size = get_value_after_label("Size", markdown_content)
    rarity = get_value_after_label("Rarity", markdown_content)
    health = re.search(r'HP\n\n(\d+)', markdown_content)
    health = health.group(1) if health else ""
    
    food = count_food_icons(markdown_content)
    
    melee_attack = get_value_after_label("MeleeAttack", markdown_content)
    attack = re.search(r'공격\n\n(\d+)', markdown_content)
    attack = attack.group(1) if attack else ""
    
    defense = re.search(r'방어\n\n(\d+)', markdown_content)
    defense = defense.group(1) if defense else ""
    
    work_speed = get_value_after_label("작업 속도", markdown_content)
    support = get_value_after_label("Support", markdown_content)
    capture_rate = get_value_after_label("CaptureRateCorrect", markdown_content)
    male_prob = get_value_after_label("MaleProbability", markdown_content)
    combi_rank = get_value_after_label("CombiRank", markdown_content)
    
    # 금화 추출
    gold_match = re.search(r'금화.*?\n\n(\d+)', markdown_content)
    gold_coin = gold_match.group(1) if gold_match else ""
    
    # 알 정보 추출
    egg_match = re.search(r'Egg\n\n.*?\]([^)]+)', markdown_content)
    egg = egg_match.group(1).strip('()') if egg_match else ""
    
    # Code 추출
    code = get_value_after_label("Code", markdown_content)
    
    # Movement 정보 추출
    slow_walk = get_value_after_label("SlowWalkSpeed", markdown_content)
    walk_speed = get_value_after_label("WalkSpeed", markdown_content)
    run_speed = get_value_after_label("RunSpeed", markdown_content)
    ride_sprint = get_value_after_label("RideSprintSpeed", markdown_content)
    transport_speed = get_value_after_label("TransportSpeed", markdown_content)
    
    # Level 60 정보 추출
    level60_match = re.search(r'##### Level 60.*?HP\n\n([^\n]+).*?공격\n\n([^\n]+).*?방어\n\n([^\n]+)', markdown_content, re.DOTALL)
    if level60_match:
        level60_health = level60_match.group(1).strip()
        level60_attack = level60_match.group(2).strip()  
        level60_defense = level60_match.group(3).strip()
    else:
        level60_health = level60_attack = level60_defense = ""
    
    # 작업 적성 추출
    work_suitabilities = extract_work_suitabilities(markdown_content)
    
    # 파트너 스킬 추출
    partner_name, partner_desc, partner_item, partner_tech = extract_partner_skill(markdown_content)
    
    # 액티브 스킬 추출
    skill_data = extract_active_skills(markdown_content)
    if len(skill_data) >= 6:
        (skill_levels, skill_names, skill_elements, skill_cool_times, 
         skill_powers, skill_descriptions, _, _) = skill_data
    else:
        # 빈 데이터로 초기화
        skill_levels = [""] * 7
        skill_names = [""] * 7
        skill_elements = [""] * 7
        skill_cool_times = [""] * 7
        skill_powers = [""] * 7
        skill_descriptions = [""] * 7
    
    # 드롭 아이템 추출
    drop_items, drop_probabilities = extract_drops(markdown_content)
    
    return {
        'id': pal_id,
        'name_kor': name_kor,
        'description_kor': description_kor,
        'elements': '|'.join(elements),
        'size': size,
        'rarity': rarity,
        'health': health,
        'food': food,
        'melee_attack': melee_attack,
        'attack': attack,
        'defense': defense,
        'work_speed': work_speed,
        'support': support,
        'capture_rate_correct': capture_rate,
        'male_probability': male_prob,
        'combi_rank': combi_rank,
        'gold_coin': gold_coin,
        'egg': egg,
        'code': code,
        'slow_walk_speed': slow_walk,
        'walk_speed': walk_speed,
        'run_speed': run_speed,
        'ride_sprint_speed': ride_sprint,
        'transport_speed': transport_speed,
        'level60_health': level60_health,
        'level60_attack': level60_attack,
        'level60_defense': level60_defense,
        'partner_skill_name': partner_name,
        'partner_skill_describe': partner_desc,
        'partner_skill_need_item': partner_item,
        'partner_skill_need_item_tech_level': partner_tech,
        'work_kindling': work_suitabilities.get('불 피우기', ''),
        'work_watering': work_suitabilities.get('관개', ''),
        'work_seeding': work_suitabilities.get('파종', ''),
        'work_generating_electricity': work_suitabilities.get('발전', ''),
        'work_handiwork': work_suitabilities.get('수작업', ''),
        'work_gathering': work_suitabilities.get('채집', ''),
        'work_lumbering': work_suitabilities.get('벌목', ''),
        'work_mining': work_suitabilities.get('채굴', ''),
        'work_medicine_production': work_suitabilities.get('제약', ''),
        'work_cooling': work_suitabilities.get('냉각', ''),
        'work_transporting': work_suitabilities.get('운반', ''),
        'work_farming': work_suitabilities.get('목장', ''),
        'active_skills_required_level_1': skill_levels[0],
        'active_skills_name_1': skill_names[0],
        'active_skills_element_1': skill_elements[0],
        'active_skills_cool_time_1': skill_cool_times[0],
        'active_skills_power_1': skill_powers[0],
        'active_skills_describe_1': skill_descriptions[0],
        'active_skills_required_level_2': skill_levels[1],
        'active_skills_name_2': skill_names[1],
        'active_skills_element_2': skill_elements[1],
        'active_skills_cool_time_2': skill_cool_times[1],
        'active_skills_power_2': skill_powers[1],
        'active_skills_describe_2': skill_descriptions[1],
        'active_skills_required_level_3': skill_levels[2],
        'active_skills_name_3': skill_names[2],
        'active_skills_element_3': skill_elements[2],
        'active_skills_cool_time_3': skill_cool_times[2],
        'active_skills_power_3': skill_powers[2],
        'active_skills_describe_3': skill_descriptions[2],
        'active_skills_required_level_4': skill_levels[3],
        'active_skills_name_4': skill_names[3],
        'active_skills_element_4': skill_elements[3],
        'active_skills_cool_time_4': skill_cool_times[3],
        'active_skills_power_4': skill_powers[3],
        'active_skills_describe_4': skill_descriptions[3],
        'active_skills_required_level_5': skill_levels[4],
        'active_skills_name_5': skill_names[4],
        'active_skills_element_5': skill_elements[4],
        'active_skills_cool_time_5': skill_cool_times[4],
        'active_skills_power_5': skill_powers[4],
        'active_skills_describe_5': skill_descriptions[4],
        'active_skills_required_level_6': skill_levels[5],
        'active_skills_name_6': skill_names[5],
        'active_skills_element_6': skill_elements[5],
        'active_skills_cool_time_6': skill_cool_times[5],
        'active_skills_power_6': skill_powers[5],
        'active_skills_describe_6': skill_descriptions[5],
        'active_skills_required_level_7': skill_levels[6],
        'active_skills_name_7': skill_names[6],
        'active_skills_element_7': skill_elements[6],
        'active_skills_cool_time_7': skill_cool_times[6],
        'active_skills_power_7': skill_powers[6],
        'active_skills_describe_7': skill_descriptions[6],
        'drops': '|'.join(drop_items),
        'drops_probability': '|'.join(drop_probabilities),
        'drops_count': str(len(drop_items))
    }

def main():
    # 모든 팰 데이터 처리
    all_pals = []
    
    for pal_id, pal_info in pals_data.items():
        print(f"Processing Pal {pal_id}: {pal_info['name_kor']}")
        
        parsed_data = parse_pal_stats_from_markdown(pal_info['markdown'])
        parsed_data['id'] = pal_id
        parsed_data['name_kor'] = pal_info['name_kor']
        parsed_data['elements'] = pal_info['elements']
        
        all_pals.append(parsed_data)
    
    # CSV 헤더 정의 (기존과 동일)
    headers = [
        'id', 'name_kor', 'description_kor', 'elements',
        'size', 'rarity', 'health', 'food', 'melee_attack', 'attack', 'defense', 
        'work_speed', 'support', 'capture_rate_correct', 'male_probability', 
        'combi_rank', 'gold_coin', 'egg', 'code',
        'slow_walk_speed', 'walk_speed', 'run_speed', 'ride_sprint_speed', 'transport_speed',
        'level60_health', 'level60_attack', 'level60_defense',
        'partner_skill_name', 'partner_skill_describe', 'partner_skill_need_item', 'partner_skill_need_item_tech_level',
        'work_kindling', 'work_watering', 'work_seeding', 'work_generating_electricity',
        'work_handiwork', 'work_gathering', 'work_lumbering', 'work_mining',
        'work_medicine_production', 'work_cooling', 'work_transporting', 'work_farming',
        'active_skills_required_level_1', 'active_skills_name_1', 'active_skills_element_1',
        'active_skills_cool_time_1', 'active_skills_power_1', 'active_skills_describe_1',
        'active_skills_required_level_2', 'active_skills_name_2', 'active_skills_element_2',
        'active_skills_cool_time_2', 'active_skills_power_2', 'active_skills_describe_2',
        'active_skills_required_level_3', 'active_skills_name_3', 'active_skills_element_3',
        'active_skills_cool_time_3', 'active_skills_power_3', 'active_skills_describe_3',
        'active_skills_required_level_4', 'active_skills_name_4', 'active_skills_element_4',
        'active_skills_cool_time_4', 'active_skills_power_4', 'active_skills_describe_4',
        'active_skills_required_level_5', 'active_skills_name_5', 'active_skills_element_5',
        'active_skills_cool_time_5', 'active_skills_power_5', 'active_skills_describe_5',
        'active_skills_required_level_6', 'active_skills_name_6', 'active_skills_element_6',
        'active_skills_cool_time_6', 'active_skills_power_6', 'active_skills_describe_6',
        'active_skills_required_level_7', 'active_skills_name_7', 'active_skills_element_7',
        'active_skills_cool_time_7', 'active_skills_power_7', 'active_skills_describe_7',
        'drops', 'drops_probability', 'drops_count'
    ]
    
    # CSV 파일 생성
    filename = 'pals_11_to_12B_complete.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        for pal in all_pals:
            # 빈 필드들을 빈 문자열로 채우기
            row = {header: pal.get(header, '') for header in headers}
            writer.writerow(row)
    
    print(f"\n✅ CSV 파일 생성 완료: {filename}")
    print(f"📊 총 {len(all_pals)}개 팰 데이터 저장")
    
    # 데이터 품질 확인
    for pal in all_pals:
        filled_fields = sum(1 for value in pal.values() if value and str(value).strip())
        total_fields = len(headers)
        completion_rate = (filled_fields / total_fields) * 100
        print(f"  - {pal['id']}: {pal['name_kor']} ({completion_rate:.1f}% 완성)")

if __name__ == "__main__":
    main() 