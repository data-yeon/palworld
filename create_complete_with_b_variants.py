#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1~10번 + B변종들을 포함한 완전한 팰 데이터 CSV 생성
5B 아이호, 6B 적부리, 10B 뎅키 포함
"""

import csv
import re

def parse_pal_data(markdown_content, pal_id, pal_name_kor):
    """마크다운 데이터를 파싱하여 완전한 팰 정보 추출"""
    
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
    
    # Food amount 추출
    food_match = re.search(r'식사량\s*(\d+)', markdown_content)
    if food_match:
        data['food_amount'] = food_match.group(1)
    
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
    egg_match = re.search(r'Egg\s*([^\\n]+)', markdown_content)
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

def create_complete_csv_with_b_variants():
    """B 변종을 포함한 완전한 CSV 생성"""
    
    print("🚀 B 변종 포함 완전한 팰 데이터 CSV 생성 시작!")
    
    # 팰 데이터 정의 (기존 1-10 + B변종들)
    pals_data = [
        ('1', '도로롱', open('pal_1_lamball.md', 'r', encoding='utf-8').read()),
        ('2', '까부냥', open('pal_2_cattiva.md', 'r', encoding='utf-8').read()),
        ('3', '꼬꼬닭', open('pal_3_chikipi.md', 'r', encoding='utf-8').read()),
        ('4', '큐룰리스', open('pal_4_lifmunk.md', 'r', encoding='utf-8').read()),
        ('5', '파이호', open('pal_5_foxparks.md', 'r', encoding='utf-8').read()),
        ('5B', '아이호', """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Kitsunebi_Ice_icon_normal.webp)](https://paldb.cc/ko/Foxparks_Cryst)

[아이호](https://paldb.cc/ko/Foxparks_Cryst)#5B

얼음 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

포옹 프로스트 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 플레이어에게 장착되어
냉기를 방출해 공격할 수 있다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Harness.webp)](https://paldb.cc/ko/Foxparks_Crysts_Harness) 기술24

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_10.webp) 냉각](https://paldb.cc/ko/Cooling)

Lv1

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

##### Stats

Size

XS

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

65

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1.1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1305

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1410

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Ice_01.webp)얼어붙은 알](https://paldb.cc/ko/Frozen_Egg)

Code

Kitsunebi_Ice

##### Movement

SlowWalkSpeed

40

WalkSpeed

80

RunSpeed

400

RideSprintSpeed

550

TransportSpeed

240

##### Level 60

HP

2937 – 3571

공격

490 – 607

방어

391 – 493

##### Summary

태어난 직후엔 냉기를 잘 못 다뤄서
걸핏하면 냉기를 뿜다가 숨이 탁 막힌다.
감기에 걸리면 콧물이 어는 바람에 숨이 가빠진다.

##### Partner Skill: 포옹 프로스트

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 플레이어에게 장착되어

냉기를 방출해 공격할 수 있다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Harness.webp)](https://paldb.cc/ko/Foxparks_Crysts_Harness) 기술24

##### Active Skills

Lv. 1 [얼음 미사일](https://paldb.cc/ko/Ice_Missile)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Frost.webp)](https://paldb.cc/ko/Ice_Skill_Fruit%3A_Ice_Missile)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 3

위력: 30

축적치:빙결

103

하늘에 뾰족한 얼음을 생성한 뒤
적을 향해 그 얼음을 발사한다.

Lv. 15 [얼음 칼날](https://paldb.cc/ko/Icicle_Cutter)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Frost.webp)](https://paldb.cc/ko/Ice_Skill_Fruit%3A_Icicle_Cutter)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 10

위력: 55

축적치:빙결

50

초승달 모양의 얼음 날을 만들어
전방으로 발사한다.

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Leather.webp)가죽](https://paldb.cc/ko/Leather) 1–2 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_IceOrgan.webp)빙결 기관](https://paldb.cc/ko/Ice_Organ) 1–3 | 100% |

##### Tribes

|     |     |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Kitsunebi_Ice_icon_normal.webp)여로를 수놓는 얼음꽃 아이호](https://paldb.cc/ko/Icy_Blossom_Voyager_Foxparks_Cryst) | Tribe Boss |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Kitsunebi_Ice_icon_normal.webp)아이호](https://paldb.cc/ko/Foxparks_Cryst) | Tribe Normal |

##### Spawner

|     |     |     |
| --- | --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Kitsunebi_Ice_icon_normal.webp)아이호](https://paldb.cc/ko/Foxparks_Cryst) | Lv. 52–55 | yamijima_7_2_DarkArea |
"""),
        ('6', '청부리', open('pal_6_fuack.md', 'r', encoding='utf-8').read()),
        ('6B', '적부리', """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_BluePlatypus_Fire_icon_normal.webp)](https://paldb.cc/ko/Fuack_Ignis)

[적부리](https://paldb.cc/ko/Fuack_Ignis)#6B

물 속성

화염 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

파이어 태클 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_001.webp)

발동하면 [적부리](https://paldb.cc/ko/Fuack_Ignis) 이(가) 적을 향해
파이어 서핑을 하며 달려든다.

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_00.webp) 불 피우기](https://paldb.cc/ko/Kindling)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_01.webp) 관개](https://paldb.cc/ko/Watering)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_04.webp) 수작업](https://paldb.cc/ko/Handiwork)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_11.webp) 운반](https://paldb.cc/ko/Transporting)

Lv1

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

##### Stats

Size

XS

Rarity

2

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

85

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1.1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1290

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1340

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Water_01.webp)축축한 알](https://paldb.cc/ko/Damp_Egg)

Code

BluePlatypus_Fire

##### Movement

SlowWalkSpeed

70

WalkSpeed

105

RunSpeed

300

RideSprintSpeed

400

TransportSpeed

202

##### Level 60

HP

2775 – 3360

공격

514 – 638

방어

342 – 430

##### Summary

배의 마찰력이 아주 강한 탓에
보디 서핑을 하면 불이 붙을 정도다.
너무 신나게 미끄러지다 간혹 불덩이가 되기도 한다.

##### Partner Skill: 파이어 태클

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_001.webp)

