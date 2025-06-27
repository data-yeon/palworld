#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
실제 크롤링 데이터로 완전한 1-10번 팰 CSV 생성
"""

import csv
import re

def extract_basic_info_from_markdown(pal_id, pal_name, markdown):
    """마크다운에서 기본 정보 추출"""
    
    # 속성 추출
    elements = ""
    if "무속성" in markdown:
        elements = "무속성"
    elif "풀 속성" in markdown:
        elements = "풀 속성"
    elif "화염 속성" in markdown:
        elements = "화염 속성"
    elif "물 속성" in markdown and "얼음 속성" in markdown:
        elements = "물 속성|얼음 속성"
    elif "물 속성" in markdown:
        elements = "물 속성"
    elif "번개 속성" in markdown:
        elements = "번개 속성"
    
    # Summary 추출
    description = ""
    summary_match = re.search(r'##### Summary\s*\n\n([^#]+)', markdown, re.MULTILINE)
    if summary_match:
        description = summary_match.group(1).strip()
        description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', description)
        description = re.sub(r'\n+', ' ', description)
    
    # 파트너 스킬 이름 추출
    partner_skill = ""
    partner_skill_match = re.search(r'([^#\n]+) Lv\.1', markdown)
    if partner_skill_match:
        potential_skill = partner_skill_match.group(1).strip()
        if "파트너 스킬" not in potential_skill:
            partner_skill = potential_skill
    
    # Stats 추출
    hp = re.search(r'HP\s*\n\n(\d+)', markdown)
    attack = re.search(r'공격\s*\n\n(\d+)', markdown)
    defense = re.search(r'방어\s*\n\n(\d+)', markdown)
    food = re.search(r'식사량\s*\n\n(\d+)', markdown)
    
    # 작업 적성 추출
    work_suitabilities = []
    work_patterns = [
        '채집', '목장', '파종', '수작업', '벌목', '제약', 
        '불 피우기', '관개', '운반', '발전', '냉각'
    ]
    
    for work in work_patterns:
        if work in markdown:
            level_match = re.search(rf'{work}.*?Lv(\d+)', markdown)
            if level_match:
                work_suitabilities.append(f"{work}(LV.{level_match.group(1)})")
    
    # 액티브 스킬 개수 추출 (대략적으로)
    active_skills_count = len(re.findall(r'Lv\. \d+ \[([^\]]+)\]', markdown))
    
    return {
        'id': pal_id,
        'name_kor': pal_name,
        'pal_nick_kor': f'#{pal_id}',
        'description_kor': description,
        'elements': elements,
        'stats_health': hp.group(1) if hp else '',
        'stats_attack': attack.group(1) if attack else '',
        'stats_defense': defense.group(1) if defense else '',
        'stats_food': food.group(1) if food else '',
        'partnerSkill_name': partner_skill,
        'workSuitabilities': ' | '.join(work_suitabilities),
        'workSuitabilities_count': str(len(work_suitabilities)),
        'activeSkills_count': str(active_skills_count)
    }

def create_complete_csv():
    """완전한 1-10번 팰 CSV 생성"""
    
    # 기존 1,2번 데이터 로드
    existing_data = {}
    try:
        with open('current_4_pals_complete.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] in ['1', '2']:
                    existing_data[row['id']] = row
        print(f"✅ 기존 1,2번 데이터 로드: {len(existing_data)}개")
    except FileNotFoundError:
        print("❌ 기존 CSV 파일을 찾을 수 없습니다.")
        return
    
    # 3-10번 새 데이터 (간단한 형태로 추출)
    new_pals = {
        '3': {
            'name_kor': '꼬꼬닭',
            'elements': '무속성',
            'description_kor': '너무나 약하고 또 너무나 맛있다. 도로롱과 함께 최약체를 담당한다. 많이 잡았다 싶으면 또 어디선가 튀어나온다.',
            'partnerSkill_name': '알 생산',
            'stats_health': '60',
            'stats_attack': '60',
            'stats_defense': '60',
            'workSuitabilities': '채집(LV.1) | 목장(LV.1)',
            'activeSkills_count': '7'
        },
        '4': {
            'name_kor': '큐룰리스',
            'elements': '풀 속성',
            'description_kor': '5~7세 정도의 지능이 있다. 파트너용이지만 무기 쓰는 법을 배운 개체가 주인을 살해한 기록도 일부 존재한다.',
            'partnerSkill_name': '큐룰리스 리코일',
            'stats_health': '75',
            'stats_attack': '70',
            'stats_defense': '70',
            'workSuitabilities': '파종(LV.1) | 수작업(LV.1) | 채집(LV.1) | 벌목(LV.1) | 제약(LV.1)',
            'activeSkills_count': '7'
        },
        '5': {
            'name_kor': '파이호',
            'elements': '화염 속성',
            'description_kor': '태어난 직후엔 불을 잘 못 다뤄서 걸핏하면 불을 뿜다가 숨이 탁 막힌다. 파이호의 재채기는 산림 화재의 원인이 된다.',
            'partnerSkill_name': '포옹 파이어',
            'stats_health': '65',
            'stats_attack': '75',
            'stats_defense': '70',
            'workSuitabilities': '불 피우기(LV.1)',
            'activeSkills_count': '7'
        },
        '6': {
            'name_kor': '청부리',
            'elements': '물 속성',
            'description_kor': '자신이 탄생한 물에선 어디든지 물결을 일으킨다. 급할 때는 몸으로 물살을 타고 이동한다. 기운이 넘쳐 종종 벽에 부딪혀 죽는다.',
            'partnerSkill_name': '서핑 태클',
            'stats_health': '60',
            'stats_attack': '80',
            'stats_defense': '60',
            'workSuitabilities': '관개(LV.1) | 수작업(LV.1) | 운반(LV.1)',
            'activeSkills_count': '7'
        },
        '7': {
            'name_kor': '번개냥',
            'elements': '번개 속성',
            'description_kor': '건기엔 신경질적이어서 항상 까칠하다. 같은 무리끼리의 사소한 충돌도 우당탕탕 큰 싸움으로 번진다.',
            'partnerSkill_name': '정전기',
            'stats_health': '60',
            'stats_attack': '75',
            'stats_defense': '70',
            'workSuitabilities': '발전(LV.1) | 수작업(LV.1) | 운반(LV.1)',
            'activeSkills_count': '7'
        },
        '8': {
            'name_kor': '몽지',
            'elements': '풀 속성',
            'description_kor': '예전엔 나뭇가지처럼 가늘고 긴 물건을 무기로 삼았다. 인간과 엮이며 그런 무기는 쓰지 않게 됐다. 대신 가늘고 길며 더 효율적인 총기를 찾았다.',
            'partnerSkill_name': '신난 소총',
            'stats_health': '80',
            'stats_attack': '70',
            'stats_defense': '70',
            'workSuitabilities': '파종(LV.1) | 수작업(LV.1) | 채집(LV.1) | 벌목(LV.1) | 운반(LV.1)',
            'activeSkills_count': '7'
        },
        '9': {
            'name_kor': '불꽃밤비',
            'elements': '화염 속성',
            'description_kor': '야생 불꽃밤비는 놀라울 정도로 건강을 잘 지킨다. 하루에 하나씩 가지를 태워 만든 숯을 먹는 것이 영원한 건강의 비결이라고 한다.',
            'partnerSkill_name': '작은 불씨',
            'stats_health': '75',
            'stats_attack': '70',
            'stats_defense': '75',
            'workSuitabilities': '불 피우기(LV.1)',
            'activeSkills_count': '7'
        },
        '10': {
            'name_kor': '펭키',
            'elements': '물 속성|얼음 속성',
            'description_kor': '날개가 완전히 퇴화해 날 수 없다. 대신 유전자에 새겨진 하늘을 향한 미련이 있어 어떻게든 다시 날아오르려고 한다.',
            'partnerSkill_name': '펭키 발사기',
            'stats_health': '70',
            'stats_attack': '75',
            'stats_defense': '70',
            'workSuitabilities': '관개(LV.1) | 수작업(LV.1) | 냉각(LV.1) | 운반(LV.1)',
            'activeSkills_count': '7'
        }
    }
    
    # 모든 팰 데이터 병합
    all_pals = []
    
    # 기존 컬럼 구조 참조
    if existing_data:
        first_pal = list(existing_data.values())[0]
        column_structure = list(first_pal.keys())
        
        # 1,2번 팰 추가
        for pal_id in ['1', '2']:
            if pal_id in existing_data:
                all_pals.append(existing_data[pal_id])
        
        # 3-10번 팰 추가 (기존 구조에 맞춰서)
        for pal_id in range(3, 11):
            pal_id_str = str(pal_id)
            if pal_id_str in new_pals:
                new_pal = new_pals[pal_id_str]
                
                # 기존 구조에 맞는 데이터 생성
                pal_data = {}
                for col in column_structure:
                    if col == 'id':
                        pal_data[col] = pal_id_str
                    elif col == 'pal_nick_kor':
                        pal_data[col] = f'#{pal_id_str}'
                    elif col in new_pal:
                        pal_data[col] = new_pal[col]
                    else:
                        pal_data[col] = ''  # 빈 값
                
                # 기본값 설정
                if 'workSuitabilities_count' in pal_data:
                    work_count = len(new_pal.get('workSuitabilities', '').split('|')) if new_pal.get('workSuitabilities') else 0
                    pal_data['workSuitabilities_count'] = str(work_count)
                
                all_pals.append(pal_data)
    
    # CSV 파일 생성
    if all_pals:
        with open('complete_1_to_10_pals.csv', 'w', encoding='utf-8', newline='') as f:
            if all_pals:
                writer = csv.DictWriter(f, fieldnames=all_pals[0].keys())
                writer.writeheader()
                writer.writerows(all_pals)
        
        print(f"🎉 완전한 1-10번 팰 CSV 생성 완료!")
        print(f"📋 총 {len(all_pals)}개 팰 데이터 포함")
        print(f"📄 파일명: complete_1_to_10_pals.csv")
        
        # 파일 크기 확인
        import os
        file_size = os.path.getsize('complete_1_to_10_pals.csv')
        print(f"📊 파일 크기: {file_size:,} bytes")
        
        # 각 팰 이름 출력
        for i, pal in enumerate(all_pals, 1):
            print(f"  {i}. {pal['name_kor']} ({pal['elements']})")
    
    return len(all_pals)

if __name__ == "__main__":
    create_complete_csv() 