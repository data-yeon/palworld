import pandas as pd
import re

# 105번 호루스 데이터
pal_105 = {
    'id': 105,
    'name_kor': '호루스',
    'description_kor': '먹잇감 무리를 발견하면 작열하는 회오리바람으로 주변 일대를 불바다로 만든다. 호루스의 서식지는 감미로운 향기가 난다.',
    'elements': '화염',
    'partnerSkill_name': '작열의 포식자',
    'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 함께 싸우는 동안 얼음 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
    'partnerSkill_needItem': '호루스 안장',
    'partnerSkill_needItemTechLevel': 38,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 9,
    'stats_health': 100,
    'stats_food': 525,
    'stats_meleeAttack': 100,
    'stats_attack': 105,
    'stats_defense': 110,
    'stats_workSpeed': 100,
    'stats_support': 90,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 370,
    'stats_goldCoin': 6720,
    'stats_egg': '열기 나는 거대한 알',
    'stats_code': 'Horus',
    'movement_slowWalkSpeed': 150,
    'movement_walkSpeed': 200,
    'movement_runSpeed': 1000,
    'movement_rideSprintSpeed': 1400,
    'movement_transportSpeed': 500,
    'level60_health': '4075-5050',
    'level60_attack': '611-765',
    'level60_defense': '586-747',
    'activeSkills': '파이어 샷|불화살|스피릿 파이어|파이어 브레스|봉황의 비행|인페르노|화염구|염황열파',
    'activeSkills_count': 8,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '발화 기관',
    'drops_count': 1,
    'workSuitabilities': '불 피우기 Lv3|운반 Lv3',
    'workSuitabilities_count': 2,
    'tribes': 'Horus',
    'tribes_count': 1,
    'spawners': '제3 사냥 금지 구역 Lv.40-45',
    'spawners_count': 1
}

# 106번 전룡맨 데이터
pal_106 = {
    'id': 106,
    'name_kor': '전룡맨',
    'description_kor': '상처로 전류를 흘려보내 상대의 몸을 불태운다. 전룡맨끼리 싸우면 순식간에 승부가 난다.',
    'elements': '용|번개',
    'partnerSkill_name': '사나운 번개용',
    'partnerSkill_describe': '함께 싸우는 동안 물 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
    'partnerSkill_needItem': '',
    'partnerSkill_needItemTechLevel': 0,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 9,
    'stats_health': 100,
    'stats_food': 475,
    'stats_meleeAttack': 100,
    'stats_attack': 130,
    'stats_defense': 100,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 140,
    'stats_goldCoin': 8320,
    'stats_egg': '용의 거대한 알',
    'stats_code': 'ThunderDragonMan',
    'movement_slowWalkSpeed': 100,
    'movement_walkSpeed': 185,
    'movement_runSpeed': 900,
    'movement_rideSprintSpeed': 1200,
    'movement_transportSpeed': 250,
    'level60_health': '4075-5050',
    'level60_attack': '733-923',
    'level60_defense': '537-683',
    'activeSkills': '케라노우스|번개 일격|스파크 샷|용의 숨결|라인 썬더|트라이 썬더|전기 볼트|폴리케라우노스',
    'activeSkills_count': 8,
    'passiveSkills': '뇌제',
    'passiveSkills_count': 1,
    'drops': '발전 기관',
    'drops_count': 1,
    'workSuitabilities': '발전 Lv4|수작업 Lv2|운반 Lv3',
    'workSuitabilities_count': 3,
    'tribes': 'ThunderDragonMan',
    'tribes_count': 1,
    'spawners': '제3 사냥 금지 구역 Lv.40-45',
    'spawners_count': 1
}

