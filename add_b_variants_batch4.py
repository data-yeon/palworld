#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
팰월드 B variants 데이터 추가 스크립트 - Batch 4
8개의 새로운 B variants를 기존 CSV에 추가합니다.
"""

import csv
import re
from typing import List, Dict, Any

def parse_active_skills(skills_text: str) -> List[Dict[str, Any]]:
    """Active Skills 텍스트를 파싱하여 구조화된 데이터로 변환"""
    skills = []
    
    # 스킬별로 분리 (Lv. 패턴으로 시작하는 부분)
    skill_blocks = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?(?=Lv\.\s*\d+|$)', skills_text, re.DOTALL)
    
    for level, skill_name in skill_blocks:
        # 속성과 쿨타임, 위력 찾기
        skill_block_text = skills_text[skills_text.find(f'Lv. {level} [{skill_name}]'):
                                     skills_text.find(f'Lv. {int(level)+1}', skills_text.find(f'Lv. {level}') + 1)
                                     if f'Lv. {int(level)+1}' in skills_text[skills_text.find(f'Lv. {level}') + 1:]
                                     else len(skills_text)]
        
        # 속성 찾기
        element_match = re.search(r'(무속성|화염 속성|물 속성|번개 속성|얼음 속성|풀 속성|땅 속성|어둠 속성)', skill_block_text)
        element = element_match.group(1) if element_match else "무속성"
        
        # 쿨타임 찾기
        cooltime_match = re.search(r'쿨타임\.webp\):\s*(\d+)', skill_block_text)
        cooltime = int(cooltime_match.group(1)) if cooltime_match else 0
        
        # 위력 찾기
        power_match = re.search(r'위력:\s*(\d+)', skill_block_text)
        power = int(power_match.group(1)) if power_match else 0
        
        skills.append({
            'level': int(level),
            'name': skill_name,
            'element': element,
            'cooltime': cooltime,
            'power': power
        })
    
    return skills

def parse_work_suitability(work_text: str) -> List[str]:
    """작업 적성 텍스트를 파싱하여 영어 작업명 리스트로 변환"""
    work_mapping = {
        '관개': 'Watering',
        '채집': 'Gathering', 
        '운반': 'Transporting',
        '냉각': 'Cooling',
        '목장': 'Farming',
        '파종': 'Planting',
        '수작업': 'Handiwork',
        '발전': 'Generating_Electricity',
        '벌목': 'Lumbering',
        '불 피우기': 'Kindling',
        '채굴': 'Mining'
    }
    
    work_list = []
    for korean, english in work_mapping.items():
        if korean in work_text:
            # 레벨 찾기
            level_pattern = f'{korean}.*?Lv(\d+)'
            level_match = re.search(level_pattern, work_text)
            level = level_match.group(1) if level_match else '1'
            work_list.append(f"{english} Lv{level}")
    
    return work_list

def add_batch4_variants():
    """Batch 4: 8개의 B variants 추가"""
    
    # 새로운 B variants 데이터
    new_variants = [
        {
            'id': '23B',
            'name': '드리문',
            'english_name': 'Killamari_Primo',
            'element': '무속성+물속성',
            'rarity': 2,
            'size': 'XS',
            'hp': 70,
            'food_amount': 3,
            'melee_attack': 100,
            'shot_attack': 60,
            'defense': 70,
            'work_speed': 100,
            'partner_skill': '꿈튀김',
            'partner_skill_desc': '보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 느린 속도로 장시간 이동이 가능해진다.',
            'work_suitability': 'Watering Lv1, Gathering Lv1, Transporting Lv2',
            'active_skills': [
                {'level': 1, 'name': '공기 대포', 'element': '무속성', 'cooltime': 2, 'power': 25},
                {'level': 7, 'name': '파워 샷', 'element': '무속성', 'cooltime': 4, 'power': 35},
                {'level': 15, 'name': '버블 샷', 'element': '물 속성', 'cooltime': 13, 'power': 65},
                {'level': 22, 'name': '파워 폭탄', 'element': '무속성', 'cooltime': 15, 'power': 70},
                {'level': 30, 'name': '산성비', 'element': '물 속성', 'cooltime': 18, 'power': 80},
                {'level': 40, 'name': '고압수 발사', 'element': '물 속성', 'cooltime': 35, 'power': 110},
                {'level': 50, 'name': '하이드로 스트림', 'element': '물 속성', 'cooltime': 55, 'power': 150}
            ]
        },
        {
            'id': '24B',
            'name': '칠테트',
            'english_name': 'Mau_Cryst',
            'element': '얼음속성',
            'rarity': 2,
            'size': 'XS',
            'hp': 70,
            'food_amount': 1,
            'melee_attack': 70,
            'shot_attack': 65,
            'defense': 70,
            'work_speed': 100,
            'partner_skill': '금화 수집',
            'partner_skill_desc': '가축 목장에 배치하면 지면에서 금화을 파내기도 한다.',
            'work_suitability': 'Cooling Lv1, Farming Lv1',
            'active_skills': [
                {'level': 1, 'name': '얼음 미사일', 'element': '얼음 속성', 'cooltime': 3, 'power': 30},
                {'level': 7, 'name': '공기 대포', 'element': '무속성', 'cooltime': 2, 'power': 25},
                {'level': 15, 'name': '모래 돌풍', 'element': '땅 속성', 'cooltime': 4, 'power': 40},
                {'level': 22, 'name': '얼음 칼날', 'element': '얼음 속성', 'cooltime': 10, 'power': 55},
                {'level': 30, 'name': '빙산', 'element': '얼음 속성', 'cooltime': 15, 'power': 70},
                {'level': 40, 'name': '서리 낀 입김', 'element': '얼음 속성', 'cooltime': 22, 'power': 90},
                {'level': 50, 'name': '눈보라 스파이크', 'element': '얼음 속성', 'cooltime': 45, 'power': 130}
            ]
        },
        {
            'id': '25B',
            'name': '일레카이트',
            'english_name': 'Celaray_Lux',
            'element': '물속성+번개속성',
            'rarity': 4,
            'size': 'M',
            'hp': 80,
            'food_amount': 3,
            'melee_attack': 100,
            'shot_attack': 75,
            'defense': 80,
            'work_speed': 100,
            'partner_skill': '짜릿바람 글라이더',
            'partner_skill_desc': '보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 빠른 속도로 장시간 이동이 가능해진다.',
            'work_suitability': 'Watering Lv1, Generating_Electricity Lv1, Transporting Lv1',
            'active_skills': [
                {'level': 1, 'name': '번개 창', 'element': '번개 속성', 'cooltime': 2, 'power': 30},
                {'level': 7, 'name': '전기 파장', 'element': '번개 속성', 'cooltime': 4, 'power': 40},
                {'level': 15, 'name': '버블 샷', 'element': '물 속성', 'cooltime': 13, 'power': 65},
                {'level': 22, 'name': '라인 썬더', 'element': '번개 속성', 'cooltime': 16, 'power': 75},
                {'level': 30, 'name': '라인 스플래시', 'element': '물 속성', 'cooltime': 22, 'power': 90},
                {'level': 40, 'name': '고압수 발사', 'element': '물 속성', 'cooltime': 35, 'power': 110},
                {'level': 50, 'name': '전기 볼트', 'element': '번개 속성', 'cooltime': 55, 'power': 150}
            ]
        },
        {
            'id': '35B',
            'name': '베노고트',
            'english_name': 'Caprity_Noct',
            'element': '어둠속성',
            'rarity': 3,
            'size': 'S',
            'hp': 100,
            'food_amount': 4,
            'melee_attack': 70,
            'shot_attack': 75,
            'defense': 90,
            'work_speed': 100,
            'partner_skill': '독샘 채집',
            'partner_skill_desc': '가축 목장에 배치하면 등에서 독샘을 떨어뜨리기도 한다.',
            'work_suitability': 'Planting Lv2, Farming Lv1',
            'active_skills': [
                {'level': 1, 'name': '독 안개', 'element': '어둠 속성', 'cooltime': 30, 'power': 0},
                {'level': 7, 'name': '바람의 칼날', 'element': '풀 속성', 'cooltime': 2, 'power': 30},
                {'level': 15, 'name': '독 사격', 'element': '어둠 속성', 'cooltime': 2, 'power': 30},
                {'level': 22, 'name': '멀티 커터', 'element': '풀 속성', 'cooltime': 12, 'power': 60},
                {'level': 30, 'name': '포이즌 샤워', 'element': '어둠 속성', 'cooltime': 22, 'power': 90},
                {'level': 40, 'name': '원형 덩굴', 'element': '풀 속성', 'cooltime': 40, 'power': 120},
                {'level': 50, 'name': '어둠의 레이저', 'element': '어둠 속성', 'cooltime': 55, 'power': 150}
            ]
        },
        {
            'id': '37B',
            'name': '산령사슴',
            'english_name': 'Eikthyrdeer_Terra',
            'element': '땅속성',
            'rarity': 6,
            'size': 'L',
            'hp': 95,
            'food_amount': 5,
            'melee_attack': 70,
            'shot_attack': 80,
            'defense': 80,
            'work_speed': 100,
            'partner_skill': '금빛 숲의 수호자',
            'partner_skill_desc': '등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해지며 나무 파괴 효율이 향상된다.',
            'work_suitability': 'Lumbering Lv2',
            'active_skills': [
                {'level': 1, 'name': '파워 샷', 'element': '무속성', 'cooltime': 4, 'power': 35},
                {'level': 7, 'name': '들이받기', 'element': '무속성', 'cooltime': 5, 'power': 50},
                {'level': 15, 'name': '바위 폭발', 'element': '땅 속성', 'cooltime': 10, 'power': 55},
                {'level': 22, 'name': '바위 대포', 'element': '땅 속성', 'cooltime': 15, 'power': 70},
                {'level': 30, 'name': '파워 폭탄', 'element': '무속성', 'cooltime': 15, 'power': 70},
                {'level': 40, 'name': '모래 폭풍', 'element': '땅 속성', 'cooltime': 18, 'power': 80},
                {'level': 50, 'name': '바위 창', 'element': '땅 속성', 'cooltime': 55, 'power': 150}
            ]
        },
        {
            'id': '39B',
            'name': '그래토',
            'english_name': 'Ribbuny_Botan',
            'element': '풀속성',
            'rarity': 1,
            'size': 'XS',
            'hp': 80,
            'food_amount': 2,
            'melee_attack': 100,
            'shot_attack': 65,
            'defense': 70,
            'work_speed': 100,
            'partner_skill': '풀뜨기 장인',
            'partner_skill_desc': '보유하고 있는 동안 풀 속성 팰의 공격력이 증가한다. 그래토가 무기 제작대나 무기 공장 등에서 일할 때 작업 효율이 향상된다.',
            'work_suitability': 'Planting Lv1, Handiwork Lv1, Gathering Lv1, Transporting Lv1',
            'active_skills': [
                {'level': 1, 'name': '바람의 칼날', 'element': '풀 속성', 'cooltime': 2, 'power': 30},
                {'level': 7, 'name': '모래 돌풍', 'element': '땅 속성', 'cooltime': 4, 'power': 40},
                {'level': 15, 'name': '씨앗 기관총', 'element': '풀 속성', 'cooltime': 9, 'power': 50},
                {'level': 22, 'name': '씨앗 지뢰', 'element': '풀 속성', 'cooltime': 13, 'power': 65},
                {'level': 30, 'name': '윈드 에지', 'element': '풀 속성', 'cooltime': 22, 'power': 90},
                {'level': 40, 'name': '원형 덩굴', 'element': '풀 속성', 'cooltime': 40, 'power': 120},
                {'level': 50, 'name': '태양 폭발', 'element': '풀 속성', 'cooltime': 55, 'power': 150}
            ]
        },
        {
            'id': '40B',
            'name': '아비스고트',
            'english_name': 'Incineram_Noct',
            'element': '어둠속성',
            'rarity': 5,
            'size': 'M',
            'hp': 95,
            'food_amount': 4,
            'melee_attack': 150,
            'shot_attack': 105,
            'defense': 85,
            'work_speed': 100,
            'partner_skill': '암흑 발톱의 사냥꾼',
            'partner_skill_desc': '발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기로 공격한다.',
            'work_suitability': 'Handiwork Lv2, Mining Lv1, Transporting Lv2',
            'active_skills': [
                {'level': 1, 'name': '파이어 샷', 'element': '화염 속성', 'cooltime': 2, 'power': 30},
                {'level': 7, 'name': '스피릿 파이어', 'element': '화염 속성', 'cooltime': 7, 'power': 45},
                {'level': 15, 'name': '불화살', 'element': '화염 속성', 'cooltime': 10, 'power': 55},
                {'level': 22, 'name': '지옥불 할퀴기', 'element': '화염 속성', 'cooltime': 10, 'power': 70},
                {'level': 30, 'name': '그림자 폭발', 'element': '어둠 속성', 'cooltime': 10, 'power': 55},
                {'level': 40, 'name': '화염구', 'element': '화염 속성', 'cooltime': 55, 'power': 150},
                {'level': 50, 'name': '인페르노', 'element': '화염 속성', 'cooltime': 40, 'power': 120}
            ]
        },
        {
            'id': '45B',
            'name': '칠리자드',
            'english_name': 'Leezpunk_Ignis',
            'element': '화염속성',
            'rarity': 3,
            'size': 'S',
            'hp': 80,
            'food_amount': 3,
            'melee_attack': 90,
            'shot_attack': 80,
            'defense': 50,
            'work_speed': 100,
            'partner_skill': '제6감',
            'partner_skill_desc': '발동하면 6번째 감각을 활용해 가까이 있는 던전의 위치를 탐지할 수 있다.',
            'work_suitability': 'Kindling Lv1, Handiwork Lv1, Gathering Lv1, Transporting Lv1',
            'active_skills': [
                {'level': 1, 'name': '파이어 샷', 'element': '화염 속성', 'cooltime': 2, 'power': 30},
                {'level': 7, 'name': '독 사격', 'element': '어둠 속성', 'cooltime': 2, 'power': 30},
                {'level': 15, 'name': '스피릿 파이어', 'element': '화염 속성', 'cooltime': 7, 'power': 45},
                {'level': 22, 'name': '파이어 브레스', 'element': '화염 속성', 'cooltime': 15, 'power': 70},
                {'level': 30, 'name': '화염 폭풍', 'element': '화염 속성', 'cooltime': 18, 'power': 80},
                {'level': 40, 'name': '인페르노', 'element': '화염 속성', 'cooltime': 40, 'power': 120},
                {'level': 50, 'name': '화염구', 'element': '화염 속성', 'cooltime': 55, 'power': 150}
            ]
        }
    ]
    
    # 기존 CSV 파일 읽기
    input_file = 'enhanced_complete_pals_batch3.csv'
    output_file = 'enhanced_complete_pals_batch4.csv'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            existing_data = list(reader)
            fieldnames = reader.fieldnames
    except FileNotFoundError:
        print(f"Error: {input_file} 파일을 찾을 수 없습니다.")
        return
    
    # 새로운 데이터를 기존 형식에 맞게 변환
    for variant in new_variants:
        # Active Skills를 JSON 형태로 변환
        active_skills_json = str(variant['active_skills']).replace("'", '"')
        
        new_row = {
            'id': variant['id'],
            'name': variant['name'],
            'english_name': variant['english_name'],
            'element': variant['element'],
            'rarity': variant['rarity'],
            'size': variant['size'],
            'hp': variant['hp'],
            'food_amount': variant['food_amount'],
            'melee_attack': variant['melee_attack'],
            'shot_attack': variant['shot_attack'],
            'defense': variant['defense'],
            'work_speed': variant['work_speed'],
            'partner_skill': variant['partner_skill'],
            'partner_skill_desc': variant['partner_skill_desc'],
            'work_suitability': variant['work_suitability'],
            'active_skills': active_skills_json,
            'active_skills_count': len(variant['active_skills']),
            'max_skill_power': max([skill['power'] for skill in variant['active_skills']]),
            'min_skill_cooltime': min([skill['cooltime'] for skill in variant['active_skills'] if skill['cooltime'] > 0]),
            'batch': 'Batch4'
        }
        
        existing_data.append(new_row)
    
    # 결과를 새 CSV 파일로 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames or [])
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"✅ Batch 4 완료!")
    print(f"   📊 추가된 B variants: 8개")
    print(f"   📁 출력 파일: {output_file}")
    print(f"   📈 총 팰 수: {len(existing_data)}개")
    
    # 배치별 통계
    batch_stats = {}
    for row in existing_data:
        batch = row.get('batch', 'Original')
        batch_stats[batch] = batch_stats.get(batch, 0) + 1
    
    print(f"\n📈 배치별 통계:")
    for batch, count in sorted(batch_stats.items()):
        print(f"   {batch}: {count}개")
    
    # B variants 통계
    b_variants = [row for row in existing_data if row['id'].endswith('B')]
    print(f"\n🎯 B variants 현황:")
    print(f"   총 B variants: {len(b_variants)}개")
    print(f"   완성도: {len(b_variants)}/59 = {len(b_variants)/59*100:.1f}%")
    
    return len(existing_data)

if __name__ == "__main__":
    print("🚀 팰월드 B variants Batch 4 추가 시작...")
    total_pals = add_batch4_variants()
    print(f"\n🎉 작업 완료! 현재 총 {total_pals}개의 팰 데이터가 있습니다.") 