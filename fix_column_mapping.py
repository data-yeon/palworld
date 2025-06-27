#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

def map_to_existing_columns(pal_data):
    """새로운 팰 데이터를 기존 CSV 컬럼 구조에 맞게 매핑"""
    mapped = {
        'id': pal_data.get('id', ''),
        'name_kor': pal_data.get('name_kor', ''),
        'pal_nick_kor': pal_data.get('pal_nick_kor', ''),
        'description_kor': pal_data.get('description_kor', ''),
        'elements': pal_data.get('elements', ''),
        'stats_size': pal_data.get('size', ''),
        'stats_rarity': pal_data.get('rarity', ''),
        'stats_health': pal_data.get('health', ''),
        'stats_food': pal_data.get('food', ''),
        'stats_attack': pal_data.get('attack', ''),
        'stats_defense': pal_data.get('defense', ''),
        'stats_meleeAttack': pal_data.get('melee_attack', ''),
        'stats_workSpeed': pal_data.get('work_speed', ''),
        'stats_support': pal_data.get('support', ''),
        'stats_captureRateCorrect': pal_data.get('capture_rate_correct', ''),
        'stats_maleProbability': pal_data.get('male_probability', ''),
        'stats_combiRank': pal_data.get('combi_rank', ''),
        'stats_goldCoin': pal_data.get('gold_coin', ''),
        'stats_egg': pal_data.get('egg', ''),
        'stats_code': pal_data.get('code', ''),
        'movement_slowWalkSpeed': pal_data.get('slow_walk_speed', ''),
        'movement_walkSpeed': pal_data.get('walk_speed', ''),
        'movement_runSpeed': pal_data.get('run_speed', ''),
        'movement_transportSpeed': pal_data.get('transport_speed', ''),
        'movement_rideSprintSpeed': pal_data.get('ride_sprint_speed', ''),
        'level60_health': pal_data.get('health_60', ''),
        'level60_attack': pal_data.get('attack_60', ''),
        'level60_defense': pal_data.get('defense_60', ''),
        'partnerSkill_name': pal_data.get('partner_skill_name', ''),
        'partnerSkill_describe': pal_data.get('partner_skill_describe', ''),
        'partnerSkill_needItem': pal_data.get('partner_skill_need_item', ''),
        'partnerSkill_needItemTechLevel': pal_data.get('partner_skill_need_item_tech_level', ''),
        'partnerSkill_level': pal_data.get('partner_skill_level', ''),
        'activeSkills': '',  # 액티브 스킬은 별도 처리 필요
        'activeSkills_count': pal_data.get('active_skills_count', '0'),
        'passiveSkills': '',  # 패시브 스킬은 별도 처리 필요
        'passiveSkills_count': '0',
        'drops': '',  # 드롭은 별도 처리 필요
        'drops_count': pal_data.get('drops_count', '0'),
        'workSuitabilities': '',  # 작업 적성은 별도 처리 필요
        'workSuitabilities_count': pal_data.get('work_suitability_count', '0'),
        'tribes': '',  # 부족은 별도 처리 필요
        'tribes_count': pal_data.get('tribes_count', '0'),
        'spawners': '',  # 스포너는 별도 처리 필요
        'spawners_count': pal_data.get('spawner_count', '0')
    }
    
    # 작업 적성 포맷팅
    if pal_data.get('work_suitability_types') and pal_data.get('work_suitability_levels'):
        types = pal_data['work_suitability_types'].split('|')
        levels = pal_data['work_suitability_levels'].split('|')
        work_suits = []
        for i, work_type in enumerate(types):
            if i < len(levels):
                work_suits.append(f"{work_type}(LV.{levels[i]})")
        mapped['workSuitabilities'] = " | ".join(work_suits)
    
    return mapped

def main():
    # 기존 CSV의 1, 2번 데이터만 로드
    existing_data = []
    with open('current_4_pals_complete.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] in ['1', '2']:
                existing_data.append(row)
    
    # JSON 데이터 로드
    with open('pal_3_to_10_data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # 3-10번 팰 데이터 변환
    new_data = []
    for pal_id, pal_info in json_data.items():
        # 간단한 매핑
        pal_data = {
            'id': pal_id,
            'name_kor': pal_info['name'],
            'elements': '',
            'partner_skill_name': '',
            'work_suitability_types': '',
            'work_suitability_levels': '',
            'work_suitability_count': '0'
        }
        
        raw_text = pal_info['raw_text']
        
        # 속성 추출
        if "무속성" in raw_text:
            pal_data['elements'] = "무속성"
        elif "풀 속성" in raw_text:
            pal_data['elements'] = "풀 속성"
        elif "화염 속성" in raw_text:
            pal_data['elements'] = "화염 속성"
        elif "물 속성" in raw_text and "얼음 속성" in raw_text:
            pal_data['elements'] = "물 속성|얼음 속성"
        elif "물 속성" in raw_text:
            pal_data['elements'] = "물 속성"
        elif "번개 속성" in raw_text:
            pal_data['elements'] = "번개 속성"
        
        # 파트너 스킬 추출
        import re
        skill_match = re.search(r'파트너 스킬 ([^\s]+) Lv\.1', raw_text)
        if skill_match:
            pal_data['partner_skill_name'] = skill_match.group(1)
        
        # 작업 적성 추출
        work_types = []
        work_levels = []
        work_patterns = [
            (r'채집 Lv(\d+)', '채집'),
            (r'목장 Lv(\d+)', '목장'),
            (r'파종 Lv(\d+)', '파종'),
            (r'수작업 Lv(\d+)', '수작업'),
            (r'벌목 Lv(\d+)', '벌목'),
            (r'제약 Lv(\d+)', '제약'),
            (r'불 피우기 Lv(\d+)', '불 피우기'),
            (r'관개 Lv(\d+)', '관개'),
            (r'운반 Lv(\d+)', '운반'),
            (r'발전 Lv(\d+)', '발전'),
            (r'냉각 Lv(\d+)', '냉각')
        ]
        
        for pattern, work_type in work_patterns:
            matches = re.findall(pattern, raw_text)
            for level in matches:
                work_types.append(work_type)
                work_levels.append(level)
        
        if work_types:
            pal_data['work_suitability_types'] = "|".join(work_types)
            pal_data['work_suitability_levels'] = "|".join(work_levels)
            pal_data['work_suitability_count'] = str(len(work_types))
        
        mapped_pal = map_to_existing_columns(pal_data)
        new_data.append(mapped_pal)
    
    # 모든 데이터 통합
    all_data = existing_data + new_data
    all_data.sort(key=lambda x: int(x['id']))
    
    # 새로운 CSV 저장
    if existing_data:
        columns = list(existing_data[0].keys())
    else:
        return
    
    with open('pal_1_to_10_final.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        
        for pal in all_data:
            complete_pal = {}
            for col in columns:
                complete_pal[col] = pal.get(col, '')
            writer.writerow(complete_pal)
    
    print(f"✅ 완성된 CSV 저장: pal_1_to_10_final.csv")
    print(f"📊 총 {len(all_data)}개 팰 포함")
    
    for pal in all_data:
        print(f"  {pal['id']}번: {pal['name_kor']} ({pal['elements']})")

if __name__ == "__main__":
    main() 