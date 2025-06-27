#!/usr/bin/env python3
"""
Palworld Advanced Batch 6 Crawler
올바른 URL 패턴으로 더 많은 B variants를 발견합니다.
"""

import re
import json

def get_known_pal_names():
    """
    이미 알려진 팰 이름들과 그들의 가능한 아종 조합들
    """
    base_pals = {
        # 화염/용 계열
        'Chillet': ['_Ignis'],  # 이미 55B 천도뇽으로 확인됨
        'Arsox': ['_Ice', '_Cryst', '_Terra'],
        'Foxparks': ['_Ice', '_Water', '_Thunder'],
        'Rooby': ['_Grass', '_Ice', '_Thunder'],
        
        # 물/전기 계열  
        'Surfent': ['_Ignis', '_Terra', '_Dark'],
        'Surfent_Terra': [],  # 이미 아종
        'Azurobe': ['_Ignis', '_Ice', '_Thunder'],
        'Celeray': ['_Lux'],  # 이미 25B 일레카이트로 확인됨
        
        # 풀/땅 계열
        'Robinquill': ['_Terra'],  # 이미 48B 산도로로 확인됨
        'Verdash': ['_Ignis', '_Ice', '_Lux'],
        'Petallia': ['_Dark', '_Ice', '_Thunder'],
        'Lyleen': ['_Noct'],
        
        # 얼음 계열
        'Loupmoon': ['_Cryst'],  # 이미 46B 얼서니로 확인됨
        'Penking': ['_Black'],  # 이미 11B 펭키드로 확인됨
        'Vanwyrm': ['_Cryst'],
        'Wumpo': ['_Botan'],
        
        # 어둠 계열
        'Felbat': ['_Fire', '_Lux'],
        'Grintale': ['_Ignis', '_Cryst'],
        'Katress': ['_Ignis'],
        'Astegon': ['_Terra'],
        
        # 땅 계열
        'Gorirat': ['_Terra'],  # 이미 49B 고릴가이아로 확인됨
        'Digtoise': ['_Lux', '_Ignis'],
        'Dumud': ['_Cryst', '_Ignis'],
        'Anubis': ['_Grass', '_Water'],
        
        # 번개 계열
        'Mossanda': ['_Lux'],  # 이미 33B 썬더판다로 확인됨
        'Univolt': ['_Dark', '_Ice'],
        'Orserk': ['_Ice', '_Terra'],
        'Relaxaurus': ['_Lux'],
        
        # 기타
        'Kingpaca': ['_Cryst'],
        'Mammorest': ['_Cryst'],
        'Quivern': ['_Botan'],
        'Elphidran': ['_Aqua'],
        'Jormuntide': ['_Ignis'],
        'Nitewing': ['_Dark'],
        'Blazehowl': ['_Noct'],
        'Ragnahawk': ['_Aqua'],
        'Suzaku': ['_Aqua'],
        'Frostallion': ['_Noct'],  # 이미 110B 그레이섀도우로 확인됨
    }
    
    return base_pals

def generate_priority_candidates():
    """
    우선 시도할 아종 후보들을 생성
    """
    base_pals = get_known_pal_names()
    candidates = []
    
    for base_name, suffixes in base_pals.items():
        for suffix in suffixes:
            url = f"https://paldb.cc/ko/{base_name}{suffix}"
            candidates.append({
                'base_name': base_name,
                'suffix': suffix,
                'url': url,
                'expected_variant': f"{base_name}{suffix}"
            })
    
    return candidates

