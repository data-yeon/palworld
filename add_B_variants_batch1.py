import pandas as pd
import re

# 88B 프로스카노 데이터
pal_88B = {
    'id': '88B',
    'name_kor': '프로스카노',
    'description_kor': '초저온의 피가 전신에 힘차게 흐르고 있다. 순식간에 가열되면 혈액이 증발해 엄청난 증기 폭발이 발생한다.',
    'elements': '얼음|땅',
    'partnerSkill_name': '얼음덩어리를 탐하는 야수',
    'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 광석 파괴 효율이 향상된다.',
    'partnerSkill_needItem': '프로스카노 안장',
    'partnerSkill_needItemTechLevel': 38,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 7,
    'stats_health': 110,
    'stats_food': 350,
    'stats_meleeAttack': 100,
    'stats_attack': 105,
    'stats_defense': 130,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 230,
    'stats_goldCoin': 7380,
    'stats_egg': '얼어붙은 대형 알',
    'stats_code': 'VolcanicMonster_Ice',
    'movement_slowWalkSpeed': 50,
    'movement_walkSpeed': 80,
    'movement_runSpeed': 550,
    'movement_rideSprintSpeed': 1000,
    'movement_transportSpeed': 235,
    'level60_health': '4400 – 5472',
    'level60_attack': '611 – 765',
    'level60_defense': '683 – 873',
    'activeSkills': '얼음 미사일|바위 폭발|빙산|서리 낀 입김|서리 폭발|눈보라 스파이크|바위 창',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '빙결 기관',
    'drops_count': 1,
    'workSuitabilities': '채굴 Lv3|냉각 Lv3',
    'workSuitabilities_count': 2,
    'tribes': '얼음 깨기에 굶주린 야수 프로스카노|프로스카노|광폭화한 프로스카노|볼카노',
    'tribes_count': 4,
    'spawners': '영봉의 동굴|얼어붙은 대형 알',
    'spawners_count': 2
}

# 84B 시니에노 데이터
pal_84B = {
    'id': '84B',
    'name_kor': '시니에노',
    'description_kor': '평범한 고기를 좋아하지만 항상 오염된 고기를 먹는다. 암흑의 발톱을 무기로 삼은 탓에 잡은 먹이가 저주받는다는 걸 깨닫지 못했기 때문이다.',
    'elements': '화염|어둠',
    'partnerSkill_name': '검은 불 사자',
    'partnerSkill_describe': '등에 타고 이동할 수 있다. 함께 싸우는 동안 무속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
    'partnerSkill_needItem': '시니에노 안장',
    'partnerSkill_needItemTechLevel': 35,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 8,
    'stats_health': 105,
    'stats_food': 475,
    'stats_meleeAttack': 100,
    'stats_attack': 115,
    'stats_defense': 80,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 670,
    'stats_goldCoin': 4360,
    'stats_egg': '열기 나는 거대한 알',
    'stats_code': 'Manticore_Dark',
    'movement_slowWalkSpeed': 60,
    'movement_walkSpeed': 90,
    'movement_runSpeed': 800,
    'movement_rideSprintSpeed': 1200,
    'movement_transportSpeed': 420,
    'level60_health': '4237 – 5261',
    'level60_attack': '660 – 828',
    'level60_defense': '440 – 557',
    'activeSkills': '그림자 폭발|불화살|파이어 브레스|유령의 불꽃|인페르노|화산의 일격|화염구|어둠의 레이저',
    'activeSkills_count': 8,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '발화 기관',
    'drops_count': 1,
    'workSuitabilities': '불 피우기 Lv3|벌목 Lv2',
    'workSuitabilities_count': 2,
    'tribes': '어두운 불꽃의 왕 시니에노|시니에노|광폭화한 시니에노|만티파이어',
    'tribes_count': 4,
    'spawners': '화산 지역|모래 언덕 동굴|열기 나는 거대한 알',
    'spawners_count': 3
}

# 12B 코치도치 데이터
pal_12B = {
    'id': '12B',
    'name_kor': '코치도치',
    'description_kor': '충격을 받으면 모았던 냉기를 방출한다. 방사상에 퍼진 냉기는 대기를 꽁꽁 얼려 습격해온 상대의 몸을 꿰뚫는다.',
    'elements': '얼음',
    'partnerSkill_name': '딱딱 폭탄',
    'partnerSkill_describe': '발동하면 코치도치을(를) 손에 장착하며 적에게 던져 착탄할 시 얼음 폭발을 일으킨다.',
    'partnerSkill_needItem': '코치도치 글러브',
    'partnerSkill_needItemTechLevel': 11,
    'partnerSkill_level': 1,
    'stats_size': 'XS',
    'stats_rarity': 2,
    'stats_health': 70,
    'stats_food': 150,
    'stats_meleeAttack': 70,
    'stats_attack': 75,
    'stats_defense': 80,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 1360,
    'stats_goldCoin': 1070,
    'stats_egg': '얼어붙은 알',
    'stats_code': 'Hedgehog_Ice',
    'movement_slowWalkSpeed': 30,
    'movement_walkSpeed': 60,
    'movement_runSpeed': 400,
    'movement_rideSprintSpeed': 550,
    'movement_transportSpeed': 215,
    'level60_health': '3100 – 3782',
    'level60_attack': '465 – 575',
    'level60_defense': '440 – 557',
    'activeSkills': '얼음 미사일|파워 샷|빙산|파워 폭탄|얼음 칼날|서리 낀 입김|눈보라 스파이크',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '빙결 기관',
    'drops_count': 1,
    'workSuitabilities': '냉각 Lv1',
    'workSuitabilities_count': 1,
    'tribes': '밟으면 위험! 코치도치|코치도치|찌릿도치',
    'tribes_count': 3,
    'spawners': '포획 케이지',
    'spawners_count': 1
}

