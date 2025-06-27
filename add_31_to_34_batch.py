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
        desc_match = re.search(r'Lv\.1[^가-힣]*([가-힣][^#]*?)(?=\n\n|\n\[|\n\[|$)', skill_section, re.DOTALL)
        if desc_match:
            skill_description = desc_match.group(1).strip()
        
        # 필요 아이템 추출
        item_match = re.search(r'기술(\d+)', skill_section)
        if item_match:
            need_item_tech_level = int(item_match.group(1))
            need_item = f"기술{need_item_tech_level}"
    
    return skill_name, skill_description, need_item, need_item_tech_level

def extract_active_skills_info(content):
    """액티브 스킬 정보 추출"""
    skills = []
    active_skills_match = re.search(r'##### Active Skills\s*(.+?)(?=\n#####|$)', content, re.DOTALL)
    if active_skills_match:
        skills_section = active_skills_match.group(1)
        skill_matches = re.finditer(r'Lv\. (\d+) \[([^\]]+)\].*?\n\n([^\n]+?)\n\n위력: (\d+)', skills_section, re.DOTALL)
        
        for match in skill_matches:
            level = int(match.group(1))
            name = match.group(2)
            element = ""
            desc = match.group(3)
            power = int(match.group(4))
            
            # 속성 정보 찾기
            element_match = re.search(r'([가-힣]+ 속성)', desc)
            if element_match:
                element = element_match.group(1)
            
            skills.append({
                'level': level,
                'name': name,
                'element': element,
                'power': power,
                'description': desc.strip()
            })
    
    # 첫 3개 스킬 정보만 반환
    while len(skills) < 3:
        skills.append({'level': 0, 'name': '', 'element': '', 'power': 0, 'description': ''})
    
    return skills[:3]

