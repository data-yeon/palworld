import pandas as pd
import re

# 109번 켄타나이트 데이터
pal_109 = {
    'id': 109,
    'name_kor': '켄타나이트',
    'description_kor': '원래 팔라디우스의 일종이었다. 나쁜 감정만 분리된 듯한 모습이지만 눈동자 속에는 일말의 자비가 반짝인다.',
    'elements': '어둠',
    'partnerSkill_name': '심연의 흑기사',
    'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해진다.',
    'partnerSkill_needItem': '켄타나이트 안장',
    'partnerSkill_needItemTechLevel': 49,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 20,
    'stats_health': 130,
    'stats_food': 600,
    'stats_meleeAttack': 100,
    'stats_attack': 145,
    'stats_defense': 120,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 70,
    'stats_goldCoin': 8930,
    'stats_egg': '암흑의 거대한 알',
    'stats_code': 'BlackCentaur',
    'movement_slowWalkSpeed': 100,
    'movement_walkSpeed': 350,
    'movement_runSpeed': 1300,
    'movement_rideSprintSpeed': 1900,
    'movement_transportSpeed': 625,
    'level60_health': '5050-6317',
    'level60_attack': '806-1018',
    'level60_defense': '635-810',
    'activeSkills': '그림자 폭발|스피릿 파이어|유령의 불꽃|악몽의 구체|바위 창|쌍창 돌격|어둠의 레이저|아포칼립스|스톤 비트',
    'activeSkills_count': 9,
    'passiveSkills': '전설|명왕',
    'passiveSkills_count': 2,
    'drops': '팰 금속 주괴|대형 팰 영혼',
    'drops_count': 2,
    'workSuitabilities': '벌목 Lv2|채굴 Lv2',
    'workSuitabilities_count': 2,
    'tribes': 'BlackCentaur',
    'tribes_count': 1,
    'spawners': '',
    'spawners_count': 0
}

# 110번 빙천마 데이터
pal_110 = {
    'id': 110,
    'name_kor': '빙천마',
    'description_kor': '겨울을 불러오는 팰파고스섬의 수호신. 일찍이 재앙이 이 땅을 석권할 때 하늘을 가로지르며 끝나지 않는 겨울을 불러와 이를 봉인했다.',
    'elements': '얼음',
    'partnerSkill_name': '빙천마',
    'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어의 공격이 얼음 속성으로 변화하고 얼음 속성 공격이 강화된다.',
    'partnerSkill_needItem': '빙천마 안장',
    'partnerSkill_needItemTechLevel': 48,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 20,
    'stats_health': 140,
    'stats_food': 475,
    'stats_meleeAttack': 100,
    'stats_attack': 140,
    'stats_defense': 120,
    'stats_workSpeed': 100,
    'stats_support': 70,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 120,
    'stats_goldCoin': 8440,
    'stats_egg': '얼어붙은 거대한 알',
    'stats_code': 'IceHorse',
    'movement_slowWalkSpeed': 120,
    'movement_walkSpeed': 120,
    'movement_runSpeed': 1200,
    'movement_rideSprintSpeed': 1800,
    'movement_transportSpeed': 440,
    'level60_health': '5375-6740',
    'level60_attack': '782-987',
    'level60_defense': '635-810',
    'activeSkills': '공기 대포|얼음 미사일|얼음 칼날|빙산|크리스탈 윙|서리 낀 입김|눈보라 스파이크|신성 폭발|더블 눈보라 스파이크',
    'activeSkills_count': 9,
    'passiveSkills': '전설|빙제',
    'passiveSkills_count': 2,
    'drops': '빙결 기관|다이아몬드',
    'drops_count': 2,
    'workSuitabilities': '냉각 Lv4',
    'workSuitabilities_count': 1,
    'tribes': 'IceHorse',
    'tribes_count': 1,
    'spawners': '',
    'spawners_count': 0
}

