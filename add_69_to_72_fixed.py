#!/usr/bin/env python3

import csv
from pathlib import Path

def main():
    # 기존 CSV 파일 읽기
    input_file = 'complete_1_to_68_pals.csv'
    output_file = 'complete_1_to_72_pals.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    # 69-72번 팰 데이터 - 실제 CSV 필드명에 맞춤
    new_pals = [
        {
            'id': 69,
            'name_kor': '핑크뇽',
            'description_kor': '하룻밤의 사랑을 찾아 항상 누군가를 뒤쫓는다. 처음엔 팰에게만 흥미를 보였지만 최근엔 사람에게도 마수를 뻗기 시작했다.',
            'elements': 'Normal',
            'partnerSkill_name': '하트 드레인',
            'partnerSkill_describe': '함께 싸우는 동안 피해를 주면 그 일부를 흡수하여 HP를 회복하는 생명 흡수 효과를 플레이어와 핑크뇽에게 부여한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1',
            'stats_size': 'L',
            'stats_rarity': 5,
            'stats_health': 120,
            'stats_food': 5,
            'stats_meleeAttack': 70,
            'stats_attack': 70,
            'stats_defense': 70,
            'stats_workSpeed': 100,
            'stats_support': '140',
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 30,
            'stats_combiRank': 940,
            'stats_goldCoin': 2450,
            'stats_egg': '평범한 대형 알',
            'stats_code': 'PinkLizard',
            'movement_slowWalkSpeed': 90,
            'movement_walkSpeed': 170,
            'movement_runSpeed': 750,
            'movement_rideSprintSpeed': 850,
            'movement_transportSpeed': 460,
            'level60_health': '4725-5895',
            'level60_attack': '441-543',
            'level60_defense': '391-493',
            'activeSkills': '파워 샷(Normal, 4초, 35) / 독 사격(Dark, 2초, 30) / 그림자 폭발(Dark, 10초, 55) / 산성비(Water, 18초, 80) / 파워 폭탄(Normal, 15초, 70) / 자폭(Normal, 55초, 230) / 팰 폭발(Normal, 55초, 150)',
            'activeSkills_count': 7,
            'passiveSkills': '어브노멀 - 무속성 피해 경감 10%',
            'passiveSkills_count': 1,
            'drops': '버섯 2-4 (100%) / 케이크 1 (1%) / 수상한 주스 1 (1%) / 이상한 주스 1 (1%) / 기억 삭제 약 1 (1%)',
            'drops_count': 5,
            'workSuitabilities': '수작업 Lv2 / 채굴 Lv1 / 제약 Lv2 / 운반 Lv2',
            'workSuitabilities_count': 4,
            'tribes': '사랑에 굶주린 팰 핑크뇽(Boss) / 핑크뇽(Normal) / 광폭화한 핑크뇽(Boss)',
            'tribes_count': 3,
            'spawners': '일반 지역(Lv.18-23) / 사막 지역(Lv.30-37) / 동굴(Lv.35-40) / 습격(Lv.5-38)',
            'spawners_count': 4
        },
        {
            'id': 70,
            'name_kor': '라비',
            'description_kor': '울 때 눈물 대신 용암이 흐른다. 흘러내린 용암은 다시 몸에 흡수되어 더욱 뜨거워진다. 흘린 눈물만큼 강해지는 것이다.',
            'elements': 'Fire',
            'partnerSkill_name': '마그마 눈물',
            'partnerSkill_describe': '가축 목장에 배치하면 발화 기관을 만들기도 한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1',
            'stats_size': 'XS',
            'stats_rarity': 1,
            'stats_health': 60,
            'stats_food': 2,
            'stats_meleeAttack': 100,
            'stats_attack': 70,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': '100',
            'stats_captureRateCorrect': 1.1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1405,
            'stats_goldCoin': 2500,
            'stats_egg': '열기 나는 알',
            'stats_code': 'LavaGirl',
            'movement_slowWalkSpeed': 65,
            'movement_walkSpeed': 98,
            'movement_runSpeed': 250,
            'movement_rideSprintSpeed': 375,
            'movement_transportSpeed': 140,
            'level60_health': '2775-3360',
            'level60_attack': '441-543',
            'level60_defense': '440-557',
            'activeSkills': '파이어 샷(Fire, 2초, 30) / 스피릿 파이어(Fire, 7초, 45) / 불화살(Fire, 10초, 55) / 유령의 불꽃(Dark, 16초, 75) / 화염 폭풍(Fire, 18초, 80) / 인페르노(Fire, 40초, 120) / 화염구(Fire, 55초, 150)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관 2-3 (100%) / 고급 팰 기름 1 (100%)',
            'drops_count': 2,
            'workSuitabilities': '불 피우기 Lv1 / 수작업 Lv1 / 운반 Lv1 / 목장 Lv1',
            'workSuitabilities_count': 4,
            'tribes': '용암 소녀 라비(Boss) / 라비(Normal)',
            'tribes_count': 2,
            'spawners': '화산 지역(Lv.9-28) / 동굴(Lv.32-38) / 알(열기 나는 알)',
            'spawners_count': 3
        },
        {
            'id': 71,
            'name_kor': '버드래곤',
            'description_kor': '버드래곤의 외골격으로 만든 피리 소리는 천 개의 봉우리를 건넌다고 한다. 고대 전쟁에선 공격 신호로 사용했다.',
            'elements': 'Fire|Dark',
            'partnerSkill_name': '하늘에서 온 습격자',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어가 적의 약점 부위를 공격할 때 주는 피해량이 증가한다.',
            'partnerSkill_needItem': '버드래곤 안장',
            'partnerSkill_needItemTechLevel': '기술21',
            'partnerSkill_level': '1',
            'stats_size': 'L',
            'stats_rarity': 4,
            'stats_health': 90,
            'stats_food': 6,
            'stats_meleeAttack': 100,
            'stats_attack': 115,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': '100',
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 660,
            'stats_goldCoin': 4360,
            'stats_egg': '열기 나는 알',
            'stats_code': 'BirdDragon',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 350,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 850,
            'movement_transportSpeed': 475,
            'level60_health': '3750-4627',
            'level60_attack': '660-828',
            'level60_defense': '488-620',
            'activeSkills': '공기 대포(Normal, 2초, 25) / 파이어 샷(Fire, 2초, 30) / 스피릿 파이어(Fire, 7초, 45) / 파이어 브레스(Fire, 15초, 70) / 플라잉 브레스(Fire, 15초, 90) / 악몽의 구체(Dark, 30초, 100) / 화염구(Fire, 55초, 150) / 어둠의 레이저(Dark, 55초, 150)',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '뼈 1-2 (100%) / 루비 1-2 (1%) / 금화 10-40 (10%)',
            'drops_count': 3,
            'workSuitabilities': '불 피우기 Lv1 / 운반 Lv3',
            'workSuitabilities_count': 2,
            'tribes': '하늘에서 온 습격자 버드래곤(Boss) / 버드래곤(Normal) / 광폭화한 버드래곤(Boss) / 시로카바네(Variant)',
            'tribes_count': 4,
            'spawners': '일반 지역(Lv.10-15) / 화산 지역(Lv.27-31) / 동굴(Lv.32-38) / 붉은 지역(Lv.50-54) / 알(열기 나는 알)',
            'spawners_count': 5
        },
        {
            'id': 72,
            'name_kor': '불무사',
            'description_kor': '죽기 무섭게 몸이 칼날처럼 변해 다음 세대로 넘겨진다. 불무사 이외의 존재가 칼을 소유하면 안에 감춰진 망자들의 끈질긴 목소리에 미쳐버리고 만다.',
            'elements': 'Fire',
            'partnerSkill_name': '번갯불 일섬',
            'partnerSkill_describe': '발동하면 목표로 삼은 적을 향해 높은 위력의 발도술로 공격한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1',
            'stats_size': 'M',
            'stats_rarity': 7,
            'stats_health': 80,
            'stats_food': 4,
            'stats_meleeAttack': 100,
            'stats_attack': 125,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': '100',
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 640,
            'stats_goldCoin': 4520,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'Ronin',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 160,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 900,
            'movement_transportSpeed': 320,
            'level60_health': '3425-4205',
            'level60_attack': '709-892',
            'level60_defense': '440-557',
            'activeSkills': '파이어 샷(Fire, 2초, 30) / 바람의 칼날(Grass, 2초, 30) / 얼음 칼날(Ice, 10초, 55) / 발도술(Fire, 9초, 65) / 파이어 브레스(Fire, 15초, 70) / 번개 일격(Electric, 40초, 120) / 인페르노(Fire, 40초, 120)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '뼈 1-2 (100%) / 금속 주괴 2-3 (100%)',
            'drops_count': 2,
            'workSuitabilities': '불 피우기 Lv2 / 수작업 Lv1 / 채집 Lv1 / 벌목 Lv3 / 운반 Lv2',
            'workSuitabilities_count': 5,
            'tribes': '유랑 무사 불무사(Boss) / 불무사(Normal) / 어둠무사(Variant)',
            'tribes_count': 3,
            'spawners': '보스 지역(Lv.23) / 화산 지역(Lv.34-37) / 금지 구역(Lv.40-45) / 무덤 지역(Lv.46-50) / 알(열기 나는 대형 알) / 습격(Lv.25-37)',
            'spawners_count': 6
        }
    ]
    
    # 기존 CSV 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing_data = list(reader)
    
    # 새 데이터 추가
    all_data = existing_data + new_pals
    
    # 새 CSV 파일로 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
    
    print(f"✅ 성공! {len(new_pals)}개 팰 추가 완료!")
    print(f"📁 출력 파일: {output_file}")
    print(f"📊 총 팰 수: {len(all_data)}개")

if __name__ == "__main__":
    main() 