발동하면 [적부리](https://paldb.cc/ko/Fuack_Ignis) 이(가) 적을 향해

파이어 서핑을 하며 달려든다.

##### Active Skills

Lv. 1 [파이어 샷](https://paldb.cc/ko/Ignis_Blast)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Flame.webp)](https://paldb.cc/ko/Fire_Skill_Fruit%3A_Ignis_Blast)

화염 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 30

축적치:화상

50

적을 향해 일직선으로 날아가는
화염 탄환을 발사한다.

Lv. 15 [버블 샷](https://paldb.cc/ko/Bubble_Blast)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Water.webp)](https://paldb.cc/ko/Water_Skill_Fruit%3A_Bubble_Blast)

물 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 13

위력: 65

축적치:젖음

100

적을 천천히 추적하는
수많은 거품을 발사한다.

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Leather.webp)가죽](https://paldb.cc/ko/Leather) 1 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalFluid.webp)팰의 체액](https://paldb.cc/ko/Pal_Fluids) 1 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_FireOrgan.webp)발화 기관](https://paldb.cc/ko/Flame_Organ) 1–2 | 50% |

##### Tribes

|     |     |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_BluePlatypus_Fire_icon_normal.webp)폭주 중인 파도 타는 꼬맹이 적부리](https://paldb.cc/ko/Runaway_Wave_Rider_Fuack_Ignis) | Tribe Boss |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_BluePlatypus_Fire_icon_normal.webp)적부리](https://paldb.cc/ko/Fuack_Ignis) | Tribe Normal |

##### Spawner

|     |     |     |
| --- | --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_BluePlatypus_Fire_icon_normal.webp)적부리](https://paldb.cc/ko/Fuack_Ignis) | Lv. 16–27 | [![](https://cdn.paldb.cc/image/Pal/Texture/BuildObject/PNG/T_icon_buildObject_FishingPond2.webp)커다란 낚시터](https://paldb.cc/ko/Large_Fishing_Pond) Medium 8.72% |
"""),
        ('7', '번개냥', open('pal_7_sparkit.md', 'r', encoding='utf-8').read()),
        ('8', '몽지', open('pal_8_tanzee.md', 'r', encoding='utf-8').read()),
        ('9', '불꽃밤비', open('pal_9_rooby.md', 'r', encoding='utf-8').read()),
        ('10', '펭키', open('pal_10_pengullet.md', 'r', encoding='utf-8').read()),
        ('10B', '뎅키', """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Penguin_Electric_icon_normal.webp)](https://paldb.cc/ko/Pengullet_Lux)

[뎅키](https://paldb.cc/ko/Pengullet_Lux)#10B

물 속성

번개 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

뎅키 발사기 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 [로켓 발사기](https://paldb.cc/ko/Rocket_Launcher) 을(를) 장착하여
[뎅키](https://paldb.cc/ko/Pengullet_Lux) 을(를) 탄환 삼아 발사한다.
착탄하여 폭발하면 [뎅키](https://paldb.cc/ko/Pengullet_Lux) 이(가) 빈사 상태가 된다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Launcher.webp)](https://paldb.cc/ko/Pengullet_Luxs_Rocket_Launcher) 기술39

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_01.webp) 관개](https://paldb.cc/ko/Watering)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_03.webp) 발전](https://paldb.cc/ko/Generating_Electricity)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_04.webp) 수작업](https://paldb.cc/ko/Handiwork)

Lv1

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_11.webp) 운반](https://paldb.cc/ko/Transporting)

Lv1

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

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

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

0.9

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1310

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1290

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Water_01.webp)축축한 알](https://paldb.cc/ko/Damp_Egg)

Code

Penguin_Electric

##### Movement

SlowWalkSpeed

30

WalkSpeed

60

RunSpeed

500

RideSprintSpeed

650

TransportSpeed

265

##### Level 60

HP

3100 – 3782

공격

490 – 607

방어

391 – 493

##### Summary

날개가 완전히 퇴화해 날 수 없다.
하늘을 향한 미련은 어느덧 질투로 변화하여
하늘을 나는 모든 것을 격추할 전기의 힘을 얻게 되었다!

##### Partner Skill: 뎅키 발사기

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 [로켓 발사기](https://paldb.cc/ko/Rocket_Launcher) 을(를) 장착하여

[뎅키](https://paldb.cc/ko/Pengullet_Lux) 을(를) 탄환 삼아 발사한다.

착탄하여 폭발하면 [뎅키](https://paldb.cc/ko/Pengullet_Lux) 이(가) 빈사 상태가 된다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Launcher.webp)](https://paldb.cc/ko/Pengullet_Luxs_Rocket_Launcher) 기술39

##### Active Skills

Lv. 1 [번개 창](https://paldb.cc/ko/Thunder_Spear)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Electric.webp)](https://paldb.cc/ko/Electric_Skill_Fruit%3A_Thunder_Spear)

번개 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 30

축적치:감전

35

직선상으로 날아가는 번개 창을
적을 향해 빠르게 발사한다.

Lv. 15 [버블 샷](https://paldb.cc/ko/Bubble_Blast)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Water.webp)](https://paldb.cc/ko/Water_Skill_Fruit%3A_Bubble_Blast)

물 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 13

위력: 65

축적치:젖음

100

적을 천천히 추적하는
수많은 거품을 발사한다.

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_ElectricOrgan.webp)발전 기관](https://paldb.cc/ko/Electric_Organ) 1–2 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalFluid.webp)팰의 체액](https://paldb.cc/ko/Pal_Fluids) 1 | 100% |

##### Tribes

|     |     |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Penguin_Electric_icon_normal.webp)과음한 뎅키](https://paldb.cc/ko/Had_One_Too_Many_Pengullet_Lux) | Tribe Boss |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Penguin_Electric_icon_normal.webp)뎅키](https://paldb.cc/ko/Pengullet_Lux) | Tribe Normal |

##### Spawner

|     |     |     |
| --- | --- | --- |
| [![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Penguin_Electric_icon_normal.webp)뎅키](https://paldb.cc/ko/Pengullet_Lux) | Lv. 16–27 | [![](https://cdn.paldb.cc/image/Pal/Texture/BuildObject/PNG/T_icon_buildObject_FishingPond2.webp)커다란 낚시터](https://paldb.cc/ko/Large_Fishing_Pond) Medium 9.96% |
"""),
    ]
    
    all_data = []
    
    for pal_id, pal_name, markdown_content in pals_data:
        print(f"📊 처리 중: {pal_id} {pal_name}")
        
        try:
            # 기존 파일인 경우 읽기, B 변종인 경우 직접 사용
            if pal_id.endswith('B'):
                content = markdown_content
            else:
                content = markdown_content
            
            parsed_data = parse_pal_data(content, pal_id, pal_name)
            all_data.append(parsed_data)
            
        except Exception as e:
            print(f"❌ {pal_id} {pal_name} 처리 중 오류: {e}")
            continue
    
    # CSV 생성
    if all_data:
        filename = 'complete_1_to_10_with_b_variants.csv'
        
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
            writer.writeheader()
            writer.writerows(all_data)
        
        print(f"\n🎉 완성! {filename} 파일 생성 완료!")
        print(f"📋 총 {len(all_data)}개 팰 데이터 (1-10 + B변종들)")
        print(f"📊 컬럼 수: {len(all_data[0].keys())}개")
        
        # 파일 내용 미리보기
        print(f"\n📄 파일 내용 미리보기:")
        for i, row in enumerate(all_data[:3]):
            print(f"  {i+1}. {row['id']} - {row['name_kor']} ({row['elements']})")
        
        if len(all_data) > 3:
            print(f"  ... (총 {len(all_data)}개)")
    
    else:
        print("❌ 생성할 데이터가 없습니다.")

if __name__ == "__main__":
    create_complete_csv_with_b_variants() 