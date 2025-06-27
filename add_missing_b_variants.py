#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
누락된 3개 B variants 추가 스크립트 (31B, 32B, 33B)
완전한 데이터와 함께 기존 CSV에 추가합니다.
"""

import csv
import json

def main():
    input_file = "enhanced_complete_pals_batch4_fixed.csv"
    output_file = "enhanced_complete_pals_batch4_final.csv"
    
    # 누락된 3개 B variants 완전 데이터
    missing_b_variants = [
        {
            "id": "31B",
            "name_kor": "샤맨더",
            "name_eng": "Gobfin_Ignis",
            "description_kor": "먼 옛날엔 거대하고 강력한 수생 팰이었지만 먹이가 적어지며 지상으로 나왔다. 걷는 데 상당한 칼로리를 연소한 결과 화염의 힘에 눈뜨게 됐다!",
            "elements": "화염",
            "stats_rarity": 3,
            "stats_health": 90,
            "stats_food": 225,
            "stats_attack": 90,
            "stats_defense": 75,
            "stats_workSpeed": 100,
            "partnerSkill_name": "삐돌이 상어",
            "partnerSkill_describe": "발동하면 목표로 삼은 적을 향해 높은 위력의 스피릿 파이어로 공격한다. 보유하고 있는 동안 플레이어의 공격력이 증가한다.",
            "workSuitabilities": "불 피우기:2,수작업:1,운반:1",
            "movement_slowWalkSpeed": 50,
            "movement_walkSpeed": 80,
            "movement_runSpeed": 400,
            "movement_rideSprintSpeed": 500,
            "movement_transportSpeed": 120,
            "level60_health": "3750 – 4627",
            "level60_attack": "538 – 670",
            "level60_defense": "415 – 525",
            "stats_egg": "열기 나는 알",
            "stats_goldCoin": 1800,
            "stats_combiRank": 1100,
            "activeSkills": json.dumps([
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30},
                {"level": 7, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 15, "name": "스피릿 파이어", "element": "화염", "cooltime": 7, "power": 45},
                {"level": 22, "name": "불화살", "element": "화염", "cooltime": 10, "power": 55},
                {"level": 30, "name": "라인 썬더", "element": "번개", "cooltime": 16, "power": 75},
                {"level": 40, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150},
                {"level": 50, "name": "인페르노", "element": "화염", "cooltime": 40, "power": 120}
            ]),
            "drops": "발화 기관 x1 (100%)",
            "spawners": "Lv. 23–28 3_2_volcano_1 | Lv. 32–35 모래 언덕 동굴"
        },
        {
            "id": "32B",
            "name_kor": "유령건다리",
            "name_eng": "Hangyu_Cryst",
            "description_kor": "얼음덩어리도 찢어버릴 만큼 거대한 팔이 특징. 대역죄인을 마을 광장에 결박하여 유령건다리의 힘으로 머리채를 쥐어뜯어버리는 잔혹한 형벌이 시행됐던 적도 있다.",
            "elements": "얼음",
            "stats_rarity": 2,
            "stats_health": 80,
            "stats_food": 150,
            "stats_attack": 80,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "partnerSkill_name": "겨울 하늘 그네",
            "partnerSkill_describe": "보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 천천히 상승 기류를 탈 수 있다.",
            "workSuitabilities": "수작업:1,채집:1,냉각:1,운반:2",
            "movement_slowWalkSpeed": 50,
            "movement_walkSpeed": 100,
            "movement_runSpeed": 400,
            "movement_rideSprintSpeed": 550,
            "movement_transportSpeed": 250,
            "level60_health": "3425 – 4205",
            "level60_attack": "490 – 607",
            "level60_defense": "391 – 493",
            "stats_egg": "얼어붙은 알",
            "stats_goldCoin": 1020,
            "stats_combiRank": 1422,
            "activeSkills": json.dumps([
                {"level": 1, "name": "공기 대포", "element": "무", "cooltime": 2, "power": 25},
                {"level": 7, "name": "얼음 미사일", "element": "얼음", "cooltime": 3, "power": 30},
                {"level": 15, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 22, "name": "얼음 칼날", "element": "얼음", "cooltime": 10, "power": 55},
                {"level": 30, "name": "빙산", "element": "얼음", "cooltime": 15, "power": 70},
                {"level": 40, "name": "서리 낀 입김", "element": "얼음", "cooltime": 22, "power": 90},
                {"level": 50, "name": "눈보라 스파이크", "element": "얼음", "cooltime": 45, "power": 130}
            ]),
            "drops": "섬유 x5–10 (100%) | 빙결 기관 x1 (100%)",
            "spawners": "Lv. 33–35 snow_5_1_snow_1 | Lv. 33–35 snow_5_2_SnowGrass"
        },
        {
            "id": "33B",
            "name_kor": "썬더판다",
            "name_eng": "Mossanda_Lux",
            "description_kor": "믿기 힘든 괴력의 소유자. 전기를 신호로 바꿔 신체 능력의 한계를 돌파했다. 최강 생물이 화제에 오르면 절대 빠지지 않는다.",
            "elements": "번개",
            "stats_rarity": 7,
            "stats_health": 100,
            "stats_food": 350,
            "stats_attack": 100,
            "stats_defense": 100,
            "stats_workSpeed": 100,
            "partnerSkill_name": "척탄 판다",
            "partnerSkill_describe": "등에 타고 이동할 수 있다. 탑승 중 수류탄 발사기 연사가 가능해진다.",
            "workSuitabilities": "발전:2,수작업:2,벌목:2,운반:3",
            "movement_slowWalkSpeed": 50,
            "movement_walkSpeed": 100,
            "movement_runSpeed": 600,
            "movement_rideSprintSpeed": 1000,
            "movement_transportSpeed": 275,
            "level60_health": "4075 – 5050",
            "level60_attack": "587 – 733",
            "level60_defense": "537 – 683",
            "stats_egg": "찌릿찌릿한 대형 알",
            "stats_goldCoin": 6610,
            "stats_combiRank": 390,
            "activeSkills": json.dumps([
                {"level": 1, "name": "스파크 샷", "element": "번개", "cooltime": 2, "power": 30},
                {"level": 7, "name": "전기 파장", "element": "번개", "cooltime": 4, "power": 40},
                {"level": 15, "name": "라인 썬더", "element": "번개", "cooltime": 16, "power": 75},
                {"level": 22, "name": "폭발 펀치", "element": "번개", "cooltime": 14, "power": 85},
                {"level": 30, "name": "트라이 썬더", "element": "번개", "cooltime": 22, "power": 90},
                {"level": 40, "name": "번개 일격", "element": "번개", "cooltime": 40, "power": 120},
                {"level": 50, "name": "전기 볼트", "element": "번개", "cooltime": 55, "power": 150}
            ]),
            "drops": "버섯 x2–3 (100%) | 발전 기관 x1–2 (100%) | 가죽 x2–3 (100%)",
            "spawners": "Lv. 35–37 화산 동굴"
        }
    ]
    
    print("🔄 기존 CSV 파일 읽는 중...")
    
    # 기존 데이터 읽기
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []
        existing_data = list(reader)
    
    print(f"📊 기존 데이터: {len(existing_data)}개 팰")
    
    # 누락된 B variants를 정확한 위치에 삽입 (31B는 23B 뒤에, 32B는 그 뒤에, 33B는 그 뒤에)
    insert_positions = []
    
    # 23B 위치 찾기
    for i, row in enumerate(existing_data):
        if row.get('id') == '23B':
            insert_positions.append(i + 1)  # 23B 뒤에
            break
    
    # 역순으로 삽입 (뒤에서부터 삽입해야 인덱스가 꼬이지 않음)
    for i, variant in enumerate(reversed(missing_b_variants)):
        if insert_positions:
            pos = insert_positions[0] + (2 - i)  # 33B, 32B, 31B 순으로 삽입
            new_row = {}
            for field in fieldnames:
                new_row[field] = variant.get(field, "")
            
            existing_data.insert(pos, new_row)
            print(f"✅ 삽입됨: {variant['id']} {variant['name_kor']} ({variant['name_eng']}) at position {pos}")
    
    # 새 CSV 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"\n🎉 완료! 총 {len(existing_data)}개 팰이 {output_file}에 저장되었습니다.")
    print(f"📈 추가된 B variants: {len(missing_b_variants)}개")
    
    # 통계 출력
    b_variants_count = sum(1 for row in existing_data if row.get('id', '').endswith('B'))
    print(f"📊 총 B variants: {b_variants_count}개")
    print(f"🎯 아종 완성도: {b_variants_count}/59 = {(b_variants_count/59)*100:.1f}%")

if __name__ == "__main__":
    main() 