def parse_pal_data(content, pal_id, pal_name):
    """팰 데이터 파싱"""
    
    # 기본 정보 추출
    nickname_match = re.search(r'\[(.*?)\]#' + str(pal_id), content)
    nickname = nickname_match.group(1) if nickname_match else ""
    
    # 설명 추출
    summary_match = re.search(r'##### Summary\s*(.+?)(?=\n#####|\n\[|$)', content, re.DOTALL)
    description = summary_match.group(1).strip() if summary_match else ""
    
    # 속성 추출
    element_match = re.search(r'(\w+ 속성)', content)
    elements = element_match.group(1) if element_match else ""
    
    # Stats 추출
    stats_section = re.search(r'##### Stats\s*(.+?)(?=\n#####)', content, re.DOTALL)
    stats = {}
    if stats_section:
        stats_text = stats_section.group(1)
        stats_patterns = {
            'Size': r'Size\s*(\S+)',
            'Rarity': r'Rarity\s*(\d+)',
            'Health': r'HP\s*(\d+)',
            'Food': r'식사량\s*(\d+)',
            'MeleeAttack': r'MeleeAttack\s*(\d+)',
            'Attack': r'공격\s*(\d+)',
            'Defense': r'방어\s*(\d+)',
            'Work_Speed': r'작업 속도\s*(\d+)',
            'Support': r'Support\s*(\d+)',
            'CaptureRateCorrect': r'CaptureRateCorrect\s*(\d+)',
            'MaleProbability': r'MaleProbability\s*(\d+)',
            'CombiRank': r'CombiRank\s*(\d+)',
            'Gold_Coin': r'금화\s*(\d+)',
            'Code': r'Code\s*(\w+)'
        }
        
        for key, pattern in stats_patterns.items():
            match = re.search(pattern, stats_text)
            stats[key] = match.group(1) if match else ""
    
    # Movement 추출
    movement_section = re.search(r'##### Movement\s*(.+?)(?=\n#####)', content, re.DOTALL)
    movement = {}
    if movement_section:
        movement_text = movement_section.group(1)
        movement_patterns = {
            'SlowWalkSpeed': r'SlowWalkSpeed\s*(\d+)',
            'WalkSpeed': r'WalkSpeed\s*(\d+)',
            'RunSpeed': r'RunSpeed\s*(\d+)',
            'RideSprintSpeed': r'RideSprintSpeed\s*(\d+)',
            'TransportSpeed': r'TransportSpeed\s*(\d+)'
        }
        
        for key, pattern in movement_patterns.items():
            match = re.search(pattern, movement_text)
            movement[key] = match.group(1) if match else ""
    
    # Level 60 stats 추출
    level60_section = re.search(r'##### Level 60\s*(.+?)(?=\n#####)', content, re.DOTALL)
    level60 = {}
    if level60_section:
        level60_text = level60_section.group(1)
        hp_match = re.search(r'HP\s*(\d+)[^\d]*(\d+)', level60_text)
        attack_match = re.search(r'공격\s*(\d+)[^\d]*(\d+)', level60_text)
        defense_match = re.search(r'방어\s*(\d+)[^\d]*(\d+)', level60_text)
        
        level60['Health_60'] = hp_match.group(1) if hp_match else ""
        level60['Attack_60'] = attack_match.group(1) if attack_match else ""
        level60['Defense_60'] = defense_match.group(1) if defense_match else ""
    
    # 파트너 스킬 정보
    partner_skill_name, partner_skill_desc, need_item, need_item_tech_level = extract_partner_skill_info(content)
    
    # 액티브 스킬 정보
    active_skills = extract_active_skills_info(content)
    
    # Egg 정보 추출
    egg_match = re.search(r'Egg\s*\[.*?\]([^\]]+)', content)
    egg = egg_match.group(1) if egg_match else ""
    
    # 44개 컬럼에 맞는 데이터 생성
    return [
        pal_id,                           # id
        pal_name,                         # name_kor  
        nickname,                         # pal_nick_kor
        description,                      # description_kor
        elements,                         # elements
        stats.get('Size', ''),            # Size
        extract_number(stats.get('Rarity', 0)),      # Rarity
        extract_number(stats.get('Health', 0)),      # Health
        extract_number(stats.get('Food', 0)),        # Food
        extract_number(stats.get('MeleeAttack', 0)), # MeleeAttack
        extract_number(stats.get('Attack', 0)),      # Attack
        extract_number(stats.get('Defense', 0)),     # Defense
        extract_number(stats.get('Work_Speed', 0)),  # Work Speed
        extract_number(stats.get('Support', 0)),     # Support
        extract_number(stats.get('CaptureRateCorrect', 0)), # CaptureRateCorrect
        extract_number(stats.get('MaleProbability', 0)),    # MaleProbability
        extract_number(stats.get('CombiRank', 0)),          # CombiRank
        extract_number(stats.get('Gold_Coin', 0)),          # Gold Coin
        egg,                              # Egg
        stats.get('Code', ''),            # Code
        extract_number(movement.get('SlowWalkSpeed', 0)),   # SlowWalkSpeed
        extract_number(movement.get('WalkSpeed', 0)),       # WalkSpeed
        extract_number(movement.get('RunSpeed', 0)),        # RunSpeed
        extract_number(movement.get('RideSprintSpeed', 0)), # RideSprintSpeed
        extract_number(movement.get('TransportSpeed', 0)),  # TransportSpeed
        extract_number(level60.get('Health_60', 0)),        # Health_60
        extract_number(level60.get('Attack_60', 0)),        # Attack_60
        extract_number(level60.get('Defense_60', 0)),       # Defense_60
        partner_skill_name,               # Partner_Skill_Name
        partner_skill_desc,               # Partner_Skill_Describe
        need_item,                        # Partner_Skill_NeedItem
        need_item_tech_level,             # Partner_Skill_NeedItemTechLevel
        '',                               # Partner_Skill_Level
        '',                               # Partner_Skill_Items
        '',                               # Partner_Skill_ItemQuantity
        '',                               # Partner_Skill_ItemProbability
        active_skills[0]['name'],         # ActiveSkill1_Name
        active_skills[0]['element'],      # ActiveSkill1_Element  
        active_skills[0]['power'],        # ActiveSkill1_Power
        active_skills[0]['description'],  # ActiveSkill1_Describe
        active_skills[1]['name'],         # ActiveSkill2_Name
        active_skills[1]['element'],      # ActiveSkill2_Element
        active_skills[1]['power'],        # ActiveSkill2_Power
        active_skills[1]['description']   # ActiveSkill2_Describe
    ]

