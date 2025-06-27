#!/usr/bin/env python3

import csv
from pathlib import Path

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_64_pals.csv'
    output_file = 'complete_1_to_68_pals.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    # 65-68번 팰 데이터 - 실제 CSV 필드명에 맞춤
    new_pals = [
        {
            'id': 65,
            'name_kor': '씨무기',
            'description_kor': '유선형의 몸을 가져 수상 활동에 적합하다. 밀렵꾼에게 자주 붙잡혀 서핑보드 대용으로 사용되고 있다.',
            'elements': 'Water',
            'partnerSkill_name': '쉬익쉬익 스위머',
            'partnerSkill_describe': '등에 타고 물 위를 이동할 수 있다. 탑승 중 수상 이동으로 인한 기력 소비를 무효화한다.',
            'partnerSkill_needItem': '씨무기 안장',
            'partnerSkill_needItemTechLevel': '기술10',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 4,
            'stats_health': 90,
            'stats_food': 5,
            'stats_meleeAttack': 70,
            'stats_attack': 90,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 560,
            'stats_goldCoin': 5050,
            'stats_egg': '축축한 알',
            'stats_code': 'Serpent',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 500,
            'movement_rideSprintSpeed': 800,
            'movement_transportSpeed': 350,
            'level60_health': '3750 – 4627',
            'level60_attack': '538 – 670',
            'level60_defense': '440 – 557',
            'activeSkills': '워터 제트(물, 30, Lv1), 용 대포(용, 30, Lv7), 아쿠아 샷(물, 40, Lv15), 버블 샷(물, 65, Lv22), 용의 파장(용, 55, Lv30), 용의 숨결(용, 70, Lv40), 하이드로 스트림(물, 150, Lv50)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '팰의 체액 1–2 (100%)',
            'drops_count': 1,
            'workSuitabilities': '관개 Lv2',
            'workSuitabilities_count': 1,
            'tribes': '씨무기(Normal), 파도 소리의 화신 씨무기(Boss), 스너펜트(Variant)',
            'tribes_count': 3,
            'spawners': 'Plains, Forest, Cave spawns',
            'spawners_count': 5
        },
        {
            'id': 66,
            'name_kor': '고스호스',
            'description_kor': '죽을 때가 가까워진 생물이 뿜어내는 독특한 냄새를 좋아한다. 고스호스에게 사랑받는다는 건 바로 그런 것이다.',
            'elements': 'Dark',
            'partnerSkill_name': '명계의 사자',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 어둠 속성으로 변화한다.',
            'partnerSkill_needItem': '고스호스 안장',
            'partnerSkill_needItemTechLevel': '기술23',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 75,
            'stats_food': 3,
            'stats_meleeAttack': 50,
            'stats_attack': 105,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1150,
            'stats_goldCoin': 1570,
            'stats_egg': '암흑의 대형 알',
            'stats_code': 'GhostBeast',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 160,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1100,
            'movement_transportSpeed': 365,
            'level60_health': '3262 – 3993',
            'level60_attack': '611 – 765',
            'level60_defense': '440 – 557',
            'activeSkills': '파이어 샷(화염, 30, Lv1), 암흑구(어둠, 40, Lv7), 불화살(화염, 55, Lv15), 그림자 폭발(어둠, 55, Lv22), 유령의 불꽃(어둠, 75, Lv30), 유령의 질주(어둠, 90, Lv35), 악몽의 구체(어둠, 100, Lv40), 어둠의 레이저(어둠, 150, Lv50)',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '뼈 1–2 (100%), 작은 팰 영혼 1 (15%), 원유 1 (50%)',
            'drops_count': 3,
            'workSuitabilities': '채집 Lv2, 채굴 Lv1',
            'workSuitabilities_count': 2,
            'tribes': '고스호스(Normal), 명계의 사자 고스호스(Boss), 광폭화한 고스호스(Boss)',
            'tribes_count': 3,
            'spawners': 'Snow areas, Cave spawns',
            'spawners_count': 6
        },
        {
            'id': 67,
            'name_kor': '드릴북이',
            'description_kor': '드릴북이의 드릴이란 이야기가 있다. 최강의 등딱지와 드릴을 가진 드릴북이가 모순에 관해 고민하는 도덕적인 이야기다.',
            'elements': 'Ground',
            'partnerSkill_name': '드릴 크래셔',
            'partnerSkill_describe': '발동하면 쉘 스핀 상태가 된다. 회전하면서 플레이어를 따라와 광석을 효율적으로 파괴한다.',
            'partnerSkill_needItem': '드릴북이의 머리띠',
            'partnerSkill_needItemTechLevel': '기술19',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 5,
            'stats_health': 80,
            'stats_food': 5,
            'stats_meleeAttack': 80,
            'stats_attack': 95,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 850,
            'stats_goldCoin': 2980,
            'stats_egg': '거친 느낌의 대형 알',
            'stats_code': 'DrillGame',
            'movement_slowWalkSpeed': 75,
            'movement_walkSpeed': 120,
            'movement_runSpeed': 300,
            'movement_rideSprintSpeed': 420,
            'movement_transportSpeed': 190,
            'level60_health': '3425 – 4205',
            'level60_attack': '563 – 702',
            'level60_defense': '635 – 810',
            'activeSkills': '아쿠아 샷(물, 40, Lv1), 바위 폭발(땅, 55, Lv7), 쉘 스핀(땅, 65, Lv15), 바위 대포(땅, 70, Lv22), 모래 폭풍(땅, 80, Lv30), 물폭탄(물, 100, Lv40), 바위 창(땅, 150, Lv50)',
            'activeSkills_count': 7,
            'passiveSkills': '단단한 피부(방어 +10%)',
            'passiveSkills_count': 1,
            'drops': '금속 광석 2–3 (100%), 고급 팰 기름 2–3 (100%)',
            'drops_count': 2,
            'workSuitabilities': '채굴 Lv3',
            'workSuitabilities_count': 1,
            'tribes': '드릴북이(Normal), 회전 착암기 드릴북이(Boss), 광폭화한 드릴북이(Boss)',
            'tribes_count': 3,
            'spawners': 'Desert areas, Cave spawns',
            'spawners_count': 5
        },
        {
            'id': 68,
            'name_kor': '냥뱃',
            'description_kor': '갑자기 다른 팰 앞에 나타나 자랑스레 날개를 펼쳐 존재감을 과시한다. 위협적인 종으로 여겨지나 어딘지 모르게 황홀한 표정을 하고 있다.',
            'elements': 'Dark',
            'partnerSkill_name': '초음파 센서',
            'partnerSkill_describe': '발동하면 초음파로 가까이 있는 팰의 위치를 탐지할 수 있다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 5,
            'stats_health': 95,
            'stats_food': 5,
            'stats_meleeAttack': 100,
            'stats_attack': 95,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 750,
            'stats_goldCoin': 3810,
            'stats_egg': '암흑의 대형 알',
            'stats_code': 'CatBat',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 140,
            'movement_runSpeed': 400,
            'movement_rideSprintSpeed': 550,
            'movement_transportSpeed': 270,
            'level60_health': '3912 – 4838',
            'level60_attack': '563 – 702',
            'level60_defense': '440 – 557',
            'activeSkills': '공기 대포(무, 25, Lv1), 독 사격(어둠, 30, Lv7), 암흑구(어둠, 40, Lv15), 그림자 폭발(어둠, 55, Lv22), 유령의 불꽃(어둠, 75, Lv30), 악몽의 구체(어둠, 100, Lv40), 어둠의 레이저(어둠, 150, Lv50)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '가죽 1–2 (100%), 작은 팰 영혼 1 (1%)',
            'drops_count': 2,
            'workSuitabilities': '채집 Lv2, 채굴 Lv2, 운반 Lv2',
            'workSuitabilities_count': 3,
            'tribes': '냥뱃(Normal), 장난꾸러기 냥뱃(Boss)',
            'tribes_count': 2,
            'spawners': 'Grass areas, Cave spawns',
            'spawners_count': 8
        }
    ]
    
    # 기존 데이터 읽기
    existing_data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            existing_data.append(row)
    
    # 새 데이터와 기존 데이터 합치기
    all_data = existing_data + new_pals
    
    # 새 CSV 파일로 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_data:
            writer.writerow(row)
    
    print(f"✅ Successfully added 65-68번 팰들 to {output_file}")
    print(f"📊 Total records: {len(all_data)}")
    print(f"🆕 New pals added: 65-씨무기, 66-고스호스, 67-드릴북이, 68-냥뱃")

if __name__ == "__main__":
    main() 