# 107번 제노그리프 데이터
pal_107 = {
    'id': 107,
    'name_kor': '제노그리프',
    'description_kor': '광기 끝에 태어난 금기의 존재. 다른 팰과 유전적 연관성이 사라진 상태이며 팰의 범주에서 벗어나 버렸는지도 모른다.',
    'elements': '어둠',
    'partnerSkill_name': '개조 유전자',
    'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 어둠 속성 공격이 강화된다. 하늘을 나는 동안 이동 속도가 상승한다.',
    'partnerSkill_needItem': '제노그리프 안장',
    'partnerSkill_needItemTechLevel': 47,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 10,
    'stats_health': 120,
    'stats_food': 525,
    'stats_meleeAttack': 130,
    'stats_attack': 120,
    'stats_defense': 140,
    'stats_workSpeed': 100,
    'stats_support': 90,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 60,
    'stats_goldCoin': 9060,
    'stats_egg': '암흑의 거대한 알',
    'stats_code': 'BlackGriffon',
    'movement_slowWalkSpeed': 80,
    'movement_walkSpeed': 80,
    'movement_runSpeed': 850,
    'movement_rideSprintSpeed': 1600,
    'movement_transportSpeed': 465,
    'level60_health': '4725-5895',
    'level60_attack': '685-860',
    'level60_defense': '732-937',
    'activeSkills': '공기 대포|암흑구|그림자 폭발|유령의 불꽃|악몽의 구체|신이 내린 재앙|어둠의 레이저|신이 내린 재앙 Ⅱ',
    'activeSkills_count': 8,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '팰 금속 주괴|카본 섬유|혁신적인 기술서',
    'drops_count': 3,
    'workSuitabilities': '채집 Lv1',
    'workSuitabilities_count': 1,
    'tribes': 'BlackGriffon',
    'tribes_count': 1,
    'spawners': '제3 사냥 금지 구역 Lv.40-45',
    'spawners_count': 1
}

# 108번 팔라디우스 데이터
pal_108 = {
    'id': 108,
    'name_kor': '팔라디우스',
    'description_kor': '원래 켄타나이트의 일종이었다. 나쁜 감정을 제거한 존재로 여겨지나 눈동자 속에선 일말의 증오가 번뜩인다.',
    'elements': '무',
    'partnerSkill_name': '하늘을 나는 성기사',
    'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 3단 점프가 가능해진다.',
    'partnerSkill_needItem': '팔라디우스 안장',
    'partnerSkill_needItemTechLevel': 49,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 20,
    'stats_health': 130,
    'stats_food': 600,
    'stats_meleeAttack': 110,
    'stats_attack': 120,
    'stats_defense': 145,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 80,
    'stats_goldCoin': 8810,
    'stats_egg': '평범하고 거대한 알',
    'stats_code': 'SaintCentaur',
    'movement_slowWalkSpeed': 50,
    'movement_walkSpeed': 100,
    'movement_runSpeed': 800,
    'movement_rideSprintSpeed': 1800,
    'movement_transportSpeed': 450,
    'level60_health': '5050-6317',
    'level60_attack': '685-860',
    'level60_defense': '756-968',
    'activeSkills': '파워 샷|얼음 미사일|빙산|파워 폭탄|눈보라 스파이크|창기병 돌격|팰 폭발|프로스트 아웃|신성 폭발',
    'activeSkills_count': 9,
    'passiveSkills': '전설|성천',
    'passiveSkills_count': 2,
    'drops': '팰 금속 주괴|다이아몬드',
    'drops_count': 2,
    'workSuitabilities': '벌목 Lv2|채굴 Lv2',
    'workSuitabilities_count': 2,
    'tribes': 'SaintCentaur',
    'tribes_count': 1,
    'spawners': '',
    'spawners_count': 0
}

# 새로운 팰들을 리스트로 정리
new_pals = [pal_105, pal_106, pal_107, pal_108]

# 기존 CSV 파일 읽기
try:
    existing_df = pd.read_csv('complete_1_to_104_pals.csv')
    print(f"기존 CSV 파일을 읽었습니다. 현재 {len(existing_df)}개의 팰이 있습니다.")
except FileNotFoundError:
    print("기존 CSV 파일을 찾을 수 없습니다. 새로운 파일을 생성합니다.")
    existing_df = pd.DataFrame()

# 새로운 팰 데이터를 DataFrame으로 변환
new_df = pd.DataFrame(new_pals)

# 기존 데이터와 새 데이터 결합
if not existing_df.empty:
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    combined_df = new_df

# CSV 파일로 저장
combined_df.to_csv('complete_1_to_108_pals.csv', index=False, encoding='utf-8')

print("\n105번부터 108번까지의 팰 데이터가 추가되었습니다!")
print(f"총 {len(combined_df)}개의 팰 데이터가 저장되었습니다.")

# 추가된 팰들 정보 출력
print("\n추가된 팰들:")
for pal in new_pals:
    print(f"- {pal['id']}번 {pal['name_kor']} ({pal['elements']})")
    print(f"  파트너 스킬: {pal['partnerSkill_name']}")
    print(f"  작업 적성: {pal['workSuitabilities']}")
    print() 