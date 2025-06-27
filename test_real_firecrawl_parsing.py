#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
실제 firecrawl 데이터로 파싱 테스트
"""

import re
from typing import Dict

def parse_real_firecrawl_data():
    """
    실제 firecrawl에서 받은 얼서니 데이터로 파싱 테스트
    """
    
    # 실제 firecrawl 결과
    real_markdown = """Update cookie preferences


[![](https://cdn.paldb.cc/image/Pal/Texture/PalIcon/Normal/T_Werewolf_Ice_icon_normal.webp)](https://paldb.cc/ko/Loupmoon_Cryst)

[얼서니](https://paldb.cc/ko/Loupmoon_Cryst)#46B

얼음 속성

[파트너 스킬](https://paldb.cc/ko/Partner_Skill)

냉기로 번쩍이는 발톱날 Lv.1

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_skill_pal_001.webp)

발동하면 목표로 삼은 적을 향해
높은 위력의 [옥설 발톱](https://paldb.cc/ko/Snow_Claw)(으)로 공격한다.


[작업 적성](https://paldb.cc/ko/Work_Suitability)

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_04.webp) 수작업](https://paldb.cc/ko/Handiwork)

Lv2

[![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_icon_palwork_10.webp) 냉각](https://paldb.cc/ko/Cooling)

Lv3

식사량

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_on.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)

##### Stats

Size

M

Rarity

3

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_00.webp)HP

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_foodamount_off.webp)식사량

350

MeleeAttack

130

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_02.webp)공격

105

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_03.webp)방어

80

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_icon_status_05.webp)작업 속도

100

Support

100

CaptureRateCorrect

1

MaleProbability

50

