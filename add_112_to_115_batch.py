import pandas as pd
import re

# 112번 벨라누아르 데이터
pal_112 = {
    'id': 112,
    'name_kor': '벨라누아르',
    'description_kor': '존재도 없이, 그저 조용히 세계를 바라볼 뿐이었다. 언제부터인가, 누군가의 시선을 갈망하게 됐다. 외부 세계를 적대시하던 욕망의 덩어리는 광란의 숙녀라고 정의되었다.',
    'elements': '어둠',
    'partnerSkill_name': '악몽의 눈동자',
    'partnerSkill_describe': '발동하면 목표로 삼은 적을 향해 높은 위력의 악몽의 빛으로 공격한다.',
    'partnerSkill_needItem': '',
    'partnerSkill_needItemTechLevel': '',
    'partnerSkill_level': 1,
    'stats_size': 'M',
    'stats_rarity': 20,
    'stats_health': 120,
    'stats_food': 300,
    'stats_meleeAttack': 100,
    'stats_attack': 150,
    'stats_defense': 100,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 10,
    'stats_combiRank': 1,
    'stats_goldCoin': 10030,
    'stats_egg': '암흑의 거대한 알',
    'stats_code': 'NightLady',
    'movement_slowWalkSpeed': 100,
    'movement_walkSpeed': 150,
    'movement_runSpeed': 600,
    'movement_rideSprintSpeed': 800,
    'movement_transportSpeed': 400,
    'level60_health': '4725 – 5895',
    'level60_attack': '831 – 1050',
    'level60_defense': '537 – 683',
    'activeSkills': '어둠 대포|어둠 파장|어둠 화살|유령의 불꽃|악몽의 구체|아포칼립스|악몽의 빛',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '',
    'drops_count': 0,
    'workSuitabilities': '수작업 Lv2|제약 Lv4|운반 Lv2',
    'workSuitabilities_count': 3,
    'tribes': '광란의 숙녀 벨라누아르|벨라누아르|벨라루주',
    'tribes_count': 3,
    'spawners': '',
    'spawners_count': 0
}

# 113번 셀레문 데이터
pal_113 = {
    'id': 113,
    'name_kor': '셀레문',
    'description_kor': '등 뒤에 떠다니는 달처럼 생긴 물체는 세대를 거듭할 때마다 아주 조금씩 원형에 가까워진다고 한다. 그 달이 완전히 찼을 때 무슨 일이 벌어질지는, 아무도 모른다.',
    'elements': '어둠|무',
    'partnerSkill_name': '셀레스티얼 다크니스',
    'partnerSkill_describe': '등에 있는 달을 타고 하늘을 날 수 있다. 탑승 중 무속성 및 어둠 속성 공격이 강화된다.',
    'partnerSkill_needItem': '셀레문 안장',
    'partnerSkill_needItemTechLevel': 53,
    'partnerSkill_level': 1,
    'stats_size': 'L',
    'stats_rarity': 9,
    'stats_health': 130,
    'stats_food': 150,
    'stats_meleeAttack': 100,
    'stats_attack': 115,
    'stats_defense': 110,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 20,
    'stats_combiRank': 345,
    'stats_goldCoin': 9500,
    'stats_egg': '암흑의 거대한 알',
    'stats_code': 'MoonQueen',
    'movement_slowWalkSpeed': 60,
    'movement_walkSpeed': 150,
    'movement_runSpeed': 1000,
    'movement_rideSprintSpeed': 1600,
    'movement_transportSpeed': 275,
    'level60_health': '5050 – 6317',
    'level60_attack': '660 – 828',
    'level60_defense': '586 – 747',
    'activeSkills': '어둠 대포|어둠 화살|에어 블레이드|신성 폭발|청월의 칼날|스타 마인|월광선',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '천 1–2|사파이어 2–3|귀중한 발톱 1',
    'drops_count': 3,
    'workSuitabilities': '수작업 Lv4|제약 Lv3|운반 Lv3',
    'workSuitabilities_count': 3,
    'tribes': '달꽃단 대장 사야&셀레문|셀레문|칠흑의 밤에 떠오른 달 셀레문',
    'tribes_count': 3,
    'spawners': '',
    'spawners_count': 0
}

