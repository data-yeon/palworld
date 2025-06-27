#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re
import os

def extract_pal_info(markdown_content, pal_number, expected_name):
    """주어진 마크다운 내용에서 팰 정보를 추출합니다."""
    
    # 기본값 설정
    result = {
        'Number': pal_number,
        'Name': expected_name,
        'NameEn': '',
        'NameJa': '',
        'ElementType1': '',
        'ElementType2': '',
        'Rarity': '',
        'Size': '',
        'HP': '',
        'ShotAttack': '',
        'MeleeAttack': '',
        'Defense': '',
        'Support': '',
        'CraftSpeed': '',
        'SlowWalkSpeed': '',
        'WalkSpeed': '',
        'RunSpeed': '',
        'RideSprintSpeed': '',
        'TransportSpeed': '',
        'Level60_HP_Min': '',
        'Level60_HP_Max': '',
        'Level60_Attack_Min': '',
        'Level60_Attack_Max': '',
        'Level60_Defense_Min': '',
        'Level60_Defense_Max': '',
        'PartnerSkill': '',
        'ActiveSkill1': '',
        'ActiveSkill1_Level': '',
        'ActiveSkill1_Power': '',
        'ActiveSkill1_CT': '',
        'ActiveSkill2': '',
        'ActiveSkill2_Level': '',
        'ActiveSkill2_Power': '',
        'ActiveSkill2_CT': '',
        'ActiveSkill3': '',
        'ActiveSkill3_Level': '',
        'ActiveSkill3_Power': '',
        'ActiveSkill3_CT': '',
        'DropItem1': '',
        'DropItem1_Quantity': '',
        'DropItem2': '',
        'DropItem2_Quantity': '',
        'DropItem3': '',
        'DropItem3_Quantity': ''
    }
    
    # 팰 이름 추출
    name_match = re.search(r'\[([^\]]+)\].*?#(\d+)', markdown_content)
    if name_match:
        result['Name'] = name_match.group(1)
        result['Number'] = name_match.group(2)
    
    # ElementType 추출 
    if '무속성' in markdown_content:
        result['ElementType1'] = 'Normal'
    elif '풀 속성' in markdown_content:
        result['ElementType1'] = 'Leaf'
    
    # Stats 섹션에서 정보 추출
    stats_section = re.search(r'##### Stats(.*?)##### Movement', markdown_content, re.DOTALL)
    if stats_section:
        stats_text = stats_section.group(1)
        
        # Size 추출
        size_match = re.search(r'Size\s*([SML])', stats_text)
        if size_match:
            result['Size'] = size_match.group(1)
            
        # Rarity 추출
        rarity_match = re.search(r'Rarity\s*(\d+)', stats_text)
        if rarity_match:
            result['Rarity'] = rarity_match.group(1)
            
        # HP 추출
        hp_match = re.search(r'HP\s*(\d+)', stats_text)
        if hp_match:
            result['HP'] = hp_match.group(1)
            
        # 공격 추출
        attack_match = re.search(r'공격\s*(\d+)', stats_text)
        if attack_match:
            result['ShotAttack'] = attack_match.group(1)
            
        # MeleeAttack 추출
        melee_match = re.search(r'MeleeAttack\s*(\d+)', stats_text)
        if melee_match:
            result['MeleeAttack'] = melee_match.group(1)
            
        # 방어 추출
        defense_match = re.search(r'방어\s*(\d+)', stats_text)
        if defense_match:
            result['Defense'] = defense_match.group(1)
            
        # Support 추출
        support_match = re.search(r'Support\s*(\d+)', stats_text)
        if support_match:
            result['Support'] = support_match.group(1)
    
    # Movement 섹션에서 정보 추출
    movement_section = re.search(r'##### Movement(.*?)##### Level 60', markdown_content, re.DOTALL)
    if movement_section:
        movement_text = movement_section.group(1)
        
        # 각 속도값 추출
        slow_walk_match = re.search(r'SlowWalkSpeed\s*(\d+)', movement_text)
        if slow_walk_match:
            result['SlowWalkSpeed'] = slow_walk_match.group(1)
            
        walk_match = re.search(r'WalkSpeed\s*(\d+)', movement_text)
        if walk_match:
            result['WalkSpeed'] = walk_match.group(1)
            
        run_match = re.search(r'RunSpeed\s*(\d+)', movement_text)
        if run_match:
            result['RunSpeed'] = run_match.group(1)
            
        ride_match = re.search(r'RideSprintSpeed\s*(\d+)', movement_text)
        if ride_match:
            result['RideSprintSpeed'] = ride_match.group(1)
            
        transport_match = re.search(r'TransportSpeed\s*(\d+)', movement_text)
        if transport_match:
            result['TransportSpeed'] = transport_match.group(1)
    
    # Level 60 스탯 추출
    level60_section = re.search(r'##### Level 60(.*?)##### Others', markdown_content, re.DOTALL)
    if level60_section:
        level60_text = level60_section.group(1)
        
        # HP 범위 추출
        hp_range_match = re.search(r'HP\s*(\d+)\s*–\s*(\d+)', level60_text)
        if hp_range_match:
            result['Level60_HP_Min'] = hp_range_match.group(1)
            result['Level60_HP_Max'] = hp_range_match.group(2)
            
        # 공격 범위 추출
        attack_range_match = re.search(r'공격\s*(\d+)\s*–\s*(\d+)', level60_text)
        if attack_range_match:
            result['Level60_Attack_Min'] = attack_range_match.group(1)
            result['Level60_Attack_Max'] = attack_range_match.group(2)
            
        # 방어 범위 추출
        defense_range_match = re.search(r'방어\s*(\d+)\s*–\s*(\d+)', level60_text)
        if defense_range_match:
            result['Level60_Defense_Min'] = defense_range_match.group(1)
            result['Level60_Defense_Max'] = defense_range_match.group(2)
    
    # 파트너 스킬 추출
    partner_skill_match = re.search(r'##### Partner Skill: ([^#]+)', markdown_content)
    if partner_skill_match:
        result['PartnerSkill'] = partner_skill_match.group(1).strip()
    
    # 액티브 스킬 추출
    active_skills_section = re.search(r'##### Active Skills(.*?)##### Passive Skills', markdown_content, re.DOTALL)
    if active_skills_section:
        skills_text = active_skills_section.group(1)
        
        # 첫 번째 스킬 추출
        skill1_match = re.search(r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?위력:\s*(\d+).*?![^:]*:\s*(\d+)', skills_text, re.DOTALL)
        if skill1_match:
            result['ActiveSkill1_Level'] = skill1_match.group(1)
            result['ActiveSkill1'] = skill1_match.group(2)
            result['ActiveSkill1_Power'] = skill1_match.group(3)
            result['ActiveSkill1_CT'] = skill1_match.group(4)
        
        # 두 번째 스킬 추출
        skills_list = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?위력:\s*(\d+).*?![^:]*:\s*(\d+)', skills_text, re.DOTALL)
        if len(skills_list) >= 2:
            result['ActiveSkill2_Level'] = skills_list[1][0]
            result['ActiveSkill2'] = skills_list[1][1]
            result['ActiveSkill2_Power'] = skills_list[1][2]
            result['ActiveSkill2_CT'] = skills_list[1][3]
        
        if len(skills_list) >= 3:
            result['ActiveSkill3_Level'] = skills_list[2][0]
            result['ActiveSkill3'] = skills_list[2][1]
            result['ActiveSkill3_Power'] = skills_list[2][2]
            result['ActiveSkill3_CT'] = skills_list[2][3]
    
    # Possible Drops 추출
    drops_section = re.search(r'##### Possible Drops(.*?)##### Tribes', markdown_content, re.DOTALL)
    if drops_section:
        drops_text = drops_section.group(1)
        
        # 드롭 아이템들 추출
        drop_patterns = re.findall(r'\[([^\]]+)\][^\d]*(\d+(?:–\d+)?)', drops_text)
        
        for i, (item_name, quantity) in enumerate(drop_patterns[:3], 1):
            result[f'DropItem{i}'] = item_name
            result[f'DropItem{i}_Quantity'] = quantity
    
    return result

def load_existing_csv(filename):
    """기존 CSV 파일을 로드합니다."""
    data = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    return data

def save_csv(data, filename):
    """데이터를 CSV 파일로 저장합니다."""
    if not data:
        return
    
    fieldnames = [
        'Number', 'Name', 'NameEn', 'NameJa', 'ElementType1', 'ElementType2',
        'Rarity', 'Size', 'HP', 'ShotAttack', 'MeleeAttack', 'Defense', 'Support', 'CraftSpeed',
        'SlowWalkSpeed', 'WalkSpeed', 'RunSpeed', 'RideSprintSpeed', 'TransportSpeed',
        'Level60_HP_Min', 'Level60_HP_Max', 'Level60_Attack_Min', 'Level60_Attack_Max',
        'Level60_Defense_Min', 'Level60_Defense_Max', 'PartnerSkill',
        'ActiveSkill1', 'ActiveSkill1_Level', 'ActiveSkill1_Power', 'ActiveSkill1_CT',
        'ActiveSkill2', 'ActiveSkill2_Level', 'ActiveSkill2_Power', 'ActiveSkill2_CT',
        'ActiveSkill3', 'ActiveSkill3_Level', 'ActiveSkill3_Power', 'ActiveSkill3_CT',
        'DropItem1', 'DropItem1_Quantity', 'DropItem2', 'DropItem2_Quantity', 
        'DropItem3', 'DropItem3_Quantity'
    ]
    
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    # 기존 CSV 로드
    existing_data = load_existing_csv('complete_1_to_34_pals.csv')
    print(f"기존 CSV 행 수: {len(existing_data)}")
    print(f"기존 CSV 컬럼 수: {len(existing_data[0]) if existing_data else 0}")
    
    # 35-38번 팰 데이터 (크롤링된 마크다운 내용)
    pals_data = {
        35: {
            'name': '베리고트',
            'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_BerryGoat_icon_normal.webp)](https://paldb.cc/ko/Caprity)

[베리고트](https://paldb.cc/ko/Caprity)#35

풀 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

열매 채집 Lv.1

##### Stats

Size

S

Rarity

3

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

100

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

90

Support

120

##### Movement

SlowWalkSpeed

70

WalkSpeed

70

RunSpeed

400

RideSprintSpeed

550

TransportSpeed

235

##### Level 60

HP

4075 – 5050

공격

441 – 543

방어

488 – 620

##### Others

##### Partner Skill: 열매 채집

##### Active Skills

Lv. 1 [바람의 칼날](https://paldb.cc/ko/Wind_Cutter)

풀 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 30

Lv. 7 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 25

Lv. 15 [모래 돌풍](https://paldb.cc/ko/Bog_Blast)

땅 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 40

##### Passive Skills

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Meat_BerryGoat.webp)베리고트 향초 고기](https://paldb.cc/ko/Caprity_Meat) 2 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Berries.webp)빨간 열매](https://paldb.cc/ko/Red_Berries) 2–4 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Horn.webp)뿔](https://paldb.cc/ko/Horn) 1–2 | 100% |

##### Tribes"""
        },
        36: {
            'name': '멜파카',
            'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Alpaca_icon_normal.webp)](https://paldb.cc/ko/Melpaca)

[멜파카](https://paldb.cc/ko/Melpaca)#36

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

털파카파카 Lv.1

##### Stats

Size

M

Rarity

3

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

90

MeleeAttack

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

90

Support

100

##### Movement

SlowWalkSpeed

62

WalkSpeed

62

RunSpeed

500

RideSprintSpeed

900

TransportSpeed

261

##### Level 60

HP

3750 – 4627

공격

465 – 575

방어

488 – 620

##### Others

##### Partner Skill: 털파카파카

##### Active Skills

Lv. 1 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 25

Lv. 7 [푹신 태클](https://paldb.cc/ko/Fluffy_Tackle)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 40

Lv. 15 [모래 돌풍](https://paldb.cc/ko/Bog_Blast)

땅 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 40

##### Passive Skills

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Wool.webp)양털](https://paldb.cc/ko/Wool) 2–5 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Leather.webp)가죽](https://paldb.cc/ko/Leather) 1 | 100% |

##### Tribes"""
        },
        37: {
            'name': '신령사슴',
            'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Deer_icon_normal.webp)](https://paldb.cc/ko/Eikthyrdeer)

[신령사슴](https://paldb.cc/ko/Eikthyrdeer)#37

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

숲의 수호자 Lv.1

##### Stats

Size

L

Rarity

4

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

95

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

Support

100

##### Movement

SlowWalkSpeed

80

WalkSpeed

120

RunSpeed

700

RideSprintSpeed

900

TransportSpeed

390

##### Level 60

HP

3912 – 4838

공격

490 – 607

방어

440 – 557

##### Others

##### Partner Skill: 숲의 수호자

##### Active Skills

Lv. 1 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 4

위력: 35

Lv. 7 [들이받기](https://paldb.cc/ko/Antler_Uppercut)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 5

위력: 50

Lv. 15 [바위 폭발](https://paldb.cc/ko/Stone_Blast)

땅 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 10

위력: 55

##### Passive Skills

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Food_Meat_Deer.webp)신령사슴의 사슴고기](https://paldb.cc/ko/Eikthyrdeer_Venison) 2 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Leather.webp)가죽](https://paldb.cc/ko/Leather) 2–3 | 100% |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Horn.webp)뿔](https://paldb.cc/ko/Horn) 2 | 100% |

##### Tribes"""
        },
        38: {
            'name': '나이트윙',
            'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_HawkBird_icon_normal.webp)](https://paldb.cc/ko/Nitewing)

[나이트윙](https://paldb.cc/ko/Nitewing)#38

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

여행의 동반자 Lv.1

##### Stats

Size

L

Rarity

3

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

100

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

95

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

Support

100

##### Movement

SlowWalkSpeed

150

WalkSpeed

150

RunSpeed

600

RideSprintSpeed

750

TransportSpeed

450

##### Level 60

HP

4075 – 5050

공격

563 – 702

방어

440 – 557

##### Others

##### Partner Skill: 여행의 동반자

##### Active Skills

Lv. 1 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 25

Lv. 7 [토네이도 어택](https://paldb.cc/ko/Tornado_Attack)

무속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 13

위력: 65

Lv. 15 [바람의 칼날](https://paldb.cc/ko/Wind_Cutter)

풀 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 2

위력: 30

##### Passive Skills

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Leather.webp)가죽](https://paldb.cc/ko/Leather) 1–3 | 100% |

##### Tribes"""
        }
    }
    
    # 35-38번 팰 파싱 및 추가
    new_data = existing_data.copy()
    
    for pal_num, pal_info in pals_data.items():
        print(f"{pal_num}번 {pal_info['name']} 파싱 중...")
        
        parsed_info = extract_pal_info(pal_info['content'], pal_num, pal_info['name'])
        new_data.append(parsed_info)
        
        print(f"✅ {pal_info['name']} 완료 (파트너 스킬: {parsed_info.get('PartnerSkill', '')[:20]})")
    
    # 새로운 CSV 파일로 저장
    output_filename = 'complete_1_to_38_pals.csv'
    save_csv(new_data, output_filename)
    
    print(f"\n✅ 완료! {output_filename} 저장됨")
    print(f"총 {len(new_data)}개 팰 (1-38번)")
    print(f"컬럼 수: {len(new_data[0]) if new_data else 0}")

if __name__ == "__main__":
    main() 