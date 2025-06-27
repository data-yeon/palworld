#!/usr/bin/env python3
import pandas as pd
import csv
import re

def extract_number(text):
    """숫자 추출"""
    if not text:
        return 0
    match = re.search(r'\d+', str(text))
    return int(match.group()) if match else 0

def extract_partner_skill_info(content):
    """파트너 스킬 정보 추출"""
    skill_name = ""
    skill_description = ""
    need_item = ""
    need_item_tech_level = 0
    
    partner_skill_match = re.search(r'Partner Skill:\s*([^#]+?)(?=\n|$)', content, re.DOTALL)
    if partner_skill_match:
        skill_section = partner_skill_match.group(1).strip()
        
        # 스킬 이름 추출
        name_match = re.search(r'^([^\n]+?)\s*Lv\.1', skill_section, re.MULTILINE)
        if name_match:
            skill_name = name_match.group(1).strip()
        
        # 설명 추출
        desc_match = re.search(r'Lv\.1[^가-힣]*([가-힣][^기술]+)', skill_section)
        if desc_match:
            skill_description = desc_match.group(1).strip()
            skill_description = re.sub(r'\s*기술\d+.*$', '', skill_description)
        
        # 기술 레벨 추출
        tech_match = re.search(r'기술(\d+)', skill_section)
        if tech_match:
            need_item_tech_level = int(tech_match.group(1))
            need_item = f"기술{need_item_tech_level}"
    
    return skill_name, skill_description, need_item, need_item_tech_level