# 114번 칼구리 데이터
pal_114 = {
    'id': 114,
    'name_kor': '칼구리',
    'description_kor': '무리 중에서도 큰 실수를 범한 녀석은 자결을 강요받는다. 한계까지 부푼 소리 주머니에 나뭇가지를 찌르면 대기권 반대편까지 날아가 저승으로 돌아간다.',
    'elements': '물',
    'partnerSkill_name': '도약의 자세',
    'partnerSkill_describe': '발동하면 칼구리가 충성심을 담아 가득 부풀어오른 배에 힘을 모은다. 플레이어가 그 위에 올라타면 높게 점프할 수 있다.',
    'partnerSkill_needItem': '',
    'partnerSkill_needItemTechLevel': '',
    'partnerSkill_level': 1,
    'stats_size': 'XS',
    'stats_rarity': 4,
    'stats_health': 80,
    'stats_food': 150,
    'stats_meleeAttack': 100,
    'stats_attack': 100,
    'stats_defense': 85,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 50,
    'stats_combiRank': 795,
    'stats_goldCoin': 2070,
    'stats_egg': '축축한 알',
    'stats_code': 'KendoFrog',
    'movement_slowWalkSpeed': 33,
    'movement_walkSpeed': 66,
    'movement_runSpeed': 300,
    'movement_rideSprintSpeed': 450,
    'movement_transportSpeed': 300,
    'level60_health': '3425 – 4205',
    'level60_attack': '587 – 733',
    'level60_defense': '464 – 588',
    'activeSkills': '아쿠아 샷|버블 샷|산성비|물폭탄|라인 스플래시|월 스플래시|하이드로 스트림',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '팰의 체액 1–2|천 1–2',
    'drops_count': 2,
    'workSuitabilities': '관개 Lv1|수작업 Lv1|채집 Lv1|운반 Lv1',
    'workSuitabilities_count': 4,
    'tribes': '할복도 주저 않으리 칼구리|칼구리',
    'tribes_count': 2,
    'spawners': '칼구리 Lv.4–7|칼구리 Lv.3–6|칼구리 Lv.40–45|할복도 주저 않으리 칼구리 Lv.47–49|칼구리 Lv.40–45|칼구리 축축한 알|칼구리 Lv.30–35|칼구리 Lv.11–18',
    'spawners_count': 8
}

# 115번 뷰티플라워 데이터
pal_115 = {
    'id': 115,
    'name_kor': '뷰티플라워',
    'description_kor': '봄이 다가오면 바람을 타고 섬에 꽃가루가 휘날린다. 토푸리의 꽃가루 알레르기는 뷰티플라워 때문에 발생한다.',
    'elements': '풀',
    'partnerSkill_name': '플로럴 부스트',
    'partnerSkill_describe': '거점에 있는 동안 뷰티플라워가 농원에 기운을 불어넣어 농작물의 성장 속도가 증가한다.',
    'partnerSkill_needItem': '',
    'partnerSkill_needItemTechLevel': '',
    'partnerSkill_level': 1,
    'stats_size': 'S',
    'stats_rarity': 4,
    'stats_health': 90,
    'stats_food': 150,
    'stats_meleeAttack': 100,
    'stats_attack': 90,
    'stats_defense': 80,
    'stats_workSpeed': 100,
    'stats_support': 100,
    'stats_captureRateCorrect': 1,
    'stats_maleProbability': 30,
    'stats_combiRank': 905,
    'stats_goldCoin': 3420,
    'stats_egg': '신록의 알',
    'stats_code': 'LeafPrincess',
    'movement_slowWalkSpeed': 50,
    'movement_walkSpeed': 100,
    'movement_runSpeed': 400,
    'movement_rideSprintSpeed': 800,
    'movement_transportSpeed': 250,
    'level60_health': '3750 – 4627',
    'level60_attack': '538 – 670',
    'level60_defense': '440 – 557',
    'activeSkills': '바람의 칼날|씨앗 기관총|멀티 커터|초록 폭풍|신성 폭발|원형 덩굴|태양 폭발',
    'activeSkills_count': 7,
    'passiveSkills': '',
    'passiveSkills_count': 0,
    'drops': '예쁜 꽃 2–3|빨간 열매 1–2',
    'drops_count': 2,
    'workSuitabilities': '파종 Lv2|수작업 Lv2|채집 Lv1|제약 Lv2',
    'workSuitabilities_count': 4,
    'tribes': '꽃가루 알레르기의 원흉 뷰티플라워|뷰티플라워',
    'tribes_count': 2,
    'spawners': '뷰티플라워 Lv.40–45|뷰티플라워 Lv.40–45|꽃가루 알레르기의 원흉 뷰티플라워 Lv.47–49|뷰티플라워 Lv.40–45|뷰티플라워 신록의 알|뷰티플라워 Lv.30–35|뷰티플라워 Lv.30–40',
    'spawners_count': 7
}

# 새로운 팰들을 리스트로 정리
new_pals = [pal_112, pal_113, pal_114, pal_115]

# 기존 CSV 파일 읽기
try:
    existing_df = pd.read_csv('complete_1_to_111_pals.csv')
    print(f"기존 CSV 파일을 읽었습니다. 현재 {len(existing_df)}개의 팰이 있습니다.")
except FileNotFoundError:
    print("기존 CSV 파일을 찾을 수 없습니다. 새로운 파일을 생성합니다.")
    existing_df = pd.DataFrame()

# 새로운 팰 데이터를 DataFrame으로 변환
new_df = pd.DataFrame(new_pals)

# 기존 데이터와 새로운 데이터 합치기
if not existing_df.empty:
    final_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    final_df = new_df

# CSV 파일로 저장
output_filename = 'complete_1_to_115_pals.csv'
final_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"\n✅ 성공적으로 저장되었습니다!")
print(f"📁 파일명: {output_filename}")
print(f"📊 총 팰 수: {len(final_df)}개")
print(f"🆕 새로 추가된 팰: {len(new_pals)}개")

# 새로 추가된 팰들 정보 출력
print(f"\n🎯 새로 추가된 팰들:")
for i, pal in enumerate(new_pals, 1):
    print(f"   {pal['id']}번 {pal['name_kor']} ({pal['elements']})")

print(f"\n📈 진행률: 115/137 (약 84%)") 