# 각 팰 정보 정의
pals_data = [
    {
        'id': 31,
        'name': '샤키드',
        'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_SharkKid_icon_normal.webp)](https://paldb.cc/ko/Gobfin)

[샤키드](https://paldb.cc/ko/Gobfin)#31

물 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

삐돌이 상어 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_001.webp)

발동하면 목표로 삼은 적을 향해
높은 위력의 [아쿠아 샷](https://paldb.cc/ko/Aqua_Gun)(으)로 공격한다.
보유하고 있는 동안 플레이어의 공격력이 증가한다.

##### Summary

먼 옛날엔 거대하고 강력한 수생 팰이었지만
먹이가 적어지며 지상으로 나왔다.
걷는 데 상당한 에너지가 필요해
점점 몸집이 작아졌고 지금은 약한 팰이 됐다.

##### Stats

Size

S

Rarity

2

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

225

MeleeAttack

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

75

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1090

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1840

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Water_01.webp)축축한 알](https://paldb.cc/ko/Damp_Egg)

Code

SharkKid

##### Movement

SlowWalkSpeed

50

WalkSpeed

80

RunSpeed

400

RideSprintSpeed

500

TransportSpeed

120

##### Level 60

HP

3750 – 4627

공격

538 – 670

방어

415 – 525

##### Active Skills

Lv. 1 [워터 제트](https://paldb.cc/ko/Hydro_Jet)

물 속성

위력: 30

적을 향해
고속 물 탄환을 발사한다.

Lv. 7 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

위력: 35

에너지를 모아
탄환 형태로 발사한다.

Lv. 15 [아쿠아 샷](https://paldb.cc/ko/Aqua_Gun)

물 속성

위력: 40

대상을 향해 일직선으로 날아가는
물 탄환을 발사한다."""
    },
    {
        'id': 32,
        'name': '건다리',
        'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_WindChimes_icon_normal.webp)](https://paldb.cc/ko/Hangyu)

[건다리](https://paldb.cc/ko/Hangyu)#32

땅 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

하늘 그네 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_008.webp)

보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다.
활공 중 천천히 상승 기류를 탈 수 있다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Gloves.webp)](https://paldb.cc/ko/Hangyus_Gloves) 기술20

##### Summary

거대한 팔은 강철도 찢어버릴 정도다.
대역죄인을 마을 광장에 결박해
[건다리](https://paldb.cc/ko/Hangyu) 에게 전신이 으스러지도록
만드는 잔혹한 형벌이 시행됐던 적도 있다.

##### Stats

Size

XS

Rarity

1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1420

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1020

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Earth_01.webp)거친 느낌의 알](https://paldb.cc/ko/Rocky_Egg)

Code

WindChimes

##### Movement

SlowWalkSpeed

50

WalkSpeed

100

RunSpeed

400

RideSprintSpeed

550

TransportSpeed

250

##### Level 60

HP

3425 – 4205

공격

441 – 543

방어

391 – 493

##### Active Skills

Lv. 1 [모래 돌풍](https://paldb.cc/ko/Bog_Blast)

땅 속성

위력: 40

끈적거리는 진흙을
적을 향해 발사한다.

Lv. 7 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

위력: 25

고속으로 날아가는 공기 덩어리를 발사한다.

Lv. 15 [바람의 칼날](https://paldb.cc/ko/Wind_Cutter)

풀 속성

위력: 30

적을 향해 일직선으로 날아가는
초고속 바람의 칼날을 발사한다."""
    },
    {
        'id': 33,
        'name': '초판다',
        'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_GrassPanda_icon_normal.webp)](https://paldb.cc/ko/Mossanda)

[초판다](https://paldb.cc/ko/Mossanda)#33

풀 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

척탄 판다 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_017.webp)

등에 타고 이동할 수 있다.
탑승 중 수류탄 발사기 연사가 가능해진다.

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Essential_SkillUnlock_Grenadelauncher.webp)](https://paldb.cc/ko/Mossandas_Grenade_Launcher) 기술24

##### Summary

믿기 힘든 괴력의 소유자.
어느 실험에서 3,000장이 넘는 종이 뭉치를 가볍게 찢었다.
육식을 안 하는 걸 감사히 생각해야 한다.

##### Stats

Size

L

Rarity

6

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

350

MeleeAttack

100

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

430

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

6200

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Leaf_01.webp)신록의 대형 알](https://paldb.cc/ko/Large_Verdant_Egg)

Code

GrassPanda

##### Movement

SlowWalkSpeed

50

WalkSpeed

100

RunSpeed

600

RideSprintSpeed

1000

TransportSpeed

275

##### Level 60

HP

4075 – 5050

공격

538 – 670

방어

488 – 620

##### Active Skills

Lv. 1 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

위력: 35

에너지를 모아
탄환 형태로 발사한다.

Lv. 7 [씨앗 기관총](https://paldb.cc/ko/Seed_Machine_Gun)

풀 속성

위력: 50

딱딱한 씨앗을 많이 쏟아내며
전방의 적을 공격한다.

Lv. 15 [바위 대포](https://paldb.cc/ko/Stone_Cannon)

땅 속성

위력: 70

바로 앞 지면에서 바위를 뽑아
적을 향해 발사한다."""
    },
    {
        'id': 34,
        'name': '캔디쉽',
        'content': """[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_SweetsSheep_icon_normal.webp)](https://paldb.cc/ko/Woolipop)

[캔디쉽](https://paldb.cc/ko/Woolipop)#34

무속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

캔디 팝 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_014.webp)

[가축 목장](https://paldb.cc/ko/Ranch) 에 배치하면,
[솜사탕](https://paldb.cc/ko/Cotton_Candy) 을(를) 떨어뜨리기도 한다.

##### Summary

전신이 설탕보다 18,000배나 달다.
향기에 이끌려 덥석 베어 문 육식 팰은
상상을 초월하는 단맛에 눈이 뒤집힌 채 졸도해 버린다.

##### Stats

Size

S

Rarity

3

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

150

MeleeAttack

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

70

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

90

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

1190

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

1450

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg.webp)평범한 알](https://paldb.cc/ko/Common_Egg)

Code

SweetsSheep

##### Movement

SlowWalkSpeed

50

WalkSpeed

100

RunSpeed

300

RideSprintSpeed

400

TransportSpeed

200

##### Level 60

HP

3100 – 3782

공격

441 – 543

방어

488 – 620

##### Active Skills

Lv. 1 [공기 대포](https://paldb.cc/ko/Air_Cannon)

무속성

위력: 25

고속으로 날아가는 공기 덩어리를 발사한다.

Lv. 7 [모래 돌풍](https://paldb.cc/ko/Bog_Blast)

땅 속성

위력: 40

끈적거리는 진흙을
적을 향해 발사한다.

Lv. 15 [파워 샷](https://paldb.cc/ko/Power_Shot)

무속성

위력: 35

에너지를 모아
탄환 형태로 발사한다."""
    }
]

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_30_pals.csv'
    output_file = 'complete_1_to_34_pals.csv'
    
    # 기존 CSV 읽기
    existing_df = pd.read_csv(input_file)
    print(f"기존 CSV 행 수: {len(existing_df)}")
    print(f"기존 CSV 컬럼 수: {len(existing_df.columns)}")
    
    # 새로운 팰 데이터 처리
    new_rows = []
    for pal_data in pals_data:
        print(f"\n{pal_data['id']}번 {pal_data['name']} 파싱 중...")
        row = parse_pal_data(pal_data['content'], pal_data['id'], pal_data['name'])
        new_rows.append(row)
        print(f"✅ {pal_data['name']} 완료 (파트너 스킬: {row[28]})")
    
    # 새로운 행들을 DataFrame으로 변환
    new_df = pd.DataFrame(new_rows, columns=existing_df.columns)
    
    # 기존 데이터와 합치기
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    
    # CSV 파일로 저장
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\n✅ 완료! {output_file} 저장됨")
    print(f"총 {len(combined_df)}개 팰 (1-{pals_data[-1]['id']}번)")
    print(f"컬럼 수: {len(combined_df.columns)}")
    
    # 새로 추가된 팰들 확인
    print("\n🎉 새로 추가된 팰들:")
    for pal_data in pals_data:
        print(f"  - {pal_data['id']}번: {pal_data['name']}")

if __name__ == "__main__":
    main() 