[CombiRank](https://paldb.cc/ko/Breeding_Farm)

805

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Money.webp)금화](https://paldb.cc/ko/Gold_Coin)

2820

Egg

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_PalEgg_Ice_01.webp)얼어붙은 알](https://paldb.cc/ko/Frozen_Egg)

Code

Werewolf\_Ice

##### Summary

머리의 뿔은 절대 녹지 않는 신비한 얼음.
뿔을 부러뜨려 빙수를 만들면
엄청난 별미가 된다고 하지만
먹은 본인도 [얼서니](https://paldb.cc/ko/Loupmoon_Cryst) 도 머리가 띵할 만큼 아파진다.

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


Lv. 7 [얼음 칼날](https://paldb.cc/ko/Icicle_Cutter)

[![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Consume_SkillCard_Frost.webp)](https://paldb.cc/ko/Ice_Skill_Fruit%3A_Icicle_Cutter)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 10

위력: 55

축적치:빙결

50

초승달 모양의 얼음 날을 만들어
전방으로 발사한다.


Lv. 15 [옥설 발톱](https://paldb.cc/ko/Snow_Claw)

![](https://cdn.paldb.cc/image/Pal/Texture/UI/InGame/T_prt_pal_skill_lock.webp)

얼음 속성

![](https://cdn.paldb.cc/image/Pal/Texture/UI/Main_Menu/T_Icon_PalSkillCoolTime.webp): 7

위력: 55

축적치:빙결

100

[얼서니](https://paldb.cc/ko/Loupmoon_Cryst) 전용 스킬.
전방으로 뛰어오르며 재빨리 2회 할퀸다.
이 참격엔 얼음 속성의 힘이 깃들어 있다.


Lv. 22 [얼음 칼날](https://paldb.cc/ko/Icicle_Cutter)

Lv. 30 [아이시클 불릿](https://paldb.cc/ko/Icicle_Bullet)

Lv. 40 [아이시클 라인](https://paldb.cc/ko/Icicle_Line)

Lv. 50 [눈보라 스파이크](https://paldb.cc/ko/Blizzard_Spike)

##### Possible Drops

| Item | Probability |
| --- | --- |
| [![](https://cdn.paldb.cc/image/Others/InventoryItemIcon/Texture/T_itemicon_Material_Bone.webp)뼈](https://paldb.cc/ko/Bone) 1 | 100% |
"""
    
    data = {
        "ID": "46B",
        "Name": "얼서니",
        "EnglishName": "",
        "Description": "",
        "Type1": "",
        "Type2": "",
        "HP": "",
        "ATK": "",
        "DEF": "",
        "WorkSpeed": "",
        "Rarity": "",
        "Size": "",
        "Tribe": "",
        "PartnerSkill": "",
        "PartnerSkillDescription": "",
        "Work1": "",
        "Work1Level": "",
        "Work2": "",
        "Work2Level": "",
        "Work3": "",
        "Work3Level": "",
        "Work4": "",
        "Work4Level": "",
        "FoodAmount": "",
        "DropItem1": "",
        "ActiveSkill1": "",
        "ActiveSkill2": "",
        "ActiveSkill3": "",
        "ActiveSkill4": "",
        "ActiveSkill5": "",
        "ActiveSkill6": "",
        "ActiveSkill7": "",
        "Nick": ""
    }
    
    print("🔍 실제 firecrawl 데이터 파싱 시작...")
    
    lines = real_markdown.split('\n')
    
    # 속성 추출
    for line in lines:
        if "얼음 속성" in line:
            data["Type1"] = "얼음"
            break
    
    # 파트너 스킬 추출
    for i, line in enumerate(lines):
        if "냉기로 번쩍이는 발톱날" in line:
            data["PartnerSkill"] = "냉기로 번쩍이는 발톱날"
            break
    
    # 작업 적성 추출 - 더 정확한 방식
    for i, line in enumerate(lines):
        # 수작업 찾기
        if "수작업" in line and "T_icon_palwork_04.webp" in line:
            data["Work1"] = "수작업"
            # 다음 몇 줄에서 Lv 찾기
            for j in range(i+1, min(i+5, len(lines))):
                if "Lv" in lines[j]:
                    level_match = re.search(r'Lv(\d+)', lines[j])
                    if level_match:
                        data["Work1Level"] = level_match.group(1)
                    break
                    
        # 냉각 찾기  
        elif "냉각" in line and "T_icon_palwork_10.webp" in line:
            data["Work2"] = "냉각"
            # 다음 몇 줄에서 Lv 찾기
            for j in range(i+1, min(i+5, len(lines))):
                if "Lv" in lines[j]:
                    level_match = re.search(r'Lv(\d+)', lines[j])
                    if level_match:
                        data["Work2Level"] = level_match.group(1)
                    break
    
    # 스탯 추출 - 패턴 매칭 방식
    # Size 추출
    size_pattern = re.search(r'Size\s*\n\s*([SMLX]{1,2})', real_markdown)
    if size_pattern:
        data["Size"] = size_pattern.group(1)
    
    # Rarity 추출
    rarity_pattern = re.search(r'Rarity\s*\n\s*(\d+)', real_markdown)
    if rarity_pattern:
        data["Rarity"] = rarity_pattern.group(1)
        
    # HP 추출
    hp_pattern = re.search(r'HP\s*\n\s*(\d+)', real_markdown)
    if hp_pattern:
        data["HP"] = hp_pattern.group(1)
        
    # 공격 추출  
    atk_pattern = re.search(r'공격\s*\n\s*(\d+)', real_markdown)
    if atk_pattern:
        data["ATK"] = atk_pattern.group(1)
        
    # 방어 추출
    def_pattern = re.search(r'방어\s*\n\s*(\d+)', real_markdown)
    if def_pattern:
        data["DEF"] = def_pattern.group(1)
        
    # 작업 속도 추출
    work_speed_pattern = re.search(r'작업 속도\s*\n\s*(\d+)', real_markdown)
    if work_speed_pattern:
        data["WorkSpeed"] = work_speed_pattern.group(1)
    
    # 식사량 추출
    food_count = real_markdown.count("T_Icon_foodamount_on.webp")
    data["FoodAmount"] = str(food_count)
    
    # 영어 이름 추출
    if "Werewolf\\_Ice" in real_markdown:
        data["EnglishName"] = "Werewolf_Ice"
    
    # 설명 추출
    summary_start = real_markdown.find("##### Summary")
    if summary_start != -1:
        summary_section = real_markdown[summary_start:summary_start + 200]
        lines = summary_section.split('\n')
        for line in lines[1:]:
            if line.strip() and not line.startswith('#') and "머리의" in line:
                data["Description"] = line.strip()
                break
    
    # 액티브 스킬 추출
    active_skills = []
    if "얼음 미사일" in real_markdown:
        active_skills.append("얼음 미사일")
    if "얼음 칼날" in real_markdown:
        active_skills.append("얼음 칼날") 
    if "옥설 발톱" in real_markdown:
        active_skills.append("옥설 발톱")
    if "아이시클 불릿" in real_markdown:
        active_skills.append("아이시클 불릿")
    if "아이시클 라인" in real_markdown:
        active_skills.append("아이시클 라인")
    if "눈보라 스파이크" in real_markdown:
        active_skills.append("눈보라 스파이크")
    
    for i, skill in enumerate(active_skills[:7], 1):
        data[f"ActiveSkill{i}"] = skill
    
    # 드롭 아이템 추출
    if "뼈" in real_markdown:
        data["DropItem1"] = "뼈"
    
    print("✅ 실제 데이터 파싱 완료!")
    
    print("\n📊 파싱 결과:")
    for key, value in data.items():
        if value:
            print(f"   {key}: {value}")
    
    return data

if __name__ == "__main__":
    parse_real_firecrawl_data() 