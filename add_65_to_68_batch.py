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
            'work_kindling': 0,
            'work_watering': 2,
            'work_planting': 0,
            'work_generating_electricity': 0,
            'work_handiwork': 0,
            'work_gathering': 0,
            'work_lumbering': 0,
            'work_mining': 0,
            'work_medicine': 0,
            'work_cooling': 0,
            'work_transporting': 0,
            'work_farming': 0,
            'active_1_name': '워터 제트',
            'active_1_element': 'Water',
            'active_1_power': 30,
            'active_1_level': 1,
            'active_2_name': '용 대포',
            'active_2_element': 'Dragon',
            'active_2_power': 30,
            'active_2_level': 7,
            'active_3_name': '아쿠아 샷',
            'active_3_element': 'Water',
            'active_3_power': 40,
            'active_3_level': 15,
            'nickname': '포켓몬 라프라스의 이미지. 서핑에 최적화된 팰'
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
            'work_kindling': 0,
            'work_watering': 0,
            'work_planting': 0,
            'work_generating_electricity': 0,
            'work_handiwork': 0,
            'work_gathering': 2,
            'work_lumbering': 0,
            'work_mining': 1,
            'work_medicine': 0,
            'work_cooling': 0,
            'work_transporting': 0,
            'work_farming': 0,
            'active_1_name': '파이어 샷',
            'active_1_element': 'Fire',
            'active_1_power': 30,
            'active_1_level': 1,
            'active_2_name': '암흑구',
            'active_2_element': 'Dark',
            'active_2_power': 40,
            'active_2_level': 7,
            'active_3_name': '불화살',
            'active_3_element': 'Fire',
            'active_3_power': 55,
            'active_3_level': 15,
            'nickname': '음모론의 완전체, 어둠의 왕국'
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
            'work_kindling': 0,
            'work_watering': 0,
            'work_planting': 0,
            'work_generating_electricity': 0,
            'work_handiwork': 0,
            'work_gathering': 0,
            'work_lumbering': 0,
            'work_mining': 3,
            'work_medicine': 0,
            'work_cooling': 0,
            'work_transporting': 0,
            'work_farming': 0,
            'active_1_name': '아쿠아 샷',
            'active_1_element': 'Water',
            'active_1_power': 40,
            'active_1_level': 1,
            'active_2_name': '바위 폭발',
            'active_2_element': 'Ground',
            'active_2_power': 55,
            'active_2_level': 7,
            'active_3_name': '쉘 스핀',
            'active_3_element': 'Ground',
            'active_3_power': 65,
            'active_3_level': 15,
            'nickname': '채굴 전용 치트키. 돌 걱정은 이제 안녕'
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
            'work_kindling': 0,
            'work_watering': 0,
            'work_planting': 0,
            'work_generating_electricity': 0,
            'work_handiwork': 0,
            'work_gathering': 2,
            'work_lumbering': 0,
            'work_mining': 2,
            'work_medicine': 0,
            'work_cooling': 0,
            'work_transporting': 2,
            'work_farming': 0,
            'active_1_name': '공기 대포',
            'active_1_element': 'Neutral',
            'active_1_power': 25,
            'active_1_level': 1,
            'active_2_name': '독 사격',
            'active_2_element': 'Dark',
            'active_2_power': 30,
            'active_2_level': 7,
            'active_3_name': '암흑구',
            'active_3_element': 'Dark',
            'active_3_power': 40,
            'active_3_level': 15,
            'nickname': '배트맨과 고양이가 합쳐진 귀여운 팰'
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