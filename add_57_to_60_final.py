#!/usr/bin/env python3

import csv
from pathlib import Path

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_56_pals.csv'
    output_file = 'complete_1_to_60_pals.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    # 57-60번 팰 데이터
    new_pals = [
        {
            'id': 57,
            'name_kor': '빙호',
            'description_kor': '오로라가 보이는 밤이면 하늘을 올려다보며 아름다운 목소리로 노래를 시작한다. 다만 그 탓에 적에게 자주 공격당한다.',
            'elements': 'Ice',
            'partnerSkill_name': '오로라의 인도',
            'partnerSkill_describe': '보유하고 있는 동안 얼음 속성 팰의 공격력이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '',
            'stats_size': 'S',
            'stats_rarity': 5,
            'stats_health': 90,
            'stats_food': 3,
            'stats_meleeAttack': 95,
            'stats_attack': 95,
            'stats_defense': 105,
            'stats_workSpeed': 100,
            'stats_support': '',
            'stats_captureRateCorrect': '',
            'stats_maleProbability': '',
            'stats_combiRank': 760,
            'stats_goldCoin': '',
            'stats_egg': '',
            'stats_code': 'Foxcicle',
            'movement_slowWalkSpeed': '',
            'movement_walkSpeed': 130,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 0,
            'movement_transportSpeed': '',
            'level60_health': '3750-4627',
            'level60_attack': '563-702',
            'level60_defense': '561-715',
            'activeSkills': '공기 대포, 얼음 미사일, 얼음 칼날, 유령의 불꽃, 빙산, 서리 낀 입김, 눈보라 스파이크',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': 'Leather x1, Ice Organ x2-3',
            'drops_count': 2,
            'workSuitabilities': 'Cooling Lv2',
            'workSuitabilities_count': 1,
            'tribes': '',
            'tribes_count': 0,
            'spawners': 'Northern ice regions, Frozen areas',
            'spawners_count': 2
        },
        {
            'id': 58,
            'name_kor': '파이린',
            'description_kor': '전신이 고효율의 방열 기관이 되어 경이적인 지구력을 발휘한다. 누가 올라타면 화상을 입지 않도록 배려해준다.',
            'elements': 'Fire',
            'partnerSkill_name': '적토마',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 화염 속성으로 변화한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '',
            'stats_size': 'L',
            'stats_rarity': 6,
            'stats_health': 100,
            'stats_food': 5,
            'stats_meleeAttack': 95,
            'stats_attack': 95,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': '',
            'stats_captureRateCorrect': '',
            'stats_maleProbability': '',
            'stats_combiRank': 360,
            'stats_goldCoin': '',
            'stats_egg': '',
            'stats_code': 'Pyrin',
            'movement_slowWalkSpeed': '',
            'movement_walkSpeed': 150,
            'movement_runSpeed': 850,
            'movement_rideSprintSpeed': 1300,
            'movement_transportSpeed': '',
            'level60_health': '4075-5050',
            'level60_attack': '563-702',
            'level60_defense': '488-620',
            'activeSkills': '모래 돌풍, 파이어 샷, 스피릿 파이어, 불화살, 화염 돌격, 인페르노, 화염구',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': 'Flame Organ x4-5, Leather x2-3',
            'drops_count': 2,
            'workSuitabilities': 'Kindling Lv2, Lumbering Lv1',
            'workSuitabilities_count': 2,
            'tribes': '',
            'tribes_count': 0,
            'spawners': 'Volcanic regions, Desert areas',
            'spawners_count': 2
        },
        {
            'id': 59,
            'name_kor': '얼음사슴',
            'description_kor': '속이 비치는 투명한 뿔은 절대 영도에서 반짝인다. 맨손으로 만지면 전신이 얼어붙어 목숨마저 가루처럼 부서져 날아간다.',
            'elements': 'Ice',
            'partnerSkill_name': '써늘한 육체',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중에는 시원하여 더위를 느끼지 않게 된다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '',
            'stats_size': 'M',
            'stats_rarity': 4,
            'stats_health': 100,
            'stats_food': 7,
            'stats_meleeAttack': 85,
            'stats_attack': 85,
            'stats_defense': 110,
            'stats_workSpeed': 100,
            'stats_support': '',
            'stats_captureRateCorrect': '',
            'stats_maleProbability': '',
            'stats_combiRank': 880,
            'stats_goldCoin': '',
            'stats_egg': '',
            'stats_code': 'Reindrix',
            'movement_slowWalkSpeed': '',
            'movement_walkSpeed': 70,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1070,
            'movement_transportSpeed': '',
            'level60_health': '4075-5050',
            'level60_attack': '514-638',
            'level60_defense': '586-747',
            'activeSkills': '공기 대포, 얼음 미사일, 얼음 칼날, 얼음뿔 돌진, 빙산, 서리 낀 입김, 눈보라 스파이크',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': 'Reindrix Venison x2, Leather x1, Horn x2, Ice Organ x2-3',
            'drops_count': 4,
            'workSuitabilities': 'Lumbering Lv2, Cooling Lv2',
            'workSuitabilities_count': 2,
            'tribes': '',
            'tribes_count': 0,
            'spawners': 'Snow forests, Frozen mountains',
            'spawners_count': 2
        },
        {
            'id': 60,
            'name_kor': '썬도그',
            'description_kor': '전속력으로 뛰면 그야말로 번개나 다름없다. 썬도그 끼리 충돌하면 천둥 같은 굉음이 울려 퍼진다.',
            'elements': 'Electric',
            'partnerSkill_name': '도약력',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해진다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '',
            'stats_size': 'M',
            'stats_rarity': 5,
            'stats_health': 90,
            'stats_food': 5,
            'stats_meleeAttack': 100,
            'stats_attack': 100,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': '',
            'stats_captureRateCorrect': '',
            'stats_maleProbability': '',
            'stats_combiRank': 740,
            'stats_goldCoin': '',
            'stats_egg': '',
            'stats_code': 'Rayhound',
            'movement_slowWalkSpeed': '',
            'movement_walkSpeed': 210,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1150,
            'movement_transportSpeed': '',
            'level60_health': '3750-4627',
            'level60_attack': '587-733',
            'level60_defense': '440-557',
            'activeSkills': '모래 돌풍, 전기 파장, 스파크 샷, 바위 폭발, 천둥 소환, 번개 구체, 라인 썬더, 전기 볼트',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': 'Electric Organ x1-2',
            'drops_count': 1,
            'workSuitabilities': 'Generating Electricity Lv2',
            'workSuitabilities_count': 1,
            'tribes': '',
            'tribes_count': 0,
            'spawners': 'Desert regions, Plains',
            'spawners_count': 2
        }
    ]
    
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
        print(f"  {pal['id']}번 {pal['name_kor']} ({pal['elements']} 속성)")

if __name__ == "__main__":
    main() 