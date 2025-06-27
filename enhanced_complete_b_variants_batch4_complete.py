#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
팰월드 B variants 완전 데이터 추가 스크립트 - Batch 4 (Complete Version)
8개의 새로운 B variants를 완전한 데이터와 함께 기존 CSV에 추가합니다.
크롤링한 완전한 정보를 바탕으로 모든 필수 필드를 포함합니다.
"""

import csv
import json

def main():
    # 기존 CSV 파일 경로
    input_file = "enhanced_complete_pals_batch3.csv"
    output_file = "enhanced_complete_pals_batch4_complete.csv"
    
    # 새로운 B variants 완전 데이터
    new_b_variants = [
        {
            # 23B 드리문 (Killamari_Primo)
            "id": "23B",
            "name_kor": "드리문",
            "name_eng": "Killamari_Primo",
            "description_kor": "적의 목을 물어 혈액을 모조리 빨아들인다. 드리문 끼리 물고 물렸을 경우에는 양쪽 모두 빨아들이는 것에만 집착하기 때문에 어느 한 쪽이 말라버릴 때까지 멈추지 않는다.",
            "elements": "무+물",
            "stats_rarity": 2,
            "stats_size": "XS",
            "stats_health": 70,
            "stats_food": 225,
            "stats_attack": 60,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 1250,
            "stats_goldCoin": 1440,
            "stats_egg": "평범한 알",
            "stats_code": "NegativeOctopus_Neutral",
            "movement_slowWalkSpeed": 60,
            "movement_walkSpeed": 120,
            "movement_runSpeed": 400,
            "movement_rideSprintSpeed": 550,
            "movement_transportSpeed": 260,
            "level60_health": "3100 – 3782",
            "level60_attack": "392 – 480", 
            "level60_defense": "391 – 493",
            "partnerSkill_name": "꿈튀김",
            "partnerSkill_describe": "보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 느린 속도로 장시간 이동이 가능해진다.",
            "partnerSkill_needItem": "기술23",
            "partnerSkill_needItemTechLevel": 23,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "공기 대포", "element": "무", "cooltime": 2, "power": 25},
                {"level": 7, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 15, "name": "버블 샷", "element": "물", "cooltime": 13, "power": 65},
                {"level": 22, "name": "파워 폭탄", "element": "무", "cooltime": 15, "power": 70},
                {"level": 30, "name": "산성비", "element": "물", "cooltime": 18, "power": 80},
                {"level": 40, "name": "고압수 발사", "element": "물", "cooltime": 35, "power": 110},
                {"level": 50, "name": "하이드로 스트림", "element": "물", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "관개:1,채집:1,운반:2",
            "workSuitabilities_count": 3,
            "drops": "팰의 체액 x1–2 (100%) | 고스문의 촉수 x1 (50%)",
            "drops_count": 2,
            "tribes": "진짜 어떤 감정도 없는 드리문 (Tribe Boss) | 드리문 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 42–44 ??? | Lv. 16–27 커다란 낚시터 Medium 9.34%",
            "spawners_count": 2
        },
        {
            # 24B 칠테트 (Mau_Cryst)
            "id": "24B", 
            "name_kor": "칠테트",
            "name_eng": "Mau_Cryst",
            "description_kor": "꼬리의 결정은 아름답지만 죽기 무섭게 망가져 버린다. 많이 키우면 재물을 불러온다고 해 다들 칠테트를 애지중지 키웠다.",
            "elements": "얼음",
            "stats_rarity": 2,
            "stats_size": "XS",
            "stats_health": 70,
            "stats_food": 100,
            "stats_attack": 65,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 1440,
            "stats_goldCoin": 1010,
            "stats_egg": "얼어붙은 알",
            "stats_code": "Bastet_Ice",
            "movement_slowWalkSpeed": 52,
            "movement_walkSpeed": 105,
            "movement_runSpeed": 475,
            "movement_rideSprintSpeed": 550,
            "movement_transportSpeed": 317,
            "level60_health": "3100 – 3782",
            "level60_attack": "416 – 511",
            "level60_defense": "391 – 493",
            "partnerSkill_name": "금화 수집",
            "partnerSkill_describe": "가축 목장에 배치하면 지면에서 금화를 파내기도 한다.",
            "partnerSkill_needItem": "",
            "partnerSkill_needItemTechLevel": 0,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "얼음 미사일", "element": "얼음", "cooltime": 3, "power": 30},
                {"level": 7, "name": "공기 대포", "element": "무", "cooltime": 2, "power": 25},
                {"level": 15, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40},
                {"level": 22, "name": "얼음 칼날", "element": "얼음", "cooltime": 10, "power": 55},
                {"level": 30, "name": "빙산", "element": "얼음", "cooltime": 15, "power": 70},
                {"level": 40, "name": "서리 낀 입김", "element": "얼음", "cooltime": 22, "power": 90},
                {"level": 50, "name": "눈보라 스파이크", "element": "얼음", "cooltime": 45, "power": 130}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "냉각:1,목장:1",
            "workSuitabilities_count": 2,
            "drops": "빙결 기관 x1–2 (100%) | 사파이어 x1 (1%)",
            "drops_count": 2,
            "tribes": "청명한 광채의 칠테트 (Tribe Boss) | 칠테트 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 30–34 snow_5_1_snow_1 | Lv. 39–41 영봉의 동굴",
            "spawners_count": 2
        },
        {
            # 25B 일레카이트 (Celaray_Lux)
            "id": "25B",
            "name_kor": "일레카이트", 
            "name_eng": "Celaray_Lux",
            "description_kor": "무늬가 화려할수록 파트너의 이목을 끌 수 있다고 한다. 역사적으로 일레카이트에게 감전된 사례는 끊이지 않으며 현재에 이르러 섬 내에서 노랑과 검은 줄무늬는 위험한 색으로 인식되고 있다.",
            "elements": "물+번개",
            "stats_rarity": 4,
            "stats_size": "M",
            "stats_health": 80,
            "stats_food": 225,
            "stats_attack": 75,
            "stats_defense": 80,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1.1,
            "stats_maleProbability": 50,
            "stats_combiRank": 830,
            "stats_goldCoin": 3430,
            "stats_egg": "축축한 알",
            "stats_code": "FlyingManta_Thunder",
            "movement_slowWalkSpeed": 30,
            "movement_walkSpeed": 150,
            "movement_runSpeed": 550,
            "movement_rideSprintSpeed": 700,
            "movement_transportSpeed": 350,
            "level60_health": "3425 – 4205",
            "level60_attack": "465 – 575",
            "level60_defense": "440 – 557",
            "partnerSkill_name": "짜릿바람 글라이더",
            "partnerSkill_describe": "보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 빠른 속도로 장시간 이동이 가능해진다.",
            "partnerSkill_needItem": "기술26",
            "partnerSkill_needItemTechLevel": 26,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "번개 창", "element": "번개", "cooltime": 2, "power": 30},
                {"level": 7, "name": "전기 파장", "element": "번개", "cooltime": 4, "power": 40},
                {"level": 15, "name": "버블 샷", "element": "물", "cooltime": 13, "power": 65},
                {"level": 22, "name": "라인 썬더", "element": "번개", "cooltime": 16, "power": 75},
                {"level": 30, "name": "라인 스플래시", "element": "물", "cooltime": 22, "power": 90},
                {"level": 40, "name": "고압수 발사", "element": "물", "cooltime": 35, "power": 110},
                {"level": 50, "name": "전기 볼트", "element": "번개", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "관개:1,발전:1,운반:1",
            "workSuitabilities_count": 3,
            "drops": "팰의 체액 x1–2 (100%)",
            "drops_count": 1,
            "tribes": "하늘을 울리는 물고기 일레카이트 (Tribe Boss) | 일레카이트 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 16–27 커다란 낚시터 Medium 12.45%",
            "spawners_count": 1
        },
        {
            # 35B 베노고트 (Caprity_Noct)
            "id": "35B",
            "name_kor": "베노고트",
            "name_eng": "Caprity_Noct", 
            "description_kor": "정신 상태에 따라 등의 덤불에 맺히는 열매의 맛이 변화한다. 악랄한 환경 속에서 자랄수록 맛이 달게 변하기에 사육당하는 대부분의 베노고트는 사랑을 배우지 못했다.",
            "elements": "어둠",
            "stats_rarity": 3,
            "stats_size": "S",
            "stats_health": 100,
            "stats_food": 300,
            "stats_attack": 75,
            "stats_defense": 90,
            "stats_workSpeed": 100,
            "stats_support": 120,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 855,
            "stats_goldCoin": 3080,
            "stats_egg": "암흑의 알",
            "stats_code": "BerryGoat_Dark",
            "movement_slowWalkSpeed": 70,
            "movement_walkSpeed": 70,
            "movement_runSpeed": 400,
            "movement_rideSprintSpeed": 550,
            "movement_transportSpeed": 235,
            "level60_health": "4075 – 5050",
            "level60_attack": "465 – 575",
            "level60_defense": "488 – 620",
            "partnerSkill_name": "독샘 채집",
            "partnerSkill_describe": "가축 목장에 배치하면 등에서 독샘을 떨어뜨리기도 한다.",
            "partnerSkill_needItem": "",
            "partnerSkill_needItemTechLevel": 0,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "독 안개", "element": "어둠", "cooltime": 30, "power": 0},
                {"level": 7, "name": "바람의 칼날", "element": "풀", "cooltime": 2, "power": 30},
                {"level": 15, "name": "독 사격", "element": "어둠", "cooltime": 2, "power": 30},
                {"level": 22, "name": "멀티 커터", "element": "풀", "cooltime": 12, "power": 60},
                {"level": 30, "name": "포이즌 샤워", "element": "어둠", "cooltime": 22, "power": 90},
                {"level": 40, "name": "원형 덩굴", "element": "풀", "cooltime": 40, "power": 120},
                {"level": 50, "name": "어둠의 레이저", "element": "어둠", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "파종:2,목장:1",
            "workSuitabilities_count": 2,
            "drops": "베리고트 향초 고기 x2 (100%) | 빨간 열매 x2–4 (100%) | 뿔 x1–2 (100%) | 독샘 x1 (100%)",
            "drops_count": 4,
            "tribes": "어두컴컴한 농장 베노고트 (Tribe Boss) | 베노고트 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 50–54 yamijima_7_6_RedArea_North | Lv. 56–58 천락의 동굴",
            "spawners_count": 2
        },
        {
            # 37B 산령사슴 (Eikthyrdeer_Terra)
            "id": "37B",
            "name_kor": "산령사슴",
            "name_eng": "Eikthyrdeer_Terra",
            "description_kor": "뿔이 제일 단단한 개체가 우두머리가 된다. 그리고 뿔을 잃으면 그 자격도 잃게 된다. 모두의 배웅을 받으며 무리를 떠나, 조용히 흙으로 돌아간다.",
            "elements": "땅",
            "stats_rarity": 6,
            "stats_size": "L",
            "stats_health": 95,
            "stats_food": 350,
            "stats_attack": 80,
            "stats_defense": 80,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 900,
            "stats_goldCoin": 2680,
            "stats_egg": "거친 느낌의 대형 알",
            "stats_code": "Deer_Ground",
            "movement_slowWalkSpeed": 80,
            "movement_walkSpeed": 120,
            "movement_runSpeed": 700,
            "movement_rideSprintSpeed": 900,
            "movement_transportSpeed": 390,
            "level60_health": "3912 – 4838",
            "level60_attack": "490 – 607",
            "level60_defense": "440 – 557",
            "partnerSkill_name": "금빛 숲의 수호자",
            "partnerSkill_describe": "등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해지며 나무 파괴 효율이 향상된다.",
            "partnerSkill_needItem": "기술25",
            "partnerSkill_needItemTechLevel": 25,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 7, "name": "들이받기", "element": "무", "cooltime": 5, "power": 50},
                {"level": 15, "name": "바위 폭발", "element": "땅", "cooltime": 10, "power": 55},
                {"level": 22, "name": "바위 대포", "element": "땅", "cooltime": 15, "power": 70},
                {"level": 30, "name": "파워 폭탄", "element": "무", "cooltime": 15, "power": 70},
                {"level": 40, "name": "모래 폭풍", "element": "땅", "cooltime": 18, "power": 80},
                {"level": 50, "name": "바위 창", "element": "땅", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "벌목:2",
            "workSuitabilities_count": 1,
            "drops": "신령사슴의 사슴고기 x2 (100%) | 가죽 x2–3 (100%) | 뿔 x2 (100%)",
            "drops_count": 3,
            "tribes": "황금 뿔 산령사슴 (Tribe Boss) | 산령사슴 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 18–22 제1 사냥 금지 구역",
            "spawners_count": 1
        },
        {
            # 39B 그래토 (Ribbuny_Botan)
            "id": "39B",
            "name_kor": "그래토",
            "name_eng": "Ribbuny_Botan",
            "description_kor": "항상 방긋방긋 웃는 얼굴로 지낸다. 가끔 까부냥의 장난으로 촉수가 묶이기도 한다. 그리고 그럴 때에는 웃는 얼굴로 폭력을 행사한다고 한다.",
            "elements": "풀",
            "stats_rarity": 1,
            "stats_size": "XS",
            "stats_health": 80,
            "stats_food": 150,
            "stats_attack": 65,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 1205,
            "stats_goldCoin": 1620,
            "stats_egg": "신록의 알",
            "stats_code": "PinkRabbit_Grass",
            "movement_slowWalkSpeed": 50,
            "movement_walkSpeed": 100,
            "movement_runSpeed": 245,
            "movement_rideSprintSpeed": 350,
            "movement_transportSpeed": 172,
            "level60_health": "3425 – 4205",
            "level60_attack": "416 – 511",
            "level60_defense": "391 – 493",
            "partnerSkill_name": "풀뜨기 장인",
            "partnerSkill_describe": "보유하고 있는 동안 풀 속성 팰의 공격력이 증가한다. 그래토가 무기 제작대나 무기 공장 등에서 일할 때 작업 효율이 향상된다.",
            "partnerSkill_needItem": "",
            "partnerSkill_needItemTechLevel": 0,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "바람의 칼날", "element": "풀", "cooltime": 2, "power": 30},
                {"level": 7, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40},
                {"level": 15, "name": "씨앗 기관총", "element": "풀", "cooltime": 9, "power": 50},
                {"level": 22, "name": "씨앗 지뢰", "element": "풀", "cooltime": 13, "power": 65},
                {"level": 30, "name": "윈드 에지", "element": "풀", "cooltime": 22, "power": 90},
                {"level": 40, "name": "원형 덩굴", "element": "풀", "cooltime": 40, "power": 120},
                {"level": 50, "name": "태양 폭발", "element": "풀", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "파종:1,수작업:1,채집:1,운반:1",
            "workSuitabilities_count": 4,
            "drops": "가죽 x1 (100%) | 예쁜 꽃 x1 (5%) | 핑토의 리본 x1 (50%) | 감자 종자 x1 (50%)",
            "drops_count": 4,
            "tribes": "번쩍이는 미소 그래토 (Tribe Boss) | 그래토 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 50–53 yamijima_7_1_YellowArea | Lv. 56–58 천락의 동굴",
            "spawners_count": 2
        },
        {
            # 40B 아비스고트 (Incineram_Noct)
            "id": "40B",
            "name_kor": "아비스고트",
            "name_eng": "Incineram_Noct",
            "description_kor": "어린 팰만 노려 자기 구역에 데리고 간다. 아이를 빼앗긴 부모 팰이 얼마나 절망에 빠졌을지 상상도 안 된다.",
            "elements": "어둠",
            "stats_rarity": 5,
            "stats_size": "M",
            "stats_health": 95,
            "stats_food": 300,
            "stats_attack": 105,
            "stats_defense": 85,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 580,
            "stats_goldCoin": 4870,
            "stats_egg": "암흑의 대형 알",
            "stats_code": "Baphomet_Dark",
            "movement_slowWalkSpeed": 80,
            "movement_walkSpeed": 160,
            "movement_runSpeed": 700,
            "movement_rideSprintSpeed": 960,
            "movement_transportSpeed": 320,
            "level60_health": "3912 – 4838",
            "level60_attack": "611 – 765",
            "level60_defense": "464 – 588",
            "partnerSkill_name": "암흑 발톱의 사냥꾼",
            "partnerSkill_describe": "발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기로 공격한다.",
            "partnerSkill_needItem": "",
            "partnerSkill_needItemTechLevel": 0,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30},
                {"level": 7, "name": "스피릿 파이어", "element": "화염", "cooltime": 7, "power": 45},
                {"level": 15, "name": "불화살", "element": "화염", "cooltime": 10, "power": 55},
                {"level": 22, "name": "지옥불 할퀴기", "element": "화염", "cooltime": 10, "power": 70},
                {"level": 30, "name": "그림자 폭발", "element": "어둠", "cooltime": 10, "power": 55},
                {"level": 40, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150},
                {"level": 50, "name": "인페르노", "element": "화염", "cooltime": 40, "power": 120}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "수작업:2,채굴:1,운반:2",
            "workSuitabilities_count": 3,
            "drops": "뿔 x1 (100%) | 가죽 x1 (100%)",
            "drops_count": 2,
            "tribes": "야음의 하이에나 아비스고트 (Tribe Boss) | 아비스고트 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 40–45 제2 사냥 금지 구역 | Lv. 29–29 습격 14-17",
            "spawners_count": 2
        },
        {
            # 45B 칠리자드 (Leezpunk_Ignis)
            "id": "45B",
            "name_kor": "칠리자드",
            "name_eng": "Leezpunk_Ignis",
            "description_kor": "자신의 포즈에 이상한 집착을 보인다. 항상 제일 뜨거운 자세를 연구하며 키우는 사람은 보기만 해도 숨이 막히는 자세를 계속 봐야만 한다.",
            "elements": "화염",
            "stats_rarity": 3,
            "stats_size": "S",
            "stats_health": 80,
            "stats_food": 225,
            "stats_attack": 80,
            "stats_defense": 50,
            "stats_workSpeed": 100,
            "stats_support": 100,
            "stats_captureRateCorrect": 1,
            "stats_maleProbability": 50,
            "stats_combiRank": 1140,
            "stats_goldCoin": 1640,
            "stats_egg": "열기 나는 알",
            "stats_code": "LizardMan_Fire",
            "movement_slowWalkSpeed": 100,
            "movement_walkSpeed": 140,
            "movement_runSpeed": 400,
            "movement_rideSprintSpeed": 550,
            "movement_transportSpeed": 270,
            "level60_health": "3425 – 4205",
            "level60_attack": "490 – 607",
            "level60_defense": "293 – 366",
            "partnerSkill_name": "제6감",
            "partnerSkill_describe": "발동하면 6번째 감각을 활용해 가까이 있는 던전의 위치를 탐지할 수 있다.",
            "partnerSkill_needItem": "",
            "partnerSkill_needItemTechLevel": 0,
            "partnerSkill_level": 1.0,
            "activeSkills": json.dumps([
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30},
                {"level": 7, "name": "독 사격", "element": "어둠", "cooltime": 2, "power": 30},
                {"level": 15, "name": "스피릿 파이어", "element": "화염", "cooltime": 7, "power": 45},
                {"level": 22, "name": "파이어 브레스", "element": "화염", "cooltime": 15, "power": 70},
                {"level": 30, "name": "화염 폭풍", "element": "화염", "cooltime": 18, "power": 80},
                {"level": 40, "name": "인페르노", "element": "화염", "cooltime": 40, "power": 120},
                {"level": 50, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150}
            ]),
            "activeSkills_count": 7,
            "workSuitabilities": "불 피우기:1,수작업:1,채집:1,운반:1",
            "workSuitabilities_count": 4,
            "drops": "발화 기관 x1–2 (100%) | 은 열쇠 x1 (2%) | 도마맨의 볏 x1 (50%)",
            "drops_count": 3,
            "tribes": "자칭 패션 리더인 칠리자드 (Tribe Boss) | 칠리자드 (Tribe Normal)",
            "tribes_count": 2,
            "spawners": "Lv. 25–31 3_2_volcano_1 | Lv. 32–36 모래 언덕 동굴",
            "spawners_count": 2
        }
    ]
    
    print("🔄 기존 CSV 파일 읽는 중...")
    
    # 기존 데이터 읽기
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []
        existing_data = list(reader)
    
    print(f"📊 기존 데이터: {len(existing_data)}개 팰")
    
    # 새로운 데이터 추가
    for variant in new_b_variants:
        # 빈 필드들을 적절히 채우기
        new_row = {}
        for field in fieldnames:
            new_row[field] = variant.get(field, "")
        
        existing_data.append(new_row)
        print(f"✅ 추가됨: {variant['id']} {variant['name_kor']} ({variant['name_eng']})")
    
    print(f"\n🎉 완료! 총 {len(existing_data)}개 팰이 {output_file}에 저장되었습니다.")
    print(f"📈 새로 추가된 B variants: {len(new_b_variants)}개")
    
    # 새 CSV 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    # 통계 출력
    b_variants_count = sum(1 for row in existing_data if row.get('id', '').endswith('B'))
    print(f"📊 총 B variants: {b_variants_count}개")
    print(f"🎯 아종 완성도: {b_variants_count}/59 = {(b_variants_count/59)*100:.1f}%")

if __name__ == "__main__":
    main() 