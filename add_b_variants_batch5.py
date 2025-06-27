#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Batch 5: 4개 새로운 B variants 추가 스크립트
46B 얼서니, 48B 산도로, 49B 고릴가이아, 55B 천도뇽
"""

import csv
import json

def main():
    input_file = "enhanced_complete_pals_batch4_final.csv"
    output_file = "enhanced_complete_pals_batch5.csv"
    
    # 새로운 4개 B variants 완전 데이터
    new_b_variants = [
        {
            "id": "46B",
            "name_kor": "얼서니",
            "name_eng": "Loupmoon_Cryst",
            "description_kor": "머리의 뿔은 절대 녹지 않는 신비한 얼음. 뿔을 부러뜨려 빙수를 만들면 엄청난 별미가 된다고 하지만 먹은 본인도 얼서니도 머리가 띵할 만큼 아파진다.",
            "elements": "얼음",
            "stats_rarity": 3,
            "stats_health": 80,
            "stats_food": 350,
            "stats_attack": 105,
            "stats_defense": 80,
            "stats_support": 100,
            "stats_melee_attack": 130,
            "stats_shot_attack": 105,
            "stats_craft_speed": 100,
            "stats_capture_rate": 1,
            "stats_exp_ratio": 1,
            "partner_skill": "냉기로 번쩍이는 발톱날",
            "partner_skill_desc": "발동하면 목표로 삼은 적을 향해 높은 위력의 옥설 발톱으로 공격한다.",
            "work_suitability": "수작업 Lv2, 냉각 Lv3",
            "work_type": "수작업,냉각",
            "work_level": "2,3",
            "food_amount": 5,
            "size": "M",
            "male_probability": 50,
            "combi_rank": 805,
            "gold_coin": 2820,
            "egg_type": "얼어붙은 알",
            "slow_walk_speed": 100,
            "walk_speed": 175,
            "run_speed": 600,
            "ride_sprint_speed": 800,
            "transport_speed": 375,
            "level_60_hp": "3425 – 4205",
            "level_60_attack": "611 – 765", 
            "level_60_defense": "440 – 557",
            "active_skills": json.dumps([
                {"level": 1, "name": "얼음 미사일", "element": "얼음", "cooltime": 3, "power": 30, "description": "하늘에 뾰족한 얼음을 생성한 뒤 적을 향해 그 얼음을 발사한다."},
                {"level": 7, "name": "얼음 칼날", "element": "얼음", "cooltime": 10, "power": 55, "description": "초승달 모양의 얼음 날을 만들어 전방으로 발사한다."},
                {"level": 15, "name": "옥설 발톱", "element": "얼음", "cooltime": 7, "power": 55, "description": "얼서니 전용 스킬. 전방으로 뛰어오르며 재빨리 2회 할퀸다."},
                {"level": 22, "name": "얼음 칼날", "element": "얼음", "cooltime": 10, "power": 55, "description": "초승달 모양의 얼음 날을 만들어 전방으로 발사한다."},
                {"level": 30, "name": "아이시클 불릿", "element": "얼음", "cooltime": 35, "power": 110, "description": "하늘에 뾰족한 얼음을 여러 개 생성한 뒤 적을 향해 발사한다."},
                {"level": 40, "name": "아이시클 라인", "element": "얼음", "cooltime": 40, "power": 120, "description": "일직선으로 나아가는 얼음 기둥을 3방향으로 생성한다."},
                {"level": 50, "name": "눈보라 스파이크", "element": "얼음", "cooltime": 45, "power": 130, "description": "거대한 얼음 덩어리를 만들어 적을 향해 빠르게 발사한다."}
            ], ensure_ascii=False),
            "possible_drops": "뼈 1개 (100%)",
            "spawner_locations": "야미지마 7-2 다크 에리어 (레벨 52-55), 천락의 동굴 (레벨 56-58)",
            "breeding_combo": "달서니 + 모프킹 = 얼서니"
        },
        {
            "id": "48B", 
            "name_kor": "산도로",
            "name_eng": "Robinquill_Terra",
            "description_kor": "바위투성이인 곳에서 수렵 생활을 하며, 사람과 성질이 아주 비슷한 팰. 유적에서 산도로의 뼈가 발견된다면 사람의 뼈 또한 반드시 출토된다.",
            "elements": "풀,땅",
            "stats_rarity": 6,
            "stats_health": 90,
            "stats_food": 225,
            "stats_attack": 105,
            "stats_defense": 80,
            "stats_support": 100,
            "stats_melee_attack": 100,
            "stats_shot_attack": 105,
            "stats_craft_speed": 100,
            "stats_capture_rate": 1,
            "stats_exp_ratio": 1,
            "partner_skill": "매의 눈",
            "partner_skill_desc": "함께 싸우는 동안 플레이어가 약점 부위에 주는 피해량이 증가한다.",
            "work_suitability": "수작업 Lv2, 채집 Lv2, 벌목 Lv1, 제약 Lv1, 운반 Lv2",
            "work_type": "수작업,채집,벌목,제약,운반",
            "work_level": "2,2,1,1,2",
            "food_amount": 3,
            "size": "M",
            "male_probability": 50,
            "combi_rank": 1000,
            "gold_coin": 2150,
            "egg_type": "신록의 대형 알",
            "slow_walk_speed": 100,
            "walk_speed": 100,
            "run_speed": 600,
            "ride_sprint_speed": 750,
            "transport_speed": 400,
            "level_60_hp": "3750 – 4627",
            "level_60_attack": "611 – 765",
            "level_60_defense": "440 – 557",
            "active_skills": json.dumps([
                {"level": 1, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40, "description": "끈적거리는 진흙을 적을 향해 발사한다."},
                {"level": 7, "name": "바람의 칼날", "element": "풀", "cooltime": 2, "power": 30, "description": "적을 향해 일직선으로 날아가는 초고속 바람의 칼날을 발사한다."},
                {"level": 15, "name": "스나이핑 샷", "element": "풀", "cooltime": 9, "power": 65, "description": "로빈몽 종의 전용 스킬. 활시위를 당겨 목표를 정한 뒤 적에게 사격을 감행한다."},
                {"level": 22, "name": "바위 폭발", "element": "땅", "cooltime": 10, "power": 55, "description": "작은 돌멩이들을 무수히 끌어모아 전방으로 발사한다."},
                {"level": 30, "name": "모래 폭풍", "element": "땅", "cooltime": 18, "power": 80, "description": "좌우에 모래 회오리를 일으켜 적에게 날린다."},
                {"level": 40, "name": "태양 폭발", "element": "풀", "cooltime": 55, "power": 150, "description": "태양의 힘을 모아 적을 향해 강력한 광선을 발사한다."},
                {"level": 50, "name": "바위 창", "element": "땅", "cooltime": 55, "power": 150, "description": "적의 발 밑에 날카로운 바위 창을 불러낸다."}
            ], ensure_ascii=False),
            "possible_drops": "밀 씨 1-2개 (50%), 화살 2-4개 (100%), 감자 종자 1개 (50%)",
            "spawner_locations": "사막 지역 (레벨 28-32), 모래 언덕 동굴 (레벨 33-40)",
            "breeding_combo": "로빈몽 + 두더비 = 산도로"
        },
        {
            "id": "49B",
            "name_kor": "고릴가이아",
            "name_eng": "Gorirat_Terra", 
            "description_kor": "지면을 때리는 리듬으로 동료와 의사소통을 한다. 고릴레이지의 팔 힘은 무척 세서 만일 고릴가이아 전원이 동시에 지면을 두들기면 팰파고스섬이 1초만에 가라앉는다.",
            "elements": "땅",
            "stats_rarity": 5,
            "stats_health": 90,
            "stats_food": 225,
            "stats_attack": 100,
            "stats_defense": 90,
            "stats_support": 100,
            "stats_melee_attack": 110,
            "stats_shot_attack": 100,
            "stats_craft_speed": 100,
            "stats_capture_rate": 1,
            "stats_exp_ratio": 1,
            "partner_skill": "풀 파워 고릴라 모드",
            "partner_skill_desc": "발동하면 야성의 힘을 해방해 일정 시간 고릴가이아의 공격력이 증가한다.",
            "work_suitability": "수작업 Lv1, 채굴 Lv2, 운반 Lv3",
            "work_type": "수작업,채굴,운반",
            "work_level": "1,2,3",
            "food_amount": 3,
            "size": "S",
            "male_probability": 50,
            "combi_rank": 1030,
            "gold_coin": 4020,
            "egg_type": "거친 느낌의 대형 알",
            "slow_walk_speed": 66,
            "walk_speed": 100,
            "run_speed": 550,
            "ride_sprint_speed": 720,
            "transport_speed": 250,
            "level_60_hp": "3750 – 4627",
            "level_60_attack": "587 – 733",
            "level_60_defense": "488 – 620",
            "active_skills": json.dumps([
                {"level": 1, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35, "description": "에너지를 모아 탄환 형태로 발사한다."},
                {"level": 7, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40, "description": "끈적거리는 진흙을 적을 향해 발사한다."},
                {"level": 15, "name": "바위 폭발", "element": "땅", "cooltime": 10, "power": 55, "description": "작은 돌멩이들을 무수히 끌어모아 전방으로 발사한다."},
                {"level": 22, "name": "바위 대포", "element": "땅", "cooltime": 15, "power": 70, "description": "바로 앞 지면에서 바위를 뽑아 적을 향해 발사한다."},
                {"level": 30, "name": "고릴라운드 콤보", "element": "무", "cooltime": 14, "power": 85, "description": "고릴레이지 전용 스킬. 지면을 2번 내리친 뒤 번쩍 뛰어올라 마지막에 강력한 펀치를 날린다."},
                {"level": 40, "name": "암석 폭발", "element": "땅", "cooltime": 35, "power": 130, "description": "지면을 뒤흔들며 주위에 거대한 암석 덩어리를 흩날린다."},
                {"level": 50, "name": "바위 창", "element": "땅", "cooltime": 55, "power": 150, "description": "적의 발 밑에 날카로운 바위 창을 불러낸다."}
            ], ensure_ascii=False),
            "possible_drops": "금속 광석 2-3개 (100%), 뼈 1개 (100%)",
            "spawner_locations": "사쿠라지마 6-5 남부 사막 (레벨 42-46), 벚꽃 동굴 (레벨 40-52)",
            "breeding_combo": "고릴레이지 + 꼬마딜로 = 고릴가이아"
        },
        {
            "id": "55B",
            "name_kor": "천도뇽",
            "name_eng": "Chillet_Ignis",
            "description_kor": "몸을 둥글게 말아 불꽃을 뿌리며 회전 이동할 수 있다. 흥분했을 때도 불꽃을 뿌린다. 너무 많이 쓰다듬으면 불타오른다.",
            "elements": "화염,용",
            "stats_rarity": 5,
            "stats_health": 90,
            "stats_food": 225,
            "stats_attack": 85,
            "stats_defense": 80,
            "stats_support": 100,
            "stats_melee_attack": 100,
            "stats_shot_attack": 85,
            "stats_craft_speed": 100,
            "stats_capture_rate": 1,
            "stats_exp_ratio": 1,
            "partner_skill": "타닥타닥 족제비",
            "partner_skill_desc": "등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 화염 속성으로 변화한다.",
            "work_suitability": "불 피우기 Lv2, 채집 Lv1",
            "work_type": "불 피우기,채집",
            "work_level": "2,1",
            "food_amount": 3,
            "size": "M",
            "male_probability": 50,
            "combi_rank": 790,
            "gold_coin": 4450,
            "egg_type": "열기 나는 대형 알",
            "slow_walk_speed": 100,
            "walk_speed": 180,
            "run_speed": 750,
            "ride_sprint_speed": 1050,
            "transport_speed": 390,
            "level_60_hp": "3750 – 4627",
            "level_60_attack": "514 – 638",
            "level_60_defense": "440 – 557",
            "active_skills": json.dumps([
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30, "description": "적을 향해 일직선으로 날아가는 화염 탄환을 발사한다."},
                {"level": 7, "name": "용의 파장", "element": "용", "cooltime": 10, "power": 55, "description": "재빨리 용의 힘을 방출하여 주위에 충격을 준다."},
                {"level": 15, "name": "불화살", "element": "화염", "cooltime": 10, "power": 55, "description": "적을 뒤쫓는 고속 불화살을 3발 연속으로 쏜다."},
                {"level": 22, "name": "파이어 브레스", "element": "화염", "cooltime": 15, "power": 70, "description": "적을 향해 화염을 방출해 지속 피해를 준다."},
                {"level": 30, "name": "로켓 태클", "element": "용", "cooltime": 6, "power": 50, "description": "베비뇽 종의 전용 스킬. 잠시 힘을 모은 후 전방으로 돌진한다."},
                {"level": 40, "name": "화염 장벽", "element": "화염", "cooltime": 30, "power": 100, "description": "적이 있는 지점에 타오르는 화염 벽을 생성한다."},
                {"level": 50, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150, "description": "머리 위에 거대한 화염구를 소환해 적을 향해 날린다."}
            ], ensure_ascii=False),
            "possible_drops": "가죽 2-3개 (100%), 발화 기관 1-2개 (100%)",
            "spawner_locations": "사쿠라지마 6-2 벚꽃 지역 (레벨 42-46), 벚꽃 동굴 (레벨 40-52)",
            "breeding_combo": "베비뇽 + 불페르노 = 천도뇽"
        }
    ]
    
    # CSV 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # 헤더 확인
    header = rows[0]
    print(f"CSV 헤더: {header}")
    
    # 새로운 행들 생성
    new_rows = []
    for variant in new_b_variants:
        row = []
        # 모든 필드를 순서대로 추가
        for field in header:
            if field == "id":
                row.append(variant["id"])
            elif field == "name_kor":
                row.append(variant["name_kor"])
            elif field == "name_eng":
                row.append(variant["name_eng"])
            elif field == "description_kor":
                row.append(variant["description_kor"])
            elif field == "elements":
                row.append(variant["elements"])
            elif field == "partner_skill":
                row.append(variant["partner_skill"])
            elif field == "partner_skill_desc":
                row.append(variant["partner_skill_desc"])
            elif field == "work_type":
                row.append(variant["work_type"])
            elif field == "stats_rarity":
                row.append(variant["stats_rarity"])
            elif field == "stats_health":
                row.append(variant["stats_health"])
            elif field == "stats_food":
                row.append(variant["stats_food"])
            elif field == "stats_attack":
                row.append(variant["stats_attack"])
            elif field == "stats_defense":
                row.append(variant["stats_defense"])
            elif field == "stats_support":
                row.append(variant["stats_support"])
            elif field == "stats_melee_attack":
                row.append(variant["stats_melee_attack"])
            elif field == "stats_shot_attack":
                row.append(variant["stats_shot_attack"])
            elif field == "stats_craft_speed":
                row.append(variant["stats_craft_speed"])
            elif field == "stats_capture_rate":
                row.append(variant["stats_capture_rate"])
            elif field == "stats_exp_ratio":
                row.append(variant["stats_exp_ratio"])
            elif field == "food_amount":
                row.append(variant["food_amount"])
            elif field == "size":
                row.append(variant["size"])
            elif field == "male_probability":
                row.append(variant["male_probability"])
            elif field == "combi_rank":
                row.append(variant["combi_rank"])
            elif field == "gold_coin":
                row.append(variant["gold_coin"])
            elif field == "egg_type":
                row.append(variant["egg_type"])
            elif field == "slow_walk_speed":
                row.append(variant["slow_walk_speed"])
            elif field == "walk_speed":
                row.append(variant["walk_speed"])
            elif field == "run_speed":
                row.append(variant["run_speed"])
            elif field == "ride_sprint_speed":
                row.append(variant["ride_sprint_speed"])
            elif field == "transport_speed":
                row.append(variant["transport_speed"])
            elif field == "level_60_hp":
                row.append(variant["level_60_hp"])
            elif field == "level_60_attack":
                row.append(variant["level_60_attack"])
            elif field == "level_60_defense":
                row.append(variant["level_60_defense"])
            elif field == "active_skills":
                row.append(variant["active_skills"])
            elif field == "possible_drops":
                row.append(variant["possible_drops"])
            elif field == "spawner_locations":
                row.append(variant["spawner_locations"])
            elif field == "breeding_combo":
                row.append(variant["breeding_combo"])
            elif field == "work_suitability":
                row.append(variant["work_suitability"])
            elif field == "work_level":
                row.append(variant["work_level"])
            else:
                row.append("")  # 빈 값으로 채움
        
        new_rows.append(row)
    
    # 새로운 행들을 추가
    all_rows = rows + new_rows
    
    # CSV 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(all_rows)
    
    print(f"✅ Batch 5 완료!")
    print(f"📁 파일: {output_file}")
    print(f"📊 추가된 B variants: {len(new_b_variants)}개")
    print("🎯 새로운 아종들:")
    for variant in new_b_variants:
        print(f"   - {variant['id']} {variant['name_kor']} ({variant['elements']})")

if __name__ == "__main__":
    main() 