# 13B 초롱이 (꽃 변종) 데이터
pal_13B = {
    'id': '13B',
    'name_kor': '초롱이',
    'description_kor': '수액 같은 몸을 가진 신기한 팰. 뒤집어쓸 게 없으면 서서히 말라가다가 결국 썩어서 없어진다.',
    'elements': '풀|땅',
    'partnerSkill_name': '나무꾼의 지원',
    'partnerSkill_describe': '보유하고 있는 동안 플레이어가 벌목할 때 피해량이 증가한다.',
    'partnerSkill_needItem': '',
    'partnerSkill_needItemTechLevel': '',
    'partnerSkill_level': 1,
    'stats_size': 'XS',
    'stats_rarity': 10,
    'stats_health': 70,
    'stats_food': 100,
    'stats_meleeAttack': 100,
    'stats_attack': 70,
    'stats_defense': 70,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1.3,
    'stats_maleProbability': 50,
    'stats_combiRank': 1240,
    'stats_goldCoin': 1310,
    'stats_egg': '신록의 거대한 알',
    'stats_code': 'PlantSlime_Flower',
    'movement_slowWalkSpeed': 50,
    'movement_walkSpeed': 50,
    'movement_runSpeed': 300,
    'movement_rideSprintSpeed': 400,
    'movement_transportSpeed': 175,
    'level60_health': '3100 – 3782',
    'level60_attack': '441 – 543',
    'level60_defense': '391 – 493',
    'activeSkills': '모래 돌풍|바람의 칼날|바위 폭발|씨앗 기관총|씨앗 지뢰|모래 폭풍|태양 폭발',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '열매 씨|예쁜 꽃|초롱이 잎사귀',
    'drops_count': 3,
    'workSuitabilities': '파종 Lv1',
    'workSuitabilities_count': 1,
    'tribes': '갑자기 변이한 초롱이|초롱이',
    'tribes_count': 2,
    'spawners': '일반 필드|구릉 동굴',
    'spawners_count': 2
}

# CSV 파일에 추가할 데이터 리스트
new_pals = [pal_88B, pal_84B, pal_12B, pal_13B]

# 기존 CSV 파일 읽기
try:
    df = pd.read_csv('complete_1_to_115_pals.csv')
    print(f"기존 CSV 파일을 읽었습니다. 현재 {len(df)}개의 팰이 있습니다.")
except FileNotFoundError:
    print("기존 CSV 파일을 찾을 수 없습니다. 새로운 파일을 생성합니다.")
    # CSV 헤더 정의
    columns = [
        'id', 'name_kor', 'description_kor', 'elements', 'partnerSkill_name', 'partnerSkill_describe', 
        'partnerSkill_needItem', 'partnerSkill_needItemTechLevel', 'partnerSkill_level', 'stats_size', 
        'stats_rarity', 'stats_health', 'stats_food', 'stats_meleeAttack', 'stats_attack', 'stats_defense', 
        'stats_workSpeed', 'stats_support', 'stats_captureRateCorrect', 'stats_maleProbability', 
        'stats_combiRank', 'stats_goldCoin', 'stats_egg', 'stats_code', 'movement_slowWalkSpeed', 
        'movement_walkSpeed', 'movement_runSpeed', 'movement_rideSprintSpeed', 'movement_transportSpeed', 
        'level60_health', 'level60_attack', 'level60_defense', 'activeSkills', 'activeSkills_count', 
        'passiveSkills', 'passiveSkills_count', 'drops', 'drops_count', 'workSuitabilities', 
        'workSuitabilities_count', 'tribes', 'tribes_count', 'spawners', 'spawners_count'
    ]
    df = pd.DataFrame(columns=columns)

# 새로운 팰 데이터를 DataFrame으로 변환
new_df = pd.DataFrame(new_pals)

# 기존 데이터와 합치기
df = pd.concat([df, new_df], ignore_index=True)

# CSV 파일로 저장
output_filename = 'complete_1_to_115_plus_B_variants.csv'
df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"\n🎉 B 변종 4개가 성공적으로 추가되었습니다!")
print(f"파일명: {output_filename}")
print(f"총 팰 수: {len(df)}개")

print("\n📊 추가된 B 변종들:")
for pal in new_pals:
    print(f"- {pal['id']} {pal['name_kor']} ({pal['elements']}): {pal['partnerSkill_name']}") 