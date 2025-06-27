#!/usr/bin/env python3
"""
Palworld Batch 6 Smart Crawler
이전에 완성된 스마트 크롤러를 사용해서 더 많은 B variants를 발견합니다.
"""

import re
import json

def test_firecrawl_simulation():
    """
    Firecrawl 시뮬레이션으로 다음 배치 후보들을 테스트
    이전 배치 5에서 46B, 48B, 49B, 55B를 추가했으므로
    이제 다른 범위의 팰들을 시도해봅시다.
    """
    
    # 이미 발견된 B variants (22개)
    known_b_variants = [
        '5B', '6B', '10B', '11B', '12B', '13B', '23B', '24B', '25B',
        '31B', '32B', '33B', '35B', '37B', '39B', '40B', '45B', 
        '46B', '48B', '49B', '55B', '110B'
    ]
    
    print(f"🔍 현재 발견된 B variants: {len(known_b_variants)}개")
    print(f"📋 목록: {', '.join(known_b_variants)}")
    
    # 다음 배치로 시도할 팰 ID 범위 (50-80)
    next_batch_candidates = []
    suffixes = ['_Ice', '_Ignis', '_Cryst', '_Lux', '_Terra', '_Dark', '_Noct', '_Fire', '_Thunder', '_Grass', '_Ground', '_Water', '_Electric', '_Flower', '_Neutral']
    
    for pal_id in range(50, 81):  # 50-80 범위
        base_id = str(pal_id)
        b_variant_id = f"{pal_id}B"
        
        # 이미 발견된 아종은 제외
        if b_variant_id not in known_b_variants:
            for suffix in suffixes:
                url_candidate = f"https://paldb.cc/ko/PAL{int(base_id):03d}{suffix}"
                next_batch_candidates.append({
                    'pal_id': base_id,
                    'b_variant_id': b_variant_id,
                    'url': url_candidate,
                    'suffix': suffix
                })
    
    print(f"\n🎯 Batch 6 후보 생성 완료: {len(next_batch_candidates)}개 URL")
    print(f"📊 범위: 팰 ID 50-80 (이미 발견된 {len(known_b_variants)}개 제외)")
    
    # 우선 시도할 몇 개 후보 출력
    priority_candidates = next_batch_candidates[:20]  # 첫 20개만
    
    print(f"\n🚀 우선 시도할 후보들:")
    for i, candidate in enumerate(priority_candidates[:10], 1):
        print(f"{i:2d}. {candidate['b_variant_id']} - {candidate['url']}")
    
    return priority_candidates

def parse_firecrawl_content(content, expected_b_id):
    """
    Firecrawl로 가져온 콘텐츠를 파싱하여 팰 정보 추출
    """
    if not content or len(content.strip()) < 100:
        return None
    
    print(f"🔍 파싱 시작: {expected_b_id}")
    
    # 기본 정보 추출
    name_pattern = r'팰 이름[:\s]*([가-힣]+)'
    english_name_pattern = r'영어 이름[:\s]*([A-Za-z_]+)'
    
    name_match = re.search(name_pattern, content)
    english_match = re.search(english_name_pattern, content)
    
    if not name_match:
        print(f"❌ 이름을 찾을 수 없음: {expected_b_id}")
        return None
    
    pal_data = {
        'ID': expected_b_id,
        'Name': name_match.group(1).strip(),
        'EnglishName': english_match.group(1).strip() if english_match else '',
        'Description': '',
        'Type1': '',
        'Type2': '',
        'PartnerSkill': '',
        'PartnerSkillDesc': '',
        'HP': '',
        'ATK': '',
        'DEF': '',
        'WorkSpeed': '',
        'Rarity': '',
        'Size': '',
        'FoodAmount': '',
        'Work1': '',
        'Work2': '',
        'Work3': '',
        'DropItem1': '',
        'DropItem2': '',
        'ActiveSkills': []
    }
    
    # 타입 정보 추출
    type_pattern = r'속성[:\s]*([가-힣\s+|,]+)'
    type_match = re.search(type_pattern, content)
    if type_match:
        types = [t.strip() for t in re.split(r'[+|,\s]+', type_match.group(1)) if t.strip()]
        pal_data['Type1'] = types[0] if len(types) > 0 else ''
        pal_data['Type2'] = types[1] if len(types) > 1 else ''
    
    # 스탯 정보 추출
    hp_pattern = r'HP[:\s]*([0-9]+)'
    atk_pattern = r'공격[력]?[:\s]*([0-9]+)'
    def_pattern = r'방어[력]?[:\s]*([0-9]+)'
    
    hp_match = re.search(hp_pattern, content)
    atk_match = re.search(atk_pattern, content)
    def_match = re.search(def_pattern, content)
    
    if hp_match:
        pal_data['HP'] = hp_match.group(1)
    if atk_match:
        pal_data['ATK'] = atk_match.group(1)
    if def_match:
        pal_data['DEF'] = def_match.group(1)
    
    print(f"✅ 파싱 성공: {pal_data['Name']} ({expected_b_id})")
    return pal_data

if __name__ == "__main__":
    print("🎮 Palworld Batch 6 Smart Crawler 시작!")
    print("=" * 50)
    
    # 다음 배치 후보 생성
    candidates = test_firecrawl_simulation()
    
    print(f"\n📋 다음 단계:")
    print(f"1. 우선 후보 {len(candidates)}개를 Firecrawl로 크롤링")
    print(f"2. 유효한 B variants 발견 시 파싱 및 CSV 추가")
    print(f"3. enhanced_complete_pals_batch6.csv 생성")
    
    print(f"\n🚀 준비 완료! 이제 실제 Firecrawl 크롤링을 시작할 수 있습니다.") 