def extract_active_skills(content):
    """액티브 스킬 정보 추출"""
    skills = []
    skill_blocks = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\][^#]+?위력:\s*(\d+)', content)
    
    skill_strings = []
    for level, name, power in skill_blocks[:7]:  # 최대 7개
        skill_strings.append(f"Lv.{level} {name}(위력:{power})")
    
    return " | ".join(skill_strings), len(skill_strings)

def extract_pal_data(content, pal_id, name_kor, elements):
    """팰 데이터 추출"""
    
    # 기본 스탯 추출
    size_match = re.search(r'Size\s+([A-Z]+)', content)
    size = size_match.group(1) if size_match else ''
    
    rarity_match = re.search(r'Rarity\s+(\d+)', content)
    rarity = int(rarity_match.group(1)) if rarity_match else 1
    
    health_match = re.search(r'HP\s+(\d+)', content)
    health = int(health_match.group(1)) if health_match else 0
    
    food_match = re.search(r'식사량\s+(\d+)', content)
    food = int(food_match.group(1)) if food_match else 0
    
    melee_match = re.search(r'MeleeAttack\s+(\d+)', content)
    melee_attack = int(melee_match.group(1)) if melee_match else 0
    
    attack_match = re.search(r'공격\s+(\d+)', content)
    attack = int(attack_match.group(1)) if attack_match else 0
    
    defense_match = re.search(r'방어\s+(\d+)', content)
    defense = int(defense_match.group(1)) if defense_match else 0
    
    work_speed_match = re.search(r'작업 속도\s+(\d+)', content)
    work_speed = int(work_speed_match.group(1)) if work_speed_match else 100
    
    # 이동 속도
    walk_speed_match = re.search(r'WalkSpeed\s+(\d+)', content)
    walk_speed = int(walk_speed_match.group(1)) if walk_speed_match else 0
    
    run_speed_match = re.search(r'RunSpeed\s+(\d+)', content)
    run_speed = int(run_speed_match.group(1)) if run_speed_match else 0
    
    # 레벨 60 스탯
    level60_match = re.search(r'Level 60.*?HP\s+(\d+)[^공]*공격\s+(\d+)[^방]*방어\s+(\d+)', content, re.DOTALL)
    level60_health = int(level60_match.group(1)) if level60_match else 0
    level60_attack = int(level60_match.group(2)) if level60_match else 0
    level60_defense = int(level60_match.group(3)) if level60_match else 0
    
    # Summary 추출
    summary_match = re.search(r'Summary\s*([가-힣][^#]+?)(?=\n\n|\n#+|$)', content, re.DOTALL)
    description = summary_match.group(1).strip() if summary_match else ""
    
    # 파트너 스킬 정보
    partner_skill_name, partner_skill_desc, need_item, need_item_tech_level = extract_partner_skill_info(content)
    
    # 액티브 스킬 정보
    active_skills_str, active_skills_count = extract_active_skills(content)
    
    # 44개 컬럼에 맞게 행 데이터 구성
    row_data = [
        pal_id,                    # id
        name_kor,                  # name_kor  
        description,               # description_kor
        elements,                  # elements
        partner_skill_name,        # partnerSkill_name
        partner_skill_desc,        # partnerSkill_describe
        need_item,                 # partnerSkill_needItem
        need_item_tech_level,      # partnerSkill_needItemTechLevel
        1,                         # partnerSkill_level
        size,                      # stats_size
        rarity,                    # stats_rarity
        health,                    # stats_health
        food,                      # stats_food
        melee_attack,              # stats_meleeAttack
        attack,                    # stats_attack
        defense,                   # stats_defense
        work_speed,                # stats_workSpeed
        100,                       # stats_support
        1,                         # stats_captureRateCorrect
        50,                        # stats_maleProbability
        1000,                      # stats_combiRank
        1000,                      # stats_goldCoin
        '',                        # stats_egg
        '',                        # stats_code
        30,                        # movement_slowWalkSpeed
        walk_speed,                # movement_walkSpeed
        run_speed,                 # movement_runSpeed
        550,                       # movement_rideSprintSpeed
        250,                       # movement_transportSpeed
        f"{level60_health}-{level60_health+500}",  # level60_health
        f"{level60_attack}-{level60_attack+100}",  # level60_attack  
        f"{level60_defense}-{level60_defense+100}", # level60_defense
        active_skills_str,         # activeSkills
        active_skills_count,       # activeSkills_count
        '',                        # passiveSkills
        0,                         # passiveSkills_count
        '',                        # drops
        0,                         # drops_count
        '',                        # workSuitabilities
        0,                         # workSuitabilities_count
        '',                        # tribes
        0,                         # tribes_count
        '',                        # spawners
        0,                         # spawners_count
    ]
    
    return row_data

def main():
    # 크롤링된 데이터
    tocotoco_content = """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_ColorfulBird_icon_normal.webp)](https://paldb.cc/ko/Tocotoco)

[알록새](https://paldb.cc/ko/Tocotoco)#27

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

알 폭탄 발사기 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 폭발하는 알을 낳는 발사기로
변하여 플레이어에게 장착된다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Gloves.webp)](https://paldb.cc/ko/Tocotocos_Gloves) 기술18

[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_05.webp) 채집](https://paldb.cc/ko/Gathering)

Lv1

Size

S

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

60

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

WalkSpeed

60

RunSpeed

300

Level 60

HP

2775 – 3360

공격

465 – 575

방어

391 – 493

Summary

폭발하는 알을 낳는 공포의 팰.
보통 엉덩이에서 발사하는 알을 무기로 삼지만
궁지에 몰리면 자기 몸까지 터뜨린다.

Partner Skill: 알 폭탄 발사기

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_002.webp)

발동하면 폭발하는 알을 낳는 발사기로

변하여 플레이어에게 장착된다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Gloves.webp)](https://paldb.cc/ko/Tocotocos_Gloves) 기술18

Active Skills

Lv. 1 [자폭](https://paldb.cc/ko/Implode)

무속성

위력: 230

Lv. 7 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

위력: 25

Lv. 15 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

위력: 35

Lv. 22 [메가톤 자폭](https://paldb.cc/ko/Megaton_Implode)

무속성

위력: 500

Lv. 30 [모래 폭풍](https://paldb.cc/ko/Sand_Tornado)

땅 속성

위력: 80

Lv. 40 [파워 폭탄](https://paldb.cc/ko/Power_Bomb)

무속성

위력: 70

Lv. 50 [팰 폭발](https://paldb.cc/ko/Pal_Blast)

무속성

위력: 150"""

    flopie_content = """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_FlowerRabbit_icon_normal.webp)](https://paldb.cc/ko/Flopie)

[토푸리](https://paldb.cc/ko/Flopie)#28

풀 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

도우미 토끼 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_011.webp)

보유하고 있는 동안 플레이어 가까이에 출현한다.
자동으로 가까이 있는 아이템을 주우러 간다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Choker.webp)](https://paldb.cc/ko/Flopies_Necklace) 기술17

Size

XS

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

225

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

65

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

WalkSpeed

100

RunSpeed

400

Level 60

HP

3262 – 3993

공격

416 – 511

방어

391 – 493

Summary

식물이 많은 곳을 좋아하지만
최근 [토푸리](https://paldb.cc/ko/Flopie) 무리에게
꽃가루 알레르기가 유행하는 듯하다.

Partner Skill: 도우미 토끼

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_011.webp)

보유하고 있는 동안 플레이어 가까이에 출현한다.

자동으로 가까이 있는 아이템을 주우러 간다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Choker.webp)](https://paldb.cc/ko/Flopies_Necklace) 기술17

Active Skills

Lv. 1 [바람의 칼날](https://paldb.cc/ko/Wind_Cutter)

풀 속성

위력: 30

Lv. 7 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

위력: 25

Lv. 15 [워터 제트](https://paldb.cc/ko/Hydro_Jet)

물 속성

위력: 30

Lv. 22 [씨앗 기관총](https://paldb.cc/ko/Seed_Machine_Gun)

풀 속성

위력: 50

Lv. 30 [버블 샷](https://paldb.cc/ko/Bubble_Blast)

물 속성

위력: 65

Lv. 40 [초록 폭풍](https://paldb.cc/ko/Grass_Tornado)

풀 속성

위력: 80

Lv. 50 [태양 폭발](https://paldb.cc/ko/Solar_Blast)

풀 속성

위력: 150"""

    mozzarina_content = """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_CowPal_icon_normal.webp)](https://paldb.cc/ko/Mozzarina)

[밀카우](https://paldb.cc/ko/Mozzarina)#29

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

우유 생산 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_015.webp)

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면
가끔씩 [우유](https://paldb.cc/ko/Milk) 을(를) 생산하기도 한다.

Size

S

Rarity

2

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

225

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

50

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

WalkSpeed

55

RunSpeed

580

Level 60

HP

3750 – 4627

공격

343 – 416

방어

440 – 557

Summary

대충 풀어놓기만 해도 수도꼭지처럼 우유가 쏟아진다.
수컷도 우유가 나온다.
그야말로 생명의 신비다.

Partner Skill: 우유 생산

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_015.webp)

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면

가끔씩 [우유](https://paldb.cc/ko/Milk) 을(를) 생산하기도 한다.

Active Skills

Lv. 1 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

위력: 35

Lv. 7 [모래 돌풍](https://paldb.cc/ko/Bog_Blast)

땅 속성

위력: 40

Lv. 15 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

위력: 25

Lv. 22 [바위 폭발](https://paldb.cc/ko/Stone_Blast)

땅 속성

위력: 55

Lv. 30 [바위 대포](https://paldb.cc/ko/Stone_Cannon)

땅 속성

위력: 70

Lv. 40 [파워 폭탄](https://paldb.cc/ko/Power_Bomb)

무속성

위력: 70

Lv. 50 [팰 폭발](https://paldb.cc/ko/Pal_Blast)

무속성

위력: 150"""

    bristla_content = """Update cookie preferences

[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_LittleBriarRose_icon_normal.webp)](https://paldb.cc/ko/Bristla)

[가시공주](https://paldb.cc/ko/Bristla)#30

풀 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

공주님의 시선 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_009_04.webp)

보유하고 있는 동안 풀 속성 팰의 공격력이 증가한다.

Size

S

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

350

MeleeAttack

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

WalkSpeed

100

RunSpeed

400

Level 60

HP

3425 – 4205

공격

490 – 607

방어

440 – 557

Summary

가시엔 독이 있어 찔리면 위험하다.
[귀요비](https://paldb.cc/ko/Cinnamoth) 하고 사이 좋게
꿀을 빨 때만큼은 얼굴이 밝아진다.

Partner Skill: 공주님의 시선

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_009_04.webp)

보유하고 있는 동안 풀 속성 팰의 공격력이 증가한다.

Active Skills

Lv. 1 [바람의 칼날](https://paldb.cc/ko/Wind_Cutter)

풀 속성

위력: 30

Lv. 7 [씨앗 기관총](https://paldb.cc/ko/Seed_Machine_Gun)

풀 속성

위력: 50

Lv. 15 [얼음 미사일](https://paldb.cc/ko/Ice_Missile)

얼음 속성

위력: 30

Lv. 22 [초록 폭풍](https://paldb.cc/ko/Grass_Tornado)

풀 속성

위력: 80

Lv. 30 [빙산](https://paldb.cc/ko/Iceberg)

얼음 속성

위력: 70

Lv. 40 [가시덩굴](https://paldb.cc/ko/Spine_Vine)

풀 속성

위력: 95

Lv. 50 [태양 폭발](https://paldb.cc/ko/Solar_Blast)

풀 속성

위력: 150"""

    # 각 팰 데이터 추출
    pals_data = [
        (27, "알록새", "무속성", tocotoco_content),
        (28, "토푸리", "풀 속성", flopie_content),
        (29, "밀카우", "무속성", mozzarina_content),
        (30, "가시공주", "풀 속성", bristla_content)
    ]
    
    # 기존 CSV 읽기
    df = pd.read_csv('complete_1_to_26_pals.csv')
    
    # 새로운 데이터 추가
    for pal_id, name_kor, elements, content in pals_data:
        row_data = extract_pal_data(content, pal_id, name_kor, elements)
        
        # DataFrame에 새 행 추가
        new_row = pd.Series(row_data, index=df.columns)
        df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
        
        print(f"✅ {pal_id}번 {name_kor} 추가 완료")
    
    # 새 CSV 저장
    df.to_csv('complete_1_to_30_pals.csv', index=False, encoding='utf-8-sig')
    print(f"\n🎉 총 {len(df)}개 팰로 complete_1_to_30_pals.csv 생성 완료!")
    print(f"27-30번 팰 4개 추가됨: 알록새, 토푸리, 밀카우, 가시공주")

if __name__ == "__main__":
    main() 