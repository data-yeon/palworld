#!/usr/bin/env python3
"""
71B 시로카바네 (Vanwyrm_Cryst) 데이터 파싱 및 CSV 추가
"""

import csv
import os

def parse_71b_sirokabane():
    """
    71B 시로카바네 데이터 생성
    """
    pal_data = {
        'ID': '71B',
        'Name': '시로카바네',
        'Description': '시로카바네의 외골격으로 만든 피리 소리는 천 개의 봉우리를 건넌다고 한다. 고대의 전쟁에선 승리의 나팔로 사용했다.',
        'Type1': '얼음',
        'Type2': '어둠',
        'PartnerSkill': '하늘에서 온 습격자',
        'PartnerSkillDesc': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어가 적의 약점 부위를 공격할 때 주는 피해량이 증가한다.',
        'HP': '90',
        'ATK': '120',
        'DEF': '95',
        'WorkSpeed': '100',
        'Rarity': '5',
        'Size': 'L',
        'FoodAmount': '6',
        'Work1': '냉각 Lv2',
        'Work2': '운반 Lv3',
        'Work3': '',
        'DropItem1': '뼈',
        'DropItem2': '빙결 기관',
        'ActiveSkills': '공기 대포, 얼음 미사일, 얼음 칼날, 서리 낀 입김, 플라잉 블리자드, 악몽의 구체, 눈보라 스파이크, 어둠의 레이저',
        'EnglishName': 'Vanwyrm_Cryst',
        # CSV 나머지 필드들을 빈 값으로 설정
        'Element1': '얼음',
        'Element2': '어둠',
        'PassiveSkill': '',
        'Element1Color': '',
        'Element2Color': '',
        'ATKRange': '',
        'DEFRange': '',
        'HPRange': '',
        'Weaknesses': '',
        'Strengths': '',
        'ImmuneToStatusEffects': '',
        'CaptureRate': '',
        'Experience': '',
        'ZukanNumber': '71',
        'ZukanNumberSuffix': 'B',
        'MinLevel': '',
        'MaxLevel': '',
        'SpawnAreas': '',
        'SpawnTimes': '',
        'BreedingFormula': '',
        'EggType': '얼어붙은 대형 알',
        'IncubationTime': '',
        'BuddySkillCooldown': '',
        'BuddySkillDamage': '',
        'BuddySkillDescription': '',
        'UniqueCombination': 'Vanwyrm + Foxcicle = Vanwyrm_Cryst',
        'Price': '4610',
        'CombiRank': '620',
        'Code': 'BirdDragon_Ice',
        'MoveSpeed': '',
        'RunSpeed': '700',
        'RideSpeed': '850',
        'TransportSpeed': '475',
        'AerialSpeed': '',
        'SwimSpeed': '700',
        'NightVision': '1',
        'Predator': '1',
        'Nocturnal': '1',
        'BiologicalGrade': '5'
    }
    
    return pal_data

def add_to_csv():
    """
    71B 시로카바네를 기존 CSV에 추가
    """
    new_pal = parse_71b_sirokabane()
    
    # 기존 CSV 파일 읽기
    input_file = 'enhanced_complete_pals_batch5.csv'
    output_file = 'enhanced_complete_pals_batch6.csv'
    
    if not os.path.exists(input_file):
        print(f"❌ 입력 파일을 찾을 수 없습니다: {input_file}")
        return
    
    # CSV 읽기 및 새 데이터 추가
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        
        # 기존 데이터 추가
        for row in reader:
            rows.append(row)
    
    # 새로운 71B 데이터를 위한 행 생성
    new_row = []
    for field in header:
        if field in new_pal:
            new_row.append(str(new_pal[field]))
        else:
            new_row.append('')  # 매칭되지 않는 필드는 빈 값
    
    rows.append(new_row)
    
    # 새 CSV 파일 작성
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"✅ 71B 시로카바네가 추가되었습니다!")
    print(f"📁 출력 파일: {output_file}")
    print(f"📊 총 {len(rows)-1}개 팰 (이전 {len(rows)-2}개 + 새로운 1개)")
    
    # 요약 정보 출력
    print(f"\n🆕 새로 추가된 B variant:")
    print(f"   ID: {new_pal['ID']}")
    print(f"   이름: {new_pal['Name']}")
    print(f"   영문명: {new_pal['EnglishName']}")
    print(f"   타입: {new_pal['Type1']}, {new_pal['Type2']}")
    print(f"   스탯: HP {new_pal['HP']}, 공격 {new_pal['ATK']}, 방어 {new_pal['DEF']}")
    print(f"   작업: {new_pal['Work1']}, {new_pal['Work2']}")

if __name__ == "__main__":
    print("🎮 71B 시로카바네 파싱 및 CSV 추가")
    print("=" * 50)
    
    add_to_csv() 