def parse_pal_data(content, expected_name):
    """
    크롤링된 콘텐츠에서 팰 데이터 추출
    """
    if not content or len(content.strip()) < 100:
        return None
    
    # B variant ID 추출 (예: #55B)
    b_id_pattern = r'#(\d+B)'
    b_id_match = re.search(b_id_pattern, content)
    
    if not b_id_match:
        return None
    
    b_id = b_id_match.group(1)
    
    # 팰 이름 추출 (한글)
    name_patterns = [
        r'\[([가-힣]+)\]\(https://paldb\.cc/ko/[^)]+\)#{}'.format(re.escape(b_id)),
        r'](#)\s*([가-힣]+)',
        r'^([가-힣]+)#{}'.format(re.escape(b_id))
    ]
    
    pal_name = None
    for pattern in name_patterns:
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            pal_name = match.group(1) if match.group(1) else match.group(2)
            break
    
    if not pal_name:
        return None
    
    # 속성 정보 추출
    type_pattern = r'((?:화염|얼음|물|번개|풀|땅|어둠|용|무) 속성)'
    type_matches = re.findall(type_pattern, content)
    
    type1 = type_matches[0].replace(' 속성', '') if len(type_matches) > 0 else ''
    type2 = type_matches[1].replace(' 속성', '') if len(type_matches) > 1 else ''
    
    # 스탯 정보 추출
    hp_pattern = r'HP\s*(\d+)'
    atk_pattern = r'공격\s*(\d+)'
    def_pattern = r'방어\s*(\d+)'
    work_speed_pattern = r'작업 속도\s*(\d+)'
    rarity_pattern = r'Rarity\s*(\d+)'
    size_pattern = r'Size\s*([A-Z]+)'
    food_amount_pattern = r'식사량\s*(\d+)'
    
    hp = re.search(hp_pattern, content).group(1) if re.search(hp_pattern, content) else ''
    atk = re.search(atk_pattern, content).group(1) if re.search(atk_pattern, content) else ''
    def_stat = re.search(def_pattern, content).group(1) if re.search(def_pattern, content) else ''
    work_speed = re.search(work_speed_pattern, content).group(1) if re.search(work_speed_pattern, content) else ''
    rarity = re.search(rarity_pattern, content).group(1) if re.search(rarity_pattern, content) else ''
    size = re.search(size_pattern, content).group(1) if re.search(size_pattern, content) else ''
    food_amount = re.search(food_amount_pattern, content).group(1) if re.search(food_amount_pattern, content) else ''
    
    # 파트너 스킬 정보 추출
    partner_skill_pattern = r'##### Partner Skill: ([^#\n]+)'
    partner_skill_match = re.search(partner_skill_pattern, content)
    partner_skill = partner_skill_match.group(1).strip() if partner_skill_match else ''
    
    # 작업 적성 정보 추출
    work_patterns = [
        r'불 피우기.*?Lv(\d+)',
        r'냉각.*?Lv(\d+)', 
        r'관개.*?Lv(\d+)',
        r'발전.*?Lv(\d+)',
        r'수작업.*?Lv(\d+)',
        r'벌목.*?Lv(\d+)',
        r'채굴.*?Lv(\d+)',
        r'채집.*?Lv(\d+)',
        r'파종.*?Lv(\d+)',
        r'운반.*?Lv(\d+)',
        r'목장.*?Lv(\d+)'
    ]
    
    work_skills = []
    for pattern in work_patterns:
        match = re.search(pattern, content)
        if match:
            work_type = pattern.split('.*?')[0]
            level = match.group(1)
            work_skills.append(f"{work_type} Lv{level}")
    
    work1 = work_skills[0] if len(work_skills) > 0 else ''
    work2 = work_skills[1] if len(work_skills) > 1 else ''
    work3 = work_skills[2] if len(work_skills) > 2 else ''
    
    # 액티브 스킬 추출
    active_skills = []
    skill_pattern = r'Lv\. \d+ \[([^\]]+)\]'
    skill_matches = re.findall(skill_pattern, content)
    active_skills = ', '.join(skill_matches[:8])  # 최대 8개까지
    
    # 드롭 아이템 추출  
    drop_pattern = r'\[([^\]]+)\]\(https://paldb\.cc/ko/[^)]+\) \d+[–-]\d+ \| 100%'
    drop_matches = re.findall(drop_pattern, content)
    drop_item1 = drop_matches[0] if len(drop_matches) > 0 else ''
    drop_item2 = drop_matches[1] if len(drop_matches) > 1 else ''
    
    parsed_data = {
        'ID': b_id,
        'Name': pal_name,
        'EnglishName': expected_name,
        'Description': '',  # 상세 설명은 별도 추출 필요
        'Type1': type1,
        'Type2': type2,
        'PartnerSkill': partner_skill,
        'PartnerSkillDesc': '',
        'HP': hp,
        'ATK': atk,
        'DEF': def_stat,
        'WorkSpeed': work_speed,
        'Rarity': rarity,
        'Size': size,
        'FoodAmount': food_amount,
        'Work1': work1,
        'Work2': work2,
        'Work3': work3,
        'DropItem1': drop_item1,
        'DropItem2': drop_item2,
        'ActiveSkills': active_skills
    }
    
    print(f"✅ 성공적으로 파싱됨: {b_id} {pal_name} ({expected_name})")
    print(f"   타입: {type1}" + (f", {type2}" if type2 else ""))
    print(f"   스탯: HP {hp}, 공격 {atk}, 방어 {def_stat}")
    print(f"   작업: {', '.join([w for w in [work1, work2, work3] if w])}")
    
    return parsed_data

if __name__ == "__main__":
    print("🎮 Palworld Advanced Batch 6 Crawler")
    print("=" * 50)
    
    candidates = generate_priority_candidates()
    print(f"🎯 생성된 우선 후보: {len(candidates)}개")
    
    print(f"\n🔥 Top 10 우선 후보:")
    for i, candidate in enumerate(candidates[:10], 1):
        print(f"{i:2d}. {candidate['expected_variant']} - {candidate['url']}")
    
    print(f"\n📋 다음 단계:")
    print(f"1. 우선 후보들을 Firecrawl로 크롤링")
    print(f"2. 성공한 경우 파싱하여 B variant 정보 추출")
    print(f"3. CSV 파일에 추가")
    
    print(f"\n🚀 준비 완료!") 