#!/usr/bin/env python3

import csv
from pathlib import Path

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_60_pals.csv'
    output_file = 'complete_1_to_64_pals.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    # 61-64번 팰 데이터 - 실제 CSV 필드명에 맞춤
    new_pals = [
        {
            'id': 61,
            'name_kor': '불이리',
            'description_kor': '기질이 워낙 예민해 기분이 상하면 동굴에 숨어 버린다. 옛 사람들은 불이리가 숨으면 흉조로 여겼다.',
            'elements': 'Fire',
            'partnerSkill_name': '무념무상',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중에는 추위나 더위의 영향을 받지 않는다.',
            'partnerSkill_needItem': '불이리 안장',
            'partnerSkill_needItemTechLevel': '기술30',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 100,
            'stats_food': 4,
            'stats_meleeAttack': 70,
            'stats_attack': 115,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 110,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 830,
            'stats_goldCoin': 3170,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'AmaterasuWolf',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 130,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1100,
            'movement_transportSpeed': 415,
            'level60_health': '4075 – 5050',
            'level60_attack': '660 – 828',
            'level60_defense': '537 – 683',
            'activeSkills': '파이어 샷|스피릿 파이어|유령의 불꽃|풍림화산|화염 폭풍|인페르노|화염구',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관|가죽',
            'drops_count': 2,
            'workSuitabilities': '불 피우기 Lv2',
            'workSuitabilities_count': 1,
            'tribes': '푸른 불꽃의 수호신 불이리|불이리|광폭화한 불이리',
            'tribes_count': 3,
            'spawners': 'Lv. 28–32|열기 나는 대형 알',
            'spawners_count': 2
        },
        {
            'id': 62,
            'name_kor': '썬더 키드',
            'description_kor': '외톨이인 팰에게 친근하게 잘 대해준다. 착각한 상대 팰이 곁을 내주기가 무섭게 이때다 하고 낙뢰로 숨통을 끊는다.',
            'elements': 'Electric',
            'partnerSkill_name': '천둥의 딸',
            'partnerSkill_describe': '보유하고 있는 동안 플레이어 가까이에 출현한다. 플레이어의 공격에 맞춰 낙뢰로 추격한다.',
            'partnerSkill_needItem': '썬더키드의 목걸이',
            'partnerSkill_needItemTechLevel': '기술22',
            'partnerSkill_level': '1',
            'stats_size': 'XS',
            'stats_rarity': 2,
            'stats_health': 70,
            'stats_food': 2,
            'stats_meleeAttack': 110,
            'stats_attack': 80,
            'stats_defense': 70,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 20,
            'stats_combiRank': 1210,
            'stats_goldCoin': 1390,
            'stats_egg': '찌릿찌릿한 알',
            'stats_code': 'RaijinDaughter',
            'movement_slowWalkSpeed': 120,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 400,
            'movement_rideSprintSpeed': 550,
            'movement_transportSpeed': 300,
            'level60_health': '3100 – 3782',
            'level60_attack': '490 – 607',
            'level60_defense': '391 – 493',
            'activeSkills': '공기 대포|전기 파장|산성비|라인 썬더|트라이 썬더|번개 일격|전기 볼트',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발전 기관|썬더키드의 구름',
            'drops_count': 2,
            'workSuitabilities': '발전 Lv1|수작업 Lv1|운반 Lv1',
            'workSuitabilities_count': 3,
            'tribes': '번개 구름의 후예 썬더 키드|썬더 키드',
            'tribes_count': 2,
            'spawners': 'Lv. 24–28|찌릿찌릿한 알',
            'spawners_count': 2
        },
        {
            'id': 63,
            'name_kor': '루나리스',
            'description_kor': '무심결에 눈을 쳐다봤다간 꼼짝없이 당하고 만다. 루나리스를 데리고 다니는 상당수는 그저 그렇게 하도록 홀렸을 뿐이다.',
            'elements': 'Neutral',
            'partnerSkill_name': '반중력',
            'partnerSkill_describe': '보유하고 있는 동안 루나리스의 반중력에 의해 플레이어의 소지 중량 제한이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 90,
            'stats_food': 2,
            'stats_meleeAttack': 80,
            'stats_attack': 100,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1110,
            'stats_goldCoin': 1760,
            'stats_egg': '평범한 대형 알',
            'stats_code': 'Mutant',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 130,
            'movement_runSpeed': 500,
            'movement_rideSprintSpeed': 650,
            'movement_transportSpeed': 315,
            'level60_health': '3750 – 4627',
            'level60_attack': '587 – 733',
            'level60_defense': '488 – 620',
            'activeSkills': '공기 대포|파워 샷|얼음 칼날|플라즈마 토네이도|파워 폭탄|눈보라 스파이크|팰 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '팰지움 파편',
            'drops_count': 1,
            'workSuitabilities': '수작업 Lv3|채집 Lv1|운반 Lv1',
            'workSuitabilities_count': 3,
            'tribes': '우주에서 온 루나리스|루나리스',
            'tribes_count': 2,
            'spawners': 'Lv. 32–32|평범한 대형 알',
            'spawners_count': 2
        },
        {
            'id': 64,
            'name_kor': '플로라디노',
            'description_kor': '한번 화를 내면 걷잡을 수 없을 정도로 분기탱천한다. 플로라디노의 꼬리를 밟다라는 말은 누군가의 격노를 샀다는 뜻이다.',
            'elements': 'Grass|Dragon',
            'partnerSkill_name': '꽃향기 감도는 용',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 풀 속성 공격이 강화된다.',
            'partnerSkill_needItem': '플로라디노 안장',
            'partnerSkill_needItemTechLevel': '기술19',
            'partnerSkill_level': '1',
            'stats_size': 'L',
            'stats_rarity': 6,
            'stats_health': 110,
            'stats_food': 6,
            'stats_meleeAttack': 90,
            'stats_attack': 85,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 150,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 820,
            'stats_goldCoin': 3240,
            'stats_egg': '신록의 대형 알',
            'stats_code': 'FlowerDinosaur',
            'movement_slowWalkSpeed': 70,
            'movement_walkSpeed': 120,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1030,
            'movement_transportSpeed': 335,
            'level60_health': '4400 – 5472',
            'level60_attack': '514 – 638',
            'level60_defense': '488 – 620',
            'activeSkills': '바람의 칼날|꼬리 채찍|용의 파장|씨앗 지뢰|용의 숨결|가시덩굴|태양 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '밀 씨|당근 씨',
            'drops_count': 2,
            'workSuitabilities': '파종 Lv2|벌목 Lv2',
            'workSuitabilities_count': 2,
            'tribes': '화원의 수호룡 플로라디노|플로라디노|광폭화한 플로라디노|찌르르디노',
            'tribes_count': 4,
            'spawners': 'Lv. 14–17|신록의 대형 알',
            'spawners_count': 2
        }
    ]
    
    # 기존 데이터 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        existing_data = list(reader)
        headers = reader.fieldnames
    
    # 새 데이터 추가
    all_data = existing_data + new_pals
    
    # 새 CSV 파일 쓰기
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_data)
    
    print(f"✅ Successfully added 61-64 pals to {output_file}")
    print(f"Total pals: {len(all_data)}")

if __name__ == "__main__":
    main() 