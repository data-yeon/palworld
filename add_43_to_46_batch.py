import csv
import re

# 현재 CSV 파일 읽기
input_file = 'complete_1_to_42_pals.csv'
output_file = 'complete_1_to_46_pals.csv'

# 기존 데이터 로드
existing_data = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        existing_data.append(row)

# 43-46번 팰 데이터 (정확한 필드명 사용)
new_pals = [
    {
        "id": "43",
        "name_kor": "도도롱",
        "description_kor": "한없이 늘어질 때는 모든 반응이 둔해진다. 28번의 자상을 입게 되더라도 다음 날이 되어서야 이를 깨닫고 목숨을 잃는다.",
        "elements": "땅|물",
        "partnerSkill_name": "토양 개선",
        "partnerSkill_describe": "보유하고 있는 동안 땅 속성 팰의 공격력이 증가한다. 가축 목장에 배치하면 고급 팰 기름을 떨어뜨리기도 한다.",
        "partnerSkill_needItem": "",
        "partnerSkill_needItemTechLevel": "0",
        "partnerSkill_levels": "Lv1: 공격 +10%, Lv2: 공격 +11%, Lv3: 공격 +13%, Lv4: 공격 +16%, Lv5: 공격 +20%",
        "partnerSkill_ranchDrop": "고급 팰 기름",
        "rarity": "4",
        "size": "M",
        "hp_base": "100",
        "hp_level1": "",
        "hp_level60": "4075-5050",
        "melee_attack": "100",
        "shot_attack": "70",
        "defense": "95",
        "defense_level60": "513-652",
        "attack_level60": "441-543",
        "support": "100",
        "work_speed": "100",
        "food_amount": "4",
        "stamina": "100",
        "walk_speed": "150",
        "run_speed": "450",
        "ride_sprint_speed": "600",
        "transport_speed": "300",
        "work_suitability": "관개1, 채굴2, 운반1, 목장1",
        "element_weaknesses": "",
        "passiveSkill_names": "",
        "passiveSkill_ranks": "",
        "active_skills": "모래 돌풍(땅속성,40위력), 아쿠아 샷(물속성,40위력), 바위 폭발(땅속성,55위력), 버블 샷(물속성,65위력), 물폭탄(물속성,100위력), 바위 창(땅속성,150위력), 하이드로 스트림(물속성,150위력)",
        "drop_items": "도도롱의 살코기 x2 (100%), 고급 팰 기름 x1 (100%)",
        "habitats": "계곡의 동굴, 모래 언덕 동굴, 낚시터",
        "breeding_rank": "895",
        "price": "4690",
        "egg_type": "거친 느낌의 알",
        "english_name": "Dumud",
        "japanese_name": "ドロミテ",
        "dexNo": "43"
    },
    {
        "id": "49", 
        "name_kor": "고릴레이지",
        "description_kor": "지면을 두드리는 리듬으로 동료와 의사소통한다. 리듬에 상응하는 의미는 무리마다 다른데 그 분류는 지금도 명확하지 않다.",
        "elements": "무속성",
        "partnerSkill_name": "풀 파워 고릴라 모드",
        "partnerSkill_describe": "발동하면 야성의 힘을 해방해 일정 시간 고릴레이지의 공격력이 증가한다.",
        "partnerSkill_needItem": "",
        "partnerSkill_needItemTechLevel": "0",
        "partnerSkill_levels": "Lv1: 공격 +50%, Lv2: 공격 +75%, Lv3: 공격 +110%, Lv4: 공격 +150%, Lv5: 공격 +200%",
        "partnerSkill_ranchDrop": "",
        "rarity": "5",
        "size": "S",
        "hp_base": "90",
        "hp_level1": "",
        "hp_level60": "3750-4627",
        "melee_attack": "110",
        "shot_attack": "95",
        "defense": "90",
        "defense_level60": "488-620",
        "attack_level60": "563-702",
        "support": "100",
        "work_speed": "100",
        "food_amount": "3",
        "stamina": "100",
        "walk_speed": "100",
        "run_speed": "550",
        "ride_sprint_speed": "720",
        "transport_speed": "250",
        "work_suitability": "수작업1, 벌목2, 운반3",
        "element_weaknesses": "",
        "passiveSkill_names": "난폭함",
        "passiveSkill_ranks": "1",
        "active_skills": "모래 돌풍(땅속성,40위력), 파워 샷(무속성,35위력), 고릴라운드 콤보(무속성,85위력,전용), 바위 폭발(땅속성,55위력), 씨앗 기관총(풀속성,50위력), 파워 폭탄(무속성,70위력), 팰 폭발(무속성,150위력)",
        "drop_items": "가죽 x1-2 (100%), 뼈 x1 (100%)",
        "habitats": "시냇물 동굴",
        "breeding_rank": "1040",
        "price": "2010",
        "egg_type": "평범한 대형 알",
        "english_name": "Gorirat",
        "japanese_name": "ゴリランダー",
        "dexNo": "49"
    },
    {
        "id": "50",
        "name_kor": "비나이트", 
        "description_kor": "퀸비나을 충실히 따르는 하인. 여왕에게 해를 끼치는 자를 철저히 배제한다. 끝내 자폭을 해서라도 여왕을 지켜낸다.",
        "elements": "풀속성",
        "partnerSkill_name": "일벌",
        "partnerSkill_describe": "가축 목장에 배치하면 벌꿀을 떨어뜨리기도 한다. 보유하고 있는 동안 퀸비나의 스테이터스가 상승한다.",
        "partnerSkill_needItem": "",
        "partnerSkill_needItemTechLevel": "0",
        "partnerSkill_levels": "Lv1: 공격 +12%/방어 +12%, Lv2: 공격 +13%/방어 +13%, Lv3: 공격 +15%/방어 +15%, Lv4: 공격 +19%/방어 +19%, Lv5: 공격 +24%/방어 +24%",
        "partnerSkill_ranchDrop": "벌꿀",
        "rarity": "4",
        "size": "M",
        "hp_base": "80",
        "hp_level1": "",
        "hp_level60": "3425-4205",
        "melee_attack": "100",
        "shot_attack": "90",
        "defense": "90",
        "defense_level60": "488-620",
        "attack_level60": "538-670",
        "support": "100",
        "work_speed": "100",
        "food_amount": "3",
        "stamina": "100",
        "walk_speed": "250",
        "run_speed": "450",
        "ride_sprint_speed": "550",
        "transport_speed": "350",
        "work_suitability": "파종1, 수작업1, 채집1, 벌목1, 제약1, 운반2, 목장1",
        "element_weaknesses": "",
        "passiveSkill_names": "",
        "passiveSkill_ranks": "",
        "active_skills": "공기 대포(무속성,25위력), 바람의 칼날(풀속성,30위력), 바늘 창(풀속성,55위력,전용), 벌의 침묵(풀속성,250위력,전용), 독 사격(어둠속성,30위력), 산성비(물속성,80위력), 초록 폭풍(풀속성,80위력), 태양 폭발(풀속성,150위력)",
        "drop_items": "벌꿀 x1-2 (100%)",
        "habitats": "시냇물 동굴",
        "breeding_rank": "1070",
        "price": "1880",
        "egg_type": "신록의 알",
        "english_name": "Beegarde",
        "japanese_name": "ビーガード",
        "dexNo": "50"
    },
    {
        "id": "51",
        "name_kor": "퀸비나",
        "description_kor": "비나이트을 총괄하는 선택받은 여왕. 위대한 여왕을 위해 일한다는 기쁨으로 죽을 때까지 일하는 하인이 끊이지 않는다.",
        "elements": "풀속성",
        "partnerSkill_name": "여왕벌의 통솔",
        "partnerSkill_describe": "함께 싸우는 동안 보유하고 있는 비나이트의 개체수가 많을수록 스테이터스가 상승한다.",
        "partnerSkill_needItem": "",
        "partnerSkill_needItemTechLevel": "0",
        "partnerSkill_levels": "Lv2: 공격 +5%, Lv3: 공격 +6%, Lv4: 공격 +7%, Lv5: 공격 +8%",
        "partnerSkill_ranchDrop": "",
        "rarity": "8",
        "size": "L",
        "hp_base": "90",
        "hp_level1": "",
        "hp_level60": "3750-4627",
        "melee_attack": "100",
        "shot_attack": "105",
        "defense": "100",
        "defense_level60": "537-683",
        "attack_level60": "611-765",
        "support": "100",
        "work_speed": "100",
        "food_amount": "7",
        "stamina": "100",
        "walk_speed": "250",
        "run_speed": "450",
        "ride_sprint_speed": "550",
        "transport_speed": "350",
        "work_suitability": "파종2, 수작업2, 채집2, 벌목1, 제약2",
        "element_weaknesses": "",
        "passiveSkill_names": "",
        "passiveSkill_ranks": "",
        "active_skills": "공기 대포(무속성,25위력), 바람의 칼날(풀속성,30위력), 독 사격(어둠속성,30위력), 스피닝 스태프(풀속성,70위력,전용), 초록 폭풍(풀속성,80위력), 가시덩굴(풀속성,95위력), 태양 폭발(풀속성,150위력)",
        "drop_items": "벌꿀 x5 (100%), 퀸비나의 지팡이 x1 (3%)",
        "habitats": "숲 지역",
        "breeding_rank": "330",
        "price": "6830",
        "egg_type": "신록의 거대한 알",
        "english_name": "Elizabee",
        "japanese_name": "エリザビー",
        "dexNo": "51"
    }
]

# 새로운 팰들을 기존 데이터에 추가
all_data = existing_data + new_pals

# CSV 파일 저장
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)

print(f"✅ 완료! {output_file} 저장됨")
print(f"총 {len(all_data)}개 팰")
print(f"- 기존 1-42번: {len(existing_data)}개")
print(f"- 새로 추가 43,49,50,51번: {len(new_pals)}개")
print(f"컬럼 수: {len(fieldnames)}") 