# 110B번 그레이섀도우 데이터
pal_110b = {
    'id': '110B',
    'name_kor': '그레이섀도우',
    'description_kor': '밤을 불러오는 팰파고스섬의 수호신. 일찍이 재앙이 이 땅을 석권할 때 하늘을 가로지르며 끝나지 않는 어둠을 불러와 이를 봉인했다.',
    'elements': '어둠',
    'partnerSkill_name': '흑천마',
    'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어의 공격이 어둠 속성으로 변화하고 어둠 속성 공격이 강화된다.',
    'partnerSkill_needItem': '그레이섀도우 안장',
    'partnerSkill_needItemTechLevel': 48,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 20,
    'stats_health': 140,
    'stats_food': 475,
    'stats_meleeAttack': 100,
    'stats_attack': 140,
    'stats_defense': 135,
    'stats_workSpeed': 100,
    'stats_support': 70,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 100,
    'stats_goldCoin': 8560,
    'stats_egg': '암흑의 거대한 알',
    'stats_code': 'IceHorse_Dark',
    'movement_slowWalkSpeed': 120,
    'movement_walkSpeed': 120,
    'movement_runSpeed': 1200,
    'movement_rideSprintSpeed': 1800,
    'movement_transportSpeed': 440,
    'level60_health': '5375-6740',
    'level60_attack': '782-987',
    'level60_defense': '708-905',
    'activeSkills': '공기 대포|암흑구|그림자 폭발|유령의 불꽃|크리스탈 윙|악몽의 구체|어둠의 레이저|더블 눈보라 스파이크|다크 위스프',
    'activeSkills_count': 9,
    'passiveSkills': '전설|명왕',
    'passiveSkills_count': 2,
    'drops': '순수한 석영|대형 팰 영혼',
    'drops_count': 2,
    'workSuitabilities': '채집 Lv4',
    'workSuitabilities_count': 1,
    'tribes': 'IceHorse_Dark',
    'tribes_count': 1,
    'spawners': '전설의 어둠 천마 그레이섀도우 Lv.60',
    'spawners_count': 1
}

# 111번 제트래곤 데이터
pal_111 = {
    'id': 111,
    'name_kor': '제트래곤',
    'description_kor': '팰파고스섬을 저 먼 하늘에서 굽어본다. 재앙이 다시 눈을 떠 대지를 가르고 하늘을 불태울 때 완전한 파멸의 섬광으로 이를 파괴하리라.',
    'elements': '용',
    'partnerSkill_name': '공중 미사일',
    'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 미사일 발사기 연사가 가능해진다.',
    'partnerSkill_needItem': '제트래곤 미사일 발사기',
    'partnerSkill_needItemTechLevel': 50,
    'partnerSkill_level': 1,
    'stats_size': 'XL',
    'stats_rarity': 20,
    'stats_health': 110,
    'stats_food': 600,
    'stats_meleeAttack': 100,
    'stats_attack': 140,
    'stats_defense': 110,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 90,
    'stats_goldCoin': 8680,
    'stats_egg': '용의 거대한 알',
    'stats_code': 'JetDragon',
    'movement_slowWalkSpeed': 200,
    'movement_walkSpeed': 800,
    'movement_runSpeed': 1700,
    'movement_rideSprintSpeed': 3300,
    'movement_transportSpeed': 1250,
    'level60_health': '4400-5472',
    'level60_attack': '782-987',
    'level60_defense': '586-747',
    'activeSkills': '스피릿 파이어|용의 파장|화염 폭풍|용의 숨결|유성 광선|화염구|용의 운석|빔 슬라이서|메테오 레인',
    'activeSkills_count': 9,
    'passiveSkills': '전설|신룡',
    'passiveSkills_count': 2,
    'drops': '순수한 석영|폴리머|카본 섬유|다이아몬드',
    'drops_count': 4,
    'workSuitabilities': '채집 Lv3',
    'workSuitabilities_count': 1,
    'tribes': 'JetDragon',
    'tribes_count': 1,
    'spawners': '',
    'spawners_count': 0
}

# 새로운 팰들을 리스트로 정리
new_pals = [pal_109, pal_110, pal_110b, pal_111]

# 기존 CSV 파일 읽기
try:
    existing_df = pd.read_csv('complete_1_to_108_pals.csv')
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
combined_df.to_csv('complete_1_to_111_pals.csv', index=False, encoding='utf-8')

print("\n109번부터 111번(+110B)까지의 전설급 팰 데이터가 추가되었습니다!")
print(f"총 {len(combined_df)}개의 팰 데이터가 저장되었습니다.")

# 추가된 팰들 정보 출력
print("\n추가된 전설급 팰들:")
for pal in new_pals:
    print(f"- {pal['id']}번 {pal['name_kor']} ({pal['elements']}) - 레어도 {pal['stats_rarity']}")
    print(f"  파트너 스킬: {pal['partnerSkill_name']}")
    print(f"  작업 적성: {pal['workSuitabilities']}")
    print(f"  패시브 스킬: {pal['passiveSkills']}")
    print() 