#!/usr/bin/env python3

import csv
import re
from pathlib import Path

def clean_text(text):
    """텍스트 정리"""
    if not text:
        return ""
    # 여러 공백을 하나로
    text = re.sub(r'\s+', ' ', text)
    # 앞뒤 공백 제거
    text = text.strip()
    return text

def parse_work_suitability(text):
    """작업 적성 파싱"""
    work_dict = {
        'kindling': 0, 'watering': 0, 'planting': 0, 'generating_electricity': 0,
        'handiwork': 0, 'gathering': 0, 'lumbering': 0, 'mining': 0,
        'medicine': 0, 'cooling': 0, 'transporting': 0, 'farming': 0
    }
    
    # 작업 적성 매핑
    work_mapping = {
        '불 피우기': 'kindling',
        '관개': 'watering', 
        '파종': 'planting',
        '발전': 'generating_electricity',
        '수작업': 'handiwork',
        '채집': 'gathering',
        '벌목': 'lumbering',
        '채굴': 'mining',
        '제약': 'medicine',
        '냉각': 'cooling',
        '운반': 'transporting',
        '목장': 'farming'
    }
    
    for korean_name, english_name in work_mapping.items():
        if korean_name in text:
            # 레벨 추출
            pattern = rf'{korean_name}.*?Lv(\d+)'
            match = re.search(pattern, text)
            if match:
                work_dict[english_name] = int(match.group(1))
    
    return work_dict

def extract_drops(text):
    """드롭 아이템 추출"""
    drops = []
    
    # 드롭 패턴들
    drop_patterns = [
        (r'가죽.*?(\d+)', 'Leather'),
        (r'빙결 기관.*?(\d+)', 'Ice Organ'),
        (r'발화 기관.*?(\d+)', 'Flame Organ'),
        (r'발전 기관.*?(\d+)', 'Electric Organ'),
        (r'뿔.*?(\d+)', 'Horn'),
        (r'얼음사슴의 사슴고기.*?(\d+)', 'Reindrix Venison')
    ]
    
    for pattern, item_name in drop_patterns:
        match = re.search(pattern, text)
        if match:
            quantity = match.group(1)
            drops.append(f"{item_name} x{quantity}")
    
    return ', '.join(drops) if drops else ""

def create_pal_data():
    """57-60번 팰 데이터 생성"""
    
    # 57번 빙호 (Foxcicle)
    foxcicle = {
        'id': 57,
        'name': '빙호',
        'element1': 'Ice',
        'element2': '',
        'hp': 90,
        'attack': 95,
        'defense': 105,
        'rarity': 5,
        'partner_skill': '오로라의 인도',
        'partner_skill_desc': '보유하고 있는 동안 얼음 속성 팰의 공격력이 증가한다.',
        'kindling': 0, 'watering': 0, 'planting': 0, 'generating_electricity': 0,
        'handiwork': 0, 'gathering': 0, 'lumbering': 0, 'mining': 0,
        'medicine': 0, 'cooling': 2, 'transporting': 0, 'farming': 0,
        'food_amount': 3,
        'description': '오로라가 보이는 밤이면 하늘을 올려다보며 아름다운 목소리로 노래를 시작한다. 다만 그 탓에 적에게 자주 공격당한다.',
        'active_skills': '공기 대포, 얼음 미사일, 얼음 칼날, 유령의 불꽃, 빙산, 서리 낀 입김, 눈보라 스파이크',
        'drops': 'Leather x1, Ice Organ x2-3',
        'size': 'S',
        'walking_speed': 130,
        'running_speed': 600,
        'riding_speed': 0,
        'hp_lv60_min': 3750,
        'hp_lv60_max': 4627,
        'attack_lv60_min': 563,
        'attack_lv60_max': 702,
        'defense_lv60_min': 561,
        'defense_lv60_max': 715,
        'craft_speed': 100,
        'combi_rank': 760,
        'spawn_locations': 'Northern ice regions, Frozen areas',
        'nickname': 'Ice Fox'
    }
    
    # 58번 파이린 (Pyrin)
    pyrin = {
        'id': 58,
        'name': '파이린',
        'element1': 'Fire',
        'element2': '',
        'hp': 100,
        'attack': 95,
        'defense': 90,
        'rarity': 6,
        'partner_skill': '적토마',
        'partner_skill_desc': '등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 화염 속성으로 변화한다.',
        'kindling': 2, 'watering': 0, 'planting': 0, 'generating_electricity': 0,
        'handiwork': 0, 'gathering': 0, 'lumbering': 1, 'mining': 0,
        'medicine': 0, 'cooling': 0, 'transporting': 0, 'farming': 0,
        'food_amount': 5,
        'description': '전신이 고효율의 방열 기관이 되어 경이적인 지구력을 발휘한다. 누가 올라타면 화상을 입지 않도록 배려해준다.',
        'active_skills': '모래 돌풍, 파이어 샷, 스피릿 파이어, 불화살, 화염 돌격, 인페르노, 화염구',
        'drops': 'Flame Organ x4-5, Leather x2-3',
        'size': 'L',
        'walking_speed': 150,
        'running_speed': 850,
        'riding_speed': 1300,
        'hp_lv60_min': 4075,
        'hp_lv60_max': 5050,
        'attack_lv60_min': 563,
        'attack_lv60_max': 702,
        'defense_lv60_min': 488,
        'defense_lv60_max': 620,
        'craft_speed': 100,
        'combi_rank': 360,
        'spawn_locations': 'Volcanic regions, Desert areas',
        'nickname': 'Flame Steed'
    }
    
    # 59번 얼음사슴 (Reindrix)
    reindrix = {
        'id': 59,
        'name': '얼음사슴',
        'element1': 'Ice',
        'element2': '',
        'hp': 100,
        'attack': 85,
        'defense': 110,
        'rarity': 4,
        'partner_skill': '써늘한 육체',
        'partner_skill_desc': '등에 타고 이동할 수 있다. 탑승 중에는 시원하여 더위를 느끼지 않게 된다.',
        'kindling': 0, 'watering': 0, 'planting': 0, 'generating_electricity': 0,
        'handiwork': 0, 'gathering': 0, 'lumbering': 2, 'mining': 0,
        'medicine': 0, 'cooling': 2, 'transporting': 0, 'farming': 0,
        'food_amount': 7,
        'description': '속이 비치는 투명한 뿔은 절대 영도에서 반짝인다. 맨손으로 만지면 전신이 얼어붙어 목숨마저 가루처럼 부서져 날아간다.',
        'active_skills': '공기 대포, 얼음 미사일, 얼음 칼날, 얼음뿔 돌진, 빙산, 서리 낀 입김, 눈보라 스파이크',
        'drops': 'Reindrix Venison x2, Leather x1, Horn x2, Ice Organ x2-3',
        'size': 'M',
        'walking_speed': 70,
        'running_speed': 700,
        'riding_speed': 1070,
        'hp_lv60_min': 4075,
        'hp_lv60_max': 5050,
        'attack_lv60_min': 514,
        'attack_lv60_max': 638,
        'defense_lv60_min': 586,
        'defense_lv60_max': 747,
        'craft_speed': 100,
        'combi_rank': 880,
        'spawn_locations': 'Snow forests, Frozen mountains',
        'nickname': 'Ice Deer'
    }
    
    # 60번 썬도그 (Rayhound)
    rayhound = {
        'id': 60,
        'name': '썬도그',
        'element1': 'Electric',
        'element2': '',
        'hp': 90,
        'attack': 100,
        'defense': 80,
        'rarity': 5,
        'partner_skill': '도약력',
        'partner_skill_desc': '등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해진다.',
        'kindling': 0, 'watering': 0, 'planting': 0, 'generating_electricity': 2,
        'handiwork': 0, 'gathering': 0, 'lumbering': 0, 'mining': 0,
        'medicine': 0, 'cooling': 0, 'transporting': 0, 'farming': 0,
        'food_amount': 5,
        'description': '전속력으로 뛰면 그야말로 번개나 다름없다. 썬도그 끼리 충돌하면 천둥 같은 굉음이 울려 퍼진다.',
        'active_skills': '모래 돌풍, 전기 파장, 스파크 샷, 바위 폭발, 천둥 소환, 번개 구체, 라인 썬더, 전기 볼트',
        'drops': 'Electric Organ x1-2',
        'size': 'M',
        'walking_speed': 210,
        'running_speed': 700,
        'riding_speed': 1150,
        'hp_lv60_min': 3750,
        'hp_lv60_max': 4627,
        'attack_lv60_min': 587,
        'attack_lv60_max': 733,
        'defense_lv60_min': 440,
        'defense_lv60_max': 557,
        'craft_speed': 100,
        'combi_rank': 740,
        'spawn_locations': 'Desert regions, Plains',
        'nickname': 'Thunder Dog'
    }
    
    return [foxcicle, pyrin, reindrix, rayhound]

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_56_pals.csv'
    output_file = 'complete_1_to_60_pals.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    # 새로운 팰 데이터
    new_pals = create_pal_data()
    
    # CSV 읽기 및 쓰기
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        existing_data = list(reader)
        headers = reader.fieldnames
    
    # 새 데이터 추가
    all_data = existing_data + new_pals
    
    # CSV 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_data)
    
    print(f"✅ 성공적으로 {len(new_pals)}개 팰을 추가했습니다!")
    print(f"📊 총 팰 수: {len(all_data)}개")
    print(f"💾 파일 저장: {output_file}")
    
    # 추가된 팰들 출력
    print("\n📋 추가된 팰들:")
    for pal in new_pals:
        print(f"  {pal['id']}번 {pal['name']} ({pal['element1']} 속성)")

if __name__ == "